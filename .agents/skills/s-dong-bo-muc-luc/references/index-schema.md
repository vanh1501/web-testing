# Index Schema — Tham Chiếu Format 12 Tệp Index

**Phiên bản:** 1.0 (01/05/2026)
**Vai trò:** Schema chuẩn cho 12 tệp index workspace. `dong-bo-muc-luc` đọc tệp này để biết format đúng khi tạo entry mới hoặc rebuild index từ đầu.
**Nguồn:** Trích từ `kb-index-format.md` Phần 2.

---

## TL;DR

12 tệp index phân 4 cấp: 1 master dashboard, 6 danh sách domain, 3 tệp project, 2 tệp giam-sat-tuan-thu. Mỗi tệp có schema cụ thể — column bắt buộc, kiểu dữ liệu, giá trị hợp lệ. Sync sai schema = vi phạm chuẩn workspace, audit fail.

---

## Cấp 1 — Master Dashboard (1 tệp)

### `Bang-Dieu-Khien/BANG-DIEU-KHIEN.md`

```markdown
# Bảng Điều Khiển — {Tên Workspace}

Cập nhật lần cuối: {YYYY-MM-DD HH:MM}

## Tổng quan

- Dự án đang chạy: {số} → xem DANH-SACH-DU-AN.md
- Báo cáo gần nhất: {tên} ({ngày}) → xem DANH-SACH-BAO-CAO.md
- Kỹ năng đang hoạt động: {số} → xem DANH-SACH-KY-NANG.md
- Sức khỏe workspace: {Tốt / Cần kiểm tra / Có vấn đề}

## Hoạt động gần đây

| Ngày | Hoạt động | Dự án | Trạng thái |
|------|-----------|-------|------------|
| {ngày} | {mô tả ngắn ≤80 ký tự} | {tên dự án} | {trạng thái} |
```

**Field bắt buộc:** Cập nhật lần cuối, 4 dòng tổng quan, ≥1 hàng hoạt động gần đây (giữ tối đa 10 hàng gần nhất).

**Trigger sync:** Mỗi lần 6 danh sách domain thay đổi.

---

## Cấp 2 — Domain Lists (6 tệp)

### `DANH-SACH-DU-AN.md`

| Cột | Kiểu | Bắt buộc | Giá trị hợp lệ |
|-----|------|---------|----------------|
| Tên dự án | Text | Có | Tự do |
| Đường dẫn | Path | Có | `Du-An/{slug}/` |
| Trạng thái | Enum | Có | `Đang làm` / `Tạm dừng` / `Đã xong` |
| Ngày tạo | Date | Có | `YYYY-MM-DD` |
| Cập nhật | Date | Có | `YYYY-MM-DD` |

### `DANH-SACH-BAO-CAO.md`

| Cột | Kiểu | Bắt buộc | Giá trị hợp lệ |
|-----|------|---------|----------------|
| Tên báo cáo | Text | Có | Tự do |
| Dự án | FK | Có | Khớp `DANH-SACH-DU-AN` |
| Đường dẫn | Path | Có | `Kho-Du-Lieu/Ket-Qua/{...}/{file}` |
| Ngày tạo | Date | Có | `YYYY-MM-DD` |
| Loại | Enum | Có | `phân tích` / `tổng hợp` / `slide` / `khác` |

### `DANH-SACH-DU-LIEU.md`

| Cột | Kiểu | Bắt buộc | Giá trị hợp lệ |
|-----|------|---------|----------------|
| Tên dataset | Text | Có | Tự do |
| Dự án | FK | Có | Khớp `DANH-SACH-DU-AN` |
| Đường dẫn | Path | Có | `Kho-Du-Lieu/Du-Lieu-Vao/{...}/{file}` |
| Ngày nhập | Date | Có | `YYYY-MM-DD` |
| Định dạng | Enum | Có | `csv` / `xlsx` / `json` / `pdf` / `khác` |

### `DANH-SACH-KY-NANG.md`

| Cột | Kiểu | Bắt buộc | Giá trị hợp lệ |
|-----|------|---------|----------------|
| Tên | Text | Có | Khớp folder name `.agents/skills/{tên}/` |
| Đường dẫn | Path | Có | `.agents/skills/{tên}/SKILL.md` |
| Lớp | Enum | Có | `Nghiệp vụ` / `Meta` |
| Mô tả ngắn | Text | Có | 1 dòng từ description frontmatter |
| Trạng thái | Enum | Có | `Hoạt động` / `Tắt` |

### `DANH-SACH-QUY-TAC.md`

| Cột | Kiểu | Bắt buộc | Giá trị hợp lệ |
|-----|------|---------|----------------|
| Tên | Text | Có | Khớp filename `r{NN}-*.md` |
| Đường dẫn | Path | Có | `.agents/quan-ly-quy-tac/{tên}.md` |
| Chế độ kích hoạt | Enum | Có | `Always On` / `Glob` / `Model Decision` / `Manual` |
| Mô tả ngắn | Text | Có | 1 dòng |
| Trạng thái | Enum | Có | `Hoạt động` / `Tắt` |

### `DANH-SACH-QUY-TRINH.md`

| Cột | Kiểu | Bắt buộc | Giá trị hợp lệ |
|-----|------|---------|----------------|
| Tên | Text | Có | Khớp filename `{tên}.md` |
| Đường dẫn | Path | Có | `.agents/workflows/{tên}.md` |
| Slash command | Text | Có | `/{tên}` (kebab-case) |
| Mô tả ngắn | Text | Có | 1 dòng |
| Trạng thái | Enum | Có | `Hoạt động` / `Tắt` |

---

## Cấp 3 — Project Files (3 tệp / dự án)

### `Du-An/{slug}/MO-DAU.md`

```markdown
# {Tên Dự Án}

## Mục tiêu
{1-2 câu kết quả cần đạt}

## Phạm vi
- Trong phạm vi: {danh sách}
- Ngoài phạm vi: {danh sách}

## Người chịu trách nhiệm
{Tên operator / vai trò}

## Ngày bắt đầu
{YYYY-MM-DD}

## Ghi chú
{Bối cảnh bổ sung nếu có}
```

**Trigger sync:** Tạo 1 lần khi `/w-khoi-tao-du-an-moi`. Sửa thủ công bởi operator.

### `Du-An/{slug}/TIEN-DO.md`

| Cột | Kiểu | Bắt buộc | Giá trị hợp lệ |
|-----|------|---------|----------------|
| Task | Text | Có | Tự do |
| Trạng thái | Enum | Có | `Đang làm` / `Chờ` / `Đã xong` |
| Ngày giao | Date | Có | `YYYY-MM-DD` |
| Ngày xong | Date | Tùy | `YYYY-MM-DD` (chỉ khi trạng thái = `Đã xong`) |
| Ghi chú | Text | Tùy | Tự do |

### `Du-An/{slug}/LICH-SU.md`

```markdown
# Lịch Sử — {Tên Dự Án}

| Ngày | Sự kiện | Chi tiết |
|------|---------|---------|
| {YYYY-MM-DD} | {sự kiện} | {chi tiết ≤120 ký tự} |
```

**Tính chất:** Append-only. Không xóa entry cũ.

---

## Cấp 4 — Governance (2 tệp)

### `Quan-Tri/LICH-SU-THAY-DOI.md`

| Cột | Kiểu | Bắt buộc | Giá trị hợp lệ |
|-----|------|---------|----------------|
| Ngày | Date | Có | `YYYY-MM-DD` |
| Thay đổi | Text | Có | Mô tả ngắn |
| Hệ thống | Enum | Có | 1 trong 6 hệ thống hoặc `Tất cả` |
| Lý do | Text | Có | Giải thích driver |
| Người thực hiện | Enum | Có | `Operator` / `Agent` / `Builder` |

**Tính chất:** Append-only.

### `Quan-Tri/CHINH-SACH.md`

Không phải index — là tệp policy cố định. Index-syncer KHÔNG sync tệp này (operator hoặc builder edit thủ công).

---

## Quy tắc validation

Khi sync, mỗi entry phải pass 4 check:

1. **Path tồn tại trên disk** — nếu không → diff "thừa"
2. **Enum value hợp lệ** — sai enum → mark "sai metadata", auto-fix
3. **Date format đúng** — `YYYY-MM-DD` strict, sai format → fix về today nếu unrecoverable
4. **Foreign key resolve** — `Dự án` trong `DANH-SACH-BAO-CAO` phải khớp 1 entry trong `DANH-SACH-DU-AN`. Không khớp → flag warning, hỏi operator.

---

## Anti-pattern bị từ chối

- Index chứa nội dung đầy đủ báo cáo (vi phạm "single source of truth")
- Trạng thái dùng giá trị tự do ("Xong rồi", "OK") thay vì enum chuẩn
- Thiếu field "Cập nhật lần cuối" ở master + 6 domain
- Entry path dùng absolute path thay vì relative từ workspace root

---

## Reference KB

- `kb-index-format.md` (toàn bộ — nguồn gốc schema)
- `kb-workspace-templates.md` (template tệp project)
- `kb-workspace-architecture.md` Phần 2 (6 hệ thống)
