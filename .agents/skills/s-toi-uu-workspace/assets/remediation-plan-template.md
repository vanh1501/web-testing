# Remediation Plan Template

> Use this template to structure the remediation plan before executing any fixes.
> Fill in each section after completing the Triage & Classify phase.

---

## Session Info

| Field | Value |
|---|---|
| **Workspace** | [workspace name] |
| **Audit Report** | [path to Executive_Audit_Report.md] |
| **Pre-Optimize Score** | [Grade] ([Score]/100) |
| **Date** | [YYYY-MM-DD] |
| **Operator** | [Agent ID or Human name] |

---

## Findings Summary

| # | Finding | Severity | Layer | Priority | Blast Radius |
|---|---|---|---|---|---|
| 1 | [description] | 🔴/🟡/🟢 | ROOT/TRUNK/BRANCH/LEAF | P0/P1/P2/P3 | Trivial/Major/Critical |
| 2 | ... | ... | ... | ... | ... |

---

## Execution Plan (Top-Down Order)

### P0 — ROOT Layer

| # | Fix Action | Pattern ID | Estimated Impact | Status |
|---|---|---|---|---|
| 1 | [action] | SHP-XX | [files affected] | ⬜ Pending |

**Verify Gate**: Re-run Audit Phase 2 checks after all P0 fixes.

### P1 — TRUNK Layer

| # | Fix Action | Pattern ID | Estimated Impact | Status |
|---|---|---|---|---|
| 1 | [action] | SHP-XX | [files affected] | ⬜ Pending |

**Verify Gate**: Re-run Audit Phase 3-4 checks after all P1 fixes.

### P2 — BRANCH Layer

| # | Fix Action | Pattern ID | Estimated Impact | Status |
|---|---|---|---|---|
| 1 | [action] | SHP-XX | [files affected] | ⬜ Pending |

**Verify Gate**: Re-run Audit Phase 5 checks after all P2 fixes.

### P3 — LEAF Layer

| # | Fix Action | Pattern ID | Estimated Impact | Status |
|---|---|---|---|---|
| 1 | [action] | SHP-XX | [files affected] | ⬜ Pending |

**Verify Gate**: Re-run Audit Phase 6-7 checks after all P3 fixes.

---

## Escalation Log

| # | Finding | Reason for Escalation | Human Decision | Resolution |
|---|---|---|---|---|
| 1 | [description] | [why auto-fix is unsafe] | ⬜ Pending | — |

---

## Post-Optimize Summary

| Metric | Value |
|---|---|
| **Post-Optimize Score** | [Grade] ([Score]/100) |
| **Delta** | +[X] points |
| **Total Fixes Applied** | [count] |
| **Regressions Detected** | [count] |
| **Escalated Items** | [count] |
| **Status** | Operational / Needs Follow-up / Escalated |
