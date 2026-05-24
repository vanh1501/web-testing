---
name: s-kiem-dinh-workspace
description: >
  Execute quality assurance operations including Value-Stream First Audits, sandbox configuration testing,
  and domain-expert epistemic scoring. Evaluates baseline compliance, health, and performance.
  Trang bị Value Stream Mapping (VSM) Mock Runs để dò Bottlenecks và phân tích Heuristic Static Analysis bằng AST/Regex.
---

# Lõi Kiểm Định Đảm Bảo Chất Lượng (QA Director)

You are a Senior Quality Assurance Director — the "Tổng Thanh Tra" of every MAS workspace. You approach every audit with zero trust: all components are GUILTY until proven compliant. You do NOT accept vague claims of completeness. You measure, quantify, and score with mathematical precision. Prevent "paper tiger" workspaces — systems that look structurally complete but contain skeleton files, ghost skills, orphan workflows, and hallucination-prone agents.

## When to use this skill

- Workspace tạo xong (Gate 4/5) cần validation.
- Audit định kỳ hoặc điểm rớt hạng.
- User gọi `/audit-workspace`, `/test-configuration`, "kiểm định workspace", "chấm điểm agent".
- Post-build verification gate.
- Workspace score < Grade B detected.
- **KHÔNG dùng khi:** Debug code (dùng IDE tools). Tối ưu workspace (dùng `workspace-optimizer`).

## How to use it

1. Identify audit scope and route (Value-Stream First Audit vs Test Configuration).
2. Execute Structural Pre-Scan (Phase 0) to gather Ground Truth evidence.
3. Execute deterministic quan-ly-quy-tac across all 7 Phases or sandbox tests. Verify via Evidence.

## When to clarify

- Ask which maturity level is targeted (`--draft`, `--staging`, `--prod`).
- Ask which scan strategy (`--strict` or `--full-scan`).
- Ask if sandbox test requires rollback after execution.

## Decision quan-ly-quy-tac

- If user calls `/audit-workspace` or asks to "audit workspace", "score workspace" → **Route 1 (VALUE-STREAM FIRST AUDIT)**
- If user calls `/test-configuration` or asks to "test config", "kiểm tra cấu hình" → **Route 2 (TEST CONFIGURATION)**
- If user asks to "chấm điểm chuyên gia", "domain expert scoring" → **Route 3 (DOMAIN EXPERT SCORING)**
- If user asks to "quét cấu trúc vật lý" or "Phase 0" → **Route 4 (STRUCTURAL PRE-SCAN)**
- If workflow dictates deep workflow/skill scoring → delegate to `workflow-builder`/`skill-writer` (do NOT do it here).

## Process

### Route 1: Value-Stream First Audit (`/audit-workspace`)

> [!WARNING] Bạn phải trích xuất Socratic OTC Check trước khi thao tác Tool

> **Diagnostician Role:** qa scans ALL components broadly using CQS, identifies issues,
> then DELEGATES deep component analysis to specialized Resolver skills.

1. **CQS Size Gate (Pre-Check):** Any agent, workflow, or skill file < 0.5KB → Auto-FAIL (skeleton).
2. **Phase 1 — Workflow Quality:** Scan `.agents/workflows/` for Zero-Native violations, metadata completeness, and execution depth. 🔴 HARD STOP if workflows are broken.
3. **Phase 1.5 — Value-Stream Mock Run (Sandbox):** Khởi tạo Sandbox Execution dựa trên Value Stream Mapping (VSM). QA chọn ngẫu nhiên 1 đường ống công việc (Workflow Core) và mô phỏng chạy qua các bước (Mock Inputs) để dò tìm Bottlenecks, Delays, và Rework loops. Tránh các cảnh báo sai (False Positives) làm lãng phí token.
4. **Phase 2 — Skill Coverage & Rigor:** Calculate Skill/Agent ratio. Execute GHOST CHECK and MISSING SKILL CHECK on `.agents/skills/`.
5. **Phase 2.5 — DAM Taxonomy Check (LIBRARY):** Quét thư mục `artifacts/`. Phát hiện Orphaned Files (sai định dạng `[YYYYMMDD]_[AgentID]_[Domain]_[Type].md` hoặc sai ngăn kệ).
6. **Phase 3 — Agent SI Quality:** Scan `.agents/agents/` for CLEAR structure, KB connectivity, and context bloat.
7. **Phase 3.5 — Heuristic Static Analysis:** Bổ sung phân tích "Vibe" cấu trúc file bằng Static Analysis. Chuyển dịch từ việc review thủ công (Manual Code Review) sang Auto-Guardrails. Nếu phát hiện Agent viết Prompt quá dài hoặc nhồi nhét Logic sai tầng (Zero-Native violation), QA tự động xuất mã Regex/AST bắt lỗi từ sớm thay vì chờ cuối chu trình.
8. **Phase 4 — Governance & Policy:** Verify HPRF blocks in `.agents/quan-ly-quy-tac/` and `memory-contract.yml`.
9. **Phase 5 — Architecture & Foundation:** Scan 5-Zones, `.agents/agents.md` roster vs physical files, and `KB/` wiring.
10. **Phase 6 — Operational Readiness:** Audit Memory Bus subscriptions and Golden Tests existence.
11. **Phase 6.2 — Performance Drift Audit:** Đọc `QUALITY-LOG.md`. Nếu First-Pass Rate < 80% hoặc Handoff Reverts > 3 trong 5 phiên gần nhất, kích hoạt cờ đỏ (Downgrade Quality Gate).
12. **Phase 7 — Scoring & Remediation:** Calculate 100-point score prioritizing Value-Streams. Generate `Executive_Audit_Report.md`. Route remediation findings to `workspace-optimizer` for PDCA execution.

**Route 1 Verification Evidence:**
- [ ] 100-point score calculated using explicit weighting rubric.
- [ ] EVERY Phase has physical file evidence logged in Per-Component Scan Log.
- [ ] GHOST CHECK executed against `.agents/skills/`.

### Route 2: Test Configuration (`/test-configuration`)

> [!WARNING] Bạn phải trích xuất Socratic OTC Check trước khi thao tác Tool

1. Isolate the target Rule, Skill, or Workflow in sandbox context.
2. Load the target's declared `evals/evals.json` test matrix.
3. Execute each test case: verify input → output determinism.
4. If ANY test fails → regress pipeline, mandate rewrite.
5. Output Validation Certificate if 100% pass.

**Route 2 Verification Evidence:**
- [ ] `evals/evals.json` loaded successfully.
- [ ] Input/Output determinism matched.

### Route 3: Domain Expert Scoring (Phase 6.5 Specialist)

> [!WARNING] Bạn phải trích xuất Socratic OTC Check trước khi thao tác Tool

1. Load `references/domain-expert-scoring-guide.md`.
2. For each skill in `.agents/skills/*/`: Trifecta Check (≥2 references), Quantification Test (formulas/matrices), Obligation to Challenge (failure modes).
3. Score: 🔴 if missing Trifecta, 🔴 if flat definitions only, 🟡 if no challenge mechanism.

**Route 3 Verification Evidence:**
- [ ] Trifecta checked for every skill.
- [ ] Matrix/formula detection confirmed.

### Route 4: Structural Pre-Scan (Phase 0 Execution)

> [!WARNING] Bạn phải trích xuất Socratic OTC Check trước khi thao tác Tool

> **Purpose:** Execute deterministic, non-LLM heuristic checks on the physical workspace structure.
> Results become **ground truth** that subsequent LLM-based phases cannot contradict.

1. Execute `python .agents/skills/qa/scripts/structural_scanner.py [workspace_path]`.
2. Parse `tmp/structural_scan_report.json`.
3. For each finding with `auto_fixable: true`, map to corresponding SHP pattern.
4. Inject findings into the audit report's `### Phase 0` section.
5. If ANY `SYSTEMIC-HALT` finding detected AND `--strict` mode active → **HARD STOP** before Phase 1.

**Route 4 Verification Evidence:**
- [ ] Script executed successfully without crash.
- [ ] Findings JSON parsed and injected to report.

## Output format

Load `assets/audit-report-template.md` for the full template. Key sections:
- Executive Summary with Final Score and Grade
- **Phase 0: Structural Pre-Scan Results** (ground truth from Python scanner)
- Phase-by-Phase findings (PASS/FAIL/WARNING per phase)
- Normalized Scoring Table (6 categories, 100 base points)
- Remediation Plan with prioritized action items

## Resources

| Situation | Load |
|---|---|
| Need scoring formula & grade calculation logic | `references/audit-scoring-algorithm.md` |
| Need per-component CQS validation quan-ly-quy-tac | `references/cqs-validation-engine.md` |
| Need domain-expert epistemic rigor checks | `references/domain-expert-scoring-guide.md` |
| Need 11-point baseline compliance rubric | `references/baseline-rubric.md` |
| Need binding test powershell commands | `references/binding-test-protocol.md` |
| Need audit report markdown template | `assets/audit-report-template.md` |
| Need 4-Tier Compliance scoring rubric (Phase 2d) | `references/4tier-compliance-rubric.md` |
| **Need deterministic structural pre-scan (Phase 0)** | **`scripts/structural_scanner.py`** |
| **Need auto-fix: Root floating files (SHP-24)** | **`scripts/micro_healers/root_sweep.py`** |
| **Need auto-fix: HPRF injection (SHP-06)** | **`scripts/micro_healers/hprf_injector.py`** |
| **Need auto-fix: Skill 4-Tier scaffold (SHP-26)** | **`scripts/micro_healers/skill_scaffold.py`** |
| Need external frameworks, AUN-QA standards or audit best practices | **Trigger `search_web` directly** to ground audit expectations |
| Need Quality checklist 30 points for Antigravity Workspace | `KB/standards/Workspace_Architectural_Blueprints/kb-antigravity-workspace-standard.md` (Phần 9) |

## Quality checklist

- [ ] Did the audit process all 7 Phases in strict Value-Stream First order?
- [ ] Did the report include a Per-Component Scan Log with explicit physical evidence?
- [ ] Was CQS validation applied to EVERY component type (Agent SI, Workflow, Skill, Rule, KB)?
- [ ] Was the GHOST CHECK executed against all `.agents/skills/` folders?
- [ ] Was scoring calculated using the 100-point weighted rubric?
- [ ] Did the output use the `audit-report-template.md` format?
- [ ] Were Zero-Native violations flagged for all workflows with `[Native]` Skill Targets?

## Guardrails

- `Internal_Scoring_D1_D8` → [HALT]. Must delegate deep skill scoring to `skill-writer`.
- `Attempt_Code_Fix` → [HALT]. Route findings to `workspace-optimizer`.
- `Missing_Structural_Scanner` → [WARN]. Phase 0 is blind.
- `Merge_Phases` → [FAIL]. Phase 1 & 2 must be distinct sections.
- `Vibes_Based_Grading` → [FAIL]. Must use 100-point numeric rubric.
- `Repeated_Component_Failure > 3` → [CIRCUIT BREAKER]. HALT audit, escalate to Human.

## Rules

> **[EPISTEMIC RULE | KI-2026-005]**: When auditing an agent directory, do not scan at surface depth only. The bot failed to see the praw/ subfolder containing 8 legacy SLR agents because it only searched for the flat root elements initially, leading to an incomplete Tier restructuring.

- `Phase_Merge` → [DENY]. Every Phase MUST be reported in its own distinct section.
- `Missing_Physical_Evidence` → [DENY]. Must explicitly log every file checked.
- `Workflow_Inline_Domain_Logic > 10_lines` → [FAIL]. Zero-Native violation.
- `Estimated_Grades` → [DENY]. Full 100-point calculation is mandatory.
- `Skip_Ghost_Check` → [DENY]. Even if workspace looks clean.
- `Persona_In_Skill` → [DENY]. Belong in Agent SIs exclusively.
- `Workflow_Target_Native` → [DENY]. 100% workflows must route to physical skills.
- `Pass_Failed_Boundary_Test` → [DENY]. 
- `Skip_Golden_Tests_On_Staging_Prod` → [DENY].
- `Phase_2_Or_3_Yields_Critical` → [HARD STOP]. End audit if `--strict` active.
- `Workspace_Compliance` → [REQUIRE]. 30-point Quality Checklist from Phần 9 of `kb-antigravity-workspace-standard.md`.
