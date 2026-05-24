# Mẫu 2 — Bảng đánh giá cơ hội cải tiến theo ESOAR

Version: v1.1  
Trạng thái: Bản nháp  
Quy trình: [Tên quy trình]

## 1. Phân loại từng bước

| Bước | Vấn đề hiện tại | Nhóm ESOAR | Lý do phân loại | Kiểm tra nguyên tắc bắt buộc |
|---:|---|---|---|---|
| 1 | | E/S/O/A/R | | |

Gợi ý điền nhóm ESOAR:

- E: Bỏ bớt.
- S: Chuẩn hóa.
- O: Tối ưu.
- A: Tự động hóa.
- R: Thiết kế lại.

## 2. Tóm tắt tỷ lệ

| Nhóm | Số bước | Tỷ lệ |
|---|---:|---:|
| E - Bỏ bớt | | |
| S - Chuẩn hóa | | |
| O - Tối ưu | | |
| A - Tự động hóa | | |
| R - Thiết kế lại | | |
| E + S + O | | |

## 3. Kiểm tra nguyên tắc bắt buộc

- Quy tắc 60/40: [ĐẠT / CẢNH BÁO / TẠM DỪNG]
- Chuẩn hóa trước khi tự động hóa: [ĐẠT / CẢNH BÁO / TẠM DỪNG]
- Thiết kế lại quá nhiều bước: [ĐẠT / CẢNH BÁO / TẠM DỪNG]

## 4. Ngoại lệ, nếu có

```yaml
meta.exception:
  rule: ""
  rationale: ""
  signoff_required: true
  signoff_owner: ""
```

## Checklist kiểm tra

- [ ] Không có bước tự động hóa khi đầu vào/đầu ra chưa rõ.
- [ ] Bước tự động hóa đã được chuẩn hóa trước.
- [ ] Nếu E+S+O dưới 60%, có lý do ngoại lệ.
- [ ] Nếu thiết kế lại quá 20% số bước, có người phê duyệt.
