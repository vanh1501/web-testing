---
description: Định nghĩa các Hook events kiểm soát vòng đời file và task trong workspace.
activation: Always On
---

# L2 Harness Hooks Policy

> [!IMPORTANT] Override Priority: High
> Enforced by Harness Layer.

## Pre-Action Hooks

### Hook 1: Pre-Delete Guard
- **Trigger:** Any `delete` or `remove` operation on files/directories.
- **Action:** HALT execution. Display confirmation prompt to Operator.
- **Bypass:** None. No exception.

### Hook 2: Pre-Overwrite Guard
- **Trigger:** Any `write_to_file` with `Overwrite: true` on existing files.
- **Action:** Create backup copy to `Du-An/_archive/` before overwriting.
- **Bypass:** New file creation (file does not exist yet).

### Hook 3: Pre-Output Routing
- **Trigger:** Any artifact output generation.
- **Action:** Validate destination matches `Kho-Du-Lieu/Ket-Qua/{du-an}/`.
- **Reject if:** Output targets workspace root or `.agents/`.

## Post-Action Hooks

### Hook 4: Post-Write Index Sync
- **Trigger:** Any successful file write operation.
- **Action:** Trigger `dong-bo-muc-luc` skill to update `Bang-Dieu-Khien/` indexes.
- **Skip if:** Write target is `Quan-Tri/AGENT-LOG.md` (log-only operation).

### Hook 5: Post-Session Checkpoint
- **Trigger:** Semantic milestone reached (major artifact delivery, task handoff).
- **Action:** Execute `luu-phien.md` workflow as side-effect.

## Escalation Hooks

### Hook 6: 3-Strike Escalation
- **Trigger:** Same operation fails 3 consecutive times.
- **Action:** HALT autonomous execution. Escalate to Operator with:
  - Problem description
  - 2 proposed solutions
  - Impact assessment

## Circuit Breaker Policy (CBP)

### 1. CLOSED State (Healthy)
- System operates normally. Max 10 consecutive tool errors allowed across the workspace before tripping.

### 2. OPEN State (Tripped)
- **Threshold:** > 10 tool errors OR `SYSTEMIC-HALT` detected.
- **Action:** Immediate lock on autonomous execution. Require manual Operator override or `/optimize-workspace` execution.

### 3. HALF-OPEN State (Testing)
- **Threshold:** First session post-recovery.
- **Action:** Execute operations with 1-strike escalation instead of 3-strike. Successful completion of 5 tasks returns state to CLOSED.
