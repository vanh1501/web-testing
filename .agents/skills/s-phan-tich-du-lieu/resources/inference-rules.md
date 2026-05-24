# Quy Tắc Suy Luận — Đoán Domain / Cadence / Pain từ tín hiệu dữ liệu

**Mục đích**: Agent quan sát file Excel/CSV và tự suy luận bối cảnh TRƯỚC khi phân tích. Đây là năng lực tư vấn cốt lõi — nhìn file 5 phút biết user đang làm gì.

**Khi nào dùng**: Step 0 (OBSERVE & INFER) của pipeline phan-tich-du-lieu. Sau khi đọc file structure + column headers + formulas, áp dụng 5 bộ quy tắc dưới để build Internal Inference Brief.

---

## Quy tắc 1: Nhận diện Ngành / Phòng ban (Domain)

Dò tên cột trong dữ liệu và khớp với bảng từ khóa:

| Từ khóa xuất hiện trong tên cột | Ngành / Phòng ban | Độ tin cậy |
|---|---|---|
| "AE", "Deal", "Pipeline", "Close Date", "Quota", "Stage", "Lead Source" | **Kinh doanh (Sales)** | 90% |
| "Ticket", "Agent", "SLA", "CSAT", "AHT", "FRT" | **Chăm sóc Khách hàng (CS)** | 90% |
| "OEE", "Downtime", "Defect", "Yield", "Shift", "Cycle Time" | **Vận hành Sản xuất (Ops)** | 90% |
| "Revenue", "Cost", "AR", "AP", "Margin", "Cash", "GL", "Budget" | **Tài chính / Kế toán** | 85% |
| "Headcount", "Attrition", "Hire", "Engagement", "FTE", "Tenure", "Nhân sự" | **Nhân sự (HR)** | 90% |
| "Campaign", "CAC", "ROAS", "Impressions", "CTR", "CPC" | **Marketing** | 90% |
| "GMV", "Conversion", "AOV", "Cart", "Sessions", "SKU" | **Thương mại điện tử (Ecom)** | 90% |

**Logic phán đoán:**
- 3+ từ khóa khớp 1 domain → Tin cậy cao
- 2+ domains cùng khớp (vd: Sales + Marketing trộn) → Đánh dấu "Đa lĩnh vực" → hỏi user chọn trọng tâm
- Không khớp domain nào → Đánh dấu "Chưa xác định" → hỏi user 1 câu multiple-choice

**Tín hiệu bổ sung:**
- Tên file/sheet chứa "sales", "revenue", "pipeline" → Tăng xác suất domain Sales
- Định dạng tiền tệ xuất hiện nhiều → Thiên về Tài chính/Kế toán
- Tên cột tiếng Việt ("Doanh thu", "Chi nhánh", "Phòng ban") → Giữ nguyên ngôn ngữ

---

## Quy tắc 2: Nhận diện Chu kỳ báo cáo (Cadence)

Dò tên sheet + pattern ngày tháng:

| Pattern phát hiện | Chu kỳ |
|---|---|
| Sheet tên: "T01, T02, ..., T12" hoặc "Jan, Feb, ..., Dec" | **Hàng tháng** |
| Sheet tên: "W01, W02, ..." hoặc "Week 1, Week 2..." | **Hàng tuần** |
| Cột ngày có dữ liệu mỗi ngày liên tục (30 ngày gần nhất) | **Hàng ngày** |
| Sheet tên: "Q1, Q2, Q3, Q4" | **Hàng quý** |
| 1 sheet duy nhất, cột ngày trải dài 6+ tháng | **Tổng hợp** — xem kỹ mật độ dữ liệu để xác định |

**Nếu không rõ**: Áp dụng mặc định theo domain (Sales/CS → Tuần, Finance/HR → Tháng, Ops/Ecom → Ngày).

---

## Quy tắc 3: Nhận diện Trọng tâm ra quyết định

Đoán user đang quan tâm điều gì từ loại biểu đồ + công thức:

| Tín hiệu | Trọng tâm suy luận |
|---|---|
| Biểu đồ đường theo thời gian | "Theo dõi xu hướng" — phát hiện pattern |
| Biểu đồ cột nhóm theo nhân viên/vùng/sản phẩm | "So sánh hiệu suất" — xếp hạng |
| Biểu đồ phễu / waterfall | "Phân tích chuyển đổi" — tìm điểm rơi |
| Conditional formatting nặng trên cột số | "Phát hiện bất thường" — tìm outlier |
| SUMIF/SUMIFS nhiều | "Tổng hợp theo chiều" — nhóm dữ liệu |
| PivotTable có sẵn | "Phân tích đa chiều" — user có kinh nghiệm |

**Cách dùng**: Kết hợp 2-3 tín hiệu → xác định mục đích phân tích. Ví dụ: Biểu đồ đường + SUMIFS + filter theo "Chi nhánh" → "Theo dõi doanh thu theo chi nhánh qua thời gian".

---

## Quy tắc 4: Đánh giá năng lực Excel của User

| Tín hiệu | Mức năng lực |
|---|---|
| Dùng Power Query, M language | **Cao** |
| Dùng Table (Ctrl+T) nhất quán | **Trung bình** |
| Dùng PivotTable + Slicer | **Trung bình** |
| Chỉ dùng SUM, AVERAGE, VLOOKUP | **Cơ bản** |
| Range cứng A1:Z500 (không dùng Table) | **Cơ bản** |
| Merge cell khắp nơi | **Mới bắt đầu** — tư duy trình bày, chưa tư duy dữ liệu |
| Không có công thức, toàn số cứng | **Mới bắt đầu** — cần hướng dẫn kỹ |

**Ý nghĩa cho phân tích**: Nếu user ở mức Cơ bản/Mới bắt đầu → Agent giải thích kết quả bằng ngôn ngữ đơn giản, tránh thuật ngữ kỹ thuật. Nếu Trung bình/Cao → có thể dùng thuật ngữ chuyên ngành.

---

## Quy tắc 5: Phát hiện Điểm đau (Pain Point)

| Tín hiệu trong file | Điểm đau suy luận |
|---|---|
| Cùng 1 dữ liệu xuất hiện ở 3+ sheet | **Sao chép thủ công** — user copy-paste giữa các sheet |
| Nhiều file "T01.xlsx, T02.xlsx" riêng biệt | **Không có template** — dựng lại mỗi kỳ |
| Biểu đồ hiển thị #N/A hoặc #REF! | **Dễ hỏng khi cập nhật** — range không tự mở rộng |
| Sheet "TEMP", "DELETE LATER", "Backup" | **Không dọn dẹp** — file phình to theo thời gian |
| Merge cell trong vùng dữ liệu | **Gãy filter/sort** — không lọc/sắp xếp được |
| Dòng trống xen kẽ trong dữ liệu | **Table auto-expand hỏng** — thêm data phải chỉnh range thủ công |

**Đánh giá mức độ:**
- 0-2 tín hiệu = Dữ liệu chấp nhận được → Chạy pipeline bình thường
- 3-4 tín hiệu = Cần dọn dẹp trước khi phân tích → Cảnh báo user
- 5+ tín hiệu = Đề nghị chuẩn hóa lại file gốc trước (route sang `thiet-ke-bao-cao-bi`)

---

## Mẫu Kết Quả Suy Luận (Internal Inference Brief)

```yaml
domain: Nhân sự (HR) — tin cậy 90%
cadence: Không xác định rõ — sheet đơn, dữ liệu snapshot
decision_focus: Tổng hợp theo chiều (phòng ban, chi nhánh, giới tính)
user_excel_level: Trung bình (có VLOOKUP, không có PivotTable)
pain_signals: 1 (Dữ liệu chấp nhận được)
file_health: Chấp nhận được → Chạy pipeline bình thường
preserved_vocab: "Chi nhánh", "Phòng ban", "Trạng thái" (giữ tiếng Việt)
```

---

v1.0 (2026-05-19) — Trích xuất và Việt hóa từ bi-reporting-architect/references/inference_rules.md
