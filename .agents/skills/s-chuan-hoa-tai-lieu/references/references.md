# Nghị định 30/2020/NĐ-CP — Complete Specification

This file contains the full technical specification for Vietnamese government administrative documents per Nghị định 30/2020/NĐ-CP. Read this only when generating a `vn-gov` preset document.

## Table of Contents

1. Page Setup (Điều 9)
2. Quốc hiệu and Tiêu ngữ (Điều 8)
3. Tên cơ quan ban hành
4. Số ký hiệu of the document
5. Địa danh and date
6. Tên loại văn bản and Trích yếu
7. Body content and numbering hierarchy
8. Kính gửi (for tờ trình / báo cáo / công văn)
9. Người ký (chức vụ + họ tên)
10. Nơi nhận
11. Phụ lục (appendices)
12. Special markers (mật, khẩn, lưu hành nội bộ)

---

## 1. Page Setup (Điều 9)

| Property | Value |
|----------|-------|
| Paper size | A4 (210 × 297 mm) |
| Orientation | Portrait (default), Landscape for large tables only |
| Top margin | 20–25 mm (2.0–2.5 cm) |
| Bottom margin | 20–25 mm |
| **Left margin** | **30–35 mm** (wide for binding) |
| Right margin | 15–20 mm |

**Body font and spacing**:
- Font: **Times New Roman**, size **13–14 pt**
- Line spacing: minimum single (1.0), maximum 1.5 lines
- Paragraph spacing (before/after): minimum 6 pt
- First line indent: **1 cm or 1.27 cm** (NOT a Western multi-tab indent)
- Body alignment: justified (canh đều hai lề)

---

## 2. Quốc hiệu and Tiêu ngữ (Điều 8)

### Quốc hiệu: "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM"

- **Position**: top of page 1, **RIGHT side** (NOT centered — this is the #1 mistake)
- Style: UPPERCASE, upright, size 12–13 pt, **bold**
- Single line

### Tiêu ngữ: "Độc lập - Tự do - Hạnh phúc"

- Position: centered directly below Quốc hiệu
- Style: title case, upright, size 13–14 pt, **bold**
- Hyphens between clauses, with spaces around hyphens
- **A horizontal line is drawn below the Tiêu ngữ**, full width of the text, single solid line
- Implementation: use paragraph `border: { bottom: { style: SINGLE, size: 6, color: "000000" } }`, NOT a 1-row table

Spacing between Quốc hiệu and Tiêu ngữ: single line.

---

## 3. Tên cơ quan ban hành

This sits in the LEFT column of the two-column header (paralleling Quốc hiệu in the right column).

Components (top to bottom):
- **Cơ quan chủ quản** (if any): e.g., "BỘ GIÁO DỤC VÀ ĐÀO TẠO"
- **Cơ quan ban hành**: e.g., "TRƯỜNG ĐẠI HỌC ABC"

Style:
- UPPERCASE, upright, size 12–13 pt, **bold**
- Cơ quan chủ quản (parent) is on the line above; cơ quan ban hành (issuer) on the line below
- Separated by single line spacing
- **A horizontal line below cơ quan ban hành**, length 1/3 to 1/2 of the text width, centered relative to the text
- Implementation: paragraph border bottom (NOT table). To make a short border, apply it to a centered paragraph with a constrained width, or use a custom border on the paragraph itself.

If `co-quan-chu-quan` is provided in front-matter, render both lines. If not, render only `co-quan-ban-hanh`.

---

## 4. Số ký hiệu

Position: centered below tên cơ quan ban hành.

Format: `Số: NN/XX-YYY`
- `NN` = sequence number, integer (Arabic digits). **Numbers < 10 must have a leading zero**: `Số: 05/CV-ABC`, never `Số: 5/CV-ABC`.
- `XX` = document type abbreviation (UPPERCASE): `QĐ` (Quyết định), `BC` (Báo cáo), `TTr` (Tờ trình), `CV` (Công văn — note: special case below), `KH` (Kế hoạch), `TB` (Thông báo), `NQ` (Nghị quyết), `CT` (Chỉ thị), `QC` (Quy chế), `QyĐ` (Quy định), `BB` (Biên bản)
- `YYY` = abbreviation of cơ quan ban hành (UPPERCASE)

**Special case for Công văn**: the abbreviation `XX` is replaced by the abbreviation of the cơ quan or the relevant unit/department. Example: `Số: 45/CV-ĐHABC` or `Số: 45/ĐHABC-ĐT` (where ĐT = Đào tạo unit).

Style:
- "Số" → lowercase, upright, size 13 pt
- The rest (abbreviation) → UPPERCASE, upright, size 13 pt
- Colon `:` after "Số", forward slash `/` between number and abbreviation, hyphen `-` between abbreviation segments (no spaces)

For Công văn only, append below: `V/v <trích yếu>` — see section 6.

---

## 5. Địa danh and Date

Position: on the SAME line as số ký hiệu, but on the RIGHT side (below Tiêu ngữ).

Format: `Hà Nội, ngày 15 tháng 5 năm 2026`
- **Day < 10**: leading zero — `ngày 05`
- **Month 1 or 2**: leading zero — `tháng 02`
- Year: 4 digits, no leading zero

Style:
- Lowercase, upright, **italic**, size 13–14 pt
- Capitalize first letter of địa danh
- Comma after địa danh

---

## 6. Tên loại văn bản and Trích yếu

Position: centered, below the two-column header (after spacing).

### For document types other than Công văn:

**Tên loại văn bản**: UPPERCASE, upright, **bold**, size 13–14 pt
- E.g., `BÁO CÁO`, `QUYẾT ĐỊNH`, `TỜ TRÌNH`, `KẾ HOẠCH`, `THÔNG BÁO`, `BIÊN BẢN`

**Trích yếu** (below tên loại): title case, upright, **bold**, size 13–14 pt
- E.g., `Về việc ban hành Quy chế Đào tạo Sau đại học`
- Or use form: `Tổng kết công tác năm học 2025-2026`

**A horizontal line below trích yếu**, length 1/3 to 1/2 of trích yếu text, centered.

### For Công văn:

No standalone "tên loại" line. Instead, immediately below số ký hiệu, on its own line:

`V/v <trích yếu công văn>`

Style: lowercase, upright, size 12–13 pt. Spacing 6 pt from số ký hiệu line above.

---

## 7. Body content and numbering hierarchy

Body style:
- Times New Roman, 13–14 pt, upright
- Justified (canh đều hai lề)
- First line indent: 1 cm or 1.27 cm
- Line spacing: 1.0 to 1.5

### Numbering hierarchy (for văn bản with structured content like Quyết định, Nghị quyết, Quy chế)

From largest to smallest:

| Level | Format | Style |
|-------|--------|-------|
| Phần | `Phần I`, `Phần II` ... | Lowercase + Roman numeral, centered, **bold**, 13–14 pt |
| Chương | `Chương I`, `Chương II` ... | Lowercase + Roman numeral, centered, **bold**, 13–14 pt |
| (Phần/Chương title) | E.g., `QUY ĐỊNH CHUNG` | UPPERCASE, centered, **bold**, 13–14 pt, on line below |
| Mục | `Mục 1`, `Mục 2` ... | Lowercase + Arabic numeral, centered, **bold**, 13–14 pt |
| Tiểu mục | `Tiểu mục 1`, `Tiểu mục 2` ... | Lowercase + Arabic numeral, centered, **bold**, 13–14 pt |
| (Mục/Tiểu mục title) | E.g., `ĐIỀU KIỆN VÀ TIÊU CHUẨN` | UPPERCASE, centered, **bold** |
| Điều | `Điều 1.`, `Điều 2.` ... | Lowercase + Arabic numeral + period, indented 1 cm or 1.27 cm, **bold**, same size as body |
| Khoản | `1.`, `2.`, `3.` ... | Arabic numeral + period, same size as body, upright. If khoản has a title, the title is **bold** on its own line. |
| Điểm | `a)`, `b)`, `c)` ... | Vietnamese alphabet + closing parenthesis, same size as body, upright |

The Vietnamese alphabet sequence for điểm: `a, ă, â, b, c, d, đ, e, ê, g, h, i, k, l, m, n, o, ô, ơ, p, q, r, s, t, u, ư, v, x, y` (no `f, j, w, z`).

### Căn cứ (legal basis) section

For Quyết định, Nghị quyết, the body starts with căn cứ statements, before the QUYẾT ĐỊNH: section:

```
Căn cứ Luật Giáo dục Đại học ngày 18 tháng 6 năm 2012;
Căn cứ Nghị định số 99/2019/NĐ-CP ngày 30 tháng 12 năm 2019 ...;
Theo đề nghị của Trưởng phòng Đào tạo,
```

Style: italic, size 13–14 pt, ending each line with `;`, final line ends with `,` or `.`.

After căn cứ, the body has:

```
QUYẾT ĐỊNH:

Điều 1. ...
Điều 2. ...
```

`QUYẾT ĐỊNH:` is uppercase, centered, bold.

---

## 8. Kính gửi (for Tờ trình / Báo cáo / Công văn)

Position: immediately below the centered tên loại + trích yếu block (or below số ký hiệu for công văn).

Format:
```
Kính gửi:
- <Cơ quan/cá nhân 1>;
- <Cơ quan/cá nhân 2>;
- <Cơ quan/cá nhân 3>.
```

Style:
- `Kính gửi:` is bold, size 13–14 pt
- Each recipient on its own line, prefixed with `-`, ending with `;` (and final one with `.`)
- Names of cơ quan in UPPERCASE if formal entity; title case for individuals

---

## 9. Người ký

Position: bottom RIGHT of the page (or last page if multi-page), below the body content.

Structure (top to bottom):

```
<Authority prefix (optional)>
<CHỨC VỤ>          ← uppercase, bold
(signature)
(seal/stamp)
<Họ và tên>        ← title case, bold
```

### Authority prefixes (tiền tố quyền hạn)

When the signer is not the head of the issuing body, prepend one of these:

| Prefix | Meaning | When to use |
|--------|---------|-------------|
| `TM.` | Thay mặt | Signing on behalf of a collective leadership |
| `Q.` | Quyền | Acting head (e.g., interim director) |
| `KT.` | Ký thay | Signing in place of (e.g., deputy signs for director) |
| `TL.` | Thừa lệnh | Signing by delegation of authority |
| `TUQ.` | Thừa uỷ quyền | Signing by written authorization |

**Format**: UPPERCASE + period. Always with the period. `TM.`, not `TM` or `tm.`.

Example:
```
KT. HIỆU TRƯỞNG
PHÓ HIỆU TRƯỞNG
(signature)
Trần Văn B
```

Or with no prefix:
```
HIỆU TRƯỞNG
(signature)
Nguyễn Văn A
```

### What NOT to include

Per Nghị định 30, **do NOT include** academic titles (PGS., TS., ThS., GS., GVCC., GVC.) before họ tên in administrative documents — only in academic/educational contexts where explicitly permitted by the head of the cơ quan.

---

## 10. Nơi nhận

Position: bottom LEFT of the page (opposite Người ký), parallel layout.

Structure:

```
Nơi nhận:        ← italic, size 13 pt
- <Recipient 1>;
- <Recipient 2>;
- Lưu: VT, <abbreviation>.
```

Style:
- `Nơi nhận:` is **italic** (not bold), size 13 pt
- Each line prefixed with `-`
- Lines ending with `;` except the last line, which ends with `.`
- **Last line is always** `Lưu: VT, <abbr>.` where VT = Văn thư (the records office) and `<abbr>` is the abbreviation of the drafting unit

For Tờ trình / Báo cáo / Công văn, the first nơi nhận entry is typically `- Như trên;` (referring back to the Kính gửi list above), avoiding redundancy.

Example for Công văn:
```
Nơi nhận:
- Như trên;
- Lưu: VT, ĐT.
```

Example for Quyết định:
```
Nơi nhận:
- Như Điều 5;
- Các đơn vị liên quan;
- Lưu: VT, TCCB.
```

---

## 11. Phụ lục (Appendices)

When the document has appendices:

- In the body, reference them: `... (chi tiết tại Phụ lục I kèm theo)`
- Each phụ lục starts on a new page
- Phụ lục label: `Phụ lục I`, `Phụ lục II` ... (Roman numerals if more than one; single phụ lục just uses `Phụ lục`)
- Style: lowercase, centered, **bold**, size 14 pt
- Phụ lục title (e.g., `DANH MỤC HỌC PHẦN`): UPPERCASE, centered, **bold**, size 13–14 pt
- Below phụ lục title, in italic 13–14 pt: `(Kèm theo Quyết định số .../.../... ngày ... tháng ... năm ... của ...)`
- Phụ lục pages are numbered separately

---

## 12. Special markers

### Mật (security classification)

If applicable, stamped on the document:
- `TUYỆT MẬT` (top secret), `TỐI MẬT` (secret), `MẬT` (confidential)
- Position: top right, below Quốc hiệu, in a single-line bordered box

### Khẩn (urgency)

If applicable:
- `HOẢ TỐC` (most urgent), `THƯỢNG KHẨN` (very urgent), `KHẨN` (urgent)
- Position: top right area, below Quốc hiệu
- In a bordered box: 30×8mm for HOẢ TỐC, 40×8mm for THƯỢNG KHẨN, 20×8mm for KHẨN
- Style: UPPERCASE, Times New Roman, 13–14 pt, upright, **bold**

### Lưu hành nội bộ / Xem xong trả lại

For documents with restricted circulation:
- Stamped at top, e.g., `LƯU HÀNH NỘI BỘ`, `XEM XONG TRẢ LẠI`
- In a bordered box, UPPERCASE, Times New Roman, 13–14 pt, **bold**

---

## Required Front-Matter Fields for vn-gov Preset

These fields MUST be in the YAML front-matter when generating a vn-gov document. If any are missing, stop and list what's missing:

| Field | Required? | Example |
|-------|-----------|---------|
| `preset` | Yes | `vn-gov` |
| `co-quan-chu-quan` | Optional | `"BỘ GIÁO DỤC VÀ ĐÀO TẠO"` |
| `co-quan-ban-hanh` | **Yes** | `"TRƯỜNG ĐẠI HỌC ABC"` |
| `so-ky-hieu` | **Yes** | `"45/CV-ĐHABC"` |
| `loai-van-ban` | **Yes** | `"CÔNG VĂN"` (or QUYẾT ĐỊNH, BÁO CÁO ...) |
| `trich-yeu` | **Yes** | `"Về việc báo cáo công tác Quý II"` |
| `dia-danh` | **Yes** | `"Hà Nội"` |
| `ngay-thang-nam` | **Yes** | `"2026-05-17"` (ISO format) |
| `kinh-gui` | Conditional | List, required only for Tờ trình/Báo cáo/Công văn |
| `noi-nhan` | **Yes** | List, always include `"Lưu: VT, <abbr>"` as last item |
| `nguoi-ky.chuc-vu` | **Yes** | `"HIỆU TRƯỞNG"` |
| `nguoi-ky.tien-to-quyen-han` | Optional | `"KT."`, `"TM."`, `"TUQ."`, `"Q."`, `"TL."`, or empty |
| `nguoi-ky.ho-ten` | **Yes** | `"Nguyễn Văn A"` |
