# BẢNG CỬU CHƯƠNG LỆNH (PROMPT CHEAT SHEET) — DAY 1
*Tài liệu tham khảo nhanh dành cho BOM và Key Persons khi vận hành Agentic Workspace*

---

## 0. GIAO DIỆN & TÍNH NĂNG CƠ BẢN CỦA GOOGLE ANTIGRAVITY

- **Khung Chat (Chatbox):** Nơi Anh/Chị nhập Lệnh (Prompt). Gõ `/` để gọi Quy trình (Workflow) và `@` để gọi Kỹ năng (Skill).
- **Cửa sổ Workspace (Bên trái):** Hiển thị cấu trúc thư mục 5-Zone.
- **Nút "Accept" / "Reject":** Khi AI đề xuất sửa file hoặc chạy lệnh, hệ thống sẽ chờ duyệt. BẮT BUỘC bấm **Accept** để AI làm tiếp.
- **Bảng Artifacts (Bên phải):** Nơi hiển thị tài liệu đầu ra (Báo cáo, Dàn ý).
- **Tính năng đính kèm (Attachment):** Kéo thả file vào Chatbox để AI đọc dữ liệu đầu vào.

---

## CÁC LỆNH THỰC HÀNH DAY 1


### 📍 GIAI ĐOẠN 1 — CÀI ĐẶT MÔI TRƯỜNG & KHỞI ĐỘNG HỆ THỐNG

**Lệnh 0 — Cài đặt Môi trường (Onboarding)**
*Dùng đầu tiên khi mới mở hệ thống để AI tự động cài đặt Python và thư viện.*
```text
/onboarding
[BỐI CẢNH]
Tôi là người dùng mới, hệ thống của tôi chưa có Python và các thư viện cần thiết.
[CHỈ THỊ]
Hãy chạy quy trình tự động cài đặt Python, cài đặt thư viện và thiết lập môi trường để tôi có thể làm việc ngay. Nếu cần chạy lệnh Terminal, hãy hiện nút Accept để tôi duyệt.
[TIÊU CHÍ ĐẦU RA]
- Báo cáo hoàn tất cài đặt trên Chat.
```


### 📍 GIAI ĐOẠN 2 — KÍCH HOẠT VÀ PHÂN TÍCH YÊU CẦU

**Lệnh 1 — Giai đoạn 2**
Gõ tuần tự các prompt dưới đây vào ô chat của workspace. Không cần dừng lại giữa các prompt.

**Prompt 1 — Khởi động hệ thống**
```text
/khoi-dong-phien
```

**Lệnh 2 — Phân tích yêu cầu (Rã task trước khi làm)**

```text
/phan-tich-nhiem-vu
[BỐI CẢNH] Tôi là Quản lý (BOM). Tôi cần đánh giá tiềm năng ứng dụng AI Agent cho phòng ban của mình và xuất bản báo cáo DOCX cùng PPTX (10-15 slides).
[CHỈ THỊ] Hãy đóng vai Kỹ sư Giải pháp. Phân rã công việc thành cấu trúc WBS gồm 5 bước logic để hoàn thành báo cáo này trong ngày hôm nay.
[DỮ LIỆU ĐẦU VÀO] Tôi đã chuẩn bị file bối cảnh phòng ban. Sẽ nạp ở bước sau.
[TIÊU CHÍ ĐẦU RA]
- Format: Danh sách gạch đầu dòng ngắn gọn.
```

**Lệnh 3 — Prompt thực thi Giai đoạn 2 (tiếp)**
**Prompt 3 — Tạo dự án cá nhân**
```text
/khoi-tao-du-an-moi
[BỐI CẢNH] WBS đã được thiết lập. Tôi cần tạo kho lưu trữ chính thức.
[CHỈ THỊ] Hãy khởi tạo dự án dựa trên kế hoạch thực hiện vừa triển khai.
[DỮ LIỆU ĐẦU VÀO] Tên dự án: tiem-nang-ai-[ten-phong-ban-cua-ban] (VD: tiem-nang-ai-hr)
[TIÊU CHÍ ĐẦU RA]
- Xác nhận đường dẫn thư mục dự án đã được tạo.
```


### 📍 GIAI ĐOẠN 3 — THIẾT LẬP BỐI CẢNH PHÒNG BAN

**Lệnh 4 — Nạp tài liệu phòng ban**
*Kéo thả các file DOCX mô tả quy trình và file Excel dữ liệu của phòng ban vào ô chat TRƯỚC khi gõ lệnh.*
```text
[BỐI CẢNH] Tôi cần Agent nắm được thực trạng công việc và quy trình của phòng ban tôi để phục vụ đánh giá tiềm năng ứng dụng AI.
[CHỈ THỊ] Lưu trữ các file tôi vừa đính kèm vào đúng cấu trúc thư mục dự án.
[DỮ LIỆU ĐẦU VÀO] [Đính kèm file DOCX mô tả quy trình + file Excel dữ liệu]
[TIÊU CHÍ ĐẦU RA]
- Vị trí lưu: Dự án `tiem-nang-ai-[ten-phong-ban-cua-ban]`.
- Xác nhận tên file và vị trí sau khi lưu.
```

**Lệnh 5 — Prompt thực thi Giai đoạn 3 (tiếp)**
**Prompt 2 — Chuẩn hóa dữ liệu để Agent đọc hiểu**
```text
/chuan-hoa-tai-lieu
[BỐI CẢNH] Agent xử lý hiệu quả nhất khi dữ liệu ở dạng văn bản thô (Markdown). Các file DOCX/Excel vừa nạp cần được chuyển đổi.
[CHỈ THỊ] Trích xuất nội dung từ tất cả file vừa nạp, chuyển đổi sang Markdown chuẩn để làm tài liệu nền tảng phục vụ phân tích.
[DỮ LIỆU ĐẦU VÀO] Các file vừa lưu ở bước trên.
[TIÊU CHÍ ĐẦU RA]
- Format: Markdown có cấu trúc rõ ràng (heading, bảng, danh sách).
- Nơi lưu: Cùng thư mục dự án. Thông báo khi hoàn tất.
```


### 📍 GIAI ĐOẠN 4 — KHÁM PHÁ CẤU TRÚC WORKSPACE

**Lệnh 6 — Giai đoạn 4**
**Prompt 3 — Agent giới thiệu Workspace theo bối cảnh của bạn**
```text
/tro-giup
[BỐI CẢNH] Tôi vừa nạp file mô tả quy trình và dữ liệu của phòng ban vào workspace.
[CHỈ THỊ] Hãy giới thiệu tổng quan workspace này cho tôi: mỗi khu vực lưu trữ (6 ngăn) dùng để làm gì, và liên hệ cụ thể với dữ liệu phòng ban tôi vừa nạp. Ví dụ: file của tôi đang nằm ở ngăn nào, kết quả phân tích sẽ xuất ra ở ngăn nào.
[DỮ LIỆU ĐẦU VÀO] Dữ liệu phòng ban đã nạp ở bước M1.
[TIÊU CHÍ ĐẦU RA]
- Giải thích ngắn gọn từng khu vực, liên hệ trực tiếp với phòng ban của tôi.
- Chỉ rõ: file tôi đang ở đâu, kết quả sẽ ra ở đâu.
```


### 📍 GIAI ĐOẠN 5 — NGHIÊN CỨU THỰC TRẠNG VÀ KINH NGHIỆM HAY

**Lệnh 7 — Giai đoạn 5 (Chuỗi 3 bước)**
**Prompt 1 — Phân tích thực trạng từ dữ liệu đã nạp**
```text
[BỐI CẢNH] Tôi đã nạp file mô tả quy trình và dữ liệu Excel của phòng ban vào workspace.
[CHỈ THỊ] Đọc toàn bộ dữ liệu đã chuẩn hóa và tóm tắt thực trạng công việc của phòng ban tôi: các quy trình chính đang vận hành, điểm mạnh, điểm nghẽn (nếu nhận thấy), và các mảng việc chiếm nhiều thời gian nhất.
[DỮ LIỆU ĐẦU VÀO] Các file Markdown đã chuẩn hóa ở bước M1.
[TIÊU CHÍ ĐẦU RA]
- Tóm tắt ngắn gọn (1 trang) gồm: danh sách quy trình chính, nhận xét sơ bộ, và 3-5 câu hỏi cần làm rõ thêm.
```

**Lệnh 8 — Prompt thực thi Giai đoạn 5 (tiếp)**
**Prompt 2 — Lên kế hoạch nghiên cứu**
```text
[BỐI CẢNH] Bản tóm tắt thực trạng đã có. Tôi cần tìm hiểu thêm từ bên ngoài.
[CHỈ THỊ] Dựa trên thực trạng phòng ban vừa phân tích, hãy lên kế hoạch nghiên cứu: liệt kê 5-7 câu hỏi cụ thể cần web search (ví dụ: best practices, case study, benchmark) để bổ sung vào báo cáo tiềm năng AI.
[DỮ LIỆU ĐẦU VÀO] Bản tóm tắt thực trạng vừa tạo.
[TIÊU CHÍ ĐẦU RA]
- Danh sách câu hỏi nghiên cứu, sắp xếp theo mức độ ưu tiên.
- Dừng lại chờ tôi duyệt trước khi chạy web search.
```

**Lệnh 9 — Prompt thực thi Giai đoạn 5 (tiếp)**
**Prompt 3 — Chạy web search và tổng hợp**
```text
/nghien-cuu-thi-truong
[BỐI CẢNH] Kế hoạch nghiên cứu đã được duyệt. Phòng ban: [Tên phòng ban]. Báo cáo nhắm tới Lãnh đạo cấp trung.
[CHỈ THỊ] Thực hiện web search theo danh sách câu hỏi đã duyệt. Tổng hợp kết quả thành báo cáo nghiên cứu. Không dùng kiến thức LLM cũ.
[DỮ LIỆU ĐẦU VÀO] Danh sách câu hỏi nghiên cứu + bản tóm tắt thực trạng.
[TIÊU CHÍ ĐẦU RA]
- Format: Báo cáo Markdown tên `GHI-CHU-XU-HUONG.md`.
- Nội dung: 3 case study/best practices thực tế phù hợp với đặc thù phòng ban, so sánh khi nào dùng Chatbot vs AI Agent.
- Có đường link nguồn trích dẫn.
- Nơi lưu: Thư mục dự án hiện tại.
```


### 📍 GIAI ĐOẠN 6A — THIẾT KẾ HƯỚNG PHÂN TÍCH TIỀM NĂNG

**Lệnh 10 — Giai đoạn 6A**

```text
[BỐI CẢNH] Tôi đã có các file dữ liệu thực trạng phòng ban và file GHI-CHU-XU-HUONG trong thư mục dự án.
[CHỈ THỊ] Đóng vai Chuyên viên Tư vấn Chiến lược. Hãy đề xuất một Kế hoạch Phân tích ngắn gọn để viết Báo cáo Tiềm năng Ứng dụng AI Agent, trong đó có phần đánh giá thực trạng hiệu quả hiện tại của phòng ban tôi.
[DỮ LIỆU ĐẦU VÀO] Các file vừa nạp ở trên.
[TIÊU CHÍ ĐẦU RA]
- Dàn ý báo cáo (5 phần: Tóm tắt, Bối cảnh & Thực trạng hiệu quả, Case Study, Tiềm năng ứng dụng, Khuyến nghị).
- Soạn sẵn 1 Mega-prompt để tôi duyệt trước khi ra lệnh viết chi tiết.
- Dừng lại chờ tôi duyệt.
```


### 📍 GIAI ĐOẠN 6B — CHẠY PHÂN TÍCH TIỀM NĂNG

**Lệnh 11 — Giai đoạn 6B**

```text
[BỐI CẢNH] Kế hoạch phân tích đã được duyệt.
[CHỈ THỊ] Dựa trên Mega-prompt bạn vừa soạn, hãy tiến hành phân tích chi tiết. Nêu bật ít nhất 3 nhóm công việc phòng ban có thể dùng Agent để tăng năng suất.
[DỮ LIỆU ĐẦU VÀO] Dữ liệu phòng ban và Ghi chú xu hướng.
[TIÊU CHÍ ĐẦU RA]
- Format: Báo cáo Markdown tên `PHAN-TICH-TIEM-NANG.md`.
- Kèm theo bảng đánh giá mức độ khả thi (Cao/Trung bình/Thấp).
- Nơi lưu: Thư mục dự án hiện tại.
```


### 📍 GIAI ĐOẠN 7 — TẠO BÁO CÁO DOCX

**Lệnh 12 — Giai đoạn 7**

```text
/chuan-hoa-tai-lieu
[BỐI CẢNH] File phân tích Markdown đã xong, tôi cần xuất bản ra định dạng MS Word để báo cáo Ban Giám Đốc.
[CHỈ THỊ] Rà soát và chuẩn hóa lại cấu trúc file `PHAN-TICH-TIEM-NANG.md` (đảm bảo thẻ heading, bảng biểu, danh sách đúng chuẩn) trước khi định dạng thành báo cáo hoàn chỉnh và kết xuất (Render) ra DOCX.
[DỮ LIỆU ĐẦU VÀO] File `PHAN-TICH-TIEM-NANG.md`.
[TIÊU CHÍ ĐẦU RA]
- Format: File vật lý `.docx`.
- Tên file: `BAO-CAO-TIEM-NANG-AI-AGENT.docx`.
- Nơi lưu: Thư mục dự án hiện tại. Thông báo khi hoàn tất để tôi tải về.
```


### 📍 GIAI ĐOẠN 8 — THIẾT KẾ VÀ KẾT XUẤT PPTX (10-15 SLIDES)

**Lệnh 13 — Giai đoạn 8 (Chuỗi 2 bước bắt buộc)**
**Prompt 1 — Soạn nội dung (Chưa xuất PPTX)**
```text
/tao-tai-lieu
[BỐI CẢNH] Tôi cần chuẩn bị slide báo cáo từ file DOCX vừa rồi để trình bày cho Ban Giám Đốc.
[CHỈ THỊ] Soạn nội dung bài thuyết trình (khoảng 10-15 slides) bám sát theo outline dưới đây. Mỗi slide chỉ nên có 1 tiêu đề và 3-4 gạch đầu dòng ngắn gọn.
[DỮ LIỆU ĐẦU VÀO] Báo cáo DOCX / Markdown Tiềm năng.
[TIÊU CHÍ ĐẦU RA]
- Format: Trình bày giàn trang bằng Markdown (sử dụng --- để ngắt slide) trong file `NOI-DUNG-SLIDE.md` để tôi review layout trước khi kết xuất.
```

**Lệnh 14 — Prompt thực thi Giai đoạn 8 (tiếp)**

```text
- Đề xuất Outline (tuân thủ):
  + Slide 1: Tiêu đề báo cáo & Tên phòng ban
  + Slide 2: Tóm tắt Thực trạng (Nỗi đau lớn nhất)
  + Slide 3-5: Case Study / Điển hình ứng dụng AI
  + Slide 6-10: Phân tích 3 mảng việc có Tiềm năng ứng dụng AI cao nhất
  + Slide 11-12: Kế hoạch triển khai & Khuyến nghị
  + Slide 13: Lời cảm ơn
- Xong dàn ý thì dừng lại chờ tôi duyệt.
```

**Lệnh 15 — Prompt thực thi M3.4 (tiếp)**
**Prompt 2 — Kết xuất PPTX tự động**
```text
/chuan-hoa-tai-lieu
[BỐI CẢNH] Dàn ý Slide đã được duyệt. Cần kết xuất thành sản phẩm vật lý.
[CHỈ THỊ] Rà soát lại cấu trúc Markdown (kiểm tra các thẻ ngắt slide ---, bullet points) cho chuẩn chỉnh. Sau đó kết xuất file `NOI-DUNG-SLIDE.md` thành PowerPoint. Quá trình render mất khoảng 2-3 phút.
[DỮ LIỆU ĐẦU VÀO] File `NOI-DUNG-SLIDE.md`.
[TIÊU CHÍ ĐẦU RA]
- Format: File `.pptx`.
- Tên file: `SLIDE-TIEM-NANG.pptx`.
- Nơi lưu: Thư mục dự án hiện tại.
```


### 📍 GIAI ĐOẠN 9 — ĐÁNH GIÁ VÀ CHỐT PHẠM VI DAY 2

**Lệnh 16 — Dành cho học viên CHƯA CÓ bài toán/quy trình**

```text
[BỐI CẢNH] Tôi chuẩn bị tham gia Day 2 khóa học Agentic Workspace. Yêu cầu: Chọn 1 quy trình (nhỏ) của phòng ban để số hóa và chuẩn hóa, sao cho AI Agent có thể vận hành dưới sự điều phối của con người trên Google Antigravity.
[CHỈ THỊ] Tôi chưa nghĩ ra nên chọn quy trình nào. Hãy gợi ý cho tôi 3-5 quy trình nhỏ, dễ làm, mang lại "Quick Win" trong phòng ban của tôi. Phỏng vấn tôi để chọn ra 1 quy trình phù hợp nhất.
[DỮ LIỆU ĐẦU VÀO] Phòng ban của tôi là: [Điền tên phòng ban].
[TIÊU CHÍ ĐẦU RA]
Sau khi phỏng vấn xong, chốt lại cho tôi thành 6 mục:
1. Tên quy trình muốn cải tiến:
2. Bước trọng tâm cần AI giải quyết:
3. Dữ liệu mẫu sẽ sử dụng:
4. Tiêu chí đánh giá "Đủ tốt để dùng":
5. Phần KHÔNG LÀM (giới hạn scope để kịp trong 1 ngày):
6. Đầu ra mong đợi (SOP/Biểu mẫu/Báo cáo):
```

**Lệnh 17 — Dành cho học viên ĐÃ CÓ bài toán/quy trình/tài liệu**

```text
[BỐI CẢNH] Tôi chuẩn bị tham gia Day 2 khóa học Agentic Workspace. Yêu cầu: Chọn 1 quy trình (nhỏ) của phòng ban để số hóa và chuẩn hóa, sao cho AI Agent có thể vận hành dưới sự điều phối của con người trên Google Antigravity.
[CHỈ THỊ] Tôi đã có sẵn ý tưởng và tài liệu. Hãy giúp tôi phân tích và thu hẹp phạm vi lại cho vừa vặn để thực hành xây dựng trong 1 ngày học.
[DỮ LIỆU ĐẦU VÀO] Phòng ban: [Điền tên phòng ban]. Ý tưởng/tài liệu: [Đính kèm hoặc mô tả ngắn].
[TIÊU CHÍ ĐẦU RA]
Sau khi phân tích xong, chốt lại cho tôi thành 6 mục:
1. Tên quy trình muốn cải tiến:
2. Bước trọng tâm cần AI giải quyết:
3. Dữ liệu mẫu sẽ sử dụng:
4. Tiêu chí đánh giá "Đủ tốt để dùng":
5. Phần KHÔNG LÀM (giới hạn scope để kịp trong 1 ngày):
6. Đầu ra mong đợi (SOP/Biểu mẫu/Báo cáo):
```

**Lệnh 18 — Đóng Phiên An Toàn**

```text
/dong-phien
```
