---
id: "WF-PM-COMPREHENSIVE-01"
name: "w-quan-tri-du-an"
description: "Pipeline Quản trị Dự án End-to-End sau scaffold: lập WBS, RACI, Timeline, Task Delegation. Chain với /w-khoi-tao-du-an-moi cho scaffolding (không duplicate). Áp dụng PMBOK 8/80 rule, Critical Path, và RACI mandatory."
version: v2.0
status: Production-Ready
semantic_triggers: ['quản trị dự án', 'project management', 'lập kế hoạch dự án', 'WBS', 'RACI', 'timeline', 'Gantt', 'phân công task', 'delegation', 'critical path']
owner: "PRO-W04"
skill_target: "00-quan-ly-du-an, 00-tao-tai-lieu"
hitl_timeout: "24h"
retry_policy: {max_attempts: 3, backoff: exponential_1s_2s_4s, fallback: "log_to_ACTION-LOG_and_report_human"}
---

- **👤 Owner:** `[@PRO-W04]`
- **🛠 Skill Target:** `[00-quan-ly-du-an, 00-tao-tai-lieu]`
- **⏱ HITL Timeout:** 24h
- **🔄 Circuit Breaker:** retry 3 lần, fallback → ACTION-LOG.md + human

# Quy Trình: /w-quan-tri-du-an (v2.0 — PM End-to-End)

## Purpose & Scope

**Purpose:** Sau khi `/w-khoi-tao-du-an-moi` đã scaffold workspace, workflow này gánh **lập kế hoạch chi tiết**: WBS phân rã, RACI matrix, Timeline + Critical Path, Task Delegation.

**Scope:** Plan-time. KHÔNG bao gồm: scaffolding (đã delegate `/w-khoi-tao-du-an-moi`), tracking running (gap, dùng `/w-phan-tich-va-bao-cao` Route 2 cho RAG status).

## Trigger

User: "lập kế hoạch dự án ABC", "WBS cho dự án X", "phân công team", "vẽ Gantt", "lập RACI matrix".

## Prerequisites

- [ ] Dự án đã scaffold (folder `Du-An/{folder}/` + 5 file PMBOK tồn tại). **Nếu chưa, workflow chain trước sang `/w-khoi-tao-du-an-moi`**
- [ ] Operator có team list (≥1 thành viên) để gán RACI

## Routing — Step 0

| Tình huống | Route |
|-----------|-------|
| Dự án mới chưa scaffold | **Route A: Full lifecycle** — chain `/w-khoi-tao-du-an-moi` → resume tại Step 2 |
| Dự án đã scaffold, cần lập WBS từ đầu | **Route B: Plan from charter** — bắt đầu Step 2 |
| Dự án đã có WBS sơ bộ, cần refine RACI + Timeline | **Route C: Refine plan** — skip Step 2, vào Step 3 |

## Steps

> [!IMPORTANT] KARPATHY VERIFICATION MANDATE
> Mỗi Step: `[Step] -> verify: [Tiêu chí]`. CẤM Blind Looping.

### Step 1 — Pre-Check Workspace (Decision branch)
**Action:** Verify `Du-An/{folder}/00_Project_Charter.md` tồn tại.
**Decision:**
- Tồn tại → proceed Step 2
- Không tồn tại → chain workflow `/w-khoi-tao-du-an-moi`, sau khi scaffold xong resume tại Step 2

**Verify:** Charter file exists + có data hydrated (không còn `[PLACEHOLDER]`).

### Step 2 — WBS Decomposition
**Action:** Gọi `00-quan-ly-du-an` (sub-mode: wbs_decompose) với inputs từ Charter (Scope, Deliverables).
**Verify:** Skill return WBS Level 0-3, mỗi atomic task tuân **PMBOK 8/80 rule** (≤80h, ≥8h). Không có task vô hạn hay quá micro.

### Step 3 — WBS Approval (HITL Gate 1)
**Action:** Trình bày WBS draft cho Operator (Project Manager).
**Decision:** Approve → Step 4 | Reject → quay Step 2 với feedback | Modify → áp feedback resubmit.
**HITL Timeout:** 24h. Sau timeout: send reminder, không auto-approve (WBS critical).

### Step 4 — RACI Matrix Assignment
**Action:** Gọi `00-quan-ly-du-an` (sub-mode: raci_assign) với team list từ Operator.
**Verify:** Mọi task có ≥1 person R (Responsible) + đúng 1 person A (Accountable). Không có task orphan.

### Step 5 — Timeline & Critical Path
**Action:** Gọi `00-quan-ly-du-an` (sub-mode: timeline_compute) — assign Start/End date per task, compute dependencies, identify Critical Path.
**Verify:** Mọi task có deadline (no NULL), Critical Path identified, không có circular dependency.

### Step 6 — Overload Check (Decision)
**Action:** Skill return per-person workload report.
**Decision:**
- Có person bị overload (>40h/tuần trong cùng window) → **WARN Operator**, suggest re-distribute hoặc deadline shift
- No overload → proceed Step 7

### Step 7 — Render Plan Documents
**Action:** Gọi `00-tao-tai-lieu` (document_type: business_proposal, style: operational) → render Markdown 3 file:
- `Du-An/{folder}/02_WBS_and_Timeline.md`
- `Du-An/{folder}/03_RACI_Matrix.md` (update existing)
- `Du-An/{folder}/04_Action_Plan.md`
**Verify:** 3 files written, format Markdown chuẩn.

### Step 8 — Delegation Kick-off
**Action:** Gọi `00-tao-tai-lieu` (document_type: meeting_minutes) sinh Action Log entries → append vào `Bang-Dieu-Khien/ACTION-LOG.md`. Notify team members (qua message body, không send email tự động).
**Verify:** ACTION-LOG.md updated với task ID + owner + deadline mỗi entry.

## HITL Gates

| Gate | Step | Timeout | Action on timeout |
|------|------|---------|-------------------|
| Gate 1 — WBS Approve | Step 3 | 24h | Reminder; KHÔNG auto-approve (critical) |
| Gate 2 — Overload Warning | Step 6 | 24h | Auto-proceed nhưng log warning trong Plan |

## Circuit Breaker Policy

| Failure mode | Detection | Retry | Fallback |
|--------------|-----------|-------|----------|
| Skill timeout | 30s no response | 3 lần | ACTION-LOG + human |
| WBS có task >80h (vi phạm PMBOK 8/80) | Skill validate | 1 lần (re-decompose) | Flag risk, proceed với warning |
| RACI orphan task (no R or A) | Skill validate | 0 (immediate) | REFUSE, ask Operator assign |
| Circular dependency | Skill detect | 0 | REFUSE, ask Operator clarify thứ tự |
| File write fail (permission) | OS error | 3 lần | Log + manual write later |

## Edge Cases & Recovery

1. **Dự án chưa scaffold** → Chain `/w-khoi-tao-du-an-moi` (Step 1 routing)
2. **Operator chưa có team list** → Ask provide. Nếu không có, mark task R/A = "TBD", workflow exit với partial_success
3. **Task >80h** → Suggest decompose; nếu Operator insist giữ, log exception trong risk register
4. **Person overload >40h/tuần** → WARN nhưng không REFUSE; Operator chịu trách nhiệm
5. **Cross-team dependency** (cần đầu mối phòng khác) → Flag stakeholder list, suggest confirm trước Step 8
6. **Charter chưa hydrate** (còn `[PLACEHOLDER]`) → REFUSE Step 2, ask Operator complete Charter trước
7. **Deadline quá khứ** (Operator nhập sai date) → REFUSE, ask correct

## Output Contract (Idempotent JSON)

```json
{
  "workflow_id": "WF-PM-COMPREHENSIVE-01",
  "route_executed": "A | B | C",
  "run_status": "success | partial_success | halt",
  "project_metadata": {
    "project_code": "PRJ-26-001",
    "project_folder": "..."
  },
  "wbs_summary": {
    "level_count": 3,
    "atomic_task_count": 24,
    "pmbok_8_80_compliance": true
  },
  "raci_summary": {
    "tasks_with_R": 24,
    "tasks_with_A": 24,
    "orphan_tasks": 0
  },
  "timeline_summary": {
    "critical_path_length_days": 45,
    "buffer_days": 5,
    "person_overload_warnings": 1
  },
  "deliverable_files": [
    "Du-An/{folder}/02_WBS_and_Timeline.md",
    "Du-An/{folder}/03_RACI_Matrix.md",
    "Du-An/{folder}/04_Action_Plan.md"
  ],
  "action_log_entries": 12,
  "hitl_gates_triggered": ["Gate 1"],
  "circuit_breaker_activated": false,
  "next_workflow_suggested": "00-phan-tich-va-bao-cao Route 2 (RAG Status tracking khi project running)"
}
```

## Cross-Workflow Chaining

- **Receives from:** `00-khoi-tao-du-an-moi` (Route A) hoặc `00-phan-tich-nhiem-vu` (Project classification)
- **Chains to:** `00-khoi-tao-du-an-moi` (Step 1 nếu chưa scaffold)
- **Hands off to:** `00-phan-tich-va-bao-cao` Route 2 (RAG Status cho tracking khi project running)

## Validation

- [ ] Mọi task có ≥1 R + đúng 1 A
- [ ] Timeline có Start/End date đầy đủ (no NULL)
- [ ] Critical Path identified, không có circular dependency
- [ ] PMBOK 8/80 rule: ≤80h và ≥8h per atomic task
- [ ] 3 deliverable files written đúng path
- [ ] `ACTION-LOG.md` cập nhật
- [ ] JSON Output Contract đầy đủ

## Resources

- Skill: `00-quan-ly-du-an` (sub-modes: wbs_decompose, raci_assign, timeline_compute)
- Skill: `00-tao-tai-lieu` (sub-mode: business_proposal, meeting_minutes)
- Templates: `Du-An/{folder}/02_*.md`, `03_*.md`, `04_*.md`
- Registry: `Bang-Dieu-Khien/ACTION-LOG.md`
