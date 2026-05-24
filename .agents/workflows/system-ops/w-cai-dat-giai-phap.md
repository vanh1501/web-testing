---
id: "WF-SYS-DEPLOY-01"
name: "w-cai-dat-giai-phap"
description: "Phễu tiếp nhận đa năng: (Route 1) ZIP Spec Pack từ ChatGPT — kiểm định 3 Lớp đầy đủ. (Route 2) ZIP Library Rebuild — nâng cấp Skill/Workflow với QA Gate gọn nhẹ. Auto-Router tự phát hiện loại gói."
version: v2.0
status: Production-Ready
semantic_triggers: ['cài đặt giải pháp', 'cai dat giai phap', 'deploy spec', 'cài đặt từ zip', 'giải nén spec', 'nạp spec pack', 'import zip', 'cài đặt kỹ năng từ file', 'nâng cấp thư viện', 'upgrade library', 'nạp skill mới']
owner: "PRO-W06"
skill_targets: ["01-tao-ky-nang-moi", "01-tao-quy-trinh-moi", "01-quan-ly-quy-tac", "01-dong-bo-muc-luc"]
hitl_timeout: "24h"
retry_policy: {max_attempts: 2, backoff: exponential_1s_2s, fallback: "skip_component_and_log_delta"}
---

- **👤 Owner:** `[@PRO-W06]` (Architect — quyền ghi `.agents/`)
- **🛠 Skill Targets:** `[01-tao-ky-nang-moi, 01-tao-quy-trinh-moi, 01-quan-ly-quy-tac, 01-dong-bo-muc-luc]`
- **⏱ HITL Timeout:** 24h, escalation → BOM admin
- **🔄 Circuit Breaker:** retry 2 lần (exponential backoff), fallback → skip component + log delta report

# Quy Trình: /w-cai-dat-giai-phap (v2.0 — Dual-Route ZIP Deployer)

## Purpose & Scope

**Purpose:** Phễu tiếp nhận đa năng cho file ZIP. Tự động phân loại 2 loại gói:
- **Route 1 (Spec Pack):** Gói đầy đủ từ ChatGPT — có Blueprint, Handoff Guide, Test Prompts. Kiểm định 3 Lớp nghiêm ngặt.
- **Route 2 (Library Upgrade):** Gói thuần component (`*-rebuild/`) — chỉ chứa Skills/Workflows đã enriched. QA Gate gọn nhẹ, tập trung vào format + conflict.

**Scope:** Bao trùm toàn bộ vòng đời từ "nhận file ZIP" đến "hệ thống sẵn sàng chạy thử". KHÔNG bao gồm: chạy thử nghiệm, tối ưu PDCA (Cụm 3 Day 2), audit chất lượng sâu (`/01-kiem-dinh-workspace`).

**Chuẩn Spec Pack bắt buộc:** Xem chi tiết tại Step 3A (Route 1).

## Trigger

Operator gõ `/w-cai-dat-giai-phap` hoặc nói: "cài đặt giải pháp", "cài đặt từ zip", "nạp spec pack", "import kỹ năng từ file", "deploy spec".

Tham số:
- `{zip-path}` — optional. Đường dẫn tệp ZIP. Nếu không cung cấp → auto-detect file `.zip` mới nhất trong `Kho-Du-Lieu/Du-Lieu-Vao/`.
- `{du-an}` — optional. Tên dự án để nhóm output. Nếu không cung cấp → trích từ tên ZIP.
- `--only {quan-ly-quy-tac|skills|workflows}` — optional. Chỉ deploy 1 loại component.
- `--mode {spec|library}` — optional. Ép route thủ công. Nếu không cung cấp → Auto-Router tự phát hiện.

## Prerequisites

- [ ] File ZIP đã tồn tại trong `Kho-Du-Lieu/Du-Lieu-Vao/`
- [ ] Workspace đã init (có `.agents/`, `Du-An/`, `Kho-Du-Lieu/`, `Bang-Dieu-Khien/`)
- [ ] Có dự án hiện tại hoặc Operator sẵn sàng tạo mới (chain `/w-00-khoi-tao-du-an-moi` nếu cần)

## Steps

> [!IMPORTANT] KARPATHY VERIFICATION MANDATE
> Trước mỗi Step BẮT BUỘC: `[Step] -> verify: [Tiêu chí đo lường cụ thể]`. CẤM Blind Looping.

### Step 1: Tiếp nhận & Định vị file ZIP

**Action:** Xác định file ZIP. Nếu Operator cung cấp `{zip-path}` → dùng path đó. Nếu không → quét `Kho-Du-Lieu/Du-Lieu-Vao/` tìm file `.zip` mới nhất (theo timestamp modified).

**Verify:** File tồn tại + extension `.zip` + kích thước > 0 bytes.

**Decision branch:**
- File không tìm thấy → **HALT**: "Không tìm thấy file ZIP. Vui lòng kiểm tra `Kho-Du-Lieu/Du-Lieu-Vao/`."
- File tìm thấy → Log tên file + kích thước → Proceed Step 2.

### Step 2: Giải nén An toàn vào Staging

**Action:**
1. Tạo thư mục staging: `.agents/tmp/staging-{YYYYMMDD-HHmm}/`.
2. Giải nén ZIP vào staging (PowerShell `Expand-Archive` hoặc Python `zipfile`).
3. File gốc trong `Du-Lieu-Vao/` giữ nguyên (L0 `Modify_Du_Lieu_Vao` → DENY).
4. Auto-detect root: Nếu ZIP có folder wrapper (double-wrapped) → tìm folder con chứa `.agents/` hoặc `README.md` làm root thực. Nếu chứa `*-rebuild/` (VD: `skills-rebuild/`, `workflow-rebuild/`) → đánh dấu là Library pattern.

**Verify:** Thư mục staging chứa ≥1 file sau giải nén.

**Edge case:**
- ZIP corrupt → **HALT** + "File ZIP bị hỏng, không thể giải nén."
- ZIP chứa >100 file → WARN "Gói lớn bất thường" + vẫn proceed.

### Step 2.5: Auto-Router — Phân loại Gói ZIP

**Action:** Quét staging để xác định loại gói:

| Dấu hiệu | Loại gói | Route |
|---|---|---|
| Có `SOLUTION_BLUEPRINT.md` hoặc `HANDOFF_GUIDE.md` | Spec Pack | → **Route 1** (Step 3A) |
| Có thư mục `*-rebuild/` chứa `SKILL.md` hoặc workflow `.md` | Library Rebuild | → **Route 2** (Step 3B) |
| Có `.agents/skills/` hoặc `.agents/workflows/` trực tiếp | Spec Pack (standard) | → **Route 1** (Step 3A) |
| Không khớp pattern nào | Không xác định | → **HITL**: Hỏi Operator chọn Route 1 hoặc 2 |

**Path Mapping (Route 2 only):** Nếu Route 2, lập bảng mapping:
- `skills-rebuild/*` → `.agents/skills/*`
- `workflow-rebuild/*` → `.agents/workflows/00-core-business/*`
- `*_INDEX.md` → Bỏ qua (sẽ tái tạo ở Step 8)
- `CHANGELOG.md` → Lưu vào `Quan-Tri/LICH-SU-THAY-DOI.md` (append)

**Verify:** Route đã xác định (1 hoặc 2). Log: "Phân loại gói: [Route X] — [lý do]."

### Step 3A: QA Gate Lớp 1 — Kiểm Đủ File (Route 1: Spec Pack)

> **Chỉ chạy nếu Auto-Router chọn Route 1.**

**Action:** Quét cấu trúc staging theo checklist:

**Required (bắt buộc):**
```
[ ] README.md
[ ] AGENTS.md hoặc GEMINI.md
[ ] SOLUTION_BLUEPRINT.md
[ ] HANDOFF_GUIDE.md
[ ] ACCEPTANCE_CRITERIA.md
[ ] TEST_PROMPTS.md
[ ] .agents/quan-ly-quy-tac/*.md (≥1 file)
[ ] .agents/workflows/*.md (≥1 file)
[ ] .agents/skills/*/SKILL.md (≥1 skill folder)
```

**Recommended (khuyến nghị):**
```
[ ] MANIFEST.md
[ ] CHANGELOG.md
[ ] business_sources/source_notes.md
```

**Verify:** Đếm required: có/thiếu. Tạo bảng kết quả.

**Decision branch:**

| Kết quả | Grade | Hành động |
|---|---|---|
| Đủ 100% required + recommended | **A** — Đạt chuẩn | → Proceed Step 4 |
| Đủ required, thiếu 1-2 recommended | **B** — Đạt có điều kiện | → **HITL Gate 1**: "Thiếu [X]. Tiếp tục?" |
| Thiếu bất kỳ required nào | **C** — Chưa đạt | → **HALT**: Liệt kê thiếu hụt. "Yêu cầu quay ChatGPT bổ sung." |

### Step 3B: QA Gate Lớp 1 — Kiểm Đủ File (Route 2: Library Upgrade)

> **Chỉ chạy nếu Auto-Router chọn Route 2.**

**Action:** Quét cấu trúc staging theo checklist nhẹ:

**Required (bắt buộc):**
```
[ ] Ít nhất 1 folder chứa SKILL.md (nếu là Skill Library)
[ ] Hoặc ít nhất 1 file .md có YAML frontmatter (nếu là Workflow Library)
[ ] Mỗi SKILL.md > 0.5KB (không phải skeleton rỗng)
```

**Recommended (khuyến nghị):**
```
[ ] CHANGELOG.md
[ ] *_INDEX.md
[ ] evals/evals.json per skill
```

**Version Compare:** Nếu skill/workflow cùng tên đã tồn tại trong workspace → so sánh file size. Nếu ZIP version nhỏ hơn hoặc bằng → WARN "Phiên bản ZIP không mới hơn. Tiếp tục?".

**Decision branch:**

| Kết quả | Grade | Hành động |
|---|---|---|
| Đủ required + có CHANGELOG | **A** | → Proceed Step 4 |
| Đủ required, thiếu CHANGELOG | **B** | → WARN + Proceed Step 4 |
| Không có SKILL.md lẫn workflow .md nào | **C** | → **HALT**: "ZIP không chứa component hợp lệ." |

### Step 4: QA Gate Lớp 2 — Kiểm Đúng Chuẩn (Format Validation)

**Action:** Quét nội dung từng component:

| Kiểm tra | Tiêu chí | Kết quả |
|---|---|---|
| Rule format | Có Purpose/Trigger. Không chứa chuỗi >10 bước. Có `risk_level` trong frontmatter. | PASS/FAIL |
| Workflow format | Có slash command. Có `## Steps`. Có Prerequisites + Inputs + Edge Cases. Chỉ điều phối. | PASS/FAIL |
| Skill format | Folder riêng. Frontmatter `name` + `description` (WHAT+WHEN). Có Human Checkpoint + QA Checklist. | PASS/FAIL |
| Naming | Tên file/folder kebab-case lowercase. | PASS/WARN |
| Placeholder | Không còn `[TBD]`, `[TODO]`, `[Add later]`, `[PLACEHOLDER]`. | PASS/FAIL |
| Path integrity | Dùng `.agents/` (không phải `agents/` hay `.agent/`). | PASS/FAIL |

**Verify:** Tạo bảng kết quả dạng PASS/WARN/FAIL per component.

**Decision branch:**
- Có lỗi FAIL → **HITL Gate 2**: Liệt kê lỗi. "Sửa tại chỗ hay quay ChatGPT bổ sung?"
  - Operator chọn "Sửa tại chỗ" → Agent sửa lỗi format cơ bản (thêm frontmatter, đổi tên).
  - Operator chọn "Quay ChatGPT" → **HALT** + giữ staging để tiếp tục sau.
- Chỉ WARN → Ghi chú + Proceed Step 4.5.
- Toàn PASS → Proceed Step 4.5.

### Step 4.5: Chuẩn hóa Tiền tố Tên (Auto-Prefix Optimization)

**Action:** Rà soát tên của toàn bộ Skills và Workflows trong thư mục staging để đảm bảo tuân thủ Naming Convention:
1. **Kiểm tra tiền tố:** Phát hiện các file Workflow / thư mục Skill chưa có tiền tố số (`00-` hoặc `01-`).
2. **Phân tích ngữ nghĩa (Auto-Categorize):** Dựa vào nội dung (Purpose/Description), tự động phân loại:
   - Thêm tiền tố `00-` (Core Business) nếu là công cụ nghiệp vụ, kinh doanh, sản xuất tài liệu, phân tích dữ liệu.
   - Thêm tiền tố `01-` (System Ops) nếu là công cụ vận hành, quản trị workspace, audit hệ thống, đóng/mở phiên.
3. **Chuẩn hóa đồng bộ:** Đổi tên tệp/thư mục ngay trên staging thành `00-{tên-cũ}` hoặc `01-{tên-cũ}`. **Đồng thời**, tự động cập nhật tất cả các liên kết nội bộ (Cross-references) như lệnh Slash Command, cấu hình `skill_targets` bên trong Workflow để ngăn chặn lỗi Dangling Component.

**Verify:** 100% Skill và Workflow trên staging đã mang chuẩn tiền tố `00-` hoặc `01-` trước khi chuyển sang Step 5.

### Step 5: QA Gate Lớp 3 — Kiểm An toàn (Safety Check)

**Action:** Kiểm tra điều kiện an toàn trước khi inject vào hệ thống sống:

| Kiểm tra | Tiêu chí |
|---|---|
| Human checkpoint | Workflow có điểm chờ duyệt ở bước rủi ro? |
| Test coverage | `TEST_PROMPTS.md` có ≥5 test tách loại: (1) happy path, (2) thiếu input, (3) sai format, (4) nhạy cảm, (5) ngoài phạm vi? |
| No deploy claim | Không tuyên bố "đã deploy" hoặc "đã chạy thật"? |
| PII protection | Không chứa dữ liệu cá nhân thật (tên, SĐT, email) trong sample? |
| Known Limitations | Root files (README/AGENTS) có mục Known Limitations? |

**Verify:** Tạo bảng kết quả. Ghi tổng hợp cả 3 Lớp vào `BAO-CAO-KIEM-DINH-SPEC.md` tại `Kho-Du-Lieu/Ket-Qua/{du-an}/`.

**Decision branch:**
- Có lỗi Safety FAIL → **HALT**: "Gói Spec chưa an toàn để pilot. Bổ sung [X]."
- Toàn PASS → Proceed Step 6.

### Step 6: Conflict Detection & Backup (Pre-Deploy)

**Action:** So sánh danh mục component trong staging với hệ thống hiện hữu:

| Component | So sánh |
|---|---|
| Rule | Tên file staging vs `.agents/quan-ly-quy-tac/` |
| Workflow | Tên file staging vs `.agents/workflows/` + slash command trùng? |
| Skill | Tên folder staging vs `.agents/skills/` |

**Conflict resolution:**

| Tình huống | Hành động |
|---|---|
| Không trùng | → Deploy trực tiếp (Step 7). |
| Trùng tên, nội dung khác | → **HITL Gate 3**: Hiển thị diff tóm tắt. Operator chọn: (a) Ghi đè (backup trước), (b) Đổi tên mới, (c) Bỏ qua. |
| Trùng tên, nội dung giống | → Skip (đã có). Log "Đã tồn tại, bỏ qua." |

**Backup:** Mọi file bị ghi đè → copy bản cũ vào `_archive/{YYYYMMDD-HHmm}/` trước khi ghi (L2 `Pre-Overwrite Guard`).

### Step 7: Deploy Components vào Hệ thống (HITL Gate Chính)

**Action:** Trình bày cho Operator bảng tổng hợp:

```
📋 KẾ HOẠCH TRIỂN KHAI
├── Rules:     [N] file → .agents/quan-ly-quy-tac/
├── Skills:    [N] folder → .agents/skills/
├── Workflows: [N] file → .agents/workflows/00-core-business/ hoặc 01-system-ops/
├── Sources:   business_sources/ → Kho-Du-Lieu/Du-Lieu-Vao/{du-an}/tai-lieu-nguon/
├── Tài liệu:  HANDOFF_GUIDE, TEST_PROMPTS, ACCEPTANCE_CRITERIA → Du-An/{du-an}/
├── Conflicts: [N] file sẽ ghi đè (đã backup)
├── Skipped:   [N] file đã tồn tại
```

**HITL Gate 4 — Maker-Checker chính:** Operator chọn "Đồng ý" → Thực thi theo thứ tự:

1. **Rules trước** — Ràng buộc phải có trước khi skill chạy. Copy file vào `.agents/quan-ly-quy-tac/`.
2. **Skills tiếp** — Delegate `@01-tao-ky-nang-moi` (Route 1 CREATE) per skill. Nếu skill spec đã chuẩn format → fast-track (copy trực tiếp + verify cross-ref). Nếu cần enrich V9 metadata → bổ sung `owner`, `hitl_timeout`.
3. **Workflows sau** — Delegate `@01-tao-quy-trinh-moi` (Route 1 CREATE) per workflow. Verify wiring: workflow gọi đúng skill vừa deploy.
4. **Business sources** — Copy `business_sources/` vào `Kho-Du-Lieu/Du-Lieu-Vao/{du-an}/tai-lieu-nguon/` (read-only input).
5. **Tài liệu bàn giao** — Copy `HANDOFF_GUIDE.md`, `TEST_PROMPTS.md`, `ACCEPTANCE_CRITERIA.md`, `SOLUTION_BLUEPRINT.md` vào `Du-An/{du-an}/`.

**Verify:** Mỗi component deploy thành công → ghi `status: ok`. Nếu fail → Circuit Breaker (retry 2, fallback skip + log).

### Step 8: Post-Deploy — Index Sync & Registry Update

**Action:**
1. Trigger `01-dong-bo-muc-luc` → cập nhật toàn bộ index `Bang-Dieu-Khien/`.
2. Cập nhật `Bang-Dieu-Khien/DANH-SACH-KY-NANG.md` với skill mới.
3. Cập nhật `.agents/workflows/00_WORKFLOW_INDEX.md` với workflow mới.
4. Ghi entry `Quan-Tri/LICH-SU-THAY-DOI.md`: "Deploy Spec Pack [tên ZIP] — [N] quan-ly-quy-tac, [N] skills, [N] workflows."
5. Ghi log `Quan-Tri/AGENT-LOG.md`.

**Verify:** Index count sau sync khớp với component count đã deploy.

### Step 9: Báo cáo Kết quả & Hướng dẫn Chạy thử

**Action:** Tạo báo cáo tổng kết `BAO-CAO-TRIEN-KHAI-SPEC.md` tại `Kho-Du-Lieu/Ket-Qua/{du-an}/`:

1. Danh sách component đã deploy (tên, đường dẫn, trạng thái).
2. Slash Commands mới (liệt kê để test ngay).
3. Hướng dẫn chạy thử (trích từ `HANDOFF_GUIDE.md`).
4. Test Prompts đề xuất (trích từ `TEST_PROMPTS.md`).
5. Rủi ro & Giới hạn (trích từ `ACCEPTANCE_CRITERIA.md`).

Dọn dẹp: Xóa `.agents/tmp/staging-{timestamp}/`.

## Phụ lục (RAG Pointer)

> [!IMPORTANT]
> Chi tiết HITL Gates, Circuit Breaker Policy, Edge Cases & Recovery, Output Contract JSON, và Cross-Workflow Chaining đã được tách ra file riêng để tuân thủ Zero-Bloat Law (< 15KB).
> 👉 **Đọc đầy đủ tại:** `components/w-deploy-appendix.md`

## HITL Gates (Tóm tắt)

| Gate | Step | Trigger |
|---|---|---|
| Gate 1 — Grade B | Step 3A/3B | Thiếu file recommended |
| Gate 2 — Format Fix | Step 4 | Component có lỗi format |
| Gate 3 — Conflict | Step 6 | Trùng tên component |
| Gate 4 — Deploy | Step 7 | Maker-Checker chính |

## Validation

- [ ] File ZIP gốc tại `Du-Lieu-Vao/` không bị sửa đổi (L0 Read-Only)
- [ ] Staging đã xóa sau deploy thành công
- [ ] Toàn bộ component mới có entry trong index tương ứng
- [ ] `LICH-SU-THAY-DOI.md` có entry deploy
- [ ] `BAO-CAO-TRIEN-KHAI-SPEC.md` tại `Ket-Qua/{du-an}/`
- [ ] Output Contract JSON đầy đủ
- [ ] Backup tồn tại tại `_archive/` nếu có file bị ghi đè

## Resources

- Skill: `01-tao-ky-nang-moi` (Route 1 CREATE)
- Skill: `01-tao-quy-trinh-moi` (Route 1 CREATE)
- Skill: `01-quan-ly-quy-tac` (nếu cần validate rule format)
- Skill: `01-dong-bo-muc-luc` (post-deploy sync)
- Registry: `Bang-Dieu-Khien/DANH-SACH-KY-NANG.md`
- Registry: `.agents/workflows/00_WORKFLOW_INDEX.md`
- Log: `Quan-Tri/LICH-SU-THAY-DOI.md`
- Log: `Quan-Tri/AGENT-LOG.md`
- Phụ lục: `components/w-deploy-appendix.md`

