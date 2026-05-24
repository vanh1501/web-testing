# Coaching Playbook — First-Cycle Coaching Protocol

**Mục đích**: Hand-hold non-tech user qua 3 kỳ đầu sau khi ship Stage 1 file đến khi self-sufficient.

**Triết lý**: Skill KHÔNG chỉ ship file rồi xong. Non-tech cần coaching để vận hành file mới — như có 1 senior consultant ngồi cùng kỳ đầu.

---

## TABLE OF CONTENTS

- [Kỳ 1: Walk-through (immediately after Stage 1 ship)](#kỳ-1-walk-through-immediately-after-stage-1-ship)
- [Kỳ 2: Self-attempt check (1 cycle later)](#kỳ-2-self-attempt-check-1-cycle-later)
- [Kỳ 3: Final tune + Stage 2 ship](#kỳ-3-final-tune--stage-2-ship)
- [Common troubleshooting scenarios](#common-troubleshooting-scenarios)
- [Coaching tone & language](#coaching-tone--language)
- [Capability gap detection](#capability-gap-detection)

---

## Kỳ 1: Walk-through (immediately after Stage 1 ship)

### Mục tiêu
User chạy 1 cycle với data thật, có support live troubleshooting.

### Skill prompt to user

```
File `[name]_v1.0.xlsx` đã ready với mock data.

**Bước test với data thật**:
1. Khi có data kỳ này, mở file
2. Vào sheet "01_input_data" (màu đỏ)
3. Xóa mock data hiện có (giữ header dòng 1)
4. Paste data thật vào từ ô A2 trở xuống
5. Vào tab Data > Refresh All (hoặc Ctrl+Alt+F5)
6. Xem sheet "04_dashboard"
7. **Screenshot dashboard gửi tôi xem**

Tôi sẽ check live và troubleshoot nếu có issue.
```

### Skill response khi user gửi screenshot

**Scenario 1: Dashboard hiện đúng**
```
Perfect! Dashboard đã work. Confirm 3 điểm:
- [ ] Số liệu khớp với expectation của bạn không?
- [ ] KPI nào quan trọng nhất bạn đang focus?
- [ ] Có điều gì muốn adjust không (vd: layout, color, KPI thêm/bớt)?

Nếu OK hết → run cycle nữa kỳ tới rồi báo tôi.
```

**Scenario 2: Dashboard broken / empty / show errors**
```
OK tôi thấy [specific issue]. Đây là cách fix:
[Step-by-step screenshot-level instructions]

Sau khi fix, screenshot lại nhé.
```

**Scenario 3: User confused, không screenshot được**
```
Không sao. Cho tôi biết:
- Bạn đang ở sheet nào? (tên hoặc màu tab)
- Click Refresh có thấy gì xảy ra không?
- Có popup error message gì hiện ra không?

Trả lời 3 câu trên rồi tôi guide tiếp.
```

### Expected outcome Kỳ 1
- User hoàn thành 1 cycle với data thật
- File adjusted v1.1 nếu phát hiện issue
- User biết quy trình refresh cơ bản

### Time investment
30-60 phút support, 1-3 turn-arounds

---

## Kỳ 2: Self-attempt check (1 cycle later)

### Mục tiêu
User tự chạy 1 cycle KHÔNG có hand-hold. Verify self-sufficiency.

### Skill prompt to user (sau ~1 tuần/tháng — tùy cadence)

```
Kỳ này bạn tự chạy cycle nhé:
1. Paste data mới vào sheet 01_input_data
2. Refresh All
3. Đọc dashboard

Sau khi xong, gửi screenshot output cho tôi check.
```

### Skill response khi user gửi output

**Scenario 1: User report "ngon, không có issue gì"**
```
Tuyệt vời. Bạn đã tự run được — chuẩn bị cho Kỳ 3 = ship full guide.

Trước đó, confirm 2 điểm:
- [ ] Có muốn thêm/bớt KPI nào không (sau khi dùng thật)?
- [ ] Có ai khác cần được train sử dụng file này không?
```

**Scenario 2: User report 1-2 minor issues**
```
Issue [X] thường gặp ở giai đoạn này. Fix:
[Step-by-step]

Tôi cũng update README sheet thêm troubleshooting note này cho lần sau. File v1.2 đính kèm.
```

**Scenario 3: User report ≥3 issues hoặc cùng issue ≥2 lần**
```
OK có pattern. Tôi nghĩ cần adjust file design thay vì fix từng issue.
Cụ thể: [identify capability gap]

Đề xuất:
- [Redesign element X để đơn giản hơn]
- [Add data validation cell Y]
- [Add Reset button Z]

File v1.2 với fix structural đính kèm. Test lại Kỳ tới.
```

### Expected outcome Kỳ 2
- User self-sufficient với core workflow
- File evolved v1.2 nếu cần
- Common issues documented cho Stage 2 troubleshooting

---

## Kỳ 3: Final tune + Stage 2 ship

### Mục tiêu
Ship full Stage 2 package: file finalized + BUILD_GUIDE.md + expanded README.

### Trigger Stage 2 khi:
- ≥2 cycles không có major issue
- User confident vận hành (không hỏi câu cơ bản nữa)
- Có feedback chi tiết về tinh chỉnh nhỏ

### Stage 2 deliverables

```
Package:
├── [name]_dashboard_v1.0.xlsx (finalized)
├── BUILD_GUIDE.md (1500-2500 words)
│   ├── Architecture rationale (vì sao 3-layer)
│   ├── Formula walkthrough per KPI
│   ├── AS-IS → TO-BE transformation log
│   ├── How-to: thêm KPI / chart / drill mới
│   ├── Troubleshooting top 10 (từ Kỳ 1-2 thực tế)
│   └── Escalation guide (khi nào migrate Power BI)
├── README sheet trong file (expanded)
└── AS-IS audit report (documentation về lý do redesign)
```

### "Graduation" message

```
Stage 2 package đã ready. Bạn đã chạy 3 cycles thành công — chính thức self-sufficient với file này.

Từ giờ:
- BUILD_GUIDE.md = reference khi cần adjust/extend file
- README sheet = quick reference cho người mới (nếu bạn handover cho team)
- Tôi sẵn sàng support khi có change lớn (vd: thêm KPI mới, migrate Power BI khi vượt scale)

Chúc bạn vận hành smooth!
```

---

## Common troubleshooting scenarios

### Issue 1: "Em paste data vào mà dashboard không hiện gì"

**Diagnosis**:
- Paste sai sheet (vào sheet model thay vì input)?
- Paste nhưng quên click Refresh?
- Data range Table không auto-expand?

**Fix**:
```
Check 3 điểm:
1. Bạn paste vào sheet màu gì? Phải là màu ĐỎ (sheet 01_input_data)
2. Sau khi paste, có click Data > Refresh All chưa?
3. Mở sheet 01_input_data, scroll xuống cuối data — có dòng nào trống giữa data không?

Trả lời 3 câu này tôi guide tiếp.
```

### Issue 2: "Số trong dashboard ra lạ, không khớp data"

**Diagnosis**:
- Data type không match (số nhập text vì có ký tự lạ)?
- Formula reference cố định không expand?
- Filter chưa clear từ kỳ trước?

**Fix**:
```
3 cách check:
1. Vào sheet 01_input_data, chọn 1 ô số → format có phải "Number" không? (xem góc dưới bên phải Excel)
2. Vào sheet 04_dashboard, click vào ô KPI nghi ngờ → đọc công thức trên thanh formula → reference range có expand đến cuối data không?
3. Có slicer nào đang filter không? Click "Clear filter" nút trên slicer.

Screenshot công thức của ô KPI sai → tôi check.
```

### Issue 3: "Chart bị #N/A hoặc trống"

**Diagnosis**:
- Source range không update
- PivotTable cần refresh riêng
- Data range có blank row giữa

**Fix**:
```
1. Right-click chart → Select Data → kiểm tra source range có cover hết data mới không
2. Nếu có PivotTable: right-click PivotTable → Refresh
3. Vào sheet input, scroll qua data — có dòng trống nào giữa không? Nếu có → xóa
```

### Issue 4: "Em sửa nhầm formula trong model"

**Diagnosis**: User accidentally edited protected sheet.

**Fix**:
```
Đừng lo. 2 cách:
1. Ctrl+Z liên tục để undo
2. Nếu đã save: tải lại file v1.0 từ template tôi gửi, copy data từ sheet input cũ sang

Để tránh lần sau: tôi update v1.1 với protection trên sheet model (chỉ cho phép view, không edit).
```

### Issue 5: "Sếp muốn thêm 1 KPI mới"

**Diagnosis**: Feature request — không phải bug.

**Fix**:
```
OK adjust được. Cho tôi biết:
1. Tên KPI mới là gì?
2. Công thức tính (vd: "X chia Y", "Tổng A trong tháng")?
3. Đặt trên dashboard ở đâu (thay 1 KPI cũ, hay thêm vào)?

Trả lời 3 câu này, tôi update file v1.1 với KPI mới.
```

---

## Coaching tone & language

### DO ✅

- **Patient, không condescending**: Coi user như người bận, không phải ngu
- **Celebrate small wins**: "OK refresh đã work, perfect"
- **Educate while fixing**: "Lý do nó broken là [...], lần sau bạn có thể tự fix bằng [...]"
- **Step-by-step screenshot-level** khi user beginner: "Mở file → click sheet tab '01_input' (màu đỏ) → click ô A2 → Ctrl+V"
- **Multiple choice questions** nếu cần clarify
- **Concrete examples** thay vì abstract
- **Acknowledge confusion**: "Phần này hơi confusing — bình thường người mới đều vướng đây"

### DON'T ❌

- **Technical jargon trừ khi cần**: "M language", "pivot cache" → translate
- **Long explanations về theory**: User chỉ cần action, không cần hiểu why deep
- **Blame user**: "Bạn làm sai bước nào?" → "Để check xem cấu hình có issue không"
- **Multiple bugs cùng lúc**: Fix 1 issue at a time, đừng overwhelm
- **Assume Excel knowledge**: Mỗi tính năng đề cập → 1 dòng explain ngắn

### Sample bad vs good

❌ Bad: "Power Query connection broken, M code có lỗi, cần refresh data model."

✅ Good: "Có vẻ kết nối data bị đứt. Đây là cách fix:
1. Vào tab Data > Queries & Connections
2. Right-click query tên 'tbl_raw' → Refresh
Nếu vẫn lỗi, screenshot popup tôi xem."

---

## Capability gap detection

Nếu user stuck cùng issue ≥2 lần → identify gap → redesign:

| Symptom | Gap identified | Fix |
|---|---|---|
| User paste vào sai sheet liên tục | Visual cue chưa đủ rõ | Add big text "PASTE DATA VÀO ĐÂY" trong sheet input, color highlight strong |
| User clear slicer sai liên tục | Slicer position hoặc affordance issue | Move slicer position, add "Reset" button hyperlink |
| User không biết Refresh ở đâu | Refresh button không obvious | Add big button "🔄 Refresh All" trên dashboard với hyperlink to macro hoặc instruction |
| User edit formula trong model | Protection chưa enable | Enable sheet protection (Review > Protect Sheet) với password admin biết |
| User không hiểu KPI số ra ý nghĩa gì | KPI label chưa rõ | Add subtitle "(target: X, alert if <Y)" dưới mỗi KPI card |
| User scared sửa gì | Permission note chưa rõ | Add clear note đầu mỗi sheet: "Sheet này [VIEW ONLY / ADMIN EDIT / FREE EDIT]" |

**Nguyên tắc**: Issue lặp lại = design issue, không phải user issue. Fix design.

---

## Coaching escalation

Nếu sau Kỳ 2 user vẫn vướng nhiều issue → consider:

1. **Live walk-through** (nếu có meeting tool): Hướng dẫn screen share thực tế 30 phút
2. **Pair down complexity**: File v1.1 đơn giản hơn (bớt KPI, bớt features), level up dần
3. **Train another person**: Có ai trong team đó tech-comfortable hơn không? Train người đó làm "admin" cho file
4. **Escalation message to user**: "File này có vẻ vẫn complex cho workflow của bạn. Đề xuất: (a) đơn giản hóa thêm v1.2, (b) train 1 colleague làm admin, (c) hire 1 part-time data person. Bạn chọn hướng nào?"
