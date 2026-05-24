# Chính Sách Vận Hành — Baseline Workspace AWF

Cập nhật lần cuối: 2026-05-01

---

## 1. Quy tắc đặt tên

### Thư mục
- Thư mục hệ thống: tiếng Việt, viết hoa chữ cái đầu, nối gạch (`Bang-Dieu-Khien/`, `Kho-Du-Lieu/`)
- Thư mục dự án: viết thường, nối gạch (`du-an-marketing-q2/`, `phan-tich-doanh-thu/`)
- Thư mục task trong dự án: viết thường, nối gạch (`lam-sach-du-lieu/`, `bao-cao-tong-hop/`)

### Tệp
- Tệp index và dashboard: VIẾT HOA toàn bộ (`BANG-DIEU-KHIEN.md`, `DANH-SACH-DU-AN.md`)
- Tệp project metadata: VIẾT HOA (`MO-DAU.md`, `TIEN-DO.md`, `LICH-SU.md`)
- Tệp artifact đầu ra: viết thường, có timestamp nếu cần version (`bao-cao-q2-2026-04-30.md`)

### Instruction layer (`.agents/`)
- Skill folder: kebab-case, lowercase (`workspace-orchestrator/`, `data-analyst/`)
- Rule file: kebab-case + `.md` (`r05-sync-index.md`)
- Workflow file: kebab-case + `.md` (`bao-cao-tuan.md`, `kiem-tra-suc-khoe.md`)

Chi tiết đầy đủ: `.agents/skills/file-organizer/resources/naming-convention.md`

## 2. Quy ước trạng thái

| Trạng thái | Ý nghĩa | Dùng ở đâu |
|------------|---------|------------|
| Đang làm | Task/dự án đang được xử lý | TIEN-DO.md, DANH-SACH-DU-AN.md |
| Chờ | Task đang chờ input hoặc review từ operator | TIEN-DO.md |
| Tạm dừng | Dự án bị tạm ngưng, có thể tiếp tục sau | DANH-SACH-DU-AN.md |
| Đã xong | Task/dự án hoàn thành | TIEN-DO.md, DANH-SACH-DU-AN.md |
| Hoạt động | Skill/rule/workflow đang được kích hoạt | DANH-SACH-KY-NANG/QUY-TAC/QUY-TRINH.md |
| Tắt | Skill/rule/workflow tạm ngưng | DANH-SACH-KY-NANG/QUY-TAC/QUY-TRINH.md |

## 3. Quy trình review

### Artifact đầu ra
- Agent sinh artifact → operator review → chấp nhận hoặc yêu cầu chỉnh
- Agent KHÔNG tự đánh dấu "Đã xong" — chỉ operator có quyền xác nhận hoàn thành

### Thay đổi instruction (skill/rule/workflow)
- Mọi thay đổi PHẢI ghi vào `Quan-Tri/LICH-SU-THAY-DOI.md`
- Thay đổi quan trọng PHẢI ghi lý do vào `So-Tay/SO-TAY-QUYET-DINH.md`
- Operator review + chấp nhận trước khi agent áp dụng

## 4. Chu kỳ audit

- **Hàng tháng (khuyến nghị):** Chạy `/kiem-tra-suc-khoe` — quét index lệch, artifact mồ côi, skill không dùng
- **Khi có vấn đề:** Operator gọi audit bất kỳ lúc nào
- **Kết quả audit:** Lưu `Quan-Tri/AUDIT/{YYYY-MM-DD}.md`
- **Findings phân loại:** Critical (chặn vận hành) / Medium (giảm hiệu quả) / Low (nice-to-have)

## 5. Quy tắc dữ liệu

### Dữ liệu đầu vào (`Kho-Du-Lieu/Du-Lieu-Vao/`)
- Chỉ đọc — agent KHÔNG sửa file gốc operator cung cấp
- Nếu cần làm sạch → tạo bản copy trong thư mục task tương ứng

### Dữ liệu đầu ra (`Kho-Du-Lieu/Ket-Qua/`)
- Ghi đè: KHÔNG — nếu cần version mới, thêm timestamp vào tên file
- Xóa: CHỈ khi operator yêu cầu rõ ràng

### Single source of truth
- Mỗi thông tin chỉ ghi 1 nơi gốc
- Index trong `Bang-Dieu-Khien/` chỉ trỏ về nơi gốc (đường dẫn + metadata tóm tắt)
- KHÔNG duplicate nội dung giữa các hệ thống

## 6. Phân quyền

| Vai trò | Quyền | Ví dụ |
|---------|-------|-------|
| Builder (AWF team) | Thiết lập workspace, tạo lớp meta, thay đổi kiến trúc gốc | Cài đặt ban đầu, sửa GEMINI.md |
| Operator | Vận hành nghiệp vụ, tùy chỉnh qua lớp meta, quản trị artifact | Giao task, review output, gọi audit |
| Agent | Thực thi theo instruction, cập nhật index, ghi log | Chạy skill, sinh báo cáo, cập nhật TIEN-DO.md |

## 7. Lifecycle skill/rule/workflow

- **Provisioning:** Mọi component ghi rõ author + ngày tạo, semver mặc định v1.0
- **Monitoring:** Báo cáo tuần `/bao-cao-tuan` tổng hợp metrics sử dụng
- **Audit:** `/kiem-tra-suc-khoe` chạy hàng tháng
- **Decommissioning:** Component không dùng 90 ngày → cảnh báo, operator quyết định giữ/archive/xóa
