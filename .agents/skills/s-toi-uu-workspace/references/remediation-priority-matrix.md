# Remediation Priority Matrix

> Reference document for the `workspace-optimizer` skill.
> Determines the strict execution order and decision quan-ly-quy-tac when planning fixes.

## Priority Levels

| Priority | Layer | Scope | Rule |
|---|---|---|---|
| **P0** | ROOT | 5-Zone directories, data placement, root files (README, QUALITY-LOG) | Fix FIRST. All other layers depend on physical structure. |
| **P1** | TRUNK | Rules (.agents/quan-ly-quy-tac/), memory contracts, .agents/agents.md, HPRF blocks | Fix SECOND. Agents and workflows cannot operate correctly without giam-sat-tuan-thu. |
| **P2** | BRANCH | KB/ wiring, .context/domain/INDEX.md sync, agent-KB connectivity | Fix THIRD. Agents need knowledge access but can function with degraded KB. |
| **P3** | LEAF | Agent SI quality, workflow structure, skills, golden tests | Fix LAST. These are consumers of Root/Trunk/Branch — fixing them first wastes work if the foundation changes. |

## Decision Tree

```
START: Read Audit Remediation Plan
  │
  ├─ Any P0 (ROOT) findings?
  │   ├─ YES → Fix ALL P0 first → Verify Gate → then check P1
  │   └─ NO  → Skip to P1
  │
  ├─ Any P1 (TRUNK) findings?
  │   ├─ YES → Fix ALL P1 → Verify Gate → then check P2
  │   └─ NO  → Skip to P2
  │
  ├─ Any P2 (BRANCH) findings?
  │   ├─ YES → Fix ALL P2 → Verify Gate → then check P3
  │   └─ NO  → Skip to P3
  │
  └─ Any P3 (LEAF) findings?
      ├─ YES → Fix ALL P3 → Final Re-Audit
      └─ NO  → No fixes needed. Log "Clean workspace."
```

## Intra-Layer Ordering Rules

Within each Priority layer, fix items in this sub-order:

### P0 (ROOT) sub-order:
1. Create missing 5-Zone directories (structure must exist before content)
2. Migrate misplaced data (e.g., domain data in .context/ → KB/)
3. Generate missing root files (README.md, QUALITY-LOG.md)
4. **Quarantine floating operational files at workspace root — SHP-24** *(Micro-Healer: root_sweep.py)*
5. **Quarantine stray agent files polluting .agents/agents/ — SHP-25** *(Semi-auto: detect + quarantine, Human confirms deletion)*

### P1 (TRUNK) sub-order:
1. Fix `memory-contract.yml` (security_gate must be intact)
2. Fix `.agents/agents.md` roster (agent names, tiers, routing)
3. Generate missing rule files (safety-guardrails, core-standards)
4. Inject HPRF blocks into rule files missing them

### P2 (BRANCH) sub-order:
1. Sync `.context/domain/INDEX.md` with actual KB/ contents
2. Remove dead links from INDEX
3. Wire agent SI files to KB paths via `## KB Connectivity`

### P3 (LEAF) sub-order:

1. Fix Context Bloat (>15KB SI files → extract to KB, replace with RAG pointer) — SHP-10
2. Fix Agent SI structure (mandatory sections, CLEAR scoring) — SHP-09
3. Fix Ghost Skills (skill exists but nobody references it) — SHP-11
4. Fix Missing Skills (workflow needs skill that doesn't exist) — SHP-12
5. Purge Ghost Files (legacy .md coexisting with SKILL.md) — SHP-19
6. Upgrade Skills to Canonical 4-Tier (references/ + assets/ + evals/) — SHP-16
6.5. **Deep Content Extraction & Enrichment — SHP-23**
     - IF 4-Tier Compliance Score ≥ 7 → SKIP (already compliant)
     - IF Extractability.auto_fixable == true → Execute SHP-23 Auto-Mode
     - IF Extractability.auto_fixable == false → Execute SHP-23 Manual-Mode (emit REMEDIATION_REQUEST.md)
     - IF 4-Tier folders exist but EMPTY → Trigger KB-fulfillment + Web Search enrichment
7. Inject Pushy Persona into flat/generic skills — SHP-17
8. Seed Evals for skills missing evals.json — SHP-22
9. Enforce Zero-Native on workflows with [Native] Skill Targets — SHP-15
10. Consolidate fragmented workflows into Master Pipelines — SHP-18
11. Clean up orphaned workflows replaced by Pipelines — SHP-20
12. Repair Call Graph (sync .agents/agents.md, golden-tests after renames) — SHP-21
13. Fix workflow structure (state checkpoints, recovery params) — SHP-13
14. Generate golden tests if missing — SHP-14

## Escalation Rules

| Blast Radius | Action |
|---|---|
| **Trivial** (typo fix, add example, create new standalone file) | Auto-fix without review |
| **Major** (modify core rule, restructure workflow, add agent to roster) | Create snapshot FIRST, then fix, then verify |
| **Critical** (rename agent ID, delete wired skill, modify memory-contract security_gate) | STOP. Present change plan to Human. Wait for approval. |
