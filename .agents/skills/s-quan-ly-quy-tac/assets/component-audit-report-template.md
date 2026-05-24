# Rule Audit Report Templates

> Asset file for the `quan-ly-quy-tac` skill.
> Used by Route 2 (AUDIT) for output formatting and Route 3 (REPAIR) for delta reporting.

---

## Template 1: Rule Scorecard (Route 2 Output)

```markdown
# RULE QUALITY AUDIT — [WORKSPACE_NAME] — [DATE]

## Executive Summary

- **Rule Files Scanned:** [N]
- **Average Rule Health:** [AVG]/100
- **CLEAR Pass Rate:** [X]/[N] files pass ≥3/5 CLEAR dimensions
- **Critical Issues:** [COUNT]
- **Orphan Rules:** [COUNT]

## Rule File Scorecard

| # | Rule File | HPRF Tier | R1 | R2 | R3 | R4 | R5 | Total | Grade | Top Issue |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [filename] | [T1-T3] | [/25] | [/20] | [/25] | [/20] | [/10] | [/100] | [A-F] | [brief] |

## CLEAR Breakdown (Per Rule)

| Rule File | C | L | E | A | R | CLEAR Total | Pass? |
|---|---|---|---|---|---|---|---|
| [filename] | [0/1] | [0/1] | [0/1] | [0/1] | [0/1] | [/5] | [✅/❌] |

## Priority Queue

### 🔴 CRITICAL (Grade D/F)
- [rule file]: [Score] — [Failing dims] → Protocol [RRx]

### ⚠️ REPAIR QUEUE (Grade C)
- [rule file]: [Issue] → Protocol [RRx]

### ✅ MONITOR ONLY (Grade A/B)
- [rule file]: [Note]
```

---

## Template 2: Delta Report (Route 3 Output)

```markdown
# RULE REPAIR REPORT — [rule-filename]

## Before / After

| Metric | Before | After | Delta |
|---|---|---|---|
| **Total Score** | [X]/100 | [Y]/100 | [+Z] |
| **R1 (HPRF)** | [/25] | [/25] | [...] |
| **R2 (Structure)** | [/20] | [/20] | [...] |
| **R3 (CLEAR)** | [/25] | [/25] | [...] |
| **R4 (Specificity)** | [/20] | [/20] | [...] |
| **R5 (Wiring)** | [/10] | [/10] | [...] |

## CLEAR Improvement

| Dim | Before | After |
|---|---|---|
| C (Concrete) | [0/1] | [0/1] |
| L (Leveled) | [0/1] | [0/1] |
| E (Exampled) | [0/1] | [0/1] |
| A (Actionable) | [0/1] | [0/1] |
| R (Ranked) | [0/1] | [0/1] |

## Changes Made
- ✅ [Protocol RRx]: [What was done]

## Files Modified
- [MODIFIED] [file] — [summary]

## Remaining TODOs
- ⚠️ [What needs human action]
```
