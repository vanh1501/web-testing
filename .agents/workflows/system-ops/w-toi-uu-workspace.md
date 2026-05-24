---
description: Overhaul the workspace using a structured 2-Round loop (Automation & Artisan)
semantic_triggers: ['optimize', 'tối ưu hóa', 'refactor', 'sửa lỗi audit']
version: 2.0.0
lifecycle: ACTIVE
last_audit: 2026-05-10
owner: GOV-COORD
skill_targets: [s-toi-uu-workspace]
dependencies: [audit-workspace]
execution_mode: sequential
---

# Workflow: Optimize Workspace v2.0 (Dual-Round + Anti-CWS Architecture)

## Goal

Read the results from the /w-kiem-dinh-workspace generated Executive_Audit_Report.md. Overhaul the workspace using a structured **2-Round loop** to fully separate high-throughput deterministic mass-edits from low-throughput high-precision semantic refactoring. This explicitly prevents Context Bloat and LLM hallucination.

## Required Input

- Path to the Executive_Audit_Report.md Indictment Registry.

## Assigned Meta-Skills & FinOps Protocol

> [!IMPORTANT] ZERO-BLOAT GUARANTEE (LAZY-LOADING)
> Workflow này có lượng tri thức cực lớn. **NGHIÊM CẤM** tải toàn bộ các Skill cùng lúc.
> Orchestrator chỉ được tải Skill Target và Checklist tương ứng vào đầu mỗi Phase, và phải giải phóng (flush) ngữ cảnh cũ trước khi chuyển Phase để bảo vệ Context Window.
> - **`	oi-uu-workspace`**: Core execution engine cho Automation (Round 1) và điều phối chung (Round 2).
> - **`toi-uu-bo-nho`**: Xử lý các lỗi liên quan đến Token Bloat, Context Drift và Memory Contract.
> - **`thiet-lap-kiem-duyet`**: Lắp ráp rào cản Maker-Checker và phân quyền bảo mật.
> - **`do-luong-hieu-suat`**: Ghi nhận log và metrics (Phase Telemetry).

## Execution Order

```
[Phase 0] Snapshot: Mandatory Pre-Change Save
[Phase 1 / QG 1] ROUND 1: AUTOMATION (Python-Driven Systemic Repair)
    ⏹ CHECKPOINT (Mandatory — flush Round 1 context)
[Phase 2A / QG 2A] ROUND 2A: ARTISAN — Structure & Code (	oi-uu-workspace)
[Phase 2B / QG 2B] ROUND 2B: ARTISAN — Memory & RBAC (toi-uu-bo-nho)
[Phase 2C / QG 2C] ROUND 2C: ARTISAN — Security & Hooks (thiet-lap-kiem-duyet)
[Phase 3] Verify (Scanner-only) & Handoff
[Phase 4] Growth Flywheel Integration
[Phase 5] Telemetry & Log Flush
```

## Steps

---

### Phase 0: Mandatory Snapshot

// turbo

- **👤 Owner:** `[@GOV-COORD]`
- **Action:** Run `git add -A && git commit -m "SNAPSHOT: Pre-optimize"` and tag the repository. Dừng ngay lập tức nếu Git không hoạt động.

---

## ⚙️ Phase 1: ROUND 1 AUTOMATION (Script Execution)

- **👤 Owner:** `[@GOV-COORD]`
- **🛠 Skill Target:** `[	oi-uu-workspace]`
- **⚙️ Action:** Khởi chạy `	oi-uu-workspace` ở chế độ **AUTOMATION**.
- **📜 RAG Pointer:** BẮT BUỘC gọi `view_file` đọc tài liệu `.agents/skills/	oi-uu-workspace/references/workspace-optimization-protocols.md` (chỉ nạp phần ROUND 1).
- **📜 SHP Reference:** Load `references/self-healing-patterns-root-trunk.md` (SHP-01 → SHP-09 cho ROOT/TRUNK repairs).
- **Mục tiêu:** CẤM LLM xuất Markdown. Chỉ sinh mã Python dọn dẹp cấu trúc vật lý, mass purge, epistemic wiring, và nén archive.

> **Quality Gate 1:** Đã chạy xong toàn bộ script Python mà không bị lỗi crash? (YES -> Tiến tới Checkpoint. NO -> Rework/Sửa lỗi Python). Sau khi pass, giải phóng file protocol khỏi RAM.

### ⏹ ROUND 1 — MANDATORY CHECKPOINT

> [!CAUTION] CONTEXT WINDOW PROTECTION (v2.0)
> Round 1 (Automation) sinh ra lượng lớn Python script output và tool call history.
> **BẮT BUỘC** thực thi `/checkpoint-session` tại đây để giải phóng hoàn toàn Context Window trước khi bắt đầu Round 2 Artisan.
> Agent **CẤM** tiếp tục Round 2 trong cùng session nếu tổng Token đã > 40K.

---

## 🎨 Phase 2A: ROUND 2 ARTISAN — Structure & Code

> **🛠 Skill Budget:** `	oi-uu-workspace` (ONLY — 1 skill per sub-phase)
> **📜 RAG Pointer:** `.agents/skills/	oi-uu-workspace/references/workspace-optimization-protocols.md` (phần ROUND 2)
> **📜 SHP Reference:** `references/self-healing-patterns-branch-leaf.md` (SHP-10 → SHP-26 cho BRANCH/LEAF repairs)

- **👤 Owner:** `[@GOV-COORD]`
- **🛠 Skill Target:** `[	oi-uu-workspace]`
- **⚙️ Action:** Khởi chạy chế độ **ARTISAN** cho lỗi kiến trúc cấu trúc thư mục, code, quy trình, và Skill/Workflow enrichment.
- **Mục tiêu:** SLOW-MODE. Sửa TỪNG FILE MỘT. Rèn Agent SI, Gọt giũa Skill, và Ép khuôn Rule HPRF.

> [!CAUTION] POST-FIX SIZE GATE (Anti-Hollow-Skeleton)
> Sau khi tạo hoặc sửa bất kỳ file SKILL.md nào, Agent **BẮT BUỘC** kiểm tra:
> - File size ≥ 1.0KB. Nếu < 1.0KB → **REJECT** output là "Hollow Skeleton" và **REWORK**.
> - SKILL.md phải chứa tối thiểu: YAML frontmatter + `## Process` section với ≥3 bước hành động.

> **Quality Gate 2A:** Circuit Breaker có bị kích hoạt (File rớt 2 lần liên tiếp) không? (YES -> Thảy file vào `Failed_Optimization_Log.md` và bỏ qua. NO -> Hoàn tất tốt đẹp).

---

## 🧠 Phase 2B: ROUND 2 ARTISAN — Memory & RBAC

> **🛠 Skill Budget:** `toi-uu-bo-nho` (ONLY — 1 skill per sub-phase)
> **📜 RAG Pointer (BẮT BUỘC LOAD ĐẦY ĐỦ):**
> - `toi-uu-bo-nho/references/memory-rbac-rubric.md`
> - `toi-uu-bo-nho/references/contract-compaction-quan-ly-quy-tac.md`
> - `toi-uu-bo-nho/references/methodology.md`

- **👤 Owner:** `[@GOV-COORD]`
- **🛠 Skill Target:** `[s-toi-uu-bo-nho]`
- **⚙️ Action:** Nếu báo cáo Audit có lỗi rỗng bộ nhớ, tràn RAM (>12K tokens), hoặc lệch RBAC Contract → Chuyển luồng cho `[s-toi-uu-bo-nho]` phẫu thuật.
- **Quy tắc Độc quyền Memory:** BẮT BUỘC ủy quyền cho skill này xử lý `memory-contract.yml`. KHÔNG tự ý chỉnh sửa.

> **Quality Gate 2B:** Memory Contract đã pass CQS Size Gate (≥ 0.5KB) và RBAC V2.0 compliance? (YES → Next. NO → Rework).

---

## 🛡️ Phase 2C: ROUND 2 ARTISAN — Security & Hooks

> **🛠 Skill Budget:** `thiet-lap-kiem-duyet` (ONLY — 1 skill per sub-phase)

- **👤 Owner:** `[@GOV-COORD]`
- **🛠 Skill Target:** `[s-thiet-lap-kiem-duyet]`
- **⚙️ Action:** Nếu báo cáo Audit báo thiếu Maker-Checker, thiếu Hooks hoặc lỗ hổng bảo mật ranh giới → Chuyển luồng cho `[s-thiet-lap-kiem-duyet]` lắp rào cản.
- **Skip Condition:** Nếu không có finding nào thuộc Security/Hooks → SKIP Phase 2C và ghi log "Phase 2C: No security findings. Skipped."

> **Quality Gate 2C:** Tất cả Circuit Breaker states (OPEN/HALF-OPEN/CLOSED) đã được định nghĩa? Escalation Protocol đã hoàn chỉnh?

---

### Phase 3: Verify & Handoff

> [!IMPORTANT] AUTO-TRIGGER AUDIT
> Cập nhật theo yêu cầu vận hành Day 2: Hệ thống sẽ tự động kích hoạt lại lệnh `/w-kiem-dinh-workspace --full-scan` để nghiệm thu toàn bộ chất lượng sau khi quá trình vá lỗi (optimize) hoàn tất.

- **👤 Owner:** `[@GOV-COORD]`
- **⚙️ Action:** 
  - Kí xác nhận tiến độ mới nhất vào đỉnh `progress.md`.
  - Tự động kích hoạt luồng `/w-kiem-dinh-workspace --full-scan` để đảm bảo hệ thống đạt chuẩn 100/100 trước khi bàn giao lại Workspace cho User.

### Phase 4: Growth Flywheel Integration (Gear 4)

- Sau khi Optimize hoàn tất, nếu Agent/Skill mới đạt Điểm Chất lượng ≥ 4.5/5:
- Tự động kích hoạt lệnh `/growth-flywheel` (Bấm phím [1] chuyển sang Mode NOU-EXTRACTION). 
- Pass Input: `source_file`, `domain`, `skill_type`.
- Chờ vòng lặp NOU-Workflow lột xác và Commit Golden Template mới cất vào Kho Tàng `INDEX.yaml`. Đóng màng Flywheel.

---

### Phase 5: Telemetry & Memory Flush (OBSERVABILITY)

- **👤 Owner:** `[@GOV-COORD]`
- **🛠 Skill Target:** `[s-do-luong-hieu-suat]`
- **⚙️ Action:** Báo cáo các chỉ số (Số file đã sửa, Gate 1 & Gate 2A/2B/2C Pass Rate, Tỷ lệ nén dung lượng, Số lỗi Circuit Breaker, Số Hollow Skeleton bị REJECT) vào khối `Workflow Telemetry` bên trong tệp `QUALITY-LOG.md` theo chuẩn M1. Giải phóng hoàn toàn Memory Bus sau khi hoàn tất.

## Changelog

- v1.0.0 (2026-05-02): Initial release. Dual-Round Architecture.
- v2.0.0 (2026-05-10): Anti-CWS upgrade. Added mandatory checkpoint between Round 1/2. Split Phase 2 into 3 sub-phases (2A/2B/2C) with 1-skill-per-phase budget. Chunked SHP references. Added Post-Fix Size Gate. Fixed Phase 3 recursion bug (scanner-only verification).
