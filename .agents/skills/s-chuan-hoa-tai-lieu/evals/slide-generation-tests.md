---
file: .agents/skills/s-chuan-hoa-tai-lieu/evals/slide-generation-tests.md
purpose: Kịch bản kiểm thử chất lượng slide đầu ra cho QA Agent và Operator chạy kiểm định định kỳ.
trigger: Khi cần chạy đánh giá chất lượng (QA scoring) cho slide đầu ra.
---

# 6 Kịch Bản Kiểm Thử Chất Lượng Slide (Sanity Check & Edge Cases)

Tài liệu này dùng làm Ground Truth cho QA Agent hoặc Operator chạy kiểm định định kỳ chất lượng slide đầu ra do AI sinh.

---

### SCENARIO 1: Happy Path - Cấu trúc Chuẩn 3 Module B2B
*   **Đầu vào:** Văn bản Outline đào tạo dài 1500 từ về "Kỹ năng Lãnh đạo".
*   **Tiêu chuẩn Đầu ra Kiểm tra:**
    *   [ ] Slide 1: Bìa có tag `<!-- _class: slide-cover -->`.
    *   [ ] Đủ 3 Slide chuyển phần (Divider) dạng `<!-- _class: slide-divider -->`.
    *   [ ] Tổng số slide dao động từ 15 đến 20 slide.
    *   [ ] 100% slide chứa HTML comment `<!-- _speaker_notes: ... -->` có độ dài tối thiểu 50 ký tự mỗi slide.

---

### SCENARIO 2: Phân Rã & Chunking Khối Dữ Liệu Béo Phì (Bloat Text)
*   **Đầu vào:** Một trang Word chứa 800 từ giải thích dông dài về cấu trúc mạng.
*   **Tiêu chuẩn Đầu ra Kiểm tra:**
    *   [ ] AI không nhồi nhét toàn bộ 800 từ vào 1 slide.
    *   [ ] Tự động chia nhỏ thành chuỗi 3 slide liên tiếp có tiêu đề nối tiếp (vd: "Cơ Chế Định Tuyến Mạng (1/3)", "Cơ Chế Định Tuyến Mạng (2/3)...").
    *   [ ] Mật độ chữ trên mỗi slide không vượt quá 8 dòng text hoặc 120 từ.

---

### SCENARIO 3: Định dạng Markdown Phức tạp (Tables & Lists Lồng nhau)
*   **Đầu vào:** Bảng đối chiếu năng lực vận hành gồm 4 cột x 6 dòng kèm các gạch đầu dòng chi tiết bên trong ô.
*   **Tiêu chuẩn Đầu ra Kiểm tra:**
    *   [ ] Trích xuất bảng giữ nguyên cấu trúc Markdown table (`|---|---|`).
    *   [ ] Gộp các bullet trong ô thành thẻ `<br>` để tránh làm vỡ định dạng cột của Marp.
    *   [ ] Gán nhãn `<!-- _layout_cue: Gamma - Comparison Table Layout -->`.

---

### SCENARIO 4: Lọc Nhiễu Học Thuật (Academic Noise Cleanse)
*   **Đầu vào:** File giáo trình đại học có Header lặp đi lặp lại "Chương 2: Thiết kế hệ thống mạng máy tính - IRJAEM e ISSN: 2584-2854".
*   **Tiêu chuẩn Đầu ra Kiểm tra:**
    *   [ ] 100% rác header/footer bị loại bỏ.
    *   [ ] Không xuất hiện cụm từ "IRJAEM" hay "ISSN" trên bất kỳ slide nào.
    *   [ ] Tên trường Đại học/Tác giả gốc (nếu không được yêu cầu) bị lược bỏ sạch khỏi header/footer của slide B2B.

---

### SCENARIO 5: Kiểm soát Trôi Lệch Bố Cục (Visual Layout Shift)
*   **Đầu vào:** Outline bài học chứa 5 mục nhưng mỗi mục chỉ có 1 dòng cụt ngủn.
*   **Tiêu chuẩn Đầu ra Kiểm tra:**
    *   [ ] AI không sử dụng Split Layout 50/50 vì ảnh sẽ chiếm dụng quá lớn gây mất cân đối.
    *   [ ] Sử dụng `3-Column Cards` hoặc `Vertical Timeline` để kéo dãn không gian hiển thị theo chiều ngang/dọc một cách hài hòa.
    *   [ ] Khoảng cách lề (padding) và cỡ chữ giữ đúng cấu hình CSS của `mindx-theme`.

---

### SCENARIO 6: Bảo Vệ Ranh Giới Speaker Notes & Slide Body
*   **Đầu vào:** Tài liệu giảng viên có ghi chú lẫn lộn "Lưu ý ở đây giảng viên phải chiếu video rồi nói..." nằm chung dòng với bài giảng.
*   **Tiêu chuẩn Đầu ra Kiểm tra:**
    *   [ ] Tách biệt hoàn toàn phần hướng dẫn giảng dạy của giảng viên vào khối `_speaker_notes`.
    *   [ ] Phần text hiển thị trên slide chỉ giữ lại kiến thức cốt lõi cho học viên nhìn.
    *   [ ] Thẻ comment đóng mở đúng quy chuẩn `<!-- _speaker_notes: [Nội dung] -->` và không để lộ thẻ thô ra màn hình trình chiếu.
