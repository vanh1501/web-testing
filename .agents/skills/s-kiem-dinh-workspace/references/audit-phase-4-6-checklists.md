# Audit Workspace — Phase 4-6 Checklists

> **Purpose:** Reference checklists for executing Phase 4 (Governance), Phase 5 (Architecture), Phase 6 (Readiness), Phase 6.5 (Harness), and Phase 6.8 (Synergy).

## Phase 4: Governance & Policy Framework (RULES)

**4a. HPRF Tier Verification:**
- Every rule file MUST have `> [!IMPORTANT] Override Priority:`. Missing: 🔴 [LOCAL-FIX].

**4b. Baseline Files & Dual-Context Compliance:**
- `memory-contract.yml` MUST exist with `security_gate.write_lock: true`. 🔴 [SYSTEMIC-HALT]
- `memory-contract.yml` MUST contain Anti-Bloat Configs: `write_quan-ly-quy-tac`, `read_quan-ly-quy-tac`, `share_quan-ly-quy-tac`. Missing = 🔴 [LOCAL-FIX].
- Metadata in `.context/PROJECT.md` MUST be complete. 🔴 [LOCAL-FIX]

**4c. Handoff V2.0 Standards:**
- File `handoff-protocol.md` BẮT BUỘC quy định rõ "V2.0 State Machine" và có "Injection Guard". Thiếu = 🔴 [LOCAL-FIX].

**4d. L0/L1 Rule Architecture (Rule Factory Compliance):**
- Thừa kế tỉ lệ 30/70 (4 thẻ L0, L1 trỏ về `MASTER-INDEX.md` và có `L1-core-cheatsheet-fallback.md`). Lỗi Bloat = 🔴 [SYSTEMIC-HALT].

## Phase 5: Architecture & Epistemic Coupling (FOUNDATION)

**5a. 5-Zone Physical & Antigravity Harness Compliance:**
- Đảm bảo 5-Zone và `artifacts/handoffs/`, `artifacts/session-reports/`, `artifacts/ki-drafts/` tồn tại. Thiếu = 🔴 [LOCAL-FIX].
- BẮT BUỘC có `progress.md` tại Root. Thiếu = 🔴 [SYSTEMIC-HALT].
- Domain data in `.context/` = 🔴 [SYSTEMIC-HALT] nếu cấu trúc sai.

**5b. MAS Hierarchy & Routing:**
- Danh bạ tại `L1-swarm-registry.md`. Nếu dùng `agents.md` dư thừa = 🔴 [LOCAL-FIX].
- Interaction Matrix phải cấm T3↔T3 giao tiếp thẳng. Lách luật = 🔴 [SYSTEMIC-HALT].

**5c. Epistemic Layer Coupling (KB & Layers):**
- `domain/INDEX.md` must map to physical files in `KB/`. Dead links = 🔴 [LOCAL-FIX].
- Orphan files in `KB/` = 🟡 Warning.
- Check Agent SIs for `[[Authorized Workflows]]` and `[[Linked Skills]]`. Missing = 🔴 [LOCAL-FIX].

**5d. Root Namespace Cleanliness (Zero-Floating Law):**
- ROOT MUST ONLY contain constitutional files and 5-Zone folders. Floating operational files = 🔴 [SYSTEMIC-HALT].

**5e. Unbounded Growth & Memory Leaks:**
- Vết Dầu Loang Artifacts (scratchpad rác quá mức) = 🟡 Warning / 🔴 [LOCAL-FIX].

**5f. Root Wiring (GEMINI/AGENT SI) Law:**
- `GEMINI.md` phải trỏ về `L0-giam-sat-tuan-thu-constitution.md`, `L0-cos-routing-protocol.md`, `.context/MASTER-INDEX.md`. Thiếu = 🔴 [SYSTEMIC-HALT].
- `[[Linked Rules]]:` phải có trong Agent SI. Vắng mặt = 🔴 [LOCAL-FIX].

**5g. QUEUE.md Schema Compliance:**
- `QUEUE.md` phải đạt chuẩn Handoff V2.0 (`HO-ID`, `From`, `To`, `Deadline`, `Priority`, `Status`). Sai lệnh = 🔴 [LOCAL-FIX].

**5h. Context Bloat & Archive Hygiene:**
- Rác text `_archive/` hoặc `legacy/` bên trong `.agents/` = 🔴 [LOCAL-FIX].

## Phase 6: Operational Readiness (RUNTIME)

**6a. Memory Bus Check:**
- Each agent SI map to domains in `keys.yaml` correctly? 🔴 [SYSTEMIC-HALT].
- **Dual-Write Validation**: `memory-contract.yml` CẦN `compaction_protocol` và `telemetry_dual_write`. Thiếu = 🔴 [LOCAL-FIX].

**6b. Golden Tests:**
- `.agents/tests/golden-tests.md` exists? (< 3 tests = 🟡; 0 tests = 🔴 [LOCAL-FIX])

**6c. Traceability Check (D2 Observability):**
- Verify memory bus logic guarantees `trace_id` and `span_id`. 🔴 [SYSTEMIC-HALT] if missing.

## Phase 6.5: Governance Harness (CIRCUIT BREAKERS)

**6.5a. Circuit Breaker Mechanism:**
- Logic for OPEN, HALF-OPEN, CLOSED states on cascading task failure? Missing = 🔴 [LOCAL-FIX].
**6.5b. Escalation Protocol:**
- 3-Tier escalation or HITL triggers? Missing = 🔴 [LOCAL-FIX].
**6.5c. Cumulative Saturation Index (CSI):**
- CSI > 40KB → 🔴 [SYSTEMIC-HALT] Token Bloat Collapse.

## Phase 6.8: Dynamic Synergy & Coordination Audit

**6.8a. Coordination Efficiency:**
- Revert Rate lặp lại quá 3 lần -> 🔴 [LOCAL-FIX].
**6.8b. Theory of Mind & Critique Density:**
- QA Agent-as-a-Judge test: Hollow QA (chỉ rà soát format) -> 🟡 System Warning.
