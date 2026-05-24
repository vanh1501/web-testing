# LLM Token Economy & Budgeting

Đây là chỉ nam Tài chính - Hệ thống (FinOps/TokenOps). Bác sĩ (Context Surgeon) phải nắm rõ cơ chế Giá Điện - Giá Bộ Nhớ của Lõi AI để thi hành cắt giảm.

## 1. Ngưỡng An Toàn Hệ Thống (Token Thresholds)
- **12,000 Tokens:** Ngưỡng Xanh (An toàn tuyệt đối). LLM giữ vững khả năng Reasoning, không bị ảo giác. Mọi Workspace chỉ được vận hành quanh mốc này.
- **15,000 Tokens:** Ngưỡng Vàng (Nguy cơ cận kề). Bắt đầu suy giảm Context Window attention (mất khả năng nhớ các chỉ thị ở giữa). Yêu cầu *Báo Cáo Cảnh Báo*.
- **20,000 Tokens:** Ngưỡng Đỏ (Nghiêm cấm). Hệ thống Hallucinate nặng, ngốn tài chính (Costly). Yêu cầu Nén Khẩn cấp (Circuit Strike).

## 2. Kỹ Thuật Nén Semantic (Semantic Compression Buffer)
Đừng cắt ghép file theo kiểu ngắt cụt đuôi chữ (Truncation) vô tri. Phải dùng "Nén Cấu Trúc Ngữ Nghĩa":
- Gói gọn 100 dòng Nhật ký vận hành (Ledger) lỗi thời thành 1 dòng tóm tắt bản thể.
- Ví dụ: Thay vì giữ 10 Logs cập nhật file A, dòng cuối cùng nên là `File A đạt mốc Final Version 1.0 (Bỏ qua các bước trung gian)`.

## 3. Circuit Break (Ngắt luồng Cứng)
Nếu quá ngân sách truy xuất, Bác Sĩ phải chèn dòng lệnh: "[CIRCUIT BROKEN] Ngừng phân tích chi tiết. Chuyển sang JSON response tiết kiệm."
