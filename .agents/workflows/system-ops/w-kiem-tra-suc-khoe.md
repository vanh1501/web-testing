---
description: Phát hiện drift sớm, quét sâu 5-Zone và dọn dẹp hệ thống vận hành tự động.
semantic_triggers: ['kiểm tra sức khỏe', 'khám sức khỏe', 'check health', 'audit system', 'dọn rác hệ thống', 'khám định kỳ']
---

- **👤 Owner:** `[@GOV-W03]`
- **🛠 Skill Target:** `[01-dong-bo-muc-luc, 01-kiem-dinh-chat-luong]`

# Quy Trình: /w-kiem-tra-suc-khoe

## Mục đích

Phát hiện drift sớm. Kích hoạt cỗ máy Hút Bụi & Chẩn Đoán (Auto-Sweep) để quét sâu 5-Zone và dọn dẹp hệ thống vận hành tự động.

## Dấu hiệu kích hoạt

- Operator gọi thủ công định kỳ (`/w-kiem-tra-suc-khoe`).
- Cảm thấy Bảng điều khiển bị outdate hoặc nhiều file rác.

## Điều kiện tiên quyết

- [ ] Workspace đã init (Có đủ 5-Zone).
- [ ] Quan-Tri/AUDIT/ tồn tại.
- [ ] BẮT BUỘC Agent phải nạp 2 kỹ năng: `01-dong-bo-muc-luc` và `01-kiem-dinh-chat-luong`.

## Các bước thực hiện (Auto-Sweep Pipeline)

> [!CAUTION] MANDATORY TOOL USAGE
> LLM (Agent) BẮT BUỘC phải dùng công cụ `list_dir` để quét thực tế các ổ đĩa trước khi đưa ra chẩn đoán. Không được phỏng đoán.

### Bước 1: Quét Lõi Hệ Thống (Zone 1 & Zone 2)
1. Quét thực tế `.agents/skills/`, `.agents/workflows/`, và `.agents/quan-ly-quy-tac/`.
2. Kích hoạt thẳng kỹ năng `01-dong-bo-muc-luc` để tự động nắn lại các đường dẫn gãy trong `Bang-Dieu-Khien/` (Không cần hỏi Operator).

### Bước 1.5: Tuần tra Ranh giới Không gian (Root & Sandbox Hygiene)
1. Quét thư mục gốc (Root directory). Bất kỳ tệp nào không thuộc cấu trúc 5-Zone chuẩn (ví dụ: các file .py, .txt bị lạc trôi ngoài Root) sẽ bị liệt kê vào Danh sách Rác.
2. Quét thư mục Sandbox `tmp/`. Xác nhận và dọn dẹp các tệp script tạm thời (.py, .ps1, .sh, .txt) được Agent tạo ra để giải quyết công việc.

### Bước 2: Dò Tìm Rác Dữ Liệu (Zone 3 & Zone 4)
1. Quét `Kho-Du-Lieu/Ket-Qua/`. Bất kỳ tệp nào không có thông tin gán mác dự án (Orphaned Artifacts) sẽ bị liệt kê vào Danh sách Rác.
2. Quét `Du-An/`. Tìm các dự án không có cập nhật trong 30 ngày (Dự án chết yểu) hoặc thiếu `TIEN-DO.md`.

### Bước 3: Tổng Hợp & Đề Xuất Dọn Dẹp (1-Click Clean)
Agent sinh báo cáo nhanh (Summary) cho Operator với định dạng:
```
Tôi đã quét xong hệ thống. Phát hiện:
- Đã tự động đồng bộ X mục trong Bảng Điều Khiển.
- Có W file lạ nằm lạc trôi ngoài Root và Sandbox `tmp/`.
- Có Y file rác trong Kho Dữ Liệu.
- Có Z dự án chết yểu cần đưa vào lưu trữ (Archive).

Anh/Chị gõ `OK` để tôi tự động xóa rác và Archive các dự án này nhé!
```

### Bước 4: Thực Thi Auto-Clean (Sau khi có lệnh OK)
1. Nếu Operator gõ `OK`, Agent sử dụng công cụ quản lý file để tự động xóa rác.
2. Di chuyển các dự án chết yểu vào `Du-An/_archive/`.
3. Sinh báo cáo Final Audit vào `Quan-Tri/AUDIT/{YYYY-MM-DD}.md`.

## Tiêu chuẩn nghiệm thu

- [ ] Báo cáo audit được tạo với trạng thái đã Clean.
- [ ] Bảng Điều Khiển khớp 100% với thực tế vật lý.

## Xử lý ngoại lệ

- Phát hiện file lớn bất thường (>50MB): Phải báo cáo riêng và không tự xóa dù có lệnh OK.
- Workspace sức khỏe tốt (không có vấn đề): Vẫn sinh báo cáo 'Workspace khỏe mạnh' — không skip.

## Tham chiếu KB nguồn

- kb-workspace-baseline.md Phần 2 (A - Quản trị)
