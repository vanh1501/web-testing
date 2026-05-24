# Workflow Audit Scoring Engine — 6-Dimension Rubric (100-Point Scale)

> Reference document for the `tao-quy-trinh-moi` skill, Route 2 (ASSESS).
> Contains the complete scoring algorithm for evaluating MAS workspace workflows.
> Agent MUST load this file when executing batch audit or single-workflow deep assessment.

---

## Pre-Scoring: Workflow Classification

Before scoring, classify each workflow file:

| Type | Structure | Description |
| --- | --- | --- |
| **TYPE-INFRA** | Infrastructure workflows | `start-session`, `end-session`, `checkpoint-session` — mandatory baseline |
| **TYPE-CORE** | Core domain workflows | Business process workflows mapped from A-ESOAR R-steps |
| **TYPE-SUPPORT** | Support workflows | `onboard-new-user`, `weekly-cycle`, `run-lab` — operational support |
| **TYPE-META** | Meta/giam-sat-tuan-thu workflows | `audit-workspace`, `optimize-workspace`, `propagate-change` — system management |

> Classification affects scoring weights: TYPE-CORE workflows are weighted 1.5x in Library Health calculation because they directly execute the workspace's value proposition.

---

## 6-Dimension Scoring

### W1 — YAML Frontmatter Quality (15 pts)

```text
+5  : YAML frontmatter exists with valid --- delimiters
+5  : `description` field exists AND >= 10 words
+5  : description explains WHEN to use (not just WHAT it does)

Penalties:
-5  : No YAML frontmatter at all (legacy format)
-3  : description < 10 words (too terse for trigger matching)
-5  : description is placeholder or copy of filename
```

### W2 — Governance Context & Metadata Completeness (20 pts)

```text
+5  : `👤 Owner:` metadata present with valid @Agent-ID
+5  : `🛠 Skill Target:` metadata present with valid skill-id
+5  : `## Goal & Governance Context` section present (Purpose + Scope)
+5  : Owner agent physically exists in `.agents/agents/`

Penalties:
-5  : Owner is `[Native]` or `[TBD]` — workflow has no responsible agent
-5  : Skill Target references a non-existent skill
-3  : Missing Goal & Governance Context section — workflow has no giam-sat-tuan-thu scope
-3  : Context lacks explicit `Scope` boundary
```

### W3 — Execution Depth & Quality Gates (20 pts)

```text
+5  : Has ≥ 3 distinct execution steps (numbered or clearly sequenced)
+5  : Has `## Audit & Metrics (Quality Gates)` section mandatory for exit
+5  : Has explicit Metrics defined for measurement
+5  : Steps are imperative ("Do X") not passive ("You might want to...")

Penalties:
-5  : Fewer than 3 steps (skeleton workflow)
-5  : No Quality Gates section (cannot be BPM compliant)
-3  : missing Metrics definition inside Quality Gates
-5  : Total content < 0.8 KB (auto-FAIL per CQS size gate)
```

### W4 — Skill Wiring Integrity (20 pts)

```text
+7  : `## Assigned Skills` or `## Skill Target` section present
+7  : ALL referenced skill IDs exist in `.agents/skills/` or `SKILLS-INDEX.md`
+6  : Every execution step that requires domain knowledge references a specific skill

Penalties:
-10 : No skill wiring at all — workflow operates "blind"
-5  : References skill that doesn't exist (broken wiring)
-3  : Skill reference is `[Native]` — inline execution without skill delegation
```

### W5 — Zero-Native Compliance (15 pts)

```text
+10 : No inline domain logic exceeding 10 lines within the workflow body
+5  : All complex operations are delegated to skills (not embedded)

Penalties:
-10 : Contains > 10 lines of inline domain execution logic (parsing, mapping, scoring)
-5  : Contains > 5 lines of inline logic but < 10 (borderline)
-3  : Contains hard-coded domain values that should be in KB or skill references
```

> **Principle:** Workflows are ORCHESTRATORS — they route and sequence. They do NOT execute domain logic. Any embedded logic > 10 lines is a Zero-Native violation that should be extracted to a skill.

### W6 — Context Budget Discipline (10 pts)

```text
+10 : Total file size < 8,000 characters (optimal)
+7  : Total file size 8,000-12,000 characters (acceptable)
+3  : Total file size 12,000-15,000 characters (borderline)
0   : Total file size > 15,000 characters (bloated)

Penalties:
-3  : Duplicate content between workflow and referenced skills/quan-ly-quy-tac
```

---

## Grade Thresholds

| Score | Grade | Label | Recommended Action |
| --- | --- | --- | --- |
| 85–100 | **A** | ✅ Production-ready | Monitor only |
| 70–84 | **B** | 🔶 Good, minor gaps | Quick patch (auto-fixable) |
| 55–69 | **C** | ⚠️ Functional but weak | Repair needed → Route 3 |
| 40–54 | **D** | 🔴 Significant issues | Full rework → Route 3 |
| < 40 | **F** | ❌ Non-functional | Rebuild → Route 1 (CREATE) |

---

## Library Health Aggregation

```text
WEIGHTED_SCORES = []
FOR EACH workflow:
    IF type == TYPE-CORE:
        WEIGHTED_SCORES.append(score * 1.5)
    ELSE:
        WEIGHTED_SCORES.append(score * 1.0)

LIBRARY_HEALTH = SUM(WEIGHTED_SCORES) / SUM(weights)

CRITICAL_COUNT = count(workflows with Grade D or F)

Library Status:
  HEALTHY   : CRITICAL_COUNT == 0 AND LIBRARY_HEALTH >= 75
  AT_RISK   : CRITICAL_COUNT <= 2 OR LIBRARY_HEALTH 60-74
  DEGRADED  : CRITICAL_COUNT > 2 OR LIBRARY_HEALTH < 60
```

---

## Coverage Analysis (Bonus Check)

After scoring individual workflows, run the A-ESOAR Coverage Check:

```text
1. Load BRD/SCOPE → extract all R-steps (Robotize) and A-steps (Augment)
2. For EACH R-step: does a corresponding workflow exist?
   → YES: covered ✅
   → NO: COVERAGE GAP 🔴 — recommend Route 1 (CREATE)
3. Coverage Ratio = covered_R_steps / total_R_steps
   → >= 0.9: FULL COVERAGE
   → 0.7-0.9: PARTIAL — flag gaps
   → < 0.7: CRITICAL GAP — prioritize workflow creation
```
