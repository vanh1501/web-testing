---
title: "Master Index — Agent Routing Guide"
domain_tags: ["index", "routing", "kb"]
summary: "Tệp định tuyến hệ thống bắt buộc của Antigravity Agent. Chứa con trỏ dẫn hướng đến các khu vực lưu trữ thực tế."
keywords: ["index", "routing", "knowledge-base"]
applicable_agents: ["ALL"]
last_updated: "2026-05-19"
version: "2.0.0"
---

# MASTER-INDEX — Bộ Định Tuyến Bắt Buộc

> **SYSTEM RULE**: Đây là tệp CẤU HÌNH ĐỊNH TUYẾN MẶC ĐỊNH được nhúng sâu vào Lõi của Antigravity Agent (Global Rule). 
> Agent bắt buộc phải đọc tệp này trước mỗi Task để biết cách tìm kiếm thông tin trong Workspace.

## 1. Định Tuyến Quản Trị & Vận Hành (Dashboard)
Toàn bộ danh sách dự án, quy tắc, kỹ năng và quy trình không nằm ở đây. Agent BẮT BUỘC phải trỏ về thư mục `Bang-Dieu-Khien/` để truy xuất:
- `Bang-Dieu-Khien/BANG-DIEU-KHIEN.md`: Tổng quan trạng thái sức khỏe hệ thống.
- `Bang-Dieu-Khien/DANH-SACH-KY-NANG.md`: Danh sách các kỹ năng (Skills) của Agent.
- `Bang-Dieu-Khien/DANH-SACH-QUY-TRINH.md`: Danh sách luồng quy trình (Workflows) tự động.
- `Bang-Dieu-Khien/DANH-SACH-QUY-TAC.md`: Danh sách các nguyên tắc vận hành (Rules).

## 2. Định Tuyến Tri Thức & Bối Cảnh (Knowledge Base)
Toàn bộ thông tin về Bối cảnh dự án, Chân dung người dùng (Persona) và Thuật ngữ không nằm ở đây. Agent BẮT BUỘC trỏ về thư mục `So-Tay/` để truy xuất:
- `So-Tay/BO-NHAN-DIEN.md`: Chân dung, vai trò và phạm vi dự án (Thay thế cho tệp `PROJECT.md` và `SCOPE.md` cũ).
- `So-Tay/THUAT-NGU.md`: Từ điển thuật ngữ kinh doanh (Thay thế cho `GLOSSARY.md` cũ).
- `So-Tay/SO-TAY-QUYET-DINH.md`: Sổ cái lưu trữ các quyết định thiết kế và bài học kinh nghiệm.
- `So-Tay/Tri-Thuc-Chuyen-Mon/`: Chứa các tài liệu học thuật chuyên sâu từng ngành (Nghiên cứu thị trường, Quản trị dự án, Phân tích dữ liệu).

## 3. Khu Vực Metadata Kỹ Thuật (System Context)
Thư mục `.context/` hiện tại chỉ chứa các tệp hệ thống vô hình đối với người dùng cuối:
- `allowed-zones.json`: Bộ giới hạn thư mục gốc dùng cho công tác kiểm định (Audit) của hệ thống MAS.
- `templates/`: Kho chứa các biểu mẫu thô (.md, .docx) để AI sinh tài liệu đầu ra.
- `standards/`: Tiêu chuẩn kỹ thuật định dạng đầu ra (Chỉ dùng nội bộ cho Agent W03 - Sinh tài liệu).

> **Lưu ý cuối cùng:** Không lưu trữ dữ liệu kinh doanh tại thư mục `.context/`. Toàn bộ dữ liệu sinh ra phải đưa vào `So-Tay/` hoặc `Du-An/`.
