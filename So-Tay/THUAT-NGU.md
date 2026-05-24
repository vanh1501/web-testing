# Thuật Ngữ Workspace

Bảng thuật ngữ chuẩn dùng xuyên suốt workspace. Agent + operator tham chiếu tệp này khi cần dùng đúng tên gọi và convention. Lifecycle: append-only, không xóa entry cũ.

## Thuật ngữ cốt lõi

| Thuật ngữ | Ý nghĩa | Ngữ cảnh sử dụng |
|-----------|---------|-------------------|
| Workspace | Toàn bộ thư mục baseline + module nghiệp vụ | Cấp tổng |
| Agent | Tác tử AI (Gemini hoặc Claude) thực thi yêu cầu | Khi nói về thực thi |
| Operator | Người vận hành workspace — quản lý cấp trung phi kỹ thuật | Khi nói về người dùng |
| Owner | MindX Operations Team — quản trị viên hệ thống | Khi nói về quản trị |
| Builder | Người cài module nghiệp vụ lên trên baseline | Khi mở rộng workspace |
| Skill | Năng lực agent tự kích hoạt khi description match request | Trong .agents/skills/ |
| Rule | Ràng buộc agent PHẢI tuân thủ — guardrail | Trong .agents/quan-ly-quy-tac/ |
| Workflow | Chuỗi bước có cấu trúc operator gọi qua slash command | Trong .agents/workflows/ |
| Index | Tệp tổng hợp metadata + đường dẫn (12 tệp trong Bang-Dieu-Khien/) | Khi nói về dashboard |
| Artifact | Tệp output do agent sinh ra (báo cáo, slide, phân tích) | Trong Kho-Du-Lieu/Ket-Qua/ |

## Trạng thái chuẩn

| Đối tượng | Trạng thái cho phép |
|-----------|---------------------|
| Dự án | `Đang làm` / `Tạm dừng` / `Đã xong` |
| Task | `Đang làm` / `Chờ` / `Đã xong` |
| Skill/Rule/Workflow | `Hoạt động` / `Tắt` |
| Sức khỏe workspace | `Tốt` / `Cần kiểm tra` / `Có vấn đề` |
| Audit finding | `Critical` / `Medium` / `Low` |

## Cách cập nhật tệp này

- Khi xuất hiện thuật ngữ mới trong workspace → thêm entry vào bảng phù hợp
- Khi thuật ngữ thay đổi ý nghĩa → cập nhật, ghi chú phiên bản cũ trong cột "Ngữ cảnh"
- Agent tham chiếu tệp này khi cần dùng đúng tên gọi và trạng thái
