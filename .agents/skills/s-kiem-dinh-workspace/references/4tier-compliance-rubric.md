# 4-Tier Compliance Rubric — Skill Maturity Scoring

> Reference document for the `qa` skill.
> Loaded during Phase 2d of `/audit-workspace` to score each skill's structural maturity.
> The CQS Validation Engine (Tầng 2) uses this rubric to compute COMPLIANCE_SCORE [0-10].

---

## Scoring Categories

### Category A: Physical Structure (4 points)

| Check | Condition | Points | Failure Indicator |
| --- | --- | --- | --- |
| A1 | `references/` directory exists AND contains ≥1 `.md` file with >500 bytes | +1 | Empty or missing references = no domain knowledge grounding |
| A2 | `assets/` directory exists AND contains ≥1 file (any format: .md, .yaml, .json, .js) | +1 | No output templates = skill cannot produce standardized outputs |
| A3 | `evals/evals.json` exists, is valid JSON, and contains ≥2 test cases (≥1 happy_path, ≥1 violation) | +1 | No evals = skill behavior is untested and non-deterministic |
| A4 | `scripts/` directory exists (may be empty if no automation needed) | +1 | Missing scaffolding = incomplete 4-Tier migration |

### Category B: SKILL.md Body Compliance (4 points)

| Check | Condition | Points | Failure Indicator |
| --- | --- | --- | --- |
| B1 | `## RESOURCES` section exists with a pipe-table containing "Situation" and "Load" columns | +1 | No routing table = SKILL.md cannot dynamically load domain knowledge |
| B2 | `## QA` section exists with ≥3 checkbox items (`- [ ]`) | +1 | No self-check = skill has no built-in quality gate |
| B3 | `## WHEN TO CLARIFY` section exists with ≥1 question | +1 | No clarification protocol = skill may hallucinate on ambiguous inputs |
| B4 | `## OUTPUT FORMAT` section exists with explicit format specification | +1 | No output spec = downstream consumers cannot parse skill output reliably |

### Category C: Content Purity (2 points)

| Check | Condition | Points | Failure Indicator |
| --- | --- | --- | --- |
| C1 | SKILL.md total line count ≤ 500 | +1 | Bloated SKILL.md = passive knowledge not extracted to references/ |
| C2 | No inline domain knowledge block >10 consecutive non-heading lines outside the `## PROCESS` section | +1 | Embedded knowledge = violates Progressive Disclosure principle |

---

## Grade Thresholds

| Score Range | Grade | Classification | Optimizer Action |
| --- | --- | --- | --- |
| 10/10 | ✅ `FULL_COMPLIANT` | Production-ready | None |
| 7-9/10 | 🟡 `PARTIAL` | Minor gaps, auto-fixable | Emit `🔴 [LOCAL-FIX]` → SHP-23 or specific SHP |
| 4-6/10 | 🔴 `SIGNIFICANT` | Major gaps | → Execute Tầng 3 Extractability Analysis |
| 0-3/10 | 🔴 `SKELETON` | Legacy or empty shell | Emit `🔴 [SYSTEMIC-HALT]` → manual creation |

---

## Evals Quality Sub-Check

After scoring A3, if `evals/evals.json` exists and passes the structural check, run the **Evals Quality Gate**:

```text
FOR EACH test_case IN evals.json.test_cases:
  IF test_case.input contains ANY of:
    - "Execute skill with valid parameters"
    - "Execute skill with missing dependencies"
    - "valid input"
    - "invalid input"
    - "[description of valid input]"
    - "[description of invalid input]"
  → FLAG as GENERIC_EVAL

IF count(GENERIC_EVAL) / count(test_cases) > 0.5:
  → 🟡 GENERIC_EVALS_WARNING
  → Deduct 0.5 from A3 score (round down to 0)
```

---

## Report Output Format

The audit report MUST include a `### Phase 2d: 4-Tier Compliance Summary` table:

```markdown
### Phase 2d: 4-Tier Compliance Summary

| # | Skill Name | A (Phys) | B (Body) | C (Purity) | Total | Grade | Remediation |
|---|---|---|---|---|---|---|---|
| 1 | bloom-verb-selector | 4/4 | 4/4 | 2/2 | 10/10 | ✅ FULL | — |
| 2 | clo-writer | 3/4 | 3/4 | 2/2 | 8/10 | 🟡 PARTIAL | SHP-22: Seed evals |
| 3 | legacy-skill | 0/4 | 1/4 | 0/2 | 1/10 | 🔴 SKELETON | SYSTEMIC-HALT |
```
