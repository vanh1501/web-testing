# Structural Repair Protocols — 5-Zone & Hierarchy Fix Recipes

> Reference document for the `architecture` skill, Route 4 (RESOLVE).
> Contains deterministic fix recipes for all physical structure and hierarchy failures.
> Agent MUST match failure type to protocol before executing repair.
>
> **Framework Position:** Repair targets identified by Route 2 (5-Zone Audit) and Route 3
> (Hierarchy Validation) using `references/5-zone-audit-checklist.md` and
> `references/hierarchy-validation-algorithm.md` respectively.

---

## Protocol Index

| ID | Trigger Condition | Source Route | Severity |
| --- | --- | --- | --- |
| SR1 | Missing Zone directory | Route 2 (5-Zone) | Critical/Warning |
| SR2 | Data placement violation (.context/ contamination) | Route 2 (5-Zone) | Critical |
| SR3 | Minimum content not met (empty zones) | Route 2 (5-Zone) | Critical |
| SR4 | .agents/agents.md roster → SI file mismatch | Route 3 (Hierarchy) | Critical |
| SR5 | Orphan SI files (not in roster) | Route 3 (Hierarchy) | Warning |
| SR6 | T3↔T3 direct communication violation | Route 3 (Hierarchy) | Critical |
| SR7 | Workflow alignment gap (listed but missing, or exists but unlisted) | Route 3 (Hierarchy) | Warning |
| SE1 | Workspace needs new Functional Group (design extension) | Route 1 (Design) | High |
| SE2 | Agent roster needs new Tier 4 specialist | Route 1 (Design) | Medium |

---

## Repair Protocols

### SR1: Missing Zone Directory (5-Zone Gaps)

**Trigger:** Required path from 5-zone-audit-checklist.md does not exist.

**Protocol:**

1. Load `references/5-zone-audit-checklist.md` — identify ALL missing paths.
2. Sort by severity: 🔴 Critical first, 🟡 Warning second.
3. For each missing path:
   - Create directory with proper structure.
   - If Zone 4a (`.agents/`): create standard sub-tree (`agents/`, `quan-ly-quy-tac/`, `workflows/`, `skills/`, `memory_bus/`, `tests/`).
   - If Zone 5 (`.context/`): create `domain/` with empty INDEX.md stub.
   - If Zone 2 (`artifacts/`): create sub-folders (`plans/`, `reports/`, `handoffs/`).
4. Verify: re-scan all zone paths → 0 missing.

### SR2: Data Placement Fix

**Trigger:** Domain data found in `.context/` OR metadata found in `KB/`.

**Protocol:**

1. List all flagged files with current path and violation type.
2. For domain data in `.context/`:
   - Identify correct destination: `KB/domain/[topic-cluster]/`.
   - Move file. Update ALL references across Agent SIs, workflows, INDEX.md.
   - Run `grep_search` for old path → update every reference.
3. For metadata in `KB/`:
   - Identify correct destination: `.context/` or `.context/domain/`.
   - Move file. Update references.
4. Verify: re-scan `.context/` for domain content → 0 violations.

### SR3: Empty Zone Content Fix

**Trigger:** Zone directory exists but fails minimum content check.

**Protocol:**

1. List zones failing minimum content (per 5-zone-audit-checklist.md):
   - `.agents/agents/` needs ≥2 files.
   - `.agents/quan-ly-quy-tac/` needs ≥3 files.
   - `.agents/workflows/` needs ≥3 files.
   - `KB/` needs ≥1 domain file.
2. For each empty/underpopulated zone:
   - If it's an orchestration zone (agents, quan-ly-quy-tac, workflows) → this is a BUILD issue, not pure architecture. Flag for `/create-workspace` or manual intervention.
   - If it's KB → delegate to `kb-architect` (Route 1: CREATE).
3. NEVER generate Agent SI files or Rules from architecture skill. That is `quan-ly-quy-tac` skill's scope. Flag and delegate.

### SR4: Roster-SI File Mismatch

**Trigger:** Agent listed in .agents/agents.md roster but SI file at declared path doesn't exist. Or SI file exists but path in roster is wrong.

**Protocol:**

1. Parse .agents/agents.md roster table → extract (agent_id, si_file_path).
2. For each entry, check `Test-Path(workspace_root + si_file_path)`.
3. If file MISSING:
   - Search `.agents/agents/` recursively for files containing the agent_id.
   - If found at different path → fix .agents/agents.md roster entry to correct path.
   - If truly missing → flag as CRITICAL. Recommend: generate SI stub with `quan-ly-quy-tac` skill (Route 1), or ask user for source.
4. Verify: re-parse roster → 0 mismatches.

### SR5: Orphan SI File Cleanup

**Trigger:** `.md` files in `.agents/agents/` that are NOT referenced by any .agents/agents.md roster entry.

**Protocol:**

1. List all `.md` files in `.agents/agents/` recursively.
2. Cross-reference against .agents/agents.md roster `si_file_path` column.
3. For each orphan file:
   - Read file content. Determine if it's a legitimate agent or leftover artifact.
   - If legitimate → add to .agents/agents.md roster at correct Tier.
   - If artifact/duplicate → move to `tmp/orphans/` (do NOT delete immediately).
   - If unclear → flag for user decision.
4. NEVER auto-delete orphan files. Always move to tmp/ first.

### SR6: T3↔T3 Communication Violation

**Trigger:** Interaction Matrix allows direct T3→T3 communication.

**Protocol:**

1. Parse Interaction Matrix table in .agents/agents.md.
2. For each T3↔T3 cell:
   - If value is NOT "❌ (Via COORD)" or equivalent → violation found.
3. Fix: Update Interaction Matrix cells to enforce Coordinator routing:
   - Replace direct communication markers with "❌ (Via COORD)".
4. Check T3 Agent SI files for direct references to other T3 agents:
   - Search for other Worker agent IDs in SI body.
   - If found → add routing note: "Route cross-domain requests through COORD."
5. Verify: re-scan matrix → 0 T3↔T3 direct cells.

### SR7: Workflow Alignment Repair

**Trigger:** Workflow listed in .agents/agents.md "Core Workflows" but file missing, or workflow file exists but not listed.

**Protocol:**

1. Extract workflow list from .agents/agents.md.
2. List all files in `.agents/workflows/`.
3. For listed-but-missing:
   - Search for similar filenames (typo detection).
   - If found with different name → fix .agents/agents.md reference.
   - If truly missing → flag for creation. Delegate to `workflow-builder` (Route 1).
4. For exists-but-unlisted:
   - Read workflow content. Determine if it's a core operational workflow or utility.
   - If core → add to .agents/agents.md "Core Workflows" section.
   - If utility/optional → leave unlisted (not all workflows need listing).
5. Verify: re-cross-reference → 0 stale references.

---

## Enrichment Scenarios

### SE1: New Functional Group

**Condition:** Workspace needs a new department/capability area.

1. Assess impact: how many new agents needed? Which existing agents interact?
2. Design new group following Enterprise Analogy. Load `references/enterprise-analogy.md`.
3. Create Agent SI stubs in proper `.agents/agents/tier_X/` directory.
4. Update .agents/agents.md: roster table + Interaction Matrix (enforce T3 routing).
5. Delegate SI content generation to `quan-ly-quy-tac` skill.

### SE2: New Specialist Agent

**Condition:** Existing Worker needs a new Tier 4 specialist.

1. Verify parent Worker exists and has capacity (≤5 specialists recommended).
2. Create SI file at `.agents/agents/tier_4_specialist_agent/[worker-dir]/`.
3. Update .agents/agents.md roster with correct parent reference.
4. Verify Interaction Matrix — specialist should only communicate within parent Worker scope.

---

## Batch Priority Matrix

```text
                HIGH Impact              LOW Impact
              (SR2, SR4, SR6)          (SR5, SR7)
  ┌─────────────────────────────┬──────────────────────────┐
  │      DO FIRST               │      BATCH LATER         │
  │  Data placement fix (SR2)   │  Orphan cleanup (SR5)    │
EASY│  Missing zones (SR1)       │  Workflow alignment (SR7)│
FIX │  Roster path fix (SR4)    │  Add to roster (SR5)     │
  ├─────────────────────────────┼──────────────────────────┤
  │      PLAN + CONFIRM         │      DEFER               │
HARD│  T3↔T3 routing fix (SR6) │  New Func Group (SE1)    │
FIX │  Empty zone fill (SR3)   │  New Specialist (SE2)    │
  │  (delegates to other skills)│                          │
  └─────────────────────────────┴──────────────────────────┘
```

**Critical Rule:** Architecture repairs that involve CONTENT creation (Agent SIs, Rules, Workflows) MUST be delegated to the appropriate Resolver skill. Architecture skill handles STRUCTURAL placement only.
