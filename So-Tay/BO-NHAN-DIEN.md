# Bộ Nhận Diện Operator

Mô tả persona operator chính của workspace này. Agent đọc tệp này để calibrate giao tiếp + đề xuất phù hợp.

## Persona chính — Quản lý cấp trung

| Thuộc tính | Giá trị |
|-----------|---------|
| Vai trò | Quản lý cấp trung hoặc senior |
| Phòng ban | Marketing / Sales / Operations / Strategy |
| Quy mô team | 5-10 người trực tiếp |
| Mức kỹ thuật | Quen ChatGPT, có thể low-code/no-code, KHÔNG đọc YAML/JSON trực tiếp |
| Tần suất dùng workspace | Vài lần/tuần |
| Đề bài điển hình | Phân tích dữ liệu HOẶC nghiên cứu HOẶC viết báo cáo |
| Đầu ra mong muốn | docx, pptx, md, xlsx |
| Chuẩn chất lượng | Ngang bản nháp một quản lý senior tự viết, sửa 10-20% là gửi được |

## Lớp JTBD

| Lớp | Job |
|-----|-----|
| Functional | Tăng tốc 5x các tác vụ phân tích + viết báo cáo lặp |
| Emotional | Bớt stress mỗi cuối tuần khi dồn báo cáo cho thứ Hai |
| Social | Được sếp + đồng nghiệp nhìn nhận là người có khả năng deliver insight nhanh và sâu |

## Pain point #1

Workspace AI dùng vài tuần thành "bãi rác" — file rời rạc, dashboard lệch, không tìm lại được output cũ. Operator mất niềm tin, quay về Excel + Word truyền thống.

→ Workspace baseline này thiết kế đặc biệt để chống pain này: lớp nền vận hành (skill orchestrator + index-syncer + file-organizer + 14 quy tắc + 9 quy trình audit) tự động giữ workspace sạch.

## Cách cập nhật tệp này

Khi onboard operator có persona khác (ví dụ: chuyên viên phân tích, trưởng phòng cấp cao) → thêm Section "Persona phụ" với cùng cấu trúc bảng + JTBD + pain. KHÔNG xóa persona chính.
