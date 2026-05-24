# DANH SÁCH QUY TRÌNH (WORKFLOWS)
*Tài liệu dành cho Học viên / Quản lý cấp trung (BOM)*

Dưới đây là danh sách các "Quy trình tự động" đã được lập trình sẵn. Để kích hoạt một quy trình, Anh/Chị chỉ cần gõ cú pháp có dấu gạch chéo `/` ở đầu vào khung chat.

## 1. Quy Trình Nghiệp Vụ (Hỗ trợ công việc)

| Lệnh Kích Hoạt | Chức Năng Của Quy Trình |
|----------------|-------------------------|
| `/w-khoi-tao-du-an-moi` | Tạo mới một dự án (tự động tạo cấu trúc thư mục, biểu mẫu). |
| `/w-phan-tich-nhiem-vu` | Rã một yêu cầu lớn thành các đầu việc nhỏ và lập kế hoạch thực hiện. |
| `/w-phan-tich-va-bao-cao` | Xử lý dữ liệu và tự động làm báo cáo (Tiến độ dự án, Báo cáo Tuần, Tháng, BI). |
| `/w-quan-tri-du-an` | Lập kế hoạch quản trị dự án toàn diện (Phân công RACI, Timeline). |
| `/w-san-xuat-tai-lieu` | Sản xuất và chuẩn hóa tài liệu doanh nghiệp (SOP, Báo cáo, Đề xuất). |
| `/w-xay-dung-quy-trinh` | Xây dựng quy trình làm việc mới hoặc chuẩn hóa quy trình hiện tại thành SOP. |
| `/w-00-tao-landing-page-theo-angle` | Biến content angle thành landing page HTML hoàn chỉnh (có kiểm claim, message match, HTML QA và GitHub handoff). |

## 2. Quy Trình Vận Hành Cơ Bản

| Lệnh Kích Hoạt | Chức Năng Của Quy Trình |
|----------------|-------------------------|
| `/w-onboarding-tour` | Tour khám phá workspace do Agent Quản Gia dẫn dắt từ A-Z cho người mới (35-45 phút). Agent làm hết, user quan sát. |
| `/w-khoi-dong-phien` | Khởi động phiên làm việc mới (Agent sẽ tải lại trí nhớ dự án). |
| `/w-dong-phien` | Đóng phiên làm việc (Agent sẽ tự động đúc rút bài học và lưu lại). |
| `/w-luu-phien` | Chụp lại tiến độ phiên làm việc hiện tại để không mất dữ liệu. |
| `/w-tro-giup` | Hiển thị danh mục tính năng và hướng dẫn giải đáp thắc mắc. |
| `/w-ve-sinh-workspace` | Dọn dẹp các tệp tin, lưu trữ các dự án cũ và sắp xếp lại không gian làm việc. |
| `/w-kiem-tra-suc-khoe` | Kiểm tra nhanh xem cấu trúc thư mục và Agent có đang hoạt động tốt hay không. |

## 3. Quy Trình Chuyên Sâu (Dành cho Quản trị viên)

| Lệnh Kích Hoạt | Chức Năng Của Quy Trình | Trùng Skill? |
|----------------|-------------------------|--------------|
| `/w-kiem-dinh-workspace` | Đánh giá chuyên sâu về chất lượng, mức độ tuân thủ của toàn bộ Workspace. | ⚠️ Trùng: `kiem-dinh-workspace` |
| `/w-audit-va-toi-uu-luong-cong-viec` | Quét kiểm tra và tự động sửa các lỗi liên quan đến Luồng công việc. | — |
| `/w-tao-ky-nang-moi` | Dạy cho Agent một kỹ năng (Skill) hoàn toàn mới. | ⚠️ Trùng: `tao-ky-nang-moi` |
| `/w-tao-quy-trinh-moi` | Xây dựng workflow mới theo chuẩn V9. | ⚠️ Trùng: `tao-quy-trinh-moi` |
| `/w-toi-uu-workspace` | Tối ưu và tự sửa workspace sau khi audit. | ⚠️ Trùng: `toi-uu-workspace` |

> [!WARNING]
> **Quy tắc Chống Trùng Tên:** Khi tạo Workflow mới, BẮT BUỘC kiểm tra xem tên có trùng với Skill nào trong `DANH-SACH-KY-NANG.md` không. Nếu trùng, phải đổi tên một trong hai hoặc được Operator phê duyệt ngoại lệ.
