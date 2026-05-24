# Enterprise Analogy Mapping

Bí quyết thiết kế Hệ thống Đa Tác Nhân (MAS) chuẩn Hierarchical Swarm là *đối chiếu quy trình phần mềm với một Tập đoàn bằng xương bằng thịt*.

## Bảng Tham Chiếu Phân Khối (Sử dụng Chọn lọc, không bê nguyên xi)

| Phòng Ban Thật (Real Enterprise) | Khối Agent Ảo (Workspace Groups) | Ví dụ Đặc thù Role |
| -------------------------------- | -------------------------------- | ------------------ |
| Ban Giám Đốc / PMO / Operations | Orchestrator & Coordinator | Nhận lệnh Human, băm nhỏ Task, phân tuyến |
| Phòng Nghiên Cứu / Thu thập | Research & Intelligence | Cào dữ liệu mạng, đọc PDF rác, trích xuất SQL |
| Phòng Sản Xuất / Kỹ Thuật | Execution / Production | Viết code, sinh Content, Ráp mô hình Excel |
| Phòng Quản lý Chất Lượng (QA/QC) | QA & Review | Rà soát lỗi, đối soát số liệu, chạy Unit Test |
| Phòng Tư vấn Chiến Lược | Strategy & Advisory | Tính ROI rủi ro, cân bằng ngân sách, phác phương hướng |
| Phòng Sáng Tạo / Design | Creative & Assets Studio | Vẽ ảnh, sinh mockup UI, viết kịch bản lôi cuốn |
| Phòng Quản Trị Dữ Liệu | Data Governance & Analytics | Đoạt chuẩn schema, lau chùi DB dơ, làm báo cáo dashboard |
| Phòng Đào Tạo & Gắn kết | Knowledge Management & Training | Nạp tri thức, phân tích lỗi định kỳ, Training tân binh |

## Cấu trúc Giao Việc Chuẩn
- Thường thấy: **Coordinator (Nhận việc)** -> **Research (Lấy Base)** -> **Production (Sản Xuất)** -> **QA (Nghiệm thu)**.
- Khi QA trả `FAIL`, Production phải làm lại (1 vòng lặp con). Mọi thứ đều ném qua QUEUE (Handoffs).
