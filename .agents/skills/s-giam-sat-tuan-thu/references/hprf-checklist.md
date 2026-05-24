# HPRF (Hierarchical Priority Resolution Framework) Checklist

This document defines the 4-block requirement for any valid HPRF Tier declaration in MAS workspace rule files.
When auditing `giam-sat-tuan-thu` Gate 1, verify that every `.agents/quan-ly-quy-tac/` file contains this exact Markdown block.

## The 4-Block Requirement

Every rule file MUST start with a block containing these 4 key-value pairs:

```markdown
> Override Priority: [Tier 0/1/2/3]
> Conflict Resolution: [Yields to Tier X / Overrides Tier Y]
> Execution Scope: [Global / Domain-Specific]
> Anti-Loop Breaker: [Condition to break rule loop]
```

## Definition of Tiers

- **Tier 0 (L0)**: Constitutional quan-ly-quy-tac. Immutable. Overrides all.
- **Tier 1 (L1)**: Workspace/Domain core quan-ly-quy-tac. Yields to L0, overrides all agent SIs.
- **Tier 2 (L2)**: Workflow-specific quan-ly-quy-tac. Yields to L0 and L1.
- **Tier 3 (L3)**: Ad-hoc task quan-ly-quy-tac. Lowest priority.

## Audit Violation Triggers

1. **Missing Block**: Any rule file without the `Override Priority:` block is a `🔴 [LOCAL-FIX]`.
2. **Invalid Tier**: If a rule file claims Tier 0 but is not one of the canonical 4 L0 files, it is a `🔴 [SYSTEMIC-HALT]`.
3. **Missing Anti-Loop**: If `Anti-Loop Breaker` is missing or empty, it is a `🟡 [WARNING]`.
