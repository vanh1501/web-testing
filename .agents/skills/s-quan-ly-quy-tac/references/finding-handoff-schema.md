# Finding Handoff Schema V1.0

> Reference document for the `quan-ly-quy-tac` skill, Route 6 (RESOLVE).
> Standardizes the data contract between Diagnostician (`qa` skill) and Resolver (`quan-ly-quy-tac` skill).
> When `qa` delegates findings from `/audit-workspace` Phase 3 or Phase 4, the payload MUST conform to this schema.

---

## Schema Definition

Each finding handed off from `qa` to `quan-ly-quy-tac` Route 6 MUST contain the following fields:

```yaml
finding:
  # Unique identifier — Pattern: F-[PHASE]-[SEQ]
  finding_id: "F-P4-001"

  # What type of component is affected
  component_type: "RULE"  # Values: RULE | AGENT_SI

  # Absolute or relative path to the failing component
  component_path: ".agents/quan-ly-quy-tac/L1-coding-standards.md"

  # Which scoring dimensions failed (from component-scoring-engine.md)
  failing_dimensions:
    - dimension: "R1"
      score: 5
      max: 25
      root_cause: "Missing HPRF Override Priority block"
    - dimension: "R3"
      score: 10
      max: 25
      root_cause: "CLEAR score 2/5 — fails Concrete and Exampled"

  # Overall severity classification
  severity: "CRITICAL"  # Values: CRITICAL | HIGH | MEDIUM

  # Recommended repair protocol from component-repair-protocols.md
  recommended_protocols: ["RR1", "RR3"]

  # Which workflow/phase generated this finding
  source: "/audit-workspace Phase 4"

  # Timestamp of diagnosis
  diagnosed_at: "2026-05-01T15:46:00+07:00"
```

---

## Severity Classification Rules

| Severity | Criteria | Action |
|---|---|---|
| **CRITICAL** | Score < 40 (Grade F) OR any R1 failure (missing HPRF) | Immediate repair — DO FIRST |
| **HIGH** | Score 40-69 (Grade C/D) OR CLEAR < 3/5 | Repair in current session |
| **MEDIUM** | Score 70-84 (Grade B) with minor gaps | Batch later or defer |

## Batch Handoff Format

When `qa` hands off multiple findings at once, wrap them in a batch envelope:

```yaml
handoff_batch:
  source_workflow: "/audit-workspace"
  source_phase: "Phase 4"
  workspace: "ws-example"
  diagnosed_at: "2026-05-01T15:46:00+07:00"
  total_findings: 3
  findings:
    - finding_id: "F-P4-001"
      # ... (full schema as above)
    - finding_id: "F-P4-002"
      # ... (full schema as above)
```

## Validation Rules

- `finding_id` MUST be unique within a batch.
- `failing_dimensions` MUST reference valid dimension IDs from `component-scoring-engine.md` (A1-A7 for Agent SIs, R1-R5 for Rules).
- `recommended_protocols` MUST reference valid protocol IDs from `component-repair-protocols.md` (AR1-AR7, RR1-RR5).
- `severity` MUST be classified using the table above — do NOT guess.
