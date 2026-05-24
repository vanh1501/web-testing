---
description: Dọn dẹp và lưu trữ (archive) các dự án không cập nhật quá 30 ngày để chống phình hệ thống.
semantic_triggers: ['vệ sinh workspace', 've sinh workspace', 'dọn dẹp', 'cleanup']
---

- **👤 Owner:** `[@Cố vấn AI MindX]`
- **🛠 Skill Target:** `[TBD]`

# Quy Trình: /w-ve-sinh-workspace

## Mục đích

Thực thi quy tắc 7. Chống workspace phình ra không kiểm soát.

## Dấu hiệu kích hoạt

Operator gọi thủ công hàng tháng HOẶC tự động ngày 1 đầu tháng

## Điều kiện tiên quyết

- [ ] Du-An/_archive/ tồn tại

## Các bước thực hiện

1. Quét toàn bộ Du-An/. Tìm dự án TIEN-DO.md không cập nhật quá 30 ngày
2. Lập danh sách dự án đề xuất lưu trữ → hỏi operator duyệt
3. Move dự án đã duyệt vào Du-An/_archive/{YYYY-MM}/
4. Cập nhật DANH-SACH-DU-AN.md
5. Ghi changelog vào LICH-SU-THAY-DOI.md

## Tiêu chuẩn nghiệm thu

- [ ] Dự án archive có trong Du-An/_archive/
- [ ] DANH-SACH-DU-AN cập nhật
- [ ] Changelog ghi

Nếu fail bất kỳ → rollback hoặc báo operator.

## Kết quả đầu ra

- Folder Du-An/_archive/{YYYY-MM}/ với dự án move vào
- Log changelog

## Xử lý ngoại lệ

- File 'rác' thực ra là file operator đang dùng ngầm: Liệt kê danh sách + xác nhận từng file trước khi xóa — không xóa batch.
- Workspace có file tạm từ agent bị crash: Xóa file tạm tự động (không cần confirm) nhưng ghi log.
- Operator muốn vệ sinh toàn bộ ngay lập tức: Tạo backup snapshot trước khi xóa — nếu không backup được thì hỏi confirm lần nữa.

## Tham chiếu KB nguồn

- kb-workspace-baseline.md Phần 2 (A - Quản trị)
