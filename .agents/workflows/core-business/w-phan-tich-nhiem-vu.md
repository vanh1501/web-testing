---
id: "WF-TASK-INTAKE-01"
name: "w-phan-tich-nhiem-vu"
description: "Gateway phân rã yêu cầu thô đầu phiên từ Operator thành Implementation Plan (WBS + Skill mapping). Chốt chặn đảm bảo mọi task đều setup đúng cấu trúc Workspace trước khi thực thi. Phân loại Task vs Project và route sang workflow scaffolder tương ứng."
version: v2.0
status: Production-Ready
semantic_triggers: ['phân tích nhiệm vụ', 'phan tich nhiem vu', 'lên kế hoạch task', 'task intake', 'rã task', 'WBS', 'implementation plan', 'kế hoạch thi công', 'phân công agent']
owner: "Cố vấn AI MindX"
skill_target: "00-phan-tich-yeu-cau, 00-quan-ly-du-an"
hitl_timeout: "24h"
retry_policy: {max_attempts: 3, backoff: exponential_1s_2s_4s, fallback: "log_to_ACTION-LOG_and_report_human"}
---

- **👤 Owner:** `[@Cố vấn AI MindX]`
- **🛠 Skill Target:** `[00-phan-tich-yeu-cau, 00-quan-ly-du-an]`
- **⏱ HITL Timeout:** 24h, escalation → BOM admin
- **🔄 Circuit Breaker:** retry 3 lần, fallback → ACTION-LOG.md + human notify

# Quy Trình: /w-phan-tich-nhiem-vu (v2.0 — Task Intake Gateway)

## Purpose & Scope

**Purpose:** Tiếp nhận yêu cầu công việc thô/lời dặn dò từ Operator, chuyển hóa thành Implementation Plan (WBS + sơ đồ phân công Agent). Là **chốt chặn (Gateway)** đảm bảo mọi task lớn/nhỏ đều được setup đúng cấu trúc Workspace trước khi thực thi.

**Scope:** Từ intake → scale assessment → WBS design → maker-checker approve → workspace scaffolding → kick-off. KHÔNG bao gồm thực thi sub-task (delegate to skill khác).

## Trigger

- Operator gõ lệnh `/w-phan-tich-nhiem-vu {Yêu-cầu-hoặc-nhiệm-vụ}`
- Hoặc Operator giao task phức tạp bằng ngôn ngữ tự nhiên → hệ thống auto-detect và kích hoạt

## Prerequisites

- [ ] Registry sẵn sàng (`DANH-SACH-KY-NANG.md`, `DANH-SACH-DU-AN.md`, `DANH-SACH-TASK.md`)
- [ ] Operator cung cấp đủ ngữ cảnh đầu vào (Mục tiêu + Deadline nếu có)

## Steps

> [!IMPORTANT] KARPATHY VERIFICATION MANDATE
> Mỗi Step BẮT BUỘC: `[Step] -> verify: [Tiêu chí đo lường cụ thể]`. CẤM Blind Looping.

### Step 1 — Task Intake & Phân Tích
**Action:** Gọi skill `00-phan-tich-yeu-cau` (sub-mode: intake) với yêu cầu thô từ Operator.
**Verify:** Skill return 3 yếu tố clear: Goal, Constraints (deadline/format), Input data. Nếu thiếu yếu tố nào, hỏi Operator tối đa 2 câu.

### Step 2 — Scale Assessment (HITL Gate 1)
**Action:** Trình bày nhận định quy mô: "Em thấy quy mô (Nhỏ/Vừa/Lớn)."
**Decision branch — chốt với Operator:**
- → **Project** (kéo dài nhiều phiên, có quy trình đầy đủ): proceed scaffold workspace mới
- → **Task ngắn hạn** (làm ngay trong phiên): proceed dùng workspace Tasks/

**Verify:** Operator explicit confirm "Task" hay "Project". KHÔNG được tự quyết.

### Step 3 — WBS Design
**Action:** Gọi skill `00-phan-tich-yeu-cau` (sub-mode: breakdown) phân rã yêu cầu thành sub-tasks + mapping mỗi sub-task → 1 skill có thật trong `DANH-SACH-KY-NANG.md`.
**Verify:** Skill return Implementation Plan với atomic tasks (≤4h effort each), mỗi task map đúng 1 skill v2.0, dependency graph rõ, risk register ≥3 risks.

### Step 4 — Maker-Checker Approve (HITL Gate 2)
**Action:** DỪNG workflow, xuất Implementation Plan ra chat. Trình bày: "Sếp xem giải pháp em lên (WBS + Phân công) đã chuẩn chưa ạ?"
**Decision branch:**
- Approve → proceed Step 5
- Reject → quay Step 3 với feedback
- Modify → áp feedback rồi resubmit
**Verify:** Operator explicit approve (text "OK"/"duyệt"/"approve"). KHÔNG được tự setup khi chưa duyệt.

> **Note:** Operator power user có thể gõ `/w-phan-tich-nhiem-vu {task} --auto` để skip Step 4 (auto-approve), nhưng vẫn in Plan ra màn hình.

### Step 5 — Workspace Setup (Routing)
**Action:** Theo phân loại Step 2:
- **Project** → trigger workflow `/w-khoi-tao-du-an-moi` (TUYỆT ĐỐI CẤM tạo thư mục tay)
- **Task** → tạo mã `TSK-{YY}-{XXX}`, tạo `Du-An/Tasks/{Mã}_{Tên}/`, đăng ký `DANH-SACH-TASK.md`. Mọi deliverable đẩy vào `Kho-Du-Lieu/Ket-Qua/Tasks/{Mã}/`

**Verify:** Mã ID hợp lệ + registry updated + folder tồn tại.

### Step 6 — Dispatch & Kick-off
**Action:** Khởi động sub-task đầu tiên trong Implementation Plan, gắn thẻ Agent được phân công (skill name) để báo cáo bắt đầu.
**Verify:** Agent confirm nhận task + ETA.

## HITL Gates

| Gate | Step | Timeout | Action on timeout | Escalation |
|------|------|---------|-------------------|------------|
| Gate 1 — Scale Assessment | Step 2 | 24h | Default Task ngắn hạn + warn Operator | BOM admin nếu workflow critical |
| Gate 2 — Plan Approve | Step 4 | 24h | Pause + send reminder. Sau 48h auto-archive | BOM admin |

## Circuit Breaker Policy

| Failure mode | Detection | Retry | Fallback |
|--------------|-----------|-------|----------|
| Skill `00-phan-tich-yeu-cau` không respond | Timeout 30s | 3 lần | ACTION-LOG + human notify |
| Sub-task không map skill nào (Gap năng lực) | Skill return `gaps_identified: [...]` | 0 (immediate) | Flag GAP trong Plan, suggest: (a) human owner, (b) tạo skill mới qua `/skill-writer` |
| `DANH-SACH-TASK.md` write fail | OS error | 3 lần | Log + manual register sau |

## Edge Cases & Recovery

1. **Workspace chưa có skill làm được** → Plan có section "Gap năng lực", đề xuất `/w-tao-ky-nang-moi` hoặc human takeover
2. **Operator lười muốn skip duyệt** → `--auto` flag, vẫn in Plan; sau 48h nếu output có issue, Operator chịu trách nhiệm
3. **Operator yêu cầu deadline phi thực tế** → Skill `00-phan-tich-yeu-cau` flag conflict trong risk register, Step 4 trình bày honest pushback
4. **Yêu cầu chứa data nhạy cảm** (PII, salary) → Skill flag Constraint, Step 5 setup folder có access-control note
5. **Dependency circular** giữa sub-tasks → Skill REFUSE, Step 3 ask Operator clarify thứ tự
6. **Cross-functional (cần đầu mối phòng khác)** → Plan list stakeholders, Step 4 yêu cầu confirm các bên trước approve

## Output Contract (Idempotent JSON)

```json
{
  "workflow_id": "WF-TASK-INTAKE-01",
  "run_status": "success | halt_at_gate | halt_at_failure",
  "intake_summary": {
    "goal": "...",
    "constraints": [...],
    "input_data": [...]
  },
  "scale_classification": "task | project",
  "implementation_plan": {
    "complexity_tier": "simple | medium | complex",
    "wbs_atomic_count": 8,
    "skill_mapping": [...],
    "critical_path_effort": "1-2 days",
    "risks_identified": 3,
    "gaps_identified": []
  },
  "approval_status": "approved | rejected | auto_approved",
  "workspace_setup": {
    "type": "project | task",
    "id": "PRJ-26-001 | TSK-26-001",
    "folder": "..."
  },
  "next_workflow_suggested": "00-khoi-tao-du-an-moi (if project) | none (if task started)"
}
```

## Cross-Workflow Chaining

- **Hands off to:**
  - `00-khoi-tao-du-an-moi` (nếu classify = Project)
  - Skill được mapped trong WBS (nếu task → trực tiếp dispatch)

## Validation

- [ ] Đã hoàn thành Scale Assessment + Operator confirm
- [ ] Đã cấp mã ID chuẩn (`TSK-{YY}-{XXX}` hoặc `PRJ-{YY}-{XXX}`)
- [ ] Có file `Action-Plan-{date}.md` với WBS rõ ràng
- [ ] Đã xin duyệt Action Plan trước khi setup workspace
- [ ] Registry tương ứng (`DANH-SACH-TASK.md` hoặc `DANH-SACH-DU-AN.md`) cập nhật
- [ ] JSON Output Contract đầy đủ

## Resources

- Skill: `00-phan-tich-yeu-cau` (sub-modes: intake, breakdown)
- Skill: `00-quan-ly-du-an` (chained via /w-khoi-tao-du-an-moi)
- Registry: `Bang-Dieu-Khien/DANH-SACH-TASK.md`, `DANH-SACH-DU-AN.md`, `DANH-SACH-KY-NANG.md`
