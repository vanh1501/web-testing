# Thuật Toán Phân Rã Công Việc (WBS Breakdown Framework)

Tài liệu này cung cấp bộ khung tiêu chuẩn để Kỹ sư Giải pháp (`phan-tich-yeu-cau`) rã một yêu cầu thô từ Operator (BOM/Key person) thành một kế hoạch thi công khoa học, đặc biệt chú trọng tích hợp quy trình **Lean Research**.

## 1. Cơ Chế Bóc Tách 3 Chiều
Khi nhận bất cứ yêu cầu nào, hãy cắt lớp nó thành 3 chiều:
1. **Goal (Mục tiêu cốt lõi):** Tại sao lại cần làm việc này? Nó giải quyết bài toán kinh doanh nào?
2. **Constraints (Ràng buộc):** Thời hạn (Deadline)? Yêu cầu định dạng (File Excel hay Slide)?
3. **Data/Input (Nguyên liệu đầu vào):** Chúng ta đang có gì trong tay? Cần tìm thêm gì?

## 2. Tiêm Tư Duy "Lean Research" vào Phân Rã Task
Nếu yêu cầu của BOM/BOD mang tính chất **"nghiên cứu thị trường", "tìm hiểu giải pháp", "phân tích đối thủ"**, BẮT BUỘC KHÔNG ĐƯỢC sinh ra một task "Nghiên cứu" chung chung kéo dài lê thê. Áp dụng cơ chế chia nhỏ:

- **Pulse 1 (Quick Scan):** Giao cho `nghien-cuu-thi-truong` làm một Quick Brief (300-500 từ) trong 1 tiếng để nắm tổng quan.
- **Pulse 2 (Deep Dive - có chọn lọc):** Từ kết quả Pulse 1, Kỹ sư Giải pháp hội ý với Operator xem cần đào sâu phần nào. Chỉ giao task đào sâu vào phần tạo ra giá trị (Value-Added).
- **Pulse 3 (Actionable Output):** Giao cho `tao-tai-lieu` hoặc `phan-tich-du-lieu` để đóng gói kết quả nghiên cứu thành Báo cáo quyết định (Go/No-Go, So sánh Options).

## 3. Cây Phân Rã Mẫu (Archetype Trees)

### Archetype A: Yêu Cầu Sản Xuất Báo Cáo Định Kỳ
1. `phan-tich-du-lieu`: Rút trích số liệu, tính toán MoM, YoY.
2. `tao-tai-lieu`: Đắp văn phong, vẽ biểu đồ Mermaid/Slide outline.

### Archetype B: Yêu Cầu Tìm Kiếm Insight / Giải Pháp
1. `nghien-cuu-thi-truong`: Thu thập thông tin, dùng Fact-Check/Benchmark pattern (được định nghĩa trong skill `nghien-cuu-thi-truong`).
2. `tu-duy-chien-luoc`: Dùng framework 5 bước để brainstorm các góc nhìn từ data vừa tìm.
3. `tao-tai-lieu`: Đóng gói thành Executive Summary trình BOD.

## 4. Bàn Giao (Routing Matrix)
Tuyệt đối không chế ra skill mới. Chỉ được gán Sub-task cho các skill hiện có trong `DANH-SACH-KY-NANG.md`. Nếu thiếu, đánh dấu `UNKNOWN_SKILL` và báo cáo lại Operator.
