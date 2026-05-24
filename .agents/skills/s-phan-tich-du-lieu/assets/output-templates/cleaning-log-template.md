# Mẫu: Nhật ký làm sạch dữ liệu

## 1. Mục đích
Mẫu này ghi lại những gì đã phát hiện và xử lý trong dữ liệu thô trước khi tính KPI, để người duyệt biết số liệu không bị “phẫu thuật thẩm mỹ” âm thầm.

## 2. Thông tin cần điền
| Trường | Mô tả | Ví dụ |
|---|---|---|
| File đầu vào | Tên file dữ liệu gốc | raw_marketing_q1.xlsx |
| Số dòng ban đầu | Tổng số dòng trước xử lý | 12.450 |
| Số dòng sau xử lý | Tổng số dòng sau xử lý | 12.430 |
| Lỗi phát hiện | Missing, duplicate, outlier, sai định dạng | 20 dòng duplicate |
| Tự xử lý | Các chỉnh sửa an toàn | Chuẩn hóa ngày |
| Cần người duyệt | Việc cần xác nhận | Có giữ outlier spend không? |

## 3. Nội dung mẫu
```markdown
# Cleaning Log — [Tên file]

## Tóm tắt
- Rows in: ...
- Rows out: ...
- Columns: ...
- Issues found: ...
- Auto-fixes applied: ...
- Human decisions required: ...

## Chi tiết lỗi
| Cột | Loại lỗi | Số lượng | Hành động | Cần duyệt? |
|---|---|---:|---|---|
| date | Sai format | 35 | Chuẩn hóa ISO | Không |
| spend | Outlier | 3 | Flag | Có |
```

## 4. Checklist kiểm tra
- [ ] Không ghi đè file gốc.
- [ ] Có log cho mọi thay đổi.
- [ ] Outlier không bị xóa nếu chưa duyệt.
- [ ] Missing data quan trọng được cảnh báo.
