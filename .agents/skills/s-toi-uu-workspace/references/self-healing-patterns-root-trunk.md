# Self-Healing Patterns — ROOT & TRUNK Layer

> Reference document for the `workspace-optimizer` skill.
> Contains deterministic fix recipes for ROOT (P0) and TRUNK (P1) audit failures.
> Agent MUST match the finding to a pattern here before executing. If no pattern matches → log as UNKNOWN_PATTERN and escalate.
>
> **Scope:** Patterns SHP-01 → SHP-09 (Physical Structure & Governance).
> **Companion file:** `self-healing-patterns-branch-leaf.md` (SHP-10 → SHP-26).

---

## Pattern Index

| ID | Finding | Layer | Pattern Name |
|---|---|---|---|
| SHP-01 | Missing 5-Zone directory | ROOT | Directory Scaffold |
| SHP-02 | Domain data in .context/ | ROOT | Data Migration |
| SHP-03 | Missing root file | ROOT | Root File Generation |
| SHP-04 | Missing memory-contract.yml | TRUNK | Contract Generation |
| SHP-05 | Missing security_gate in memory-contract | TRUNK | Security Gate Injection |
| SHP-06 | Rule file missing HPRF block | TRUNK | HPRF Block Injection |
| SHP-07 | .agents/agents.md roster mismatch | TRUNK | Roster Reconciliation |
| SHP-08 | Dead links in INDEX.md | BRANCH | Index Sync |
| SHP-09 | Agent SI missing KB connectivity | BRANCH | KB Wiring |

---

## Pattern Details

### SHP-01: Directory Scaffold
**Symptom**: One or more 5-Zone directories do not exist on disk.
**Fix**:
1. Create the missing directory path.
2. Add a `.gitkeep` file inside if the directory is expected to be empty initially.
3. Verify the directory exists after creation.

### SHP-02: Data Migration
**Symptom**: `.context/` contains domain knowledge files (methodology, templates, raw data) instead of only metadata.
**Fix**:
1. Identify the correct destination subfolder within `KB/` (match by domain topic).
2. Copy each file to `KB/[subfolder]/`. Verify byte count matches.
3. Delete the source file from `.context/`.
4. Update `.context/domain/INDEX.md` to point to the new `KB/` path.
5. Run `grep_search` for the old `.context/` path → update all references.

### SHP-03: Root File Generation
**Symptom**: `README.md`, `QUALITY-LOG.md`, or `IMPROVEMENT-BACKLOG.md` missing at workspace root.
**Fix**:
1. Read `.agents/agents.md` to extract workspace identity (name, purpose, team).
2. Generate the missing file with standard template header.
3. For `QUALITY-LOG.md`: include the column header `| Date | Agent | Action | Score | Detail |`.

### SHP-04: Contract Generation
**Symptom**: `.agents/memory_bus/memory-contract.yml` does not exist.
**Fix**:
1. Read `.agents/agents.md` to map the full agent roster with tiers.
2. Read `.agents/memory_bus/keys.yaml` to identify domain keys.
3. Generate `memory-contract.yml` with:
   - `security_gate.write_lock: true`
   - `security_gate.lock_provider: state.json`
   - Domain → Writer mapping derived from agent roster.
   - `conflict_quan-ly-quy-tac` for parallel write protection.

### SHP-05: Security Gate Injection
**Symptom**: `memory-contract.yml` exists but is missing the `security_gate` block.
**Fix**:
1. Prepend the standard security_gate block:
   ```yaml
   security_gate:
     write_lock: true
     lock_provider: state.json
     unauthorized_write_action: reject_and_log
   ```
2. Verify the YAML is valid after injection.

### SHP-06: HPRF Block Injection
**Symptom**: A rule file in `.agents/quan-ly-quy-tac/` is missing the `> [!IMPORTANT] Override Priority:` preamble.
**Fix**:
1. Determine the file's tier classification:
   - Constitution/Protocol → Tier 1
   - Orchestration/Standards → Tier 2
   - Domain/Specs → Tier 3
2. Inject the corresponding HPRF block at the top of the file (after any YAML frontmatter).

### SHP-07: Roster Reconciliation
**Symptom**: Files in `.agents/agents/` do not match the roster in `.agents/agents.md`.
**Fix**:
1. List all `.md` files in `.agents/agents/` (recursive).
2. Extract all agent IDs from `.agents/agents.md` roster table.
3. For each undocumented file → add to .agents/agents.md roster (determine Tier from file content).
4. For each roster entry without a file → flag as Ghost Agent for Human review.

### SHP-08: Index Sync
**Symptom**: `.context/domain/INDEX.md` contains dead links or is missing KB entries.
**Fix**:
1. List all files in `KB/` recursively.
2. Compare against entries in INDEX.md.
3. Remove entries pointing to non-existent files.
4. Add entries for files not yet indexed.

### SHP-09: KB Wiring
**Symptom**: Agent SI file lacks a `## KB Connectivity` section or has no `view_file` instruction for its domain KB.
**Fix**:
1. Identify which `KB/[subfolder]` maps to this agent's domain (from .agents/agents.md functional group).
2. Append a `## KB Connectivity` section with explicit `view_file` instructions pointing to the specific KB path.
