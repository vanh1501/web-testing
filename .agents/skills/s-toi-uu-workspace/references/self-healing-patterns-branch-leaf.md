# Self-Healing Patterns — BRANCH & LEAF Layer

> Reference document for the `workspace-optimizer` skill.
> Contains deterministic fix recipes for BRANCH (P2) and LEAF (P3) audit failures.
> Agent MUST match the finding to a pattern here before executing. If no pattern matches → log as UNKNOWN_PATTERN and escalate.
>
> **Scope:** Patterns SHP-10 → SHP-26 (Content Quality & Enrichment).
> **Companion file:** `self-healing-patterns-root-trunk.md` (SHP-01 → SHP-09).

---

## Pattern Index

| ID | Finding | Layer | Pattern Name |
|---|---|---|---|
| SHP-10 | Agent SI > 15KB (Context Bloat) | LEAF | Bloat Extraction |
| SHP-11 | Ghost Skill (unwired) | LEAF | Skill Wiring |
| SHP-12 | Missing required Skill | LEAF | Skill Provisioning |
| SHP-13 | Workflow missing state checkpoints | LEAF | Workflow Hardening |
| SHP-14 | Missing golden tests | LEAF | Test Seeding |
| SHP-15 | Workflow has [Native] Skill Target | LEAF | Zero-Native Enforcement |
| SHP-16 | Skill missing 4-Tier structure | LEAF | Canonical 4-Tier Upgrade |
| SHP-17 | Skill SKILL.md is flat/generic persona | LEAF | Pushy Persona Injection |
| SHP-18 | Multiple <3-step workflows overlap | LEAF | Pipeline Consolidation |
| SHP-19 | Legacy .md file coexists with SKILL.md | LEAF | Ghost File Purge |
| SHP-20 | Workflow replaced by Master Pipeline | LEAF | Orphan Workflow Cleanup |
| SHP-21 | .agents/agents.md workflow list stale after rename | LEAF | Call Graph Repair |
| SHP-22 | Skill missing evals/evals.json | LEAF | Evals Seeding |
| SHP-23 | Skill fails 4-Tier Compliance (<7/10) with extractable content | LEAF | Deep Content Extraction & 4-Tier Enrichment |
| SHP-24 | Floating operational files at workspace root | ROOT | Root Floating File Quarantine |
| SHP-25 | Agent pollution in .agents/agents/ | ROOT | Agent Pollution Quarantine |
| SHP-26 | Skill folder missing canonical subdirectories | LEAF | Mandatory Pre-Scaffold Enforcement |

---

## Pattern Details

### SHP-10: Bloat Extraction
**Symptom**: Agent SI file exceeds 15KB.
**Fix**:
1. Parse the SI file for embedded inline templates, long examples, or verbose methodology (>20 lines).
2. Extract each bloc to `KB/templates/[agent_name]_[topic].md`.
3. Replace original text with a RAG pointer: `> Load: view_file KB/templates/[agent_name]_[topic].md`.
4. Verify file size is now < 15KB.

### SHP-11: Skill Wiring
**Symptom**: A skill exists in `.agents/skills/[name]/SKILL.md` but no workflow or agent references it.
**Fix**:
1. Read the skill's `description` to understand its purpose.
2. Scan `.agents/workflows/` and `.agents/agents/` for the most semantically relevant file.
3. Inject `## Assigned Skills` block referencing the skill's Canonical ID.
4. Register the skill in `00_SKILL_INDEX.md` if not already present.

### SHP-12: Skill Provisioning
**Symptom**: A workflow/agent references a skill that does not exist on disk.
**Fix**:
1. Invoke the `skill-writer` skill to generate a Canonical 4-Tier skill.
2. Save to `.agents/skills/[skill-id]/`.
3. Register in `00_SKILL_INDEX.md`.

> [!CAUTION] POST-FIX SIZE GATE (v2.0 — Anti-Hollow-Skeleton)
> After generating a new skill, the agent MUST verify:
> - `SKILL.md` file size ≥ 1.0KB. If < 1.0KB → REJECT output as "Hollow Skeleton" and REWORK.
> - `SKILL.md` MUST contain at minimum: YAML frontmatter + `## Process` section with ≥3 actionable steps.
> - Empty YAML-only files are a SYSTEMIC-HALT violation.

### SHP-13: Workflow Hardening
**Symptom**: Workflow lacks state checkpoint logic or recovery parameters.
**Fix**:
1. Add `> [!CAUTION] Recovery:` block with rollback instructions.
2. Add checkpoint step referencing `/checkpoint-session` at logical milestones.

### SHP-14: Test Seeding

**Symptom**: `.agents/tests/golden-tests.md` is missing or has 0 test cases.

**Fix**:

1. Read the workspace's core workflows to identify primary happy-path scenarios.
2. Generate 3-5 golden test cases with Input → Expected Output → Pass Criteria.
3. Save to `.agents/tests/golden-tests.md`.

### SHP-15: Zero-Native Workflow Enforcement

**Symptom**: A workflow step declares `🛠 Skill Target: [Native]` or contains >20 lines of hardcoded execution logic (prompts, frameworks, step-by-step domain instructions).

**Fix**:

1. Identify the domain logic embedded in the workflow.
2. Determine which existing skill should own this logic (or create one via SHP-12).
3. Extract the logic into the skill's `references/` or `assets/` directory.
4. Replace the Native execution block with a routing reference: `🛠 Skill Target: [skill-name]`.
5. Verify the workflow body is now ≤ routing + gate checks, no domain payload.

### SHP-16: Canonical 4-Tier Skill Upgrade

**Symptom**: A skill folder contains only `SKILL.md` without `references/`, `assets/`, or `evals/` subdirectories. Or SKILL.md lacks the Canonical sections (ROLE, PURPOSE, PROCESS, RESOURCES, QA, RULES).

**Fix**:

1. Create missing subdirectories: `references/`, `assets/`, `evals/`.
2. If SKILL.md is in legacy format (flat `## Description` + `## Instructions`), rewrite to Canonical format: `## ROLE`, `## PURPOSE`, `## PROCESS`, `## OUTPUT FORMAT`, `## RESOURCES`, `## QA`, `## RULES`.
3. Extract any domain knowledge >4 lines into `references/[topic].md`.
4. Extract any output templates into `assets/[template].md`.
5. Generate a minimal `evals/evals.json` with ≥1 happy-path test case (see SHP-22).
6. Verify SKILL.md is now routing-focused and ≤ 500 lines.

> [!CAUTION] POST-FIX SIZE GATE (v2.0 — Anti-Hollow-Skeleton)
> After upgrading a skill to 4-Tier, the agent MUST verify:
> - `SKILL.md` file size ≥ 1.0KB. If < 1.0KB → REJECT and REWORK with domain payload.
> - At least 1 file in `references/` directory (not just `.gitkeep`).
> - Hollow scaffolding (directories exist but ALL empty) is NOT considered compliant.

### SHP-17: Pushy Persona Injection

**Symptom**: A skill's SKILL.md uses generic/passive language ("You should try to...", "Consider doing...") instead of pushy, expert-driven commands.

**Fix**:

1. Rewrite `## ROLE` to use a specific expert persona title (e.g., "Senior OBE Compliance Auditor", "Kế Toán Trưởng Kiểm Định").
2. Replace all passive verbs with imperative commands: "Use X", "Execute Y", "REJECT if Z".
3. Add explicit rejection criteria in `## RULES`: "REJECT if input lacks...", "CẤM...", "KHÔNG chấp nhận...".
4. Add the 3-Strike Escalation reference if the skill handles iterative tasks.
5. Verify persona does NOT leak into Agent SI (Persona belongs in SKILL.md for domain skills, SI for identity).

### SHP-18: Pipeline Consolidation

**Symptom**: Multiple workflows with <3 steps each cover overlapping domain areas (e.g., `/design-plo`, `/map-curriculum`, `/generate-bdmo` all serve the same curriculum pipeline).

**Fix**:

1. Identify the logical grouping: which workflows are sequential steps of the same business process?
2. Create a single Master Pipeline workflow (e.g., `build-ctdt-pipeline.md`) that orchestrates the sequence.
3. Each former sub-workflow becomes a Step in the Master Pipeline, routing to the appropriate skill.
4. Delete the redundant sub-workflows.
5. Update .agents/agents.md "Core Workflows" section to list only Master Pipelines.
6. Update golden-tests.md to reference new pipeline names.

### SHP-19: Ghost File Purge

**Symptom**: A legacy `.md` file (e.g., `skill-name.md`) coexists alongside the new `SKILL.md` in the same skill folder, causing confusion about which file is authoritative.

**Fix**:

1. Verify `SKILL.md` contains complete, production-ready content (not a skeleton).
2. Compare legacy file content with SKILL.md — extract any unique domain knowledge NOT in SKILL.md into `references/`.
3. Delete the legacy file.
4. Run `grep_search` for the legacy filename across all workflows and agents to ensure no stale references.

### SHP-20: Orphan Workflow Cleanup

**Symptom**: A workflow file exists on disk but has been functionally replaced by a Master Pipeline (SHP-18). No agent or other workflow references it.

**Fix**:

1. Confirm the workflow is truly orphaned: `grep_search` for its filename and trigger name across `.agents/agents/`, `.agents/workflows/`, and `.agents/agents.md`.
2. If 0 references found AND a Master Pipeline covers its functionality → delete the file.
3. Log deletion in `QUALITY-LOG.md`.
4. If references exist → update them to point to the Master Pipeline first, then delete.

### SHP-21: Call Graph Repair

**Symptom**: After renaming/consolidating workflows (SHP-18/SHP-20), references in `.agents/agents.md`, Agent SIs, and `golden-tests.md` still use old workflow names.

**Fix**:

1. Build a rename map: `{old_workflow_name → new_pipeline_name}`.
2. Run `grep_search` for each old name across ALL workspace files.
3. Replace every occurrence with the new pipeline name.
4. Special attention: `.agents/agents.md` "Core Workflows" section, `golden-tests.md` Component fields, Agent SI "Workflows Bắt Buộc" sections.
5. Verify 0 stale references remain after replacement.

### SHP-22: Evals Seeding

**Symptom**: A skill folder's `evals/evals.json` is missing or empty.

**Fix**:

1. Read the skill's `## PROCESS` section to identify primary function.
2. Generate `evals/evals.json` with minimum 2 test cases:

```json
{
  "skill": "[skill-name]",
  "version": "1.0",
  "test_cases": [
    {
      "id": "TC-01",
      "type": "happy_path",
      "input": "[description of valid input]",
      "expected_output": "[description of expected output]",
      "pass_criteria": "[measurable criteria]"
    },
    {
      "id": "TC-02",
      "type": "violation",
      "input": "[description of invalid input]",
      "expected_output": "REJECT or ERROR with specific message",
      "pass_criteria": "[rejection correctly triggered]"
    }
  ]
}
```

3. Save to `.agents/skills/[skill-name]/evals/evals.json`.

### SHP-23: Deep Content Extraction & 4-Tier Enrichment

**Symptom**: SKILL.md contains embedded passive knowledge (tables, formulas, templates, examples, dictionaries) that should be in `references/` or `assets/`. Audit's Extractability Analysis (CQS Tầng 3) returns `extractable: true` and/or 4-Tier Compliance Score < 7.

**Pre-Condition**: The CQS Validation Engine has produced an Extractability Report for this skill with classified `extraction_targets`.

**Fix (Auto-Mode — when ALL `extraction_targets` have `auto_fixable: true`):**

1. Parse the Extractability Report's `extraction_targets` array.
2. For each target:
   a. Read the source lines from SKILL.md (specified in `source_lines`).
   b. Write them into the designated path (`references/[topic].md` or `assets/[template].md`).
   c. Remove the source lines from SKILL.md.
   d. Add a corresponding entry to the `## RESOURCES` routing table in SKILL.md.
3. If `## RESOURCES` section does not exist in SKILL.md, create it with a standard table header:
   ```
   ## RESOURCES
   | Situation | Load |
   |---|---|
   ```
4. Verify SKILL.md line count is now ≤ 500.
5. If `evals/evals.json` is missing or contains generic placeholders → chain to SHP-22 (Evals Seeding).
6. If `references/` was populated from extraction but SKILL.md still lacks `## WHEN TO CLARIFY` or `## QA` → inject minimal stubs to pass Tầng 2.

**Fix (Manual-Mode — when ANY `extraction_target` has `auto_fixable: false`):**

1. Generate a `REMEDIATION_REQUEST.md` artifact using `assets/remediation-request-template.md` with:
   - Skill name, current 4-Tier Compliance Score, and Extractability Report summary.
   - List of specific ambiguous areas flagged (with exact line numbers and quoted content).
   - Proposed extraction plan for Human review (best-effort draft).
   - Three action options: `[A] Approve auto-extraction as-is`, `[B] Manually restructure`, `[C] Defer`.
2. Queue the request in `artifacts/handoffs/QUEUE.md` with priority `P3-MANUAL`.
3. **HALT processing for THIS specific skill only** — continue SHP-23 execution for remaining skills in the batch.
4. When Human responds:
   - If `[A]`: Re-execute Auto-Mode treating all targets as `auto_fixable: true`.
   - If `[B]`: Log as `HUMAN_MANUAL_FIX` → monitor for completion in next audit cycle.
   - If `[C]`: Log as `DEFERRED` with timestamp → re-surface in 30 days.

**Fix (Empty-Shell-Mode — when 4-Tier folders exist but are EMPTY):**

1. Check if workspace has a `knowledge/` or `KB/` directory with relevant KI files.
2. If matching KI files found → Copy them into the skill's `references/` directory.
3. If no matching KI files → Trigger web search to populate `references/` with domain-authoritative content.
4. After enrichment, generate the `## RESOURCES` routing table mapping to the newly created files.
5. Regenerate `evals/evals.json` with domain-specific test cases (not generic placeholders).

### SHP-24: Root Floating File Quarantine

**Symptom**: Heuristic scanner (Phase 0) detects `.py`, `.sh`, `.csv`, `.json`, `.log`, `.txt` files at the workspace root directory. These are operational artifacts that violate the Zero-Floating Law (Phase 5d).

**Fix**:

1. Create `tmp/` directory if it does not exist.
2. Move each floating file to `tmp/[filename]`.
3. Run `grep_search` to check if any workflow/skill/agent references the file by filename.
4. If referenced → update all references to point to `tmp/[filename]`.
5. Log each relocation in `QUALITY-LOG.md`.

**Micro-Healer**: `.agents/skills/qa/scripts/micro_healers/root_sweep.py`
**Automation Level**: Fully auto-fixable.

### SHP-25: Agent Pollution Quarantine

**Symptom**: `.agents/agents/` root directory contains `.md` files that do not belong to the workspace's .agents/agents.md hierarchy. Typically caused by deploying a child workspace's agents into the meta-workspace accidentally.

**Fix**:

1. Read `.agents/agents.md` roster to build the known-agents set (all GOV-* IDs).
2. List all `.md` files directly at `.agents/agents/` root (not in tier subdirectories).
3. For each file NOT matching a known agent ID:
   a. Read file content to detect signs of origin workspace (domain-specific quan-ly-quy-tac, role names).
   b. Move file to `tmp/quarantine/[filename]`.
   c. Log in `QUALITY-LOG.md` with origin analysis.
4. If file IS a known agent but placed at root instead of its tier subdirectory → relocate to correct tier dir.

**Micro-Healer**: Semi-automatic. Scanner detects; Human confirms origin before deletion.
**Automation Level**: Detection = auto. Quarantine = auto. Deletion = requires Human approval.

### SHP-26: Mandatory Pre-Scaffold Enforcement

**Symptom**: A skill's `SKILL.md` exists but the skill folder is missing ≥1 of the canonical 4-Tier subdirectories (`assets/`, `references/`, `evals/`, `scripts/`). This is distinct from SHP-16 (which handles content-level fixes) — SHP-26 enforces the **physical temporal constraint** that directories MUST exist BEFORE any content-level remediation can proceed.

**Pre-Condition**: This pattern MUST execute BEFORE SHP-16 and SHP-23 in the LEAF remediation sub-order.

**Fix**:

1. For EACH skill folder that has `SKILL.md` but is missing subdirectories:
   a. Create all 4 required directories: `assets/`, `references/`, `evals/`, `scripts/`.
   b. Place a `.gitkeep` in each empty directory for Git tracking.
2. Verify all 4 directories exist on disk after creation.
3. Only then proceed to SHP-16/SHP-23 for content-level enrichment.

**Micro-Healer**: `.agents/skills/qa/scripts/micro_healers/skill_scaffold.py`
**Automation Level**: Fully auto-fixable.
