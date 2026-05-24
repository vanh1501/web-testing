# Mẫu: Bảng KPI

## 1. Mục đích
Mẫu này dùng để chuẩn hóa bảng KPI đầu ra sau khi tính toán, giúp người đọc thấy ngay chỉ số nào đạt, lệch hoặc cần xử lý.

## 2. Khi nào dùng
- Sau bước tính KPI.
- Trước khi viết báo cáo Pyramid.
- Khi cần đối chiếu số liệu giữa các kỳ.

## 3. Cấu trúc bảng
| Metric ID | Tên KPI | Công thức | Kỳ hiện tại | Kỳ trước | Target | Chênh lệch | Trạng thái | Cảnh báo |
|---|---|---|---:|---:|---:|---:|---|---|
| KPI-001 | ROAS | revenue / spend | 3.45x | 4.20x | 4.00x | -18% | Không đạt | Facebook Ads giảm mạnh |

## 4. Quy tắc điền
- Mỗi KPI phải có công thức rõ.
- Nếu KPI là tỷ lệ, phải kiểm tra mẫu số khác 0.
- Không thay đổi công thức KPI nếu chưa có BOM xác nhận.
- Nếu target chưa có, ghi “chưa có target” thay vì tự bịa. Nhân loại đã đủ khổ vì những con số tự tin vô căn cứ.

## 5. Checklist kiểm tra
- [ ] Mỗi KPI có công thức.
- [ ] Có kỳ hiện tại, kỳ trước và target nếu có.
- [ ] Có trạng thái đạt/chưa đạt/cần xem lại.
- [ ] Có cảnh báo với KPI bất thường.
- [ ] Không dùng dữ liệu cá nhân nếu không cần thiết.
