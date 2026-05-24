---
description: >
  Workspace quality assessment — evaluates baseline compliance, health, and performance.
  Use when 'audit', 'kiểm định workspace', 'check quality', 'đánh giá chất lượng'.
  Version 3.0 (Micro-Audit Batch Edition).
semantic_triggers: ['audit', 'kiểm định', 'đánh giá chất lượng', 'check workspace']
version: 3.0.0
lifecycle: ACTIVE
last_audit: 2026-05-10
owner: GOV-W03
skill_targets: [kiem-dinh-workspace, quan-ly-quy-tac, giam-sat-tuan-thu, architecture, toi-uu-bo-nho, skill-writer, workflow-builder]
dependencies: []
execution_mode: sequential
---
# Workflow: Audit Workspace v3.0

## Goal & Governance Context

**Purpose:** Conduct a **Relentless Semantic Audit (Kính Hiển Vi)** — executing a full 100% sweep with ZERO early-stopping parameters. Outputs an `Executive_Audit_Report.md`.
**Scope & SLA:** Applies to all `managed_workspaces/` AND Master Repo self-audit. Excludes `_archive/` and `tmp/` directories.

## Batch Orchestration Architecture (v3.0 — Micro-Audit)

> [!CAUTION] CONTEXT WINDOW PROTECTION
> Workflow v2.4 (Monolithic) đã chứng minh thất bại do **Context Window Starvation**: 12 Phase + 7 Skill nhồi vào 1 session → Các Skill cuối (Phase 6+) bị bỏ qua hoặc thực thi hời hợt.
>
> **v3.0 giải quyết triệt để** bằng cách chia thành **4 Đợt (Batch) độc lập**. Mỗi Đợt:
> - Chạy trong **1 session riêng biệt** (hoặc cách nhau bởi `/checkpoint-session`).
> - Load tối đa **2 Skill** + references tương ứng.
> - Ghi findings ra file JSON riêng: `tmp/audit_batch_{A|B|C|D}.json`.
> - Đợt D tổng hợp tất cả findings để tính điểm.

```
Đợt A (kiem-dinh-workspace)          → Phase 0, 0.5, 1, 2, 2.5
    ⏹ CHECKPOINT
Đợt B (arch+gov)    → Phase 3, 4, 5
    ⏹ CHECKPOINT  
Đợt C (memory+gov)  → Phase 6, 6.2, 6.5, 6.8
    ⏹ CHECKPOINT
Đợt D (kiem-dinh-workspace+scoring)  → Phase 7, 7.5, 8
```

## Audit Mode & Parameters

The caller MUST specify 2 parameters before running:
1. **Maturity Level:** `--draft`, `--staging`, `--prod`.
2. **Scan Strategy:** `--strict` (Default), `--full-scan`, `--auto-heal`.
3. **Dynamic Insight Context (Optional):** `--insight-pattern=[Path]`.

## Steps

---

## ═══════ ĐỢT A: STRUCTURAL & VALUE STREAM ═══════

> **🛠 Skill Budget:** `qa` (ONLY)
> **📖 References:** `audit-phase-1-3-checklists.md`
> **📦 Output:** `tmp/audit_batch_A.json`

### Phase 0: Structural Pre-Scan (DETERMINISTIC — Non-LLM)

// turbo

- **👤 Owner:** `[@GOV-W03]`
- **🛠 Skill Target:** `[qa]`
- **⚙️ Action:** Execute `python .agents/skills/w-kiem-dinh-workspace/scripts/structural_scanner.py [workspace_path]`.
- **📦 Output Required:** `tmp/structural_scan_report.json`

> [!NOTE] ZONE 6 (DOMAIN EXTENSION ZONES)
> `structural_scanner.py` sẽ tự động đọc `.context/allowed-zones.json` (nếu có) để cấp phép cho các thư mục bản địa hóa (Localized Folders) không thuộc 5-Zone mặc định.

> [!CAUTION]
> Phase 0 results are **GROUND TRUTH**. LLM-based Phases 1-6.8 MUST NOT contradict a finding that Phase 0 has already confirmed.

---

### Phase 0.5: SOW Traceability & Scope Mapping (COVERAGE AUDIT)

- **👤 Owner:** `[@GOV-W03]`
- **🛠 Skill Target:** `[qa]`
- **⚙️ Action:** Cross-reference Business Requirements (SOW) against physical implemented structures.

> **Quality Gate:** Coverage ratio MUST be calculated. If < 0.7 → HALT and escalate.

---

### Phase 1: Workflow Quality & Routing Logic (VALUE STREAM)

- **👤 Owner:** `[@GOV-W03]`
- **🛠 Skill Target:** `[qa]`
- **⚙️ Action:** Apply CQS Compliance, Zero-Native Law, and Binding Density checks on every workflow in `.agents/workflows/`.

> **Quality Gate:** Every workflow file MUST be touched. Missing a single file = audit FAIL.

### Phase 2: Skill Coverage & Rigor (ARSENAL)

- **👤 Owner:** `[@GOV-W03]`
- **🛠 Skill Target:** `[qa]`
- **⚙️ Action:** Evaluate Skill Supply/Demand Ratio, Ghost Check, Domain Expert Payload, and 4-Tier Structural Analysis.

### Phase 2.5: DAM Taxonomy & Orphan File Sweep (LIBRARY)

- **👤 Owner:** `[@GOV-W03]`
- **🛠 Skill Target:** `[qa]`
- **⚙️ Action:** Quét các thư mục `Quan-Tri/` và `So-Tay/`. Flag tất cả các file vi phạm Naming Convention hoặc nằm sai Sub-folder (Orphaned Files). Yêu cầu đổi tên hoặc di dời lập tức.

> [!IMPORTANT] RAG POINTER MANDATE
> Để kiểm định Phase 1, 2, 2.5, Agent **BẮT BUỘC** gọi `view_file` đọc tài liệu checklist sau:
> `.agents/skills/w-kiem-dinh-workspace/references/audit-phase-1-3-checklists.md`

> **Quality Gate:** Phase 0.5-2.5 phải phát hiện ≥1 finding hoặc xác nhận explicit PASS cho mỗi checklist item. Không được skip.

### ⏹ ĐỢT A — CHECKPOINT

> [!CAUTION] MANDATORY CHECKPOINT
> Ghi toàn bộ findings của Đợt A vào `tmp/audit_batch_A.json`.
> Thực thi `/checkpoint-session` hoặc `/end-session` để **giải phóng hoàn toàn Context Window** trước khi bắt đầu Đợt B.
> Agent **CẤM** tiếp tục Đợt B trong cùng session nếu tổng Token đã > 40K.

---

## ═══════ ĐỢT B: ARCHITECTURE & GOVERNANCE ═══════

> **🛠 Skill Budget:** `architecture` + `giam-sat-tuan-thu` + `quan-ly-quy-tac`
> **📖 References:** `audit-phase-1-3-checklists.md` (Phase 3) + `audit-phase-4-6-checklists.md` (Phase 4-5)
> **📦 Output:** `tmp/audit_batch_B.json`

### Phase 3: Phantom Agent Architecture Check (WORKERS)

- **👤 Owner:** `[@GOV-W03]`
- **🛠 Skill Target:** `[s-thiet-ke-kien-truc]`
- **⚙️ Action:** Verify Phantom Agent model compliance. Check `L1-swarm-registry.md` for ID, Tier, Role, Linked Skills.

### Phase 4: Governance & Policy Framework (RULES)

- **👤 Owner:** `[@GOV-W02]`
- **🛠 Skill Target:** `[giam-sat-tuan-thu, quan-ly-quy-tac]`
- **⚙️ Action:** Verify HPRF Tier blocks, Baseline Files, Dual-Context Compliance, Handoff V2.0, L0/L1 Rule Architecture.

### Phase 5: Architecture & Epistemic Coupling (FOUNDATION)

- **👤 Owner:** `[@GOV-W01]`
- **🛠 Skill Target:** `[s-thiet-ke-kien-truc]`
- **⚙️ Action:** Validate 5-Zone Physical compliance, MAS Hierarchy & Routing, Epistemic Layer Coupling (KB), Root Namespace Cleanliness, Root Wiring.

> [!IMPORTANT] RAG POINTER MANDATE
> Để kiểm định Phase 3, Agent gọi `view_file` đọc: `.agents/skills/w-kiem-dinh-workspace/references/audit-phase-1-3-checklists.md`
> Để kiểm định Phase 4-5, Agent gọi `view_file` đọc: `.agents/skills/w-kiem-dinh-workspace/references/audit-phase-4-6-checklists.md`

> **Quality Gate:** Phase 3-5 phải áp dụng toàn bộ tiêu chí (3a-3c, 4a-4d, 5a-5h). Không được bỏ sót.

### ⏹ ĐỢT B — CHECKPOINT

> [!CAUTION] MANDATORY CHECKPOINT
> Ghi toàn bộ findings của Đợt B vào `tmp/audit_batch_B.json`.
> Thực thi `/checkpoint-session` hoặc `/end-session` để giải phóng Context Window.

---

## ═══════ ĐỢT C: RUNTIME & MEMORY ═══════

> **🛠 Skill Budget:** `toi-uu-bo-nho` + `giam-sat-tuan-thu`
> **📖 References (BẮT BUỘC LOAD ĐẦY ĐỦ):**
> - `toi-uu-bo-nho/references/memory-rbac-rubric.md`
> - `toi-uu-bo-nho/references/contract-compaction-quan-ly-quy-tac.md`
> - `toi-uu-bo-nho/references/methodology.md`
> - `qa/references/audit-phase-4-6-checklists.md` (Phần Phase 6+)
> **📦 Output:** `tmp/audit_batch_C.json`

> [!WARNING] FULL SKILL ACTIVATION
> Đây là Đợt duy nhất mà Skill `toi-uu-bo-nho` được kích hoạt **Route 2 (Memory Bus Engineering)** đầy đủ. Agent **BẮT BUỘC** phải load cả 3 file references ở trên TRƯỚC KHI bắt đầu kiểm tra. Nếu không load được → HALT và báo lỗi.

### Phase 6: Operational Readiness & Memory Audit (RUNTIME)

- **👤 Owner:** `[@GOV-W04]`
- **🛠 Skill Target:** `[toi-uu-bo-nho, qa]`
- **⚙️ Action:** 
  - `[s-toi-uu-bo-nho]` Route 2: Validate Memory Bus, Token Economy, và Memory Contract tuân thủ RBAC V2.0.
    - **Step 1:** CQS Size Gate — memory-contract.yml < 0.5KB → Auto-FAIL (skeleton).
    - **Step 2:** Load 3 references (xem trên) → Kiểm tra RBAC routing, Dual-Write config, Compaction quan-ly-quy-tac.
    - **Step 3:** Xuất Delta Report nếu cần vá.
  - `[qa]`: Validate Golden Tests, Traceability Check (D2 Observability).

### Phase 6.2: Dynamic Performance & Drift Audit (PDCA)

- **👤 Owner:** `[@GOV-W03]`
- **🛠 Skill Target:** `[qa]`
- **⚙️ Action:** Đọc file `QUALITY-LOG.md`. Nếu First-Pass Rate < 80% hoặc Handoff Reverts > 3 trong 5 phiên gần nhất, tự động đánh tụt hạng Quality Gate và trigger `/w-toi-uu-workspace`.

### Phase 6.5: Governance Harness (CIRCUIT BREAKERS)

- **👤 Owner:** `[@GOV-W02]`
- **🛠 Skill Target:** `[s-giam-sat-tuan-thu]`
- **⚙️ Action:** Verify Circuit Breaker mechanism (OPEN/HALF-OPEN/CLOSED states), Escalation Protocol, CSI threshold.

### Phase 6.8: Dynamic Synergy & Coordination Audit

- **👤 Owner:** `[@GOV-W03]`
- **🛠 Skill Target:** `[qa]`
- **⚙️ Action:** Evaluate Coordination Efficiency (Revert Rate) and Theory of Mind Critique Density.

> **Quality Gate:** Phase 6-6.8 phải áp dụng toàn bộ tiêu chí (6a-6c, 6.5a-6.5c, 6.8a-6.8b). Không được bỏ sót.

### ⏹ ĐỢT C — CHECKPOINT

> [!CAUTION] MANDATORY CHECKPOINT
> Ghi toàn bộ findings của Đợt C vào `tmp/audit_batch_C.json`.
> Thực thi `/checkpoint-session` hoặc `/end-session` để giải phóng Context Window.

---

## ═══════ ĐỢT D: SCORING & ENRICHMENT ═══════

> **🛠 Skill Budget:** `qa` + `skill-writer` + `workflow-builder` + `do-luong-hieu-suat`
> **📖 References:** `audit-rubric.md`
> **📦 Input:** Tổng hợp từ `tmp/audit_batch_A.json` + `tmp/audit_batch_B.json` + `tmp/audit_batch_C.json`
> **📦 Output:** `Quan-Tri/AUDIT/Executive_[ws-name]_[date].md`

> [!IMPORTANT] BATCH AGGREGATION
> Trước khi bắt đầu Phase 7, Agent **BẮT BUỘC** chạy script tổng hợp:
> `python .agents/skills/w-kiem-dinh-workspace/scripts/audit_batch_aggregator.py [workspace_path]`
> Script này gộp 3 file batch A/B/C thành 1 file tổng: `tmp/audit_aggregate.json`.

### Phase 7: Normalized Scoring & Remediation (CONCLUSION)

- **👤 Owner:** `[@GOV-W03]`
- **🛠 Skill Target:** `[qa]`
- **⚙️ Action:** Đọc `tmp/audit_aggregate.json`. Calculate Complexity Normalization Factor ($N_c$), apply the Scoring Rubric, and compile Component Expert Ranking Index (CERI).
- **📦 Output Required:** `Quan-Tri/AUDIT/Executive_[ws-name]_[date].md` (which MUST INCLUDE CERI Table) and handoff trigger to `/w-toi-uu-workspace`.

> [!IMPORTANT] RAG POINTER MANDATE
> Để lấy Ma trận Điểm (Scoring Rubric), Grading Tiers và Metrics (Quality Gates), bạn **BẮT BUỘC** phải gọi công cụ `view_file` nhắm vào đường dẫn vật lý sau:
> `.agents/workflows/components/audit-rubric.md`

**7a. Component Expert Ranking Index (CERI) Table:**
- Trong báo cáo Executive, BẮT BUỘC chèn Bảng `Component Expert Level Ranking` (Level 1-2 Junior đến Level 4-5 Global Executive).

---

### Phase 7.5: On-Demand Enrichment & Generation (OPTIONAL)

- **👤 Owner:** `[@GOV-COORD]`
- **🛠 Skill Target:** `[skill-writer, workflow-builder]`
- **⚙️ Action:** 
  - Nếu kết quả kiểm định ở Phase 1 hoặc 2 phát hiện thiếu hụt Skill/Workflow cốt lõi và User có yêu cầu bổ sung ("khi cần"), kích hoạt `skill-writer` hoặc `workflow-builder` (Route 1: CREATE) để tự động khởi tạo các thành phần này.
  - **Guardrail:** Bắt buộc phải có Socratic OTC Check trước khi generate.

---

### Phase 8: Telemetry & Memory Flush (OBSERVABILITY)

- **👤 Owner:** `[@GOV-COORD]`
- **🛠 Skill Target:** `[s-do-luong-hieu-suat]`
- **⚙️ Action:** Báo cáo các chỉ số (Success Rate, Gate Pass Rate, Cảnh báo Context Bloat) vào khối `Workflow Telemetry` bên trong tệp `QUALITY-LOG.md` theo chuẩn M1. Giải phóng hoàn toàn Memory Bus sau khi hoàn tất.
