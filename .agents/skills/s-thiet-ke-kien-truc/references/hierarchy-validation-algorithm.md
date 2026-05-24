# Hierarchy Validation Algorithm — .agents/agents.md Cross-Check

> Reference document for the `architecture` skill (Route 3).
> Use during Phase 4 of `/audit-workspace` to verify MAS hierarchy integrity.

---

## Step 1: Parse .agents/agents.md Roster

```
1. Read .agents/agents.md
2. Find the "## Agent Roster" or equivalent table
3. FOR EACH row in roster table:
   EXTRACT: agent_id, tier, role, parent, si_file_path
   ADD to roster_list[]
4. Count agents per tier:
   - Tier 1 (Human): exactly 1
   - Tier 2 (Coordinator): exactly 1
   - Tier 3 (Worker): ≥ 1
   - Tier 4 (Specialist): ≥ 0
```

## Step 2: Physical File Cross-Reference

```
FOR EACH agent IN roster_list:
    physical_path = workspace_root + agent.si_file_path
    IF NOT exists(physical_path):
        ADD finding(🔴 Critical, "Agent {agent.agent_id} listed in roster but SI file missing: {physical_path}")

# Reverse check: orphan files
FOR EACH md_file IN .agents/agents/**/*.md:
    IF md_file NOT referenced by any roster entry:
        ADD finding(🟡 Warning, "Orphan SI file not in roster: {md_file}")
```

## Step 3: Tier Naming Convention Check

```
CHECK Tier 2 agent uses "COORD" suffix or contains "Coordinator" in role
CHECK Tier 3 agents use "W-XX" or "Worker" naming pattern  
CHECK Tier 4 agents reference their parent Worker correctly

IF naming deviates significantly → 🟡 Warning (non-standard but functional)
```

## Step 4: Interaction Matrix Validation

```
1. Find "## Interaction Matrix" table in .agents/agents.md
2. Verify matrix dimensions match roster size (N agents → N×N matrix)
3. FOR EACH cell[T3_worker_A][T3_worker_B] where A ≠ B:
    IF cell value is NOT "❌ (Via COORD)" or equivalent ban marker:
        ADD finding(🔴 Critical, "T3↔T3 direct communication allowed: {A} → {B}")
4. Verify T4 specialists ONLY communicate within their parent T3 domain
```

## Step 5: Core Workflows Alignment

```
1. Find "## Core Workflows" section in .agents/agents.md
2. FOR EACH listed workflow_name:
    physical_path = .agents/workflows/{workflow_name}.md
    IF NOT exists(physical_path):
        ADD finding(🟡 Warning, ".agents/agents.md lists workflow {workflow_name} but file not found")
3. FOR EACH workflow_file IN .agents/workflows/:
    IF workflow_file NOT listed in Core Workflows:
        ADD finding(🟡 Warning, "Workflow {workflow_file} exists but not listed in .agents/agents.md")
```

## Output Schema

```markdown
## Hierarchy Validation Report

| Check | Status | Details |
|---|---|---|
| Roster Completeness | ✅/❌ | [X agents, Y tiers] |
| Physical File Match | ✅/❌ | [missing: list, orphans: list] |
| Naming Convention | ✅/🟡 | [deviations: list] |
| Interaction Matrix | ✅/❌ | [T3↔T3 violations: count] |
| Workflow Alignment | ✅/🟡 | [stale refs: count, unlisted: count] |
```
