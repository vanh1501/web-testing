# Executive Audit Report Template

> Asset template for the `qa` skill.
> Use this template to generate the standardized `Executive_Audit_Report.md` in Phase 7.
> Replace all `[PLACEHOLDER]` values with actual audit data.

---

```markdown
# Executive Audit Report — [WORKSPACE_NAME]

**Date:** [YYYY-MM-DD]
**Auditor:** `[@GOV-W03]` (QA & Audit Director)
**Workspace:** `[WORKSPACE_NAME]` ([WORKSPACE_DESCRIPTION])
**Maturity Level:** `[--draft|--staging|--prod]`
**Scan Strategy:** `[--strict|--full-scan]`

---

## Executive Summary

[2-3 sentences describing overall workspace health, focusing heavily on value-stream viability and skill coverage.]

**Final Score:** `[SCORE]/100` (Grade: **[A+|A|B|C|D|F]**)
**Verdict:** **[Go-Live Ready | Needs Remediation | Critical Rebuild Required]**

---

## Phase 1: Workflow Quality & Routing (VALUE STREAM)
- **Zero-Native Law:** [Any [Native] targets or embedded logic? YES/NO]
- **CQS Compliance:** [Summary — skeletons, bloat, metadata gates]
- **Binding Density:** [Orphan workflows, call graph integrity]
- **Verdict:** [✅ PASS | 🟡 PASS WITH WARNINGS | ❌ FAIL]

## Phase 2: Skill Coverage & Rigor (ARSENAL)
- **Supply/Demand Ratio:** [Ratio] - [Analysis]
- **Ghost/Missing Skills:** [X ghosts, Y missing]
- **Domain Expert Rigor:** [Trifecta/Quantification checks]
- **Verdict:** [✅ PASS | 🟡 PASS WITH WARNINGS | ❌ FAIL]

## Phase 3: Agent SI Quality (WORKERS)
- **CQS & Context:** [Summary — skeletons, bloat, section completeness]
- **Epistemic Connectivity:** [KB Connectivity sections present?]
- **Verdict:** [✅ PASS | 🟡 PASS WITH WARNINGS | ❌ FAIL]

## Phase 4: Governance & Policy (RULES)
- **HPRF Blocks:** [X/Y rule files have proper HPRF tier blocks]
- **Baseline Files:** [memory-contract.yml, metadata status]
- **Verdict:** [✅ PASS | 🟡 PASS WITH WARNINGS | ❌ FAIL]

## Phase 5: Architecture & Knowledge (FOUNDATION)
- **5-Zone Structure:** [Zone 1-5 completeness, correct data placement]
- **MAS Hierarchy:** [Roster alignment, Interaction Matrix T3↔T3 ban]
- **Epistemic Wiring:** [INDEX coverage, Orphan KBs]
- **Verdict:** [✅ PASS | 🟡 PASS WITH WARNINGS | ❌ FAIL]

## Phase 6: Operational Readiness (RUNTIME)
- **Memory Bus:** [Subscription check results]
- **Golden Tests:** [count — ≥3 required for staging/prod]
- **Verdict:** [✅ PASS | 🟡 PASS WITH WARNINGS | ❌ FAIL]

---

## Per-Component Scan Log (MANDATORY PHYSICAL EVIDENCE)

| Component Name | File Path | Timestamp Checked | Verdict | Evidence / Finding (Specific Line or Issue) |
|---|---|---|---|---|
| `wf-01-example` | `.agents/workflows/...` | 14:02:11 | 🔴 FAIL | Embedded 15 lines of prompt logic (Zero-Native violation) |
| `skill-example` | `.agents/skills/...` | 14:02:15 | ✅ PASS | Fully conforms |
| `[Agent Name]` | `.agents/agents/...` | ... | ... | ... |
*(Must contain EVERY workflow and skill file checked. Failure to log physical evidence invalidates the audit).*

---

## Normalized Scoring Calculation

| Category | Points Earned / Max | Notes |
|----------|------------|---------------|
| **Workflow Quality** | [X] / 30 | [brief note] |
| **Agent & Skill Quality** | [X] / 25 | [brief note] |
| **Arch. Foundation & Rules**| [X] / 20 | [brief note] |
| **Hierarchy** | [X] / 10 | [brief note] |
| **KB Wiring** | [X] / 10 | [brief note] |
| **Operational Core** | [X] / 5 | [brief note] |
| **Total Score** | **[SCORE] / 100 ([GRADE])** | [verdict] |

---

## Remediation Plan

| # | Finding | Severity | Phase | Recommended Fix | SHP Pattern |
|---|---|---|---|---|---|
| 1 | [description] | 🔴/🟡 | Workflow/Skill/Agent/Etc | [action] | SHP-XX |
| 2 | ... | ... | ... | ... | ... |

> **Next Step:** Run `/optimize-workspace` with this report to auto-remediate findings.
```
