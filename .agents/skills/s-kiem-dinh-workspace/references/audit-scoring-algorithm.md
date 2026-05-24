# Audit Scoring Algorithm — 100-Point Weighted Rubric

> Reference document for the `qa` skill.
> Contains the exact mathematical scoring formula used in Phase 8 of `/audit-workspace`.
> Agent MUST use this algorithm — no estimated grades allowed.

---

## Scoring Categories & Weights

| Category | Max Points | Phases Covered | Deduction Rules |
| --- | --- | --- | --- |
| **Workflow Quality** | 30 pts | Phase 1 (CQS, Binding, Call Graph, Zero-Native) | -5 per [Native] target, -5 per missing metadata |
| **Agent & Skill Quality** | 25 pts | Phase 2 (Skill Coverage & Rigor) + Phase 3 (SI Quality) | -5 per skeleton, -5 per ghost skill |
| **Arch. Foundation & Rules**| 20 pts | Phase 4 (Governance/HPRF) + Phase 5 (5-Zone) | 5-Zone: 10 pts, Governance: 10 pts |
| **Hierarchy** | 10 pts | Phase 5 (Roster, Matrix, Tiers) | -3 per missing SI file, -5 for T3↔T3 violation |
| **KB Wiring** | 10 pts | Phase 5 (INDEX sync, Agent-KB connectivity) | -2 per orphan KB, -3 per missing KB Connectivity |
| **Operational Core** | 5 pts | Phase 6 (Memory Bus, Golden Tests, Session Lifecycle) | -2 per missing golden test |

**Total: 100 points**

---

## Deduction Rules (Per Finding)

### Critical Findings (🔴)

| Finding Type | Deduction | Category |
| --- | --- | --- |
| Missing 5-Zone directory (Zone 2-5) | -5 pts | Arch. Foundation |
| Domain data in .context/ | -5 pts | Arch. Foundation |
| Missing .agents/agents.md or PROJECT.md | -15 pts (Fatal) | Arch. Foundation |
| Missing memory-contract.yml | -5 pts | Arch. Foundation |
| Missing security_gate in memory-contract | -5 pts | Arch. Foundation |
| Rule file missing HPRF block | -3 pts | Arch. Foundation |
| Agent SI listed in roster but file missing | -5 pts | Hierarchy |
| T3↔T3 direct communication allowed | -10 pts | Hierarchy |
| Agent SI missing KB Connectivity | -5 pts | KB Wiring |
| Dead link in INDEX.md | -3 pts | KB Wiring |
| Ghost Skill detected | -5 pts | Agent & Skill Quality |
| Missing Required Skill | -5 pts | Agent & Skill Quality |
| Skill contains ## Voice/Persona | -3 pts | Agent & Skill Quality |
| Agent SI > 25KB (extreme bloat) | -5 pts | Agent & Skill Quality |
| Domain skill missing Canonical Trifecta | -3 pts | Agent & Skill Quality |
| Flat knowledge (no quantifiers) | -3 pts | Agent & Skill Quality |
| Missing golden-tests.md | -5 pts | Operational Core |
| Session workflow not adapted from baseline | -3 pts | Operational Core |
| Workflow declares [Native] Skill Target | -5 pts | Workflow Quality |
| Workflow missing Owner/Skill Target metadata | -5 pts | Workflow Quality |

### Warning Findings (🟡)

| Finding Type | Deduction | Category |
| --- | --- | --- |
| Missing Zone 1 (tmp/) | -1 pt | Arch. Foundation |
| Agent SI > 15KB (bloat warning) | -1 pt | Agent & Skill Quality |
| Orphan KB file (not referenced) | -1 pt | KB Wiring |
| Orphan workflow (no backlinks) | -1 pt | Workflow Quality |
| Workflow > 15KB without justification | -1 pt | Workflow Quality |
| Missing challenge mechanism in skill | -1 pt | Agent & Skill Quality |
| Golden tests < 3 cases | -1 pt | Operational Core |

---

## Complexity Normalization Factor ($N_c$)

For large workspaces (>10 agents), Warning-level deductions are halved to avoid over-penalizing normal complexity:

```
IF agent_count > 10:
    warning_deductions = warning_deductions * 0.5
    critical_deductions = critical_deductions  # unchanged
```

For small workspaces (≤4 agents), all deductions apply at full weight.

---

## Grade Thresholds

| Grade | Score Range | Verdict |
| --- | --- | --- |
| **A+** | 95-100 | Flawless. Production-ready. |
| **A** | 90-94 | Fully compliant. Go-live ready. |
| **B** | 80-89 | Mostly compliant. Minor findings only. |
| **C** | 65-79 | Needs remediation. ≥1 critical error. NOT go-live ready. |
| **D** | 50-64 | Significant issues. Foundational gaps. |
| **F** | <50 | Critical failure. Immediate rebuild required. |

---

## Scoring Calculation Procedure

```
1. Initialize score = 100
2. For each finding in audit_results:
   a. Look up finding_type in Deduction Rules table
   b. If not found → log as UNKNOWN, apply -1 default
   c. Apply deduction to the corresponding Category
   d. Cap each category at 0 (no negative scores per category)
3. Apply Complexity Normalization if agent_count > 10
4. Final_Score = SUM(all category scores)
5. Grade = lookup Grade Thresholds table
6. Output: Final_Score, Grade, Category Breakdown
```
