---
id: "WF-SYS-BUILD-WF-01"
name: "w-s-tao-quy-trinh-moi"
description: "Build workflow mới theo chuẩn V9. Capture intent, validate spec, tạo file, register vào index."
version: v1.0
status: Production-Ready
semantic_triggers: ['tạo quy trình mới', 'tao quy trinh moi', 'build workflow', 'thêm workflow']
owner: "PRO-W06"
skill_targets: ["01-dong-bo-muc-luc"]
hitl_timeout: "24h"
---

- **👤 Owner:** `[@PRO-W06]` (Architect — quyền ghi `.agents/`)
- **🛠 Skill Target:** `[01-dong-bo-muc-luc]`

# Quy Trình: /build-workflow

## Mục đích

Orchestrate 4 bước build workflow mới — từ capture intent đến register vào index. Đảm bảo mọi workflow mới trong `.agents/workflows/` tuân thủ chuẩn V9: có frontmatter, slash command, Steps, Decision Branches, HITL Gate. Là tầng phòng vệ chống "viết workflow monolithic" — trộn logic điều phối với xử lý nghiệp vụ.

## Dấu hiệu kích hoạt

Operator hoặc Builder gõ `/build-workflow {ten-workflow}` khi cần thêm workflow mới.

Tham số:
- `{ten-workflow}` — bắt buộc, kebab-case lowercase (vd `phan-tich-doi-thu`, `bao-cao-hieu-suat`)
- `{purpose}` — optional, 1 câu mô tả; nếu không có → workflow capture intent
- `--prefix {00|01|02}` — optional. `00` = core-business (mặc định), `01` = system-ops, `02` = reporting

## Điều kiện tiên quyết

- [ ] Workspace baseline đã init (có `.agents/workflows/`)
- [ ] Tên workflow đề xuất chưa trùng trong `00_WORKFLOW_INDEX.md`
- [ ] Tên không match L1 baseline workflow ID (khoi-dong-phien, dong-phien, luu-phien, kiem-dinh-workspace)

## Các bước thực hiện

### Bước 1 — Capture intent (5 phút)

4 câu hỏi cốt lõi:

1. **Workflow này giúp Operator làm gì?** (kết quả cụ thể, không generic)
2. **Kích hoạt khi nào?** — slash command hoặc trigger ngữ cảnh cụ thể
3. **Workflow gọi Skill nào?** — liệt kê skill targets. Nếu workflow tự xử lý nghiệp vụ → STOP, đề xuất tách thành Skill
4. **Output là gì?** — file báo cáo, log entry, hay trạng thái hệ thống thay đổi?

Nếu Operator không trả lời được câu 1 hoặc 3 → STOP: "Workflow chưa đủ rõ — cần xác định rõ mục đích và Skill phục vụ."

### Bước 2 — Design spec (10 phút)

Output Bước 2 là **spec sheet**, gồm:

#### 2a. Frontmatter draft

```yaml
---
id: "WF-{PREFIX}-{NAME}-{NN}"
name: "w-{ten-workflow}"
description: "{Mô tả 1 câu}"
version: v1.0
status: Draft
semantic_triggers: ['{trigger 1}', '{trigger 2}']
owner: "{Owner ID}"
skill_targets: ["{skill-1}", "{skill-2}"]
---
```

#### 2b. Body outline (8 section bắt buộc)

```
1. ## Mục đích (1-2 câu)
2. ## Dấu hiệu kích hoạt (slash command + ngữ cảnh)
3. ## Điều kiện tiên quyết (checklist)
4. ## Các bước thực hiện (Steps — chỉ điều phối, gọi Skill)
5. ## Tiêu chuẩn nghiệm thu (checklist đo lường)
6. ## Kết quả đầu ra (file/trạng thái)
7. ## Xử lý ngoại lệ (3-5 edge cases)
8. ## Tham chiếu (quan-ly-quy-tac + KB nguồn)
```

**Gate Bước 2:** Operator review spec sheet → OK thì sang Bước 3.

### Bước 3 — Build workflow file (10-15 phút)

**Nguyên tắc cốt lõi:** Workflow CHỈ ĐIỀU PHỐI. Nếu đang viết logic xử lý > 10 bước → STOP, tách ra Skill.

1. Tạo file tại `.agents/workflows/{prefix}-{ten-workflow}.md`
2. Prefix routing: `00-` → `00-core-business/`, `01-` → `01-system-ops/`, `02-` → `02-reporting/`
3. Viết frontmatter + 8 section theo spec
4. Validate:
   - [ ] Có slash command rõ ràng
   - [ ] Có Prerequisites + Inputs
   - [ ] Có HITL Gate ở bước rủi ro
   - [ ] Có Edge Cases (≥3)
   - [ ] Body ≤ 300 dòng (nếu vượt → tách components/)
   - [ ] Không chứa `[TBD]`, `[TODO]`, `[PLACEHOLDER]`
   - [ ] Path dùng `.agents/` (không phải `.agent/`)
   - [ ] `risk_level` trong frontmatter nếu applicable

### Bước 4 — Register & Verify (5 phút)

1. Cập nhật `00_WORKFLOW_INDEX.md` — thêm entry mới
2. Cập nhật `Quan-Tri/LICH-SU-THAY-DOI.md` — append "Tạo workflow {name}"
3. Trigger `01-dong-bo-muc-luc` để đồng bộ
4. Verify cross-ref: workflow gọi đúng skill tồn tại trong DANH-SACH-KY-NANG

**Gate Bước 4:** Workflow xuất hiện trong INDEX + cross-ref skill hợp lệ.

## Tiêu chuẩn nghiệm thu

- [ ] Frontmatter đầy đủ (id, name, description, triggers, skill_targets)
- [ ] Body ≤300 dòng, có 8 section bắt buộc
- [ ] Workflow không tự xử lý nghiệp vụ (chỉ gọi Skill)
- [ ] Có HITL Gate ở bước rủi ro
- [ ] Tên kebab-case lowercase
- [ ] Không trùng workflow ID có sẵn
- [ ] INDEX cập nhật
- [ ] LICH-SU-THAY-DOI có entry

## Kết quả đầu ra

- File `.agents/workflows/{prefix}-{ten-workflow}.md`
- 00_WORKFLOW_INDEX.md cập nhật
- LICH-SU-THAY-DOI.md append entry

## Xử lý ngoại lệ

- **Workflow quá đơn giản (<5 bước, không gọi Skill):** Có thể là Rule chứ không phải Workflow → đề xuất chuyển thành Rule.
- **Workflow gọi Skill chưa tồn tại:** WARN liệt kê broken dependency. Đề xuất build Skill trước (`/build-skill`).
- **Builder muốn skip Bước 2 review:** KHÔNG skip. Spec review <5 phút nhưng ngăn build sai hướng.
- **Trùng slash command với workflow khác:** HALT — buộc đổi tên hoặc merge logic.
