---
name: s-quan-ly-du-an
description: >
  Thợ mộc khởi tạo dự án mới chuẩn PMBOK — clone bộ 5 Skeleton Templates (Project Charter, Master Index,
  RACI Matrix, Risk Issue Log, Change Log), thay thế placeholder `{{VAR}}` bằng metadata thực, tạo cấu trúc
  thư mục dự án + data warehouse, và đăng ký dự án vào Bảng Điều Khiển. Biến quy trình khởi tạo thủ công
  10-15 lượt hội thoại thành cơ chế 1-shot tự động. Kích hoạt khi user nói "tạo dự án mới", "khởi tạo project",
  "scaffold dự án", "setup workspace dự án", "kick off project", hoặc workflow `/w-khoi-tao-du-an-moi` gọi.
  KHÔNG dùng khi: dự án đã có structure cần update (dùng skill update khác), tracking/reporting dự án đang chạy
  (chưa cover, gap), retrospective sau close project (chưa cover, gap).
version: v2.0
status: Production-Ready
scope_note: |
  Skill này CHỈ làm scaffolder — khởi tạo cấu trúc dự án ban đầu.
  KHÔNG cover: tracking tiến độ, escalation, retrospective. Đó là scope của skill `quan-ly-du-an-running` (chưa build).
hook_summary:
  - HOOK_PROJECT_TEMPLATE_SET: bộ template (mặc định PMBOK 5 file, có thể swap Scrum/Kanban)
  - HOOK_FOLDER_STRUCTURE: cấu trúc thư mục (mặc định Du-An + Kho-Du-Lieu)
  - HOOK_REGISTRY_PATH: nơi đăng ký dự án (mặc định Bang-Dieu-Khien/DANH-SACH-DU-AN.md)
---

# Project Scaffolder — Thợ Mộc Khởi Tạo Dự Án (PMBOK)

## Mục đích

Biến khởi tạo dự án từ quy trình thủ công 10-15 lượt hội thoại thành cơ chế **1-shot automate**. Agent đọc template, thay biến, tạo thư mục, ghi file — Operator chỉ cung cấp metadata ban đầu.

**Phạm vi:** CHỈ scaffolder ban đầu. KHÔNG cover PM advisor cho dự án đang chạy (sẽ là skill khác).

## When to use this skill

- User nói "tạo dự án mới", "khởi tạo project", "set up dự án", "kick off project"
- Workflow `/w-khoi-tao-du-an-moi` được trigger
- Cần bộ 5 file PMBOK (Charter / Master Index / RACI / Risk Log / Change Log) + folder structure

**KHÔNG dùng khi:**
- Dự án đã tồn tại, cần update/maintain → skill khác
- Cần tracking tiến độ / báo cáo status dự án đang chạy → gap, ask user setup skill mới
- Cần retrospective sau close → gap

## How to use it

### Đầu vào bắt buộc

Agent **PHẢI** thu thập đủ trước khi bắt đầu:

| Biến | Ý nghĩa | Ví dụ | Bắt buộc? |
|------|---------|-------|-----------|
| `{{PROJECT_NAME}}` | Tên đầy đủ dự án | "Vận hành E-commerce Đa Sàn Elmich 2026" | ✅ |
| `{{PROJECT_CODE}}` | Mã viết tắt | "ECOM-2026-001" | ✅ (auto-gen nếu thiếu) |
| `{{PROJECT_FOLDER}}` | Tên thư mục (không dấu) | "Ecom-Operation-2026" | ✅ (auto-gen nếu thiếu) |
| `{{DATE}}` | Ngày khởi tạo | "2026-05-15" | ✅ (auto từ hệ thống) |
| `{{PM_NAME}}` | Project Manager | "Sếp Hậu" | ✅ |
| `{{SPONSOR}}` | Sponsor/Chủ dự án | "CEO Elmich" | ⬜ (default = PM) |
| `{{COORDINATOR}}` | Điều phối viên | "MindX Operations" | ⬜ (default = "Trợ lý AI") |

**Auto-gen logic:** Nếu Operator chỉ cho Tên dự án, agent tự sinh `PROJECT_CODE` (viết tắt + năm) và `PROJECT_FOLDER` (loại dấu, gạch ngang).

### Step 1 — Pre-Check: Folder Existence

Gọi `scripts/check_project_exists.py --folder={PROJECT_FOLDER}` trước khi proceed.
- Nếu folder đã tồn tại → REFUSE create, HỎI Operator: rename hay overwrite (cần confirm explicit)
- Nếu chưa → proceed Step 2

### Step 2 — Scaffold Folder Structure

Gọi `scripts/scaffold_pmbok.py --name={PROJECT_NAME} --code={PROJECT_CODE} --folder={PROJECT_FOLDER} --pm={PM_NAME} --sponsor={SPONSOR}`.

Script tự động:
1. Tạo 3 thư mục:
   - `Du-An/{{PROJECT_FOLDER}}/` — Root dự án
   - `Kho-Du-Lieu/Du-Lieu-Vao/{{PROJECT_FOLDER}}/` — Input chờ
   - `Kho-Du-Lieu/Ket-Qua/{{PROJECT_FOLDER}}/` — Output xả
2. Clone 5 templates từ `.agents/templates/pmbok/`:
   - `00_Project_Charter.md`
   - `00_Project_Master_Index.md`
   - `00_RACI_Matrix.md`
   - `00_Risk_Issue_Log.md`
   - `00_Change_Log.md`
3. Hydrate placeholder `{{...}}` bằng metadata thực
4. Ghi vào `Du-An/{{PROJECT_FOLDER}}/`

### Step 3 — Register Project

Append metadata dự án vào `Bang-Dieu-Khien/DANH-SACH-DU-AN.md` (auto by script).

### Step 4 — Confirmation

Script return JSON với danh sách file đã tạo. Agent liệt kê cho Operator kiểm tra.

## Edge cases & escalation

1. **Folder đã tồn tại** → REFUSE, ask Operator rename hoặc explicit confirm overwrite
2. **Template files missing trong `.agents/templates/pmbok/`** → REFUSE, ask user setup templates trước
3. **Placeholder `{{VAR}}` không có data** → Auto-fill default (vd SPONSOR = PM_NAME, COORDINATOR = "Trợ lý AI"), warn user
4. **Tên dự án có ký tự đặc biệt** ($, &, /) → Auto-sanitize folder name, keep nguyên project_name trong content
5. **Path write permission denied** → REFUSE, escalate "Cần quyền ghi vào Du-An/, xin Operator check permission"
6. **Project_code trùng dự án cũ** → Append suffix v2/v3, warn user
7. **Operator yêu cầu thêm folder ngoài 3 default** (vd "thêm thư mục Hợp đồng") → Accept, log custom_folders trong manifest
8. **Workflow `/w-khoi-tao-du-an-moi` chỉ cho 1 field PROJECT_NAME** → Auto-gen các field còn lại, present manifest cho Operator confirm trước Step 2

## Anti-patterns

- ❌ Ghi đè thư mục dự án đã tồn tại không hỏi
- ❌ Tự sáng tác nội dung nghiệp vụ vào template (chỉ thay biến `{{}}`, giữ placeholder `(Mô tả...)` cho Operator điền)
- ❌ Xóa hoặc sửa file của dự án khác khi scaffolding
- ❌ Skip registration vào DANH-SACH-DU-AN.md
- ❌ Im lặng khi thiếu file template

## Output Contract (Idempotent JSON)

```json
{
  "scaffold_result": "success | folder_exists | permission_denied | template_missing | partial_success",
  "project_metadata": {
    "project_name": "Vận hành E-commerce Đa Sàn Elmich 2026",
    "project_code": "ECOM-2026-001",
    "project_folder": "Ecom-Operation-2026",
    "pm": "Sếp Hậu",
    "sponsor": "CEO Elmich",
    "coordinator": "Trợ lý AI",
    "date_created": "2026-05-15"
  },
  "files_created": [
    {"path": "Du-An/Ecom-Operation-2026/00_Project_Charter.md", "status": "ok"},
    {"path": "Du-An/Ecom-Operation-2026/00_Project_Master_Index.md", "status": "ok"},
    {"path": "Du-An/Ecom-Operation-2026/00_RACI_Matrix.md", "status": "ok"},
    {"path": "Du-An/Ecom-Operation-2026/00_Risk_Issue_Log.md", "status": "ok"},
    {"path": "Du-An/Ecom-Operation-2026/00_Change_Log.md", "status": "ok"}
  ],
  "folders_created": [
    "Du-An/Ecom-Operation-2026/",
    "Kho-Du-Lieu/Du-Lieu-Vao/Ecom-Operation-2026/",
    "Kho-Du-Lieu/Ket-Qua/Ecom-Operation-2026/"
  ],
  "registry_updated": true,
  "auto_filled_fields": ["sponsor (default=PM_NAME)", "coordinator (default='Trợ lý AI')"],
  "ship_decision": "ship | warn | halt",
  "confidence_level": "high | medium | low",
  "escalation_needed": false,
  "next_steps": ["Operator điền chi tiết business logic vào Charter", "Sau scaffold → khi PM running mới gọi skill quan-ly-du-an-running (chưa build)"]
}
```

## Confidence Calibration

**F1 — Confidence signaling:**
- `high`: 7/7 trường input có hoặc auto-fill được, không folder collision, mọi template file tồn tại, scaffold success 5/5 files
- `medium`: 1-2 trường auto-fill default (vd SPONSOR=PM_NAME), template scaffold OK
- `low`: Có warning (vd PROJECT_CODE collision phải append v2), partial_success (vd 4/5 files create OK, 1 failed)

**F2 — Escalation triggers:**
- Folder existence collision → REFUSE, ask explicit overwrite
- Template files missing → REFUSE, ask setup
- Write permission denied → REFUSE, ask permission check
- Operator yêu cầu modify scope (vd tracking/retro) → REFUSE, point out skill này chỉ scaffolder, suggest tạo skill mới

**F3 — Self-critique:**
- `auto_filled_fields` field LIST tất cả trường default được apply (để Operator review)
- Section `next_steps` rõ Operator phải tự điền business logic — skill không bịa
- Nếu confidence=low → warning "Scaffold partial, cần Operator manual fix trước go-live"

## Cross-skill chaining

- **Nhận input từ:** `phan-tich-yeu-cau` (sau khi có Implementation Plan, scaffolder tạo workspace)
- **Truyền output cho:** Không có downstream skill mặc định — sau scaffold là Operator manual work
- **Gap note:** Sau khi dự án scaffold xong và running, cần skill `quan-ly-du-an-running` (chưa build) để PM advisor. Operator phải tự setup hoặc gọi human PM.

## Resources

| Mục đích | File |
|----------|------|
| PMBOK Executive SOP | `references/pmbok-executive-sop.md` |
| PMBOK Skeleton templates | `.agents/templates/pmbok/` (external) |

**Scripts:**
- `scripts/scaffold_pmbok.py` — Main scaffolder (clone + hydrate)
- `scripts/check_project_exists.py` — Pre-check folder existence

## BOM Hands-On Example

**Input từ Operator:**
> "Em muốn tạo dự án mới: Vận hành E-commerce Đa Sàn Elmich 2026, em là PM, CEO Elmich là sponsor"

**Skill xử lý:**

1. Auto-fill:
   - PROJECT_NAME: "Vận hành E-commerce Đa Sàn Elmich 2026"
   - PROJECT_CODE: "ECOM-2026-001" (auto-gen từ name + year + counter)
   - PROJECT_FOLDER: "Ecom-Operation-2026" (auto-sanitize)
   - DATE: 2026-05-15 (system)
   - PM_NAME: "Em" (Operator)
   - SPONSOR: "CEO Elmich"
   - COORDINATOR: "Trợ lý AI" (default)

2. Pre-check: `Du-An/Ecom-Operation-2026/` chưa tồn tại → OK proceed

3. Run `scaffold_pmbok.py` → 5 files create OK + 3 folders + 1 registry update

4. JSON contract: `scaffold_result: success, confidence: high`

5. Output cho Operator:
   - ✅ Tạo 5 file PMBOK trong `Du-An/Ecom-Operation-2026/`
   - ✅ Tạo 2 folder data warehouse
   - ✅ Đăng ký dự án vào `DANH-SACH-DU-AN.md`
   - 👉 Next: Em mở `00_Project_Charter.md` điền chi tiết business goal, scope, deliverables

## Guardrails

- `Overwrite_Without_Confirm` → [DENY] Không ghi đè folder dự án đã tồn tại
- `Fake_Business_Content` → [DENY] Chỉ thay biến `{{}}`, không sáng tác nội dung nghiệp vụ
- `Cross_Project_Modify` → [DENY] Không xóa/sửa file của dự án khác
- `Skip_Registration` → [DENY] LUÔN update DANH-SACH-DU-AN.md

## Rules

- `Template_Supremacy`: Clone từ `.agents/templates/pmbok/`, không từ scratch
- `Placeholder_Preservation`: `(Mô tả...)` text giữ nguyên cho Operator điền sau
- `One_Shot_Atomicity`: Hoặc scaffold success 100% hoặc REFUSE — không partial commit
- `Auto_Fill_Transparency`: Mọi field auto-fill PHẢI list trong `auto_filled_fields` để Operator biết
