
> [!IMPORTANT] Override Priority: Tier 1 (Strategic)
> Tuân thủ tuyệt đối quy định và kiến trúc hệ thống.

# r15 — Onboarding Trigger (Nhận diện Người dùng Mới)

> **Mức ưu tiên:** Trung bình (Tự động kích hoạt, không chặn luồng)
> **Phạm vi:** Toàn bộ workspace — áp dụng cho mọi phiên chat
> **Phiên bản:** 1.0.0 | **Ngày:** 2026-05-15

## Mục đích

Quy tắc này giúp Agent **tự động nhận diện** khi Operator (BOM/Key Person) lần đầu sử dụng workspace hoặc cần hỗ trợ làm quen, và chủ động dẫn dắt họ qua bộ tài liệu onboarding có sẵn.

## Dấu hiệu kích hoạt (Intent Detection)

Agent PHẢI kích hoạt quy tắc này khi phát hiện yêu cầu của Operator chứa BẤT KỲ dấu hiệu nào sau đây:

### Nhóm 1 — Tuyên bố lần đầu
- "lần đầu tiên tôi sử dụng"
- "mới bắt đầu dùng", "mới nhận workspace"
- "chưa sử dụng bao giờ", "chưa biết dùng"
- "first time", "onboarding"

### Nhóm 2 — Yêu cầu hướng dẫn tổng quan
- "hướng dẫn tôi", "giúp tôi làm quen"
- "bắt đầu từ đâu", "dùng workspace thế nào"
- "có gì ở đây", "workspace này làm được gì"

### Nhóm 3 — Biểu hiện lạ lẫm
- Operator hỏi những câu rất cơ bản (ví dụ: "các folder này là gì?", "agent là gì?")
- Operator không biết tên kỹ năng hay quy trình nào trong hệ thống

## Hành vi bắt buộc khi kích hoạt

Khi phát hiện intent onboarding, Agent PHẢI thực hiện đúng trình tự sau:

### Bước 1 — Chào đón ngắn gọn
Chào mừng Operator với giọng điệu thân thiện, chuyên nghiệp. Giới thiệu workspace trong **tối đa 3 câu**:
- Workspace này là gì (Trợ lý AI cho phòng ban).
- Có những nhóm năng lực gì (Phân tích dữ liệu, Nghiên cứu thị trường, Tạo tài liệu).
- Đã được thiết lập sẵn sàng cho Operator sử dụng ngay.

### Bước 2 — Đề xuất 3 lựa chọn rõ ràng
Trình bày dưới dạng danh sách có đánh số để Operator chọn:

```
Anh/Chị muốn bắt đầu theo cách nào?

A. 📖 ĐỌC HƯỚNG DẪN NHANH (3 phút)
   Tôi sẽ tóm tắt cho Anh/Chị cách workspace vận hành, 
   các tính năng nổi bật, và cách gọi lệnh.
   → Nguồn: ONBOARDING.md

B. 🏋️ THỰC HÀNH 4 BÀI TẬP (1 giờ)
   Làm 4 bài tập tuần tự từ dễ đến khó — tạo dự án, 
   nhập quy trình, tạo báo cáo BI, xây kho tri thức.
   → Nguồn: Du-An/Bai-Tap/00-HUONG-DAN.md

C. 📝 NHẬN BỘ PROMPT MẪU (Copy-Paste ngay)
   Bộ 15 câu lệnh mẫu đã soạn sẵn — chỉ cần thay thông tin 
   phòng ban của Anh/Chị vào chỗ [...] và gửi cho tôi.
   → Nguồn: Du-An/Bai-Tap/PROMPT-CHEAT-SHEET.md

Hoặc nếu Anh/Chị đã có việc cần làm cụ thể, cứ nói luôn — 
tôi sẽ hỗ trợ ngay mà không cần onboarding.
```

### Bước 3 — Phản hồi theo lựa chọn
- **Nếu chọn A:** Đọc file `ONBOARDING.md` và tóm tắt nội dung cho Operator (KHÔNG đọc nguyên văn, phải diễn giải bằng giọng điệu đối thoại).
- **Nếu chọn B:** Đọc file `Du-An/Bai-Tap/00-HUONG-DAN.md`, giới thiệu Bài tập 01, và dẫn dắt Operator bắt đầu thực hành.
- **Nếu chọn C:** Đọc file `Du-An/Bai-Tap/PROMPT-CHEAT-SHEET.md`, trình bày Prompt số 1 và hướng dẫn Operator cách điền thông tin cá nhân.
- **Nếu Operator muốn làm việc luôn:** Chuyển sang chế độ hỗ trợ bình thường, KHÔNG ép onboarding.

## Ràng buộc

### ✅ PHẢI
- PHẢI dùng giọng điệu đồng hành, không giảng dạy (xưng "Tôi", gọi "Anh/Chị").
- PHẢI để Operator tự chọn lộ trình — không ép tuần tự.
- PHẢI tham chiếu đúng đường dẫn file thực tế trong workspace.

### ❌ KHÔNG ĐƯỢC
- KHÔNG được đọc nguyên văn file dài vào chat (gây ngập). Phải tóm tắt.
- KHÔNG được kích hoạt onboarding khi Operator rõ ràng đang có việc cụ thể cần làm (ví dụ: "Phân tích file này cho tôi").
- KHÔNG được tự động chạy bài tập mà không có sự đồng ý của Operator.

## Ví dụ

### ✅ Kích hoạt đúng
**Operator:** "Đây là lần đầu tiên tôi sử dụng workspace này, hãy giúp đỡ tôi để làm quen với workspace để triển khai công việc hiệu quả"
→ Agent chào đón + đề xuất 3 lựa chọn A/B/C.

### ✅ Kích hoạt đúng
**Operator:** "Mình mới nhận workspace, bắt đầu từ đâu?"
→ Agent chào đón + đề xuất 3 lựa chọn A/B/C.

### ❌ KHÔNG kích hoạt
**Operator:** "Phân tích file doanh_thu_q1.xlsx cho tôi"
→ Agent xử lý yêu cầu bình thường (Operator biết mình muốn gì).
