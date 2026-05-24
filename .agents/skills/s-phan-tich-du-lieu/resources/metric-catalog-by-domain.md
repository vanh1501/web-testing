# Catalog Chỉ Số Theo Ngành / Phòng Ban

**Mục đích**: Cung cấp bộ chỉ số mẫu cho 7 lĩnh vực phổ biến. Agent dùng kết quả Inference (Step 0) để chọn đúng bộ chỉ số, sau đó đề xuất cho user confirm trước khi tính toán.

**Cách dùng**: Step 2 (KPI Calculation) — Agent tra bảng dưới theo domain đã suy luận, đề xuất 5 chỉ số core, user chọn Yes/Adjust.

---

## 1. Kinh doanh (Sales)

| # | Tên Chỉ số | Công thức | Ngưỡng tốt | Ngưỡng cảnh báo |
|---|---|---|---|---|
| 1 | Doanh thu thuần | Tổng giá trị đơn hàng đã hoàn thành | Theo target | Dưới 80% target |
| 2 | Tỷ lệ chốt (Win Rate) | Số đơn chốt / Tổng số đơn tiếp cận * 100% | ≥25% | <15% |
| 3 | Giá trị đơn trung bình (ASP) | Tổng doanh thu / Số đơn hàng | Theo ngành | Giảm >10% so kỳ trước |
| 4 | Vòng quay Pipeline | Số ngày trung bình từ Lead → Close | ≤30 ngày | >45 ngày |
| 5 | Hiệu suất theo Sales Rep | Doanh thu từng người / Target từng người * 100% | ≥100% | <80% |

---

## 2. Chăm sóc Khách hàng (CS)

| # | Tên Chỉ số | Công thức | Ngưỡng tốt | Ngưỡng cảnh báo |
|---|---|---|---|---|
| 1 | CSAT (Hài lòng KH) | Số phản hồi tốt / Tổng phản hồi * 100% | ≥85% | <70% |
| 2 | Thời gian phản hồi đầu (FRT) | Thời gian trung bình từ lúc nhận ticket đến phản hồi đầu | ≤2 giờ | >4 giờ |
| 3 | Thời gian xử lý trung bình (AHT) | Tổng thời gian xử lý / Số ticket | ≤15 phút | >30 phút |
| 4 | Tỷ lệ giải quyết lần đầu (FCR) | Số ticket đóng lần đầu / Tổng ticket * 100% | ≥75% | <60% |
| 5 | Backlog tồn đọng | Số ticket mở cuối kỳ - Số ticket mở đầu kỳ | ≤0 (giảm) | Tăng >20% |

---

## 3. Vận hành Sản xuất (Ops)

| # | Tên Chỉ số | Công thức | Ngưỡng tốt | Ngưỡng cảnh báo |
|---|---|---|---|---|
| 1 | OEE (Hiệu suất thiết bị tổng thể) | Availability * Performance * Quality | ≥85% | <65% |
| 2 | Tỷ lệ lỗi (Defect Rate) | Số sản phẩm lỗi / Tổng sản phẩm * 100% | ≤1% | >3% |
| 3 | Thời gian dừng máy (Downtime) | Tổng giờ dừng máy ngoài kế hoạch / Tổng giờ vận hành * 100% | ≤5% | >10% |
| 4 | Năng suất lao động | Sản lượng / Số nhân công / Số ca | Theo target | Giảm >10% so kỳ trước |
| 5 | Thời gian chu kỳ (Cycle Time) | Thời gian trung bình hoàn thành 1 đơn vị sản phẩm | Theo chuẩn | Tăng >15% |

---

## 4. Tài chính / Kế toán

| # | Tên Chỉ số | Công thức | Ngưỡng tốt | Ngưỡng cảnh báo |
|---|---|---|---|---|
| 1 | Biên lợi nhuận gộp | (Doanh thu - Giá vốn) / Doanh thu * 100% | ≥30% | <20% |
| 2 | Số ngày thu hồi công nợ (DSO) | Công nợ phải thu / Doanh thu trung bình ngày | ≤30 ngày | >60 ngày |
| 3 | Tỷ lệ chi phí / Doanh thu | Tổng chi phí vận hành / Doanh thu * 100% | ≤70% | >85% |
| 4 | Dòng tiền ròng | Tổng thu - Tổng chi trong kỳ | >0 (dương) | <0 liên tục 2 kỳ |
| 5 | Chênh lệch ngân sách | (Chi thực tế - Ngân sách dự kiến) / Ngân sách * 100% | ≤5% | >15% |

---

## 5. Nhân sự (HR)

| # | Tên Chỉ số | Công thức | Ngưỡng tốt | Ngưỡng cảnh báo |
|---|---|---|---|---|
| 1 | Tổng nhân sự hiện tại | Số người có Trạng thái = "Đang làm việc" | Theo định biên | Chênh >10% so định biên |
| 2 | Tỷ lệ nghỉ việc (Turnover) | Số người Đã nghỉ việc / Tổng nhân sự * 100% | ≤10% | >15% |
| 3 | Thời gian tuyển dụng (Time-to-Hire) | Số ngày trung bình từ Ngày mở tuyển đến Ngày nhận việc | ≤30 ngày | >45 ngày |
| 4 | Phân bổ theo phòng ban | (Số người tại Phòng ban / Tổng nhân sự) * 100% | Theo định biên | Lệch >20% so định biên |
| 5 | Tỷ lệ giữ chân nhân sự mới (<1 năm) | Số người mới còn ở lại / Tổng người mới tuyển trong 12 tháng * 100% | ≥80% | <60% |

---

## 6. Marketing

| # | Tên Chỉ số | Công thức | Ngưỡng tốt | Ngưỡng cảnh báo |
|---|---|---|---|---|
| 1 | ROAS (Lợi nhuận trên chi phí QC) | Doanh thu từ quảng cáo / Chi phí quảng cáo | ≥4.0 | <2.5 |
| 2 | CAC (Chi phí thu hút 1 KH) | Tổng chi phí MKT / Số khách hàng mới | ≤500K | >800K |
| 3 | CTR (Tỷ lệ nhấp) | Số lượt nhấp / Số lượt hiển thị * 100% | ≥2% | <1% |
| 4 | Tỷ lệ chuyển đổi (CVR) | Số đơn hàng / Số lượt nhấp * 100% | ≥5% | <2% |
| 5 | Chi phí mỗi Lead (CPL) | Tổng chi phí MKT / Số lead thu được | Theo ngành | Tăng >20% so kỳ trước |

---

## 7. Thương mại điện tử (Ecom)

| # | Tên Chỉ số | Công thức | Ngưỡng tốt | Ngưỡng cảnh báo |
|---|---|---|---|---|
| 1 | GMV (Tổng giá trị giao dịch) | Tổng doanh thu trên sàn | Theo target | Dưới 80% target |
| 2 | Tỷ lệ chuyển đổi (CVR) | Số đơn hàng / Số lượt truy cập * 100% | ≥3% | <1.5% |
| 3 | Giá trị đơn trung bình (AOV) | Tổng doanh thu / Số đơn hàng | Theo ngành | Giảm >10% so kỳ trước |
| 4 | Tỷ lệ bỏ giỏ (Cart Abandonment) | Số giỏ bỏ / Tổng giỏ tạo * 100% | ≤60% | >75% |
| 5 | Tỷ lệ hoàn/hủy đơn | Số đơn hoàn + hủy / Tổng đơn * 100% | ≤3% | >5% |

---

## Hướng dẫn sử dụng cho Agent

1. **Tra bảng**: Dùng domain từ Step 0 Inference → tìm đúng section
2. **Đề xuất**: Show 5 chỉ số core cho user dưới dạng danh sách, kèm giải thích 1 dòng
3. **User confirm**: "5 chỉ số trên có phù hợp không? Anh/Chị muốn thay đổi chỉ số nào?"
4. **Tính toán**: Viết Python script tính toán từng chỉ số đã được confirm
5. **So sánh**: Nếu có target/ngưỡng → tự động đánh dấu chỉ số nào đạt/cảnh báo

**Lưu ý**: Nếu file đầu vào có sheet HUONG_DAN chứa công thức riêng → ƯU TIÊN dùng công thức trong file, bỏ qua catalog mặc định.

---

v1.0 (2026-05-19) — Mở rộng từ 4 phòng ban lên 7 domains, chuẩn hóa theo tiếng Việt
