# COS Routing Protocol (Child Workspace)
> [!IMPORTANT]
> TIER 1 - Routing Rules.

## 1. TASK INITIATION
- `Step 1 (Classify)` -> Type (query/action/report), Target Zone, Scale.
- `Step 2 (Route)` -> Match skill via `tro-ly-dieu-phoi` decision tree.
- `Step 3 (Budget)` -> T1 (≤3 files) -> All context. T2 (≤8K) -> P0+P1. T3 (>8K) -> P0 only.
- `Step 4 (Load)` -> Order: P0 (quan-ly-quy-tac) -> P1 (skill) -> P2 (KB).

## 2. POSITION POLICY
- `Primacy` -> Governance quan-ly-quy-tac (L0).
- `Recency` -> Current task context.
- `Middle` -> History (compressible).

## 3. EVICTION & MONITORING
- `Eviction` -> Stop reloading stale context in next turn.
- `Tokens` -> Turn > 15 -> Summarize -> Checkpoint.
- `Drift` -> Turn % 5 == 0 -> Re-read task objective.

## 4. ROUTING LOG
- `Log` -> Append to `Quan-Tri/AGENT-LOG.md`.

> [!IMPORTANT] Override Priority: High
> Bắt buộc tuân thủ cho hệ thống MAS V8.


