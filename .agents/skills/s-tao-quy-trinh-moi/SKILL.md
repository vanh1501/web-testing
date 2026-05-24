---
name: s-tao-quy-trinh-moi
description: >
  Analyzes, designs, scores, and repairs operational workflows for MAS workspaces.
  4-Route Engine: CREATE (build), ASSESS (7D scoring), RESOLVE (repair), LIFECYCLE (registry).
  Use when creating workflows, auditing quality, fixing wiring, or managing lifecycle.
  Even if the user only says "thêm 1 workflow mới", trigger this to enforce coverage analysis.
  Trang bị Directed Acyclic Graph (DAG) Traceability, Critical Path Method (CPM) Time-Boxing,
  Route Loading Matrix (P0/P1 context budget), và Testing Pyramid (T1-T4).
---

# Workflow Builder

You are a Senior Process Architect — the **RESOLVER** in the Diagnostician→Resolver pipeline for the Workflow component layer. The `qa` skill (Diagnostician) detects workflow-level issues during `/audit-workspace Phase 1`. When the diagnosis involves workflows, you receive the findings and execute expert-level resolution: create new workflows, deep-assess quality via 6-Dimension scoring, and repair/enrich deficient workflows. Without systematic coverage analysis, agents create 2-3 "obvious" workflows while leaving critical processes uncovered. This skill enforces Value Chain traceability AND quality standards — every R-step gets a workflow, every workflow gets proper wiring and depth.

## When to use this skill

- User nói "tạo workflow", "build process", "kiểm tra workflow", "fix workflow", "thiết kế quy trình".
- `/audit-workspace Phase 1` delegates deep workflow scoring.
- `/optimize-workspace P3 LEAF` delegates workflow repair.
- Value Chain đã map A-ESOAR nhưng chưa có workflow tương ứng.
- **KHÔNG dùng khi:** Workspace-level audits (dùng `qa`). Agent SI issues (dùng `rules`). Skill issues (dùng `skill-writer`).

## How to use it

1. Route 1 (CREATE): A-ESOAR coverage → Architecture → Build 5-Tier → Wiring verify.
2. Route 2 (ASSESS): Inventory → Archetype Detection → 7-Dimension Score → Coverage Analysis → Triage Report.
3. Route 3 (RESOLVE): Smart Triage → Map root causes → WR1-WR7 repair protocols → Closed-Loop re-score → delta report.
4. Route 4 (LIFECYCLE): Registry sync → State transitions → Deprecation → Archive.

## When to clarify

- **Route 1 (CREATE):** Ask which A-ESOAR R-steps are highest priority. Ask about session management needs. Confirm naming conventions.
- **Route 2 (ASSESS):** Ask for workflow path(s) or confirm "tất cả" means scan whole `.agents/workflows/`. Ask depth: `--quick` (scorecard) or `--deep` (per-dimension evidence).
- **Route 3 (RESOLVE):** Ask if auto-repair is authorized or review-first mode. If workflow is actively wired by agents, confirm before restructuring.

## Decision rules

- If user mentions "tạo", "build", "thiết kế" + workflow → **Route 1 (CREATE)**
- If user mentions "audit", "kiểm tra", "scan", "đánh giá" + workflow → **Route 2 (ASSESS)**
- If user mentions "fix", "sửa", "optimize", "repair" + workflow → **Route 3 (RESOLVE)**
- If user mentions "lifecycle", "version", "deprecate", "archive", "registry" → **Route 4 (LIFECYCLE)**
- If `/audit-workspace Phase 1` delegates findings → **Route 2 (ASSESS)**
- If `/optimize-workspace P3 LEAF` delegates repair → **Route 3 (RESOLVE)**
- If Route 2 output has Grade C or lower → auto-suggest Route 3 handoff
- If user says "tạo workflow" but A-ESOAR mapping doesn't exist → HALT and ask for mapping first
- If WORKFLOW-REGISTRY.md drift detected → auto-trigger Route 4 sync

## Process

### Route 1: CREATE — Build New Workflows

> [!WARNING] Bạn phải trích xuất Socratic OTC Check trước khi thao tác Tool

1. **Analyze:** Load A-ESOAR. Extract R/A-steps. Build Coverage Matrix. Identify gaps.
2. **Name Collision Check & Prefix Injection (MANDATORY):** 
   - Trước khi scaffold, BẮT BUỘC kiểm tra tên workflow mới có trùng với bất kỳ skill nào trong `.agents/skills/` không. Nếu trùng → HALT.
   - BẮT BUỘC nối tiền tố `w-` vào tên workflow và lệnh kích hoạt do người dùng cung cấp (ví dụ: User nhập `bao-cao` → tên file là `w-bao-cao.md` và slash command là `/w-bao-cao`).
3. **Design:** Classify (Infrastructure/Core/Support). Single vs multi-agent. Pre-register skills.
3. **Domain Intelligence (Domain only):** Load `references/domain-workflow-intelligence-pipeline.md` → Discovery (≥3 searches) → Translation → Validation.
4. **Develop:** Build 5-Section Architecture. Inject metadata. Wire `## Assigned Skills`. Budget < 12K chars. **[HARD-GATE]** Validation fail → rework loop. **[CPM]** Project-based → embed Time-Boxing. Run T1 Dry-Run before save (load `references/workflow-testing-framework.md`).
5. **Verify (DAG Traceability):** Coverage check. Skill binding (no A→B→A cycles). Budget check. Routing check.

**Route 1 Verification Evidence:**
- [ ] `grep_search` for `## Assigned Skills` in new workflow → must find ≥1 match
- [ ] Word count < 12,000 chars (context budget)
- [ ] Coverage matrix updated — no R-step left uncovered
- [ ] Domain Intelligence Pipeline executed (Domain Workspace only): ≥3 sources documented

> Load `references/workflow-anatomy.md` for 5-Section format. Load `references/workflow-coverage-matrix.md` for coverage template.

### Route 2: ASSESS — Deep Workflow Quality Evaluation

> [!WARNING] Bạn phải trích xuất Socratic OTC Check trước khi thao tác Tool

> **Diagnostician→Resolver Pipeline:**
> - `qa` skill runs `/audit-workspace Phase 1` with surface CQS checks.
> - If CQS detects workflows needing deep analysis → delegates to THIS route.
> - This route CAN also run standalone when user asks "audit workflows" directly.

1. **CQS Size Gate:** File < 0.5KB → Auto-FAIL. File > 12K chars → 🟡 WARNING. Load `references/workflow-scoring-engine.md`.
2. **Archetype Detection:** Classify: `GOVERNANCE` (>5 WFs, has audit) | `PRODUCTION` (<8 WFs) | `UTILITY` (single-purpose). Apply weight profile.
3. **Inventory:** List `.agents/workflows/*.md`. Classify TYPE-INFRA/CORE/SUPPORT/META.
4. **7-Dimension Score:** Score W1-W7 (115 raw → normalized 100). Flag missing Hard-Gates, Triad Loop handoffs.
5. **Root Cause Analysis:** Map each failing dimension to specific root cause.
6. **Cross-Workflow Pattern Detection (Batch):** Detect duplicate skills, orphan workflows, circular dependencies.
7. **Coverage Analysis:** Cross-reference A-ESOAR R-steps. Calculate coverage ratio.
8. **Self-Review:** Verify: all 7 dims scored? Archetype weights applied? No dimension conflation?
9. **Token Cost Analysis:** Calculate Effective Context Load per workflow. Load `references/workflow-observability-framework.md`.
10. **Triage & Report:** Sort by severity. Use `assets/workflow-audit-report-template.md`. Classify CRITICAL/REPAIR/ENRICH/MONITOR.
11. **Handoff:** Return findings → Route 3 (RESOLVE). Or ask user "Bắt đầu repair từ Critical trước?"

**Route 2 Verification Evidence:**
- [ ] CQS Size Gate applied — skeletons auto-failed, bloated files flagged
- [ ] Workspace archetype detected and weight profile applied
- [ ] All 7 dimensions scored — no "N/A" without written justification
- [ ] Coverage ratio calculated as decimal (e.g., 0.85)
- [ ] Report uses template structure — not freeform text

### Route 3: RESOLVE — Repair & Enrich Workflows

> [!WARNING] Bạn phải trích xuất Socratic OTC Check trước khi thao tác Tool

> Receives findings from Route 2 or `workspace-optimizer` (P3 LEAF). Proposes fix → confirms → implements.

1. **Smart Triage:** DETERMINISTIC (auto-fix, no approval) | STRUCTURAL (propose→execute) | CREATIVE (full approval). Execute DETERMINISTIC immediately.
2. **Accept Diagnosis:** Map root causes to WR1-WR7 / WE1-WE2 via `references/finding-handoff-schema.md`. Load `references/workflow-repair-protocols-detail.md` for step-by-step execution.
3. **Propose Fix Strategy:** Numbered action plan → present for approval.
4. **Execute Repairs:** Priority: WR4→WR5→WR2→WR3→WR1→WR6→WR7. Composition via `references/workflow-composition-protocols.md`.
5. **Enrichment:** WE1 (missing workflows), WE2 (unadapted infra).
6. **Closed-Loop Re-Score:** Re-run Route 2. Compare before vs after.
7. **T3 Regression:** Verify dependents not broken. Load `references/workflow-testing-framework.md`.
8. **Circuit Breaker:** `after_score < 70` after 2 iterations → HALT → escalate. Saga compensation for partial rollback.
9. **Delta Report:** Before/after via `assets/workflow-audit-report-template.md` Template 3.

**Critical Rules:** No WE1 without user confirmation. Propose BEFORE execute. DETERMINISTIC bypasses proposal but appears in delta.

### Route 4: LIFECYCLE — Workflow Lifecycle Management

> [!WARNING] Socratic OTC Check required before execution

1. **Inventory Refresh:** Scan `.agents/workflows/` vs WORKFLOW-REGISTRY.md. Detect drift.
2. **State Transition:** Validate DRAFT→STAGING→ACTIVE→DEPRECATED→ARCHIVED criteria. STAGING→ACTIVE requires T4 Golden Test pass.
3. **Version Diff (MAJOR bumps):** Generate diff report via `references/workflow-composition-protocols.md` Protocol 4.
4. **Deprecation:** Mark DEPRECATED, inject notice, set grace period, notify dependents.
5. **Archive & Purge:** Move past-grace to `_archive/`, update registry.
6. **Registry Sync:** WORKFLOW-REGISTRY.md = filesystem SSoT.

> Load `references/workflow-lifecycle-framework.md` and `references/workflow-registry-schema.md`.

## Output format

- **Route 1:** Workflow files at `.agents/workflows/` + updated `workflow-routing.md`.
- **Route 2:** Batch Scorecard (quick) or Per-Dimension Deep Assessment (deep) + Coverage Matrix.
- **Route 3:** Delta Report (before/after per workflow) + remaining human TODOs.
- **Route 4:** Updated WORKFLOW-REGISTRY.md + drift resolution log.

## Resources — Route Loading Matrix

> [!IMPORTANT] CONTEXT BUDGET RULE
> **Max 2 P0 references per route execution.** P1 references load ONLY when specific sub-protocol is needed. Total context per route MUST stay < 25K chars (SKILL.md + refs). Violating this budget → [HALT] + decompose task.

### Route 1: CREATE

| Priority | Reference | Size | When |
|---|---|---|---|
| **P0** | `references/workflow-anatomy.md` | 2.9K | Always — 5-Section Architecture |
| **P0** | `references/workflow-coverage-matrix.md` | 2.2K | Always — A-ESOAR gap mapping |
| P1 | `references/domain-workflow-intelligence-pipeline.md` | 3.7K | Domain Workspaces only |
| P1 | `references/workflow-design-intelligence.md` | 5.5K | Complex patterns needed |
| P1 | `references/workflow-testing-framework.md` | 6.8K | T1 Dry-Run (Step 4) |

### Route 2: ASSESS

| Priority | Reference | Size | When |
|---|---|---|---|
| **P0** | `references/workflow-scoring-engine.md` | 7.0K | Always — 7D scoring rubric |
| **P0** | `assets/workflow-audit-report-template.md` | 3.3K | Always — report output format |
| P1 | `references/workflow-design-intelligence.md` | 5.5K | Anti-pattern detection |
| P1 | `references/workflow-observability-framework.md` | 6.9K | Token Cost Analysis (Step 9) |
| P1 | `references/finding-handoff-schema.md` | 1.8K | Handoff to Route 3 |

### Route 3: RESOLVE

| Priority | Reference | Size | When |
|---|---|---|---|
| **P0** | `references/workflow-repair-protocols-index.md` | 2.5K | Always — Protocol Index + Triage Matrix |
| **P0** | `references/finding-handoff-schema.md` | 1.8K | Always — diagnosis input |
| P1 | `references/workflow-repair-protocols-detail.md` | 9.9K | Step-by-step protocol execution |
| P1 | `references/workflow-composition-protocols.md` | 5.8K | WR6 decomposition / merge |
| P1 | `references/workflow-testing-framework.md` | 6.8K | T3 Regression (Step 7) |

### Route 4: LIFECYCLE

| Priority | Reference | Size | When |
|---|---|---|---|
| **P0** | `references/workflow-lifecycle-framework.md` | 8.5K | Always — state machine |
| **P0** | `references/workflow-registry-schema.md` | 2.5K | Always — SSoT schema |
| P1 | `references/workflow-composition-protocols.md` | 5.8K | Version Diff (Step 3) |
| P1 | `references/workflow-observability-framework.md` | 6.9K | Drift alerting |

### Cross-Route

| Priority | Reference | When |
|---|---|---|
| P2 | **`search_web`** | Domain grounding — Domain Workspaces only |

## Quality checklist

- [ ] R1: DIP executed for Domain Workspaces? ≥3 sources documented?
- [ ] R1: All A-ESOAR R-steps covered? `## Assigned Skills` valid?
- [ ] R1: Pre-Flight CQS + T1 Dry-Run passed before saving?
- [ ] R2: CQS Size Gate + archetype detected? ALL 7 dims scored?
- [ ] R2: Coverage ratio calculated? Token Cost report generated?
- [ ] R2: Priority Queue (CRITICAL/REPAIR/ENRICH/MONITOR) in report?
- [ ] R3: Smart Triage applied? Correct protocol matched? Delta report generated?
- [ ] R3: Closed-Loop Re-Score passed? T3 Regression on dependents?
- [ ] R3: WE1/WR5 confirmed with user? Saga compensation available if partial fail?
- [ ] R4: WORKFLOW-REGISTRY.md matches filesystem? Lifecycle states valid?
- [ ] R4: Deprecated past grace → archived? MAJOR bump has Diff report?
- [ ] R4: STAGING→ACTIVE requires T4 Golden Test pass?

## Guardrails

- `Workflow_Size > 12K_chars` -> [HALT]. Mandatory decomposition via `references/workflow-composition-protocols.md`.
- `Circular_Skill_Dependency (DAG Violation: A→B→A)` -> [HALT] + report to user.
- `Workflow_Count > 8` -> [HALT]. Require explicit Human approval.
- `turbo-all + Destructive_Cmds` -> [WARNING] flag.
- `Skill_Ref_Not_In_Skills_Dir` -> 🔴 [BROKEN WIRING] halt + report.
- `A-ESOAR_Coverage < 0.7` -> [ALERT] user.
- `Hallucinate_Domain_Standards` -> [BANNED]. MUST use `search_web` via DIP.
- `Route3_Without_ReScore` -> [BANNED]. Closed-Loop Gate is mandatory.
- `Skip_CQS_Size_Gate` -> [DENY]. File < 0.5KB = skeleton.
- `Propose_Before_Execute` -> [REQUIRE] fix strategy before repair.
- `STAGING_To_ACTIVE_Without_Test` -> [DENY]. T1 Dry-Run + T4 Golden Test mandatory.
- `Route3_Without_Regression` -> [DENY]. T3 Regression check mandatory after repair.
- `MAJOR_Version_Without_Diff` -> [DENY]. Version Diff report required before MAJOR bump.

## Rules

- `Create_Without_AESOAR` -> [DENY]. Coverage check is prerequisite.
- `Blind_Workflow (no ## Assigned Skills)` -> [DENY]. Epistemic wiring mandatory.
- `Soft_Suggestion_In_QA_Workflow` -> [DENY]. MUST use Hard-Gate (Pass/Fail) rework loops.
- `Save_Without_CQS_PreFlight` -> [DENY]. Metadata injection mandatory.
- `Copy_Baseline_Verbatim` -> [DENY]. MUST customize for domain.
- `Workspace_Level_Audits` -> [DENY]. That is `qa` skill scope. Workflow-level ONLY.
- `Route3_Without_Delta` -> [DENY]. Re-score + delta report mandatory.
- `Execute_Without_Proposal` -> [DENY]. Propose first, Human/Workflow approves.
- `Structure_Compliance` -> [REQUIRE] Phần 5 of `KB/standards/Workspace_Architectural_Blueprints/kb-antigravity-workspace-standard.md`.
- `Domain_Workflow_Without_DIP` -> [DENY] for Domain Workspaces. Research grounding mandatory.
## 7. QA Checklist
- [ ] Đã kiểm tra chuẩn định dạng đầu ra chưa?
- [ ] Tone và Voice có phù hợp với ngữ cảnh yêu cầu không?
- [ ] Đã bổ sung đẩy đủ các thẻ Meta/Frontmatter (nếu có)?

## 6. Anti-patterns (L?i C?m K?)
- Kh�ng vi ph?m nguy�n t?c thi?t k? lu?ng.

