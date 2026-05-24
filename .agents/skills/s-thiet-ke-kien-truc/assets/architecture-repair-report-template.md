# Architecture Repair Report Template

> Asset file for the `architecture` skill.
> Template for Route 4 (RESOLVE) output — delta reports for structural and hierarchy fixes.

---

## Template 1: Structural Repair Report

```markdown
# Architecture Repair Report — [Workspace Name]

**Date:** [YYYY-MM-DD]
**Pre-Audit Source:** `/audit-workspace` Phase 2 + Phase 4
**Workspace:** `[path]`

## 5-Zone Fixes

| # | Protocol | Target | Action | Status |
|---|---|---|---|---|
| 1 | SR1 | [missing path] | Created directory | ✅ |
| 2 | SR2 | [misplaced file] | Moved to [correct zone] | ✅ |

## Hierarchy Fixes

| # | Protocol | Target | Action | Status |
|---|---|---|---|---|
| 1 | SR4 | [agent_id] | Fixed SI path in .agents/agents.md | ✅ |
| 2 | SR6 | [T3↔T3 cell] | Enforced COORD routing | ✅ |

## Cross-References Updated

| File | Old Reference | New Reference |
|---|---|---|
| [file path] | [old path] | [new path] |

## Delegated to Other Resolvers

| Finding | Delegated To | Reason |
|---|---|---|
| Empty `.agents/quan-ly-quy-tac/` | `quan-ly-quy-tac` skill | Content creation is quan-ly-quy-tac scope |
| KB coverage gap | `kb-architect` skill | KB design is kb-architect scope |

## Remaining Issues

- [ ] [issue requiring human decision]

## Pre/Post Score Comparison

| Check Area | Before | After |
|---|---|---|
| 5-Zone Compliance | [X]/[Y] checks passed | [X]/[Y] checks passed |
| Hierarchy Validation | [X]/[Y] checks passed | [X]/[Y] checks passed |
| Data Placement | [N] violations | [N] violations |
```
