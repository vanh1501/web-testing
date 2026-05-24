---
id: "WF-PRJ-INIT-01"
name: "w-khoi-tao-du-an-moi"
description: "Khởi tạo dự án mới chuẩn PMBOK bằng cơ chế 1-shot: clone 5 file Skeleton Template, hydrate placeholder, tạo cấu trúc thư mục, đăng ký vào Bảng Điều Khiển. Chống tình trạng Operator phải gõ từng file thủ công."
version: v2.0
status: Production-Ready
semantic_triggers: ['tạo dự án', 'tạo du an', 'dự án mới', 'du an moi', 'khởi tạo project', 'khoi tao project', 'new project', 'kick off project', 'scaffold dự án', 'PMBOK setup']
owner: "PRO-W05"
skill_target: "00-quan-ly-du-an"
hitl_timeout: "24h"
retry_policy: {max_attempts: 3, backoff: exponential_1s_2s_4s, fallback: "log_to_ACTION-LOG_and_report_human"}
---

- **👤 Owner:** `[@PRO-W05]`
- **🛠 Skill Target:** `[00-quan-ly-du-an]`
- **⏱ HITL Timeout:** 24h, escalation → BOM admin (Sếp Hậu)
- **🔄 Circuit Breaker:** retry 3 lần (exponential backoff), fallback → ghi `Bang-Dieu-Khien/ACTION-LOG.md` + ping human

# Quy Trình: /w-khoi-tao-du-an-moi (v2.0 — PMBOK Scaffolding Engine)

## Purpose & Scope

**Purpose:** Khởi tạo dự án mới chuẩn PMBOK 1-shot. Chuyển từ quy trình thủ công 10-15 lượt hội thoại → automate hoàn toàn.

**Scope:** Bao trùm 3 thư mục cốt lõi (`Du-An/`, `Du-Lieu-Vao/`, `Ket-Qua/`) + 5 file PMBOK templates (Charter, Master Index, RACI, Risk Log, Change Log) + đăng ký registry. KHÔNG bao gồm: tracking dự án đang chạy (skill khác), retrospective (skill khác).

## Trigger

Operator ra lệnh: "tạo dự án mới", "khởi tạo project", "set up dự án mới", "kick off project", hoặc bất kỳ yêu cầu nào ngụ ý cần track 1 initiative riêng biệt với mã quản trị.

## Prerequisites

- [ ] Workspace đã init (`Du-An/`, `Kho-Du-Lieu/`, `Bang-Dieu-Khien/` tồn tại)
- [ ] (Optional) Bộ template tại `.agents/templates/pmbok/` — nếu không có, skill `00-quan-ly-du-an` dùng default fallback

## Steps

> [!IMPORTANT] KARPATHY VERIFICATION MANDATE
> Trước mỗi Step BẮT BUỘC: `[Step] -> verify: [Tiêu chí đo lường cụ thể]`. CẤM Blind Looping.

### Step 1: Thu thập Metadata từ Operator
**Action:** Hỏi Operator cung cấp metadata tối thiểu (tên dự án bắt buộc; còn lại auto-fill).
**Verify:** `PROJECT_NAME` non-empty; nếu Operator chỉ cho 1 câu "tạo dự án ABC", auto-suggest:
- `PROJECT_CODE` = `PRJ-{YY}-{XXX}` (next available)
- `PROJECT_FOLDER` = slugify(PROJECT_NAME)
- `DATE` = system today
- `PM_NAME` = "Sếp" (default)
- `SPONSOR` = `PM_NAME` (default)

### Step 2: Pre-Check Folder Existence (Decision)
**Action:** Gọi `00-quan-ly-du-an` skill, sub-action `check_project_exists.py`.
**Verify:** Return `exists: false` để proceed.

**Decision branch:**
- `exists: true` → **HITL Gate 1** (xem section HITL Gates) → Operator chọn overwrite/rename
- `exists: false` → proceed Step 3

### Step 3: Scaffold via Skill
**Action:** Delegate `00-quan-ly-du-an` (sub-action `scaffold_pmbok.py`) với metadata thu thập từ Step 1.
**Verify:** Skill return JSON `scaffold_result: "success"` + `files_created` đủ 5 file + `registry_updated: true`.

### Step 4: Xác nhận & Handoff
**Action:** Trình bày JSON output cho Operator: 3 folder created + 5 file PMBOK + 1 registry update.
**Verify:** Output Contract đầy đủ (xem section Output Contract).

## HITL Gates

| Gate | Step | Timeout | Action on timeout | Escalation |
|------|------|---------|-------------------|------------|
| Gate 1 — Folder collision | Step 2 | 24h | Pause workflow + send reminder | BOM admin manual decide |
| Gate 2 — Final confirm (optional) | Step 4 | 24h | Auto-finalize (folder đã tạo, không rollback) | Log to ACTION-LOG |

## Circuit Breaker Policy

| Failure mode | Detection | Retry | Fallback |
|--------------|-----------|-------|----------|
| Skill `00-quan-ly-du-an` không respond | Timeout 30s | 3 lần (1s, 2s, 4s backoff) | Log to ACTION-LOG + report human |
| Write permission denied | OS error | 1 lần (check permission) | REFUSE + ask BOM permission |
| Template `.agents/templates/pmbok/` missing | File not found | 0 (immediate fallback) | Dùng default template inline (skill 00-quan-ly-du-an handle) |
| Registry append fail | Write error | 3 lần | Log + manual add registry sau |

## Edge Cases & Recovery

1. **Trùng tên/mã dự án** → HITL Gate 1, Operator chọn: (a) overwrite (cần explicit `--allow-overwrite`), (b) rename project_folder/code
2. **Template `.agents/templates/pmbok/` không đủ 5 file** → Skill fallback default templates, warn user "Đang dùng default, recommend setup template chính thức sau"
3. **Operator muốn thêm file custom** → Accept, file custom đặt tên `01_`, `02_` (không prefix `00_`); skill log vào `custom_folders`
4. **Tên dự án có ký tự đặc biệt** ($, &, /) → Auto-sanitize folder name (slugify), giữ PROJECT_NAME nguyên trong content
5. **Project_code trùng dự án cũ** → Auto-append `-v2`, `-v3` suffix, warn Operator
6. **Write permission denied** → Circuit Breaker fallback (xem table trên)

## Output Contract (Idempotent JSON)

```json
{
  "workflow_id": "WF-PRJ-INIT-01",
  "run_status": "success | partial_success | halt",
  "project_metadata": {
    "project_name": "...",
    "project_code": "PRJ-26-001",
    "project_folder": "...",
    "pm": "...",
    "sponsor": "..."
  },
  "files_created": [{"path": "...", "status": "ok"}],
  "folders_created": [...],
  "registry_updated": true,
  "auto_filled_fields": ["sponsor (default=PM)"],
  "hitl_gates_triggered": [],
  "circuit_breaker_activated": false,
  "next_workflow_suggested": "00-quan-tri-du-an (sau scaffold, để lập WBS/RACI/Timeline)"
}
```

## Cross-Workflow Chaining

- **Receives from:** `00-phan-tich-nhiem-vu` (khi confirm Project, không phải Task ngắn hạn)
- **Hands off to:** `00-quan-tri-du-an` (sau scaffold, để lập WBS/RACI/Timeline chi tiết)

## Validation

- [ ] Mã Dự án tuân thủ format `PRJ-{YY}-{XXX}`
- [ ] Thư mục `Du-An/{folder}/` tồn tại với đủ 5 file `00_*.md`
- [ ] Thư mục `Kho-Du-Lieu/Du-Lieu-Vao/{folder}/` tồn tại
- [ ] Thư mục `Kho-Du-Lieu/Ket-Qua/{folder}/` tồn tại
- [ ] `DANH-SACH-DU-AN.md` cập nhật dòng mới
- [ ] Không còn `[PLACEHOLDER]` chưa được thay thế trong 5 file
- [ ] JSON Output Contract đầy đủ các fields declared

## Resources

- Skill: `00-quan-ly-du-an` (sub-actions: `check_project_exists.py`, `scaffold_pmbok.py`)
- Template path: `.agents/templates/pmbok/` (optional, fallback default)
- Registry: `Bang-Dieu-Khien/DANH-SACH-DU-AN.md`
