# L0 Safety & Escalation (Child Workspace)
> [!IMPORTANT]
> TIER 1 - SUPREME PRIORITY. Safety > Speed.

## 1. EXECUTION LIMITS
- `FileMod_Limit/Session <= 20` -> [IF > 20: HALT -> Require Operator Checkpoint].
- `Transient_Error (timeout, 5xx)` -> Retry max 3 with backoff. Same args OK.
- `Deterministic_Error (syntax, logic, 400)` -> MUST change strategy each retry. `Fail_Count == 3` -> HALT + Escalate.
- `Destructive_Cmds (rm, drop, format)` -> [HALT -> Require Operator Approval].
- `Backup_Before_Overwrite` -> [REQUIRE] copy original to `Du-An/_archive/` before overwriting.

## 2. DATA SAFETY
- `Credentials_Hardcode` -> [DENY]. Use environment variables.
- `PII_Data` -> [REQUIRE MASKING].
- `External_Services` -> [DENY] unless configured via MCP.
- `Read_Only_Tools` -> [ALLOW AUTO-RUN]. Gather context before asking Operator.

## 3. ESCALATION PROTOCOL
- `Technical_Blocker` -> [ESCALATE: Problem + 2 Solutions + Impact].
- `Security_Concern` -> [HALT IMMEDIATELY]. Report to operator.
- `Scope_Creep` -> [PAUSE]. Estimate effort, ask: Backlog or Immediate?

## 4. STOP BOUNDARIES
Interrupt and request Operator Approval IF:
- `Logic_Ambiguous`: Missing parameters for safe execution.
- `Data_Risks`: Overwriting files without backup.
- `Plan_Invalidation`: Mid-step conflicts with giam-sat-tuan-thu quan-ly-quy-tac.

## 5. OPERATIONAL POLICY
- `Scope`: Operate ONLY within this workspace directory.
- `Restricted_Zones`: NEVER wipe index files in `Bang-Dieu-Khien/`. NEVER overwrite `Quan-Tri/CHINH-SACH.md` without confirm.

> [!IMPORTANT] Override Priority: High
> Bắt buộc tuân thủ cho hệ thống MAS V8.


