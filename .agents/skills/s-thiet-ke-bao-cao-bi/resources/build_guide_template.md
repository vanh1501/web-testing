# Build Guide Template — Stage 2 Deliverable

**Mục đích**: Template để generate `BUILD_GUIDE.md` cho user trong Step 6 Kỳ 3 (Stage 2 ship). Document hand-off cho user vận hành file lâu dài.

**Cách dùng**: Sau Kỳ 2 coaching thành công, customize template dưới với thông tin cụ thể của file user, ship cùng file `.xlsx` finalized.

**Target length**: 1500-2500 words, đủ chi tiết để user maintain + extend file mà không cần skill support.

---

## TEMPLATE STRUCTURE

Generate file `BUILD_GUIDE.md` với 8 sections dưới. Customize phần `[BRACKETS]` theo context cụ thể.

---

```markdown
# BUILD GUIDE — [Tên file dashboard]

**Version**: 1.0 | **Created**: [date] | **For**: [user role/name]

## TỔNG QUAN

Đây là hướng dẫn vận hành và duy trì file `[tên_file].xlsx` — hệ thống báo cáo BI 
cho [domain/role] với cadence [Daily/Weekly/Monthly].

**Mục tiêu của file**:
- [Decision 1 mà file phục vụ]
- [Decision 2]
- [Decision 3]

**Time burden**: Trước ~[X] giờ/kỳ → Sau ~[Y] phút/kỳ (~[Z]% giảm)

---

## 1. KIẾN TRÚC FILE (Architecture Rationale)

### Cấu trúc 3-layer

```
File: [tên_file].xlsx
├── 00_README          (🔵 Hướng dẫn)
├── 01_input_data      (🔴 KHÔNG SỬA — chỉ paste data vào)
├── 02_input_contract  (🟠 Sửa cẩn thận — map raw schema)
├── 03_model           (🟡 Admin only — chứa formulas)
├── 04_dashboard       (🔵 View only — KPI cards + chart + slicer)
├── 05_drill_[kpi1]    (🔵 PivotTable detail)
├── 05_drill_[kpi2]    (🔵 PivotTable detail)
├── 06_settings        (⚪ Targets, named ranges)
└── 99_archive         (⚪ Snapshot kỳ cũ — không dùng workflow)
```

### Tại sao 3-layer?

Phân tách Raw / Model / Display giải quyết 3 vấn đề lớn của file cũ:

1. **Refresh fragility**: Trước đây data và formula trộn → mỗi lần data đổi vỡ formula. 
   Giờ data ở sheet riêng (01) → formula ở sheet riêng (03) → dashboard chỉ link kết quả (04). 
   Data đổi không ảnh hưởng formula structure.

2. **Permission clarity**: User biết sheet nào không sửa (đỏ), sheet nào sửa cẩn thận (cam), 
   sheet nào admin (vàng), sheet nào view (xanh). Tránh "sửa nhầm" làm vỡ file.

3. **Maintenance ease**: Khi cần thêm KPI mới → chỉ sửa sheet 03_model và 04_dashboard, 
   không động vào raw data layer.

### Color code semantic

| Màu | Sheet role | Permission |
|---|---|---|
| 🔴 Đỏ | Raw input | Chỉ PASTE data, không sửa structure |
| 🟠 Cam | Input contract | Sửa khi raw schema đổi (cột mới/đổi tên) |
| 🟡 Vàng | Model | Admin only — chỉ sửa nếu hiểu formula |
| 🔵 Xanh | Dashboard + Drill | View only — slicer OK, không edit cell |
| ⚪ Xám | Settings + Archive | Config + lưu trữ |

---

## 2. WORKFLOW HÀNG KỲ

### Quy trình refresh ([cadence])

```
Bước 1: Lấy data kỳ mới từ [nguồn data]
Bước 2: Mở file `[tên_file].xlsx`
Bước 3: Vào sheet "01_input_data" (màu đỏ)
Bước 4: Xóa data cũ (giữ header dòng 1)
Bước 5: Paste data mới từ ô A2 trở xuống
Bước 6: Vào tab Data > Refresh All (hoặc nhấn Ctrl+Alt+F5)
Bước 7: Vào sheet "04_dashboard" để đọc kết quả
Bước 8: Save file (Ctrl+S) — KHÔNG dùng "Save As"
```

**Thời gian dự kiến**: ~[X] phút/kỳ

### Lưu ý quan trọng

- **KHÔNG dùng "Save As"**: Save As tạo file mới mất kết nối Power Query (nếu có). Luôn Ctrl+S.
- **KHÔNG đổi tên column trong sheet 01**: Vi phạm schema → vỡ formula. Nếu raw nguồn đổi tên cột → fix trong sheet 02_input_contract.
- **KHÔNG xóa dòng header (dòng 1) trong sheet 01**: Header là schema. Xóa = mất reference.

---

## 3. CÔNG THỨC THEO TỪNG KPI

Walkthrough chi tiết công thức của 5 KPI core. Khi cần adjust, biết chỗ.

### KPI 1: [Tên KPI]

**Vị trí**: Sheet `04_dashboard`, ô [X1]

**Công thức**:
```excel
=SUMIFS([model_range], [criteria_range], [criteria])
```

**Giải thích**:
- Lấy [aggregation] của [metric] từ sheet 03_model
- Filter theo [dimension] = [value]
- Period = [time window: today / WTD / MTD]

**Khi cần thay đổi**: 
- Đổi target → sheet `06_settings`, ô [Y]
- Đổi cách tính → sửa formula trong sheet `03_model` ô [Z], không sửa trực tiếp dashboard

[Lặp lại format trên cho 5 KPI]

---

## 4. SO SÁNH CŨ vs MỚI

### Những gì THAY ĐỔI

| Aspect | File cũ | File mới |
|---|---|---|
| Số sheets | [X] | [Y] |
| Cách refresh | [Manual copy-paste / VLOOKUP chain] | [Power Query auto / 1-click Refresh All] |
| Thời gian/kỳ | ~[X] giờ | ~[Y] phút |
| KPI count | [X] (trong đó [N] orphan) | [Y] (all linked to decision) |
| [Other aspect] | [Old] | [New] |

### Những gì GIỮ NGUYÊN

- **Vocabulary**: Vẫn dùng "[term tiếng Việt user quen]", không đổi sang tiếng Anh
- **Layout familiar**: [Element X vẫn ở vị trí góc trên bên phải / etc.]
- **[Other preservation]**

### Element đã ELIMINATE

[List elements đã loại bỏ + lý do]
- Sheet "[X]" — snapshot kỳ cũ, không link decision
- Column "[Y]" — orphan, không ai reference
- Chart pie 12-slice — replace bằng bar chart (dễ đọc hơn)

---

## 5. HOW-TO: Thêm/sửa KPI mới

### Thêm 1 KPI mới

```
Bước 1: Vào sheet 03_model
Bước 2: Thêm 1 cột mới (vd: cột AA)
Bước 3: Viết formula tính KPI mới (vd: =SUMIFS(...))
Bước 4: Vào sheet 04_dashboard
Bước 5: Copy 1 KPI card cũ (4 ô chiều dọc)
Bước 6: Paste vào vị trí mới
Bước 7: Sửa link reference của 4 ô (Title / Number / vs Target / Sparkline) đến column AA mới
Bước 8: Refresh All → check
```

### Sửa target của KPI

```
Bước 1: Vào sheet 06_settings
Bước 2: Tìm row "[Tên KPI]"
Bước 3: Sửa giá trị cột "Target"
Bước 4: Refresh All
```

### Thêm 1 drill sheet mới

```
Bước 1: Copy sheet 05_drill_[existing] (right-click tab > Move or Copy > Create copy)
Bước 2: Rename sheet thành 05_drill_[new_kpi]
Bước 3: Click vào PivotTable trong sheet → PivotTable Analyze > Change Data Source 
        → trỏ vào range cần drill mới
Bước 4: Adjust Row/Column/Value fields
Bước 5: Vào sheet 04_dashboard → thêm hyperlink "→ Drill [new KPI]" trỏ tới sheet drill mới
```

---

## 6. TROUBLESHOOTING (Top 10 issues)

### Issue 1: Dashboard không update sau khi paste data

**Triệu chứng**: Paste data mới rồi mà KPI vẫn show số cũ.

**Fix**:
1. Click Data > Refresh All
2. Nếu vẫn không update: check sheet 01_input — data có thực sự được paste vào không?
3. Nếu data nằm sai sheet → cut paste lại vào sheet 01 (màu đỏ)

### Issue 2: KPI hiện #N/A hoặc #REF!

**Fix**:
1. Click vào ô lỗi → đọc formula
2. Identify reference broken (vd: range không tồn tại, sheet đổi tên)
3. Fix reference hoặc undo change gần nhất (Ctrl+Z)

### Issue 3: Chart bị trống / không hiện gì

**Fix**:
1. Right-click chart > Select Data > kiểm tra Source range
2. Nếu source range cố định (vd: A1:A100) → expand đến cuối data hoặc convert sang Table
3. Refresh All

### Issue 4: Slicer cleared sai → data hiện thiếu

**Fix**:
1. Click vào slicer
2. Click nút "Clear Filter" (icon góc trên phải slicer)
3. Hoặc dùng nút "Reset All" trong dashboard (nếu có)

### Issue 5: Cột raw bị đổi tên / thêm cột mới

**Triệu chứng**: Sau khi paste data kỳ mới, dashboard ra số sai.

**Fix**:
1. Vào sheet 02_input_contract
2. Tìm row của cột đã đổi tên
3. Update formula reference tới tên cột mới
4. Refresh All

### Issue 6: File quá chậm / lag khi mở

**Diagnosis**: Có thể có quá nhiều conditional formatting hoặc data quá lớn.

**Fix**:
1. Check sheet 03_model: có CF rules >5 trên cùng range không? → giảm
2. Check data size: >100K rows? → consider Power Query với load to data model only (không load to sheet)
3. Nếu vẫn lag: cân nhắc migrate sang Power BI Desktop

### Issue 7: Sửa nhầm formula trong sheet 03_model

**Fix**:
1. Ctrl+Z ngay (undo)
2. Nếu đã save và không undo được:
   - Tải file `[tên_file]_v1.0_backup.xlsx` (skill đã ship cùng)
   - Copy sheet 03_model từ backup sang file đang dùng
3. Lưu ý: sheet 03 đã có protection → trong tương lai cần unprotect mới sửa được

### Issue 8: Muốn thêm filter mới cho dashboard

**Fix**:
1. Vào sheet 04_dashboard
2. Click vào 1 PivotTable hoặc Table source
3. PivotTable Analyze > Insert Slicer
4. Chọn dimension muốn filter (vd: Region, Product Category)
5. Move slicer vào vị trí trên dashboard

### Issue 9: Format số / ngày bị sai

**Fix**:
1. Chọn column bị sai format
2. Right-click > Format Cells
3. Chọn category đúng (Number / Date / Currency)
4. Apply

### Issue 10: User mới trong team muốn dùng file

**Fix**:
1. Share file qua cloud drive (OneDrive / Google Drive)
2. Send họ link tới sheet "00_README" để đọc Quick Start
3. Train họ 1 lần qua quy trình refresh (Section 2 của guide này)

---

## 7. KHI NÀO MIGRATE LÊN POWER BI?

File `.xlsx` này hoạt động tốt cho [scope hiện tại]. Tuy nhiên có ngưỡng phải migrate:

### Trigger migration

Khi gặp ≥1 điều kiện dưới, consider migrate sang Power BI Desktop (free) hoặc Power BI Service:

1. **Data >500K rows**: Excel lag severe, refresh chậm >10 giây
2. **>5 data sources cần join**: Power Query trong Excel handle được nhưng kém Power BI
3. **Real-time update**: Cần dashboard refresh <1 giờ → Power BI Service scheduled refresh
4. **>10 concurrent users edit cùng lúc**: Excel conflict → Power BI có row-level security
5. **Audit trail compliance**: Cần version history + access log
6. **Cross-org sharing với access control**: Power BI có sharing model chuyên dụng

### Migration approach

Khi đến lúc migrate:
1. Document KPI definitions từ file Excel này (đã có sẵn ở Section 3 của guide)
2. Export schema sheet 01_input và 02_contract làm reference
3. Trong Power BI Desktop:
   - Get Data > Excel → import file này
   - Recreate KPI measures dùng DAX (tương tự công thức Excel)
   - Recreate dashboard visuals
4. Test parallel 1 cycle (cả Excel và Power BI cùng chạy) → so sánh kết quả
5. Cutover khi confident

Skill `bi-reporting-architect` có thể support migration spec — quay lại nhờ help khi cần.

---

## 8. SUPPORT & RESOURCES

### Liên hệ khi cần help

- **Quick question**: Reply skill conversation
- **Issue lớn**: Document issue + screenshot, gửi skill conversation để debug
- **Feature request lớn**: Define requirement → skill có thể design v1.1 / v2.0

### File-related artifacts

- `[tên_file]_dashboard_v1.0.xlsx` — file chính
- `[tên_file]_dashboard_v1.0_backup.xlsx` — backup copy (giữ riêng, không sửa)
- `AS-IS_audit_report.md` — documentation về file cũ (lý do redesign)
- `BUILD_GUIDE.md` — file này

### Khuyến nghị maintain habit

- **Weekly**: Run refresh đúng quy trình. Không "Save As".
- **Monthly**: Review xem có element nào trong dashboard không còn dùng → ELIMINATE
- **Quarterly**: Review KPI definitions còn relevant không. Adjust nếu business strategy đổi.
- **Annually**: Re-audit toàn bộ file. Skill có thể support audit cycle.

---

**Chúc bạn vận hành smooth! 🚀**
```

---

## CUSTOMIZATION CHECKLIST

Khi generate file BUILD_GUIDE.md cụ thể, customize:

- [ ] `[Tên file dashboard]` — actual filename
- [ ] `[user role/name]` — Sales Manager / CS Lead / etc.
- [ ] `[domain]` — Sales / CS / Ops / Finance / HR / Marketing / Ecom
- [ ] `[Daily/Weekly/Monthly]` — actual cadence
- [ ] Section 1: cấu trúc file thực tế (số sheet, tên sheet)
- [ ] Section 2: workflow refresh cụ thể (bao nhiêu phút/kỳ thực tế)
- [ ] Section 3: 5 KPI thực tế với công thức cụ thể
- [ ] Section 4: AS-IS vs TO-BE comparison cụ thể với numbers
- [ ] Section 6: Top 10 issues — replace generic với issues thực tế từ Kỳ 1-2 coaching
- [ ] Vocabulary: giữ tiếng Việt user dùng, không generic English
- [ ] File backup name: actual backup file name nếu có ship

**Quan trọng**: BUILD_GUIDE.md cá nhân hóa cho user cụ thể, không phải generic doc. User đọc phải thấy "ờ guide này nói về file của tôi".
