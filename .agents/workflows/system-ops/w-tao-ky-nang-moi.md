---
description: Build skill mới theo Progressive Disclosure pattern gồm 5 bước chuẩn hóa MAS V8.
semantic_triggers: ['tạo kỹ năng mới', 'tao ky nang moi', 'build skill']
---

- **👤 Owner:** `[@Cố vấn AI MindX]`
- **🛠 Skill Target:** `[TBD]`

# Quy Trình: /build-skill

## Mục đích

Orchestrate 5 bước build skill theo Progressive Disclosure pattern — từ capture intent đến verify cross-ref. Đảm bảo mọi skill mới trong `.agents/skills/` tuân r17 + Phần 3 KB Antigravity. Là tầng phòng vệ chống "build skill flat monolithic" — vấn đề phổ biến khi chưa codify quy trình.

## Dấu hiệu kích hoạt

Builder hoặc Brain gõ `/build-skill {ten-skill}` khi cần thêm skill mới vào workspace.

Tham số:
- `{ten-skill}` — bắt buộc, kebab-case lowercase (vd `data-cleaning`, `report-generator`)
- `{purpose}` — optional, 1 câu mô tả nếu đã rõ; nếu không có → workflow capture intent

## Điều kiện tiên quyết

- [ ] Workspace baseline đã init (có `.agents/skills/` folder + 7 skill hiện tại)
- [ ] Tên skill đề xuất chưa trùng skill nào trong `DANH-SACH-KY-NANG.md`
- [ ] Tên không match L1 baseline skill ID (tro-ly-dieu-phoi, dong-bo-muc-luc, quan-ly-kho-tri-thuc) — vi phạm `kb-composition-quan-ly-quy-tac` Phần 3 Case 1
- [ ] Có ý tưởng rõ về use case skill giải quyết — tránh build skill mơ hồ

## Các bước thực hiện

### Bước 1 — Capture intent (5-10 phút)

Reference methodology từ `skill-creator` của Anthropic (Capture Intent phase). 4 câu hỏi cốt lõi:

1. **Skill này enable Agent làm gì?** (output cụ thể, không generic)
2. **Trigger khi nào?** — phrases / contexts cụ thể operator hay gõ
3. **Output format mong đợi?** — file md/xlsx/docx? prompt response? log entry?
4. **Có pattern wisdom nào trong KB project tham khảo được không?** — Reference `kb-antigravity-workspace-standard` Phần 12 (7 W3 patterns: data-cleaning, report-generator, kpi-calculator, brand-identity, sync-index, weekly-report, audit)

Nếu builder không trả lời được 1 câu nào trong 4 → STOP, đề xuất "Skill chưa đủ context — quay lại sau khi rõ use case."

### Bước 2 — Design spec (10-15 phút)

Output Bước 2 là **spec sheet** (chưa phải code/file), gồm 4 phần:

#### 2a. Frontmatter draft

```yaml
---
name: "w-{ten-skill}"
description: {WHAT, ngôi 3} . Use when {WHEN context 1}, {WHEN context 2}, hoặc {WHEN context 3}. ≤100 token.
---
```

Validate: ngôi 3, có WHAT + WHEN, ≤100 token. Nếu pushy mode (per skill-creator hint) — thêm "Make sure to use this skill whenever {keyword 1}, {keyword 2}, even if {keyword negative}".

#### 2b. Body outline (6 section bắt buộc)

```
1. # Title + 1-2 câu intro
2. ## When to use this skill (bullet list use cases + KHÔNG dùng khi)
3. ## How to use it (Step 1-N)
4. ## Decision tree (logic chính)
5. ## Examples (reference path)
6. ## Edge cases & escalation
```

Sketch 1-2 câu mỗi section.

#### 2c. Resources list

Identify nội dung structured ≥30 dòng cần tách (theo r17 threshold):

| Nội dung | Loại | File đề xuất |
|----------|------|--------------|
| {Schema entry / data structure} | schema | `resources/{name}-schemas.md` |
| {Detection pattern / heuristic} | patterns | `resources/{name}-patterns.md` |
| {Template paste-ready} | template | `resources/{name}-template.md` |
| {Decision rubric / criteria} | criteria | `resources/{name}-criteria.md` |
| {Edge case catalog ≥10} | edge cases | `resources/edge-cases.md` |

Nếu skill đơn giản (không có chunk ≥30 dòng) → resources/ rỗng OK, đánh dấu trong spec sheet.

#### 2d. Examples list

Tối thiểu 1 file `examples/example-{name}-flow.md` mô tả luồng end-to-end.

**Gate Bước 2:** Builder hoặc operator review spec sheet. Nếu OK → sang Bước 3. Nếu cần điều chỉnh scope → quay lại Bước 1.

### Bước 3 — Build resources/ FIRST (15-30 phút)

**Quan trọng:** Build resources/ **trước**, không build SKILL.md trước. Lý do: resources là structured data, dễ define rõ; sau đó SKILL.md body chỉ cần reference path → tránh tendency embed inline.

Cho mỗi resources file đã list ở Bước 2c:

1. Tạo `resources/{name}.md` với header + intro 1 đoạn giới thiệu mục đích
2. Fill nội dung cốt lõi (schema/pattern/template/criteria)
3. Thêm validation quan-ly-quy-tac + edge cases nội bộ (mở rộng cho resources tự đứng được)
4. Phiên bản dưới đáy: "v1.0 (YYYY-MM-DD) — Initial từ Build {ten-skill}"

Build song song nhiều resources files — không sequential. Mỗi file độc lập về nội dung.

**Gate Bước 3:** Mỗi resources file pass tiêu chí:
- [ ] Header rõ + intro mô tả mục đích
- [ ] Nội dung cốt lõi đầy đủ (không placeholder)
- [ ] Có validation quan-ly-quy-tac / edge cases
- [ ] Phiên bản ghi rõ

### Bước 4 — Build SKILL.md body referencing resources (10-15 phút)

**Quan trọng:** Body chỉ chứa **logic + reference path**, không inline structured content.

Áp template SKILL.md theo `kb-antigravity-workspace-standard` Phần 3.6:

```markdown
---
{frontmatter từ Bước 2a}
---

# {Title}

{Intro 1-2 câu}

## When to use this skill
{Bullet list}

**KHÔNG dùng khi:**
{Bullet list}

## How to use it

### Step 1 — {Action}
{Logic + reference resources nếu có}

### Step 2 — {Action}
{Logic + reference resources nếu có}

(... các step khác)

### Step N — Validation
{Checklist}

## Decision tree
{Logic chính}

## Examples
Xem `examples/{file}.md` cho luồng end-to-end.

## Xử lý ngoại lệ
{3-5 case ngắn + escalate khi nào}

## Resources
- `resources/{file-1}.md` — {1 dòng mô tả}
- `resources/{file-2}.md` — {1 dòng mô tả}
- `examples/{file}.md` — {1 dòng mô tả}

## Scripts
{Nếu có scripts/ — không thì ghi "không có scripts"}

---

## Quy tắc liên quan
{Bullet list quan-ly-quy-tac có liên quan}

## Tham chiếu KB nguồn
{Bullet list KB project có liên quan}
```

**Khi viết Step 1-N body:** Check sau mỗi Step — nội dung đang viết ra ≥30 dòng không? Nếu có → STOP, tách ngược ra resources, body chỉ giữ "Áp {logic} theo `resources/{file}.md`".

**Gate Bước 4:** Body ≤500 dòng. Không inline structured content ≥30 dòng. Reference resources qua path tương đối.

### Bước 5 — Build examples + Verify cross-ref (10 phút)

#### 5a. Build examples

Tạo `examples/example-{name}-flow.md` với luồng end-to-end:
- Bối cảnh giả định
- Trigger chain (workflow nào gọi skill, hoặc operator gõ gì)
- Output từng step
- Edge case demo (tùy chọn)
- Validate gates demo (tùy chọn)

#### 5b. Verify cross-ref

Run automated checks:

| Check | Validation |
|-------|-----------|
| Body reference resources path tồn tại | Mỗi `resources/{x}.md` mention trong body → file thực sự tồn tại |
| Body reference examples path tồn tại | `examples/{x}.md` mention trong body → file thực sự tồn tại |
| Frontmatter description match body | Mention skill làm gì + khi nào → match Bước 2a draft |
| r17 compliance | Body ≤500 dòng + có 6 section bắt buộc + resources tách nếu cần |
| Skill ID không trùng | Tên không match L1 baseline + skill hiện có |

#### 5c. Register vào index

- Update `Bang-Dieu-Khien/DANH-SACH-KY-NANG.md` — thêm row mới với name + path + lớp + mô tả + trạng thái
- Update `Quan-Tri/LICH-SU-THAY-DOI.md` — append entry "Build skill {name}"
- Trigger `dong-bo-muc-luc` để đồng bộ

**Gate Bước 5:** Toàn bộ check pass. Skill register thành công vào DANH-SACH-KY-NANG → tro-ly-dieu-phoi có thể trigger.

## Tiêu chuẩn nghiệm thu

End-to-end checklist khi build hoàn thành:

- [ ] Frontmatter `description` ngôi 3, có WHAT + WHEN, ≤100 token
- [ ] Body SKILL.md ≤500 dòng (chạy `wc -l SKILL.md` xác nhận)
- [ ] Body có 6 section bắt buộc
- [ ] Resources tách nếu có chunk ≥30 dòng (per r17 threshold)
- [ ] Có ≥1 file `examples/`
- [ ] Body reference resources/examples qua path, không inline
- [ ] Tên skill kebab-case lowercase
- [ ] Không trùng skill ID có sẵn
- [ ] DANH-SACH-KY-NANG cập nhật
- [ ] LICH-SU-THAY-DOI có entry

Fail bất kỳ → STOP, không register skill, báo builder fix.

## Kết quả đầu ra

- Folder `.agents/skills/{ten-skill}/` với:
  - `SKILL.md` (≤500 dòng)
  - `resources/*.md` (tách theo threshold)
  - `examples/example-{name}-flow.md`
- DANH-SACH-KY-NANG.md cập nhật
- LICH-SU-THAY-DOI.md append entry
- Tóm tắt cho builder:
  ```
  Skill {name} build xong.
  - Body: {N} dòng
  - Resources: {M} files
  - Examples: 1 file
  - r17 compliance: PASS
  - Đã register vào DANH-SACH-KY-NANG
  ```

## Xử lý ngoại lệ

- **Builder build skill cực đơn giản (1 nhiệm vụ, body <200 dòng):** OK skip resources/ rỗng. Vẫn yêu cầu examples/. Workflow KHÔNG ép tách resources nếu không có chunk ≥30 dòng — r17 threshold conditional.
- **Skill có scripts/ thay resources/:** OK. Bước 3 tạo `scripts/{name}.py` thay vì `resources/`. Body reference qua `scripts/{name}.py --help`.
- **Build skill phải copy từ skill-creator của Anthropic:** Workflow vẫn chạy 5 bước nhưng Bước 1+2 fast-track (đã có spec từ skill-creator). Bước 3+4+5 vẫn enforce strict.
- **Build skill mới override skill có sẵn:** STOP — vi phạm `kb-composition-quan-ly-quy-tac` Case 1. Builder phải rename hoặc dùng pattern extends (chưa support v0.3).
- **Builder muốn skip Bước 5b verify:** KHÔNG skip. Skip = skill có thể có cross-ref dead, agent fail runtime. Verify cost <2 phút.
- **Build skill batch 3-5 skills cùng lúc:** Chạy workflow tuần tự cho từng skill — không parallel. Lý do: cross-ref check phải đảm bảo skill A không reference skill B chưa register.

## Quy tắc liên quan

- Quy tắc 09 (`r09-changelog-required.md`): Mỗi build skill → ghi changelog
- Quy tắc 11 (`r11-quality-gate.md`): Bước 5 quality gate enforced
- Quy tắc 17 (`r17-skill-build-spec.md`): Workflow này thực thi r17

## Tham chiếu KB nguồn

- `kb-antigravity-workspace-standard.md` Phần 1.4 (Progressive Disclosure 3-tier)
- `kb-antigravity-workspace-standard.md` Phần 3 (skill spec đầy đủ)
- `kb-antigravity-workspace-standard.md` Phần 12 (7 W3 wisdom patterns — reference khi build)
- `kb-composition-quan-ly-quy-tac.md` Phần 3 (conflict policy — Case 1 ID trùng L1)
- `/mnt/skills/examples/skill-creator` (Anthropic methodology reference — không load trực tiếp)
