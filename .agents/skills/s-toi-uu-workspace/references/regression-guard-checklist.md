# Regression Guard Checklist

> Reference document for the `workspace-optimizer` skill.
> Execute this 9-point checklist AFTER completing fixes in each architectural layer.
> All 9 checks MUST pass before proceeding to the next layer.

---

## Pre-Condition

- All planned fixes for the current layer have been applied.
- The Verify Gate (re-audit of the corresponding Phase) has passed.

## Checklist

### 1. Path Integrity Check
- Run `grep_search` for the OLD path/name of every file that was moved, renamed, or deleted.
- Expected result: **0 matches** (no orphan references remain).
- If matches found → update those references immediately.

### 2. Downstream Reference Check
- For every entity modified (rule file, agent ID, skill name, KB file):
  - Search ALL `.agents/workflows/`, `.agents/agents/`, `.agents/quan-ly-quy-tac/`, `.agents/skills/` for references.
  - Verify each reference points to the CURRENT (post-fix) location/name.
- If stale references found → update in the same session.

### 3. YAML Validity Check
- For every `.yml` or `.yaml` file modified: verify it parses without error.
- Key files: `memory-contract.yml`, `keys.yaml`, `state.json`.
- If parse error → fix syntax immediately.

### 4. Memory Bus Consistency Check
- Verify `state.json` is valid JSON.
- Verify `ledger.md` has a proper table header and no orphan rows.
- Verify `keys.yaml` domain keys still match `memory-contract.yml` domains.

### 5. Agent SI Size Check
- Verify NO Agent SI file exceeds 15KB after fixes.
- If any file grew due to injected sections → apply SHP-10 (Bloat Extraction).

### 6. Skill Wiring Check
- Verify `00_SKILL_INDEX.md` (if exists) lists ALL skills in `.agents/skills/`.
- Verify every `## Assigned Skills` block in workflows references an existing skill folder.
- If phantom references found → either create the skill or remove the reference.

### 7. Workflow Routing Check
- Verify `workflow-routing.md` (if exists) contains entries for ALL workflows in `.agents/workflows/`.
- Verify each routing entry has at least 1 keyword trigger.

### 8. No-Deletion Audit Trail
- For every file DELETED during this session:
  - Confirm it was logged in `QUALITY-LOG.md` with reason.
  - Confirm a snapshot was taken BEFORE the deletion.
  - Confirm no active workflow or agent references the deleted file.

### 9. Output Size Gate (Anti-Hollow-Skeleton)
- For every file CREATED or MODIFIED during this session:
  - Verify `SKILL.md` files are ≥ 1.0KB. If < 1.0KB → flag as **Hollow Skeleton** and REJECT.
  - Verify `SKILL.md` files contain at minimum: YAML frontmatter + `## Process` section with ≥3 actionable steps.
  - Verify rule files (`.agents/quan-ly-quy-tac/*.md`) are ≥ 0.5KB.
  - Empty YAML-only files or files with only frontmatter headers are a SYSTEMIC-HALT violation.
- **Rationale:** This check was added after the AMYHair_CRM_ERP incident (2026-05-09) where 6 domain skills passed all other checks despite being completely empty (only YAML headers, ~400 bytes each).

## Pass/Fail Criteria

| Result | Action |
|---|---|
| All 9 checks PASS | Proceed to next layer or close session |
| 1-2 checks FAIL (minor) | Fix inline, re-run failed checks only |
| 3+ checks FAIL | STOP. Log as `REGRESSION_DETECTED`. Escalate to Human. Consider `/restoresnapshot`. |
