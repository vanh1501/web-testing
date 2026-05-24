# Memory Contract V2.0 Schema

This document defines the required schema for `memory-contract.yml` located at `.agents/memory_bus/memory-contract.yml`.
When auditing `giam-sat-tuan-thu` Gate 2, verify these keys exist and match the required values.

## Mandatory Keys & Values

```yaml
security_gate:
  write_lock: true # MUST be true

write_quan-ly-quy-tac:
  ki_fields:
    - domain_tag
    - ki_type
    - summary
    - insight
    - confidence
    # All 5 fields MUST be present

read_quan-ly-quy-tac:
  ki_check_mandatory:
    priority: 1 # MUST be 1

share_quan-ly-quy-tac:
  telemetry_dual_write:
    enabled: true # MUST be true

compaction_protocol:
  trigger_kb: # MUST be defined (not empty)

trace_id:
  inject_on: "start-session" # MUST be exactly "start-session"
```

## Audit Violation Triggers

1. **Missing File**: If `memory-contract.yml` does not exist at `.agents/memory_bus/`, it is a `🔴 [SYSTEMIC-HALT]`.
2. **Missing/Invalid Field**: If any required field is missing or has an invalid value, it is a `🔴 [LOCAL-FIX]`.
