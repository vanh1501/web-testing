# Workflow Audit & Repair Report Templates

> Asset file for the `tao-quy-trinh-moi` skill.
> Used by Route 2 (ASSESS) for output formatting and Route 3 (RESOLVE) for delta reporting.

---

## Template 1: Batch Scorecard (Route 2 Output)

```markdown
# WORKFLOW LIBRARY AUDIT REPORT — [WORKSPACE_NAME] — [DATE]

## Executive Summary

- **Workflows Scanned:** [N]
- **Library Health Score:** [AVG]/100
- **Library Status:** [HEALTHY / AT_RISK / DEGRADED]
- **Critical Issues:** [COUNT]
- **A-ESOAR Coverage:** [X]/[Y] R-steps covered ([Z]%)
- **Requested by:** [WORKFLOW_NAME or "standalone"]

## Scorecard

| # | Workflow | Type | W1 | W2 | W3 | W4 | W5 | W6 | Total | Grade | Top Issue |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [name] | [INFRA/CORE/SUPPORT/META] | [/15] | [/20] | [/20] | [/20] | [/15] | [/10] | [/100] | [A-F] | [brief] |

## Priority Queue

### 🔴 CRITICAL (Grade D/F — Fix immediately)
- [workflow]: [Score] — [Failing dimensions]

### ⚠️ REPAIR QUEUE (Grade C — Fix this session)
- [workflow]: [Issue summary]

### 🔶 ENRICH QUEUE (Coverage gaps / unadapted infra)
- [R-step without workflow] or [unadapted template]

### ✅ MONITOR ONLY (Grade A/B)
- [workflow]: [Minor note]

## A-ESOAR Coverage Matrix

| R-Step | Description | Workflow Exists? | Workflow Name | Status |
|---|---|---|---|---|
| R1 | [desc] | ✅ / ❌ | [name or "MISSING"] | [OK / GAP] |
```

---

## Template 2: Single Workflow Deep Assessment (Route 2 — Detail Mode)

```markdown
# WORKFLOW ASSESSMENT — [workflow-name]

## Classification
- **Type:** [INFRA / CORE / SUPPORT / META]
- **File Size:** [N] characters
- **Total Steps:** [N]
- **Decision Points:** [N]
- **Skill References:** [N]

## Scoring Breakdown

| Dim | Dimension | Score | Max | Evidence |
|---|---|---|---|---|
| W1 | Frontmatter Quality | [X] | 15 | [finding] |
| W2 | Metadata Completeness | [X] | 20 | [finding] |
| W3 | Execution Depth | [X] | 20 | [finding] |
| W4 | Skill Wiring | [X] | 20 | [finding] |
| W5 | Zero-Native Compliance | [X] | 15 | [finding] |
| W6 | Context Budget | [X] | 10 | [finding] |
| | **TOTAL** | **[X]** | **100** | **Grade: [A-F]** |

## Findings

### 🔴 Critical
- [Finding with evidence and root cause]

### 🟡 Warning
- [Finding with evidence]

### ✅ Strengths
- [What the workflow does well]

## Recommended Actions
1. [Action] — Protocol [WR1-WR6 / WE1-WE2]
```

---

## Template 3: Delta Report (Route 3 Output — After Repair)

```markdown
# WORKFLOW REPAIR REPORT — [workflow-name]

## Before / After

| Metric | Before | After | Delta |
|---|---|---|---|
| **Total Score** | [X]/100 ([Grade]) | [Y]/100 ([Grade]) | [+Z] |
| **W1 Frontmatter** | [X]/15 | [Y]/15 | [+Z] |
| **W2 Metadata** | [X]/20 | [Y]/20 | [+Z] |
| **W3 Execution** | [X]/20 | [Y]/20 | [+Z] |
| **W4 Skill Wiring** | [X]/20 | [Y]/20 | [+Z] |
| **W5 Zero-Native** | [X]/15 | [Y]/15 | [+Z] |
| **W6 Budget** | [X]/10 | [Y]/10 | [+Z] |

## Changes Made
- ✅ [Protocol ID]: [What was done]

## Files Created/Modified
- [MODIFIED] `[workflow-file].md` — [summary]
- [NEW] `[skill or reference file]` — [if created during WR5 extraction]

## Remaining TODOs (Human Action Required)
- ⚠️ [What could not be auto-resolved and why]
```
