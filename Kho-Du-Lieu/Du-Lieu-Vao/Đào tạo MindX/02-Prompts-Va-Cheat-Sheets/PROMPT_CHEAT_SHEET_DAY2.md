# BẢNG CỬU CHƯƠNG LỆNH (PROMPT CHEAT SHEET) — DAY 2
*Tài liệu tham khảo nhanh dành cho BOM và Key Persons khi vận hành Agentic Workspace*

---

## CÁC LỆNH THỰC HÀNH DAY 2


### 📍 GIAI ĐOẠN 1 — ÔN TẬP DAY 1 & THU HẸP GIẢI PHÁP NHANH

**Lệnh 1 — Nêu bài toán cho Trợ lý Phân tích**
*Copy và điền vào `[...]`, gửi cho Custom GPT:*
```text
Tôi cần bạn đóng vai Trợ lý Phân tích (BA/Consultant) để giúp tôi thiết kế giải pháp cho một nghiệp vụ/quy trình.
(Đính kèm file CHUAN-BI-QUY-TRINH-DAY2-[PHONG-BAN].md từ cuối Day 1 vào đây)

1. Bối cảnh (Bổ sung thêm chi tiết nếu file đính kèm chưa đủ rõ)
- Phòng ban/bộ phận: [Điền: vd: Phòng Kinh doanh]
- Người sử dụng chính: [Điền: vd: Trưởng nhóm Sales]
- Người duyệt/quản lý: [Điền: vd: Giám đốc Kinh doanh]
- Cách đang làm hiện tại: [Điền: vd: Nhân viên gửi báo cáo bằng email cuối tuần]

2. Nhiệm vụ
- Tôi muốn chuẩn hóa/tối ưu/xây mới: [Điền tên quy trình]
- Vấn đề hiện tại: [Điền: chậm, sai số liệu, khó kiểm soát...]
- Mục tiêu quản trị: [Điền: giảm thời gian, tăng chất lượng báo cáo...]

3. Dữ liệu đầu vào
- SOP/tài liệu hiện có: [có/không, mô tả]
- File Excel/biểu mẫu: [có/không, mô tả]
- Báo cáo mẫu: [có/không, mô tả]
- Dữ liệu nhạy cảm cần tránh: [có/không]

4. Yêu cầu đầu ra
- Tôi muốn nhận được: [SOP / checklist / báo cáo / bộ triển khai cho Antigravity]
- Người đọc/sử dụng đầu ra: [Điền vai trò]
- Tiêu chí thành công: [Điền]

Hãy thực hiện theo 4 bước:
1. Tóm tắt lại bài toán bằng ngôn ngữ dễ hiểu.
2. Đánh giá thông tin đã đủ/chưa đủ.
3. Hỏi tối đa 3 câu quan trọng nhất.
4. Khi đủ thông tin, viết bản chốt hướng giải pháp để tôi duyệt.
```

**Lệnh 2 — Duyệt hướng giải pháp**
*Sau khi Custom GPT viết Concept, nếu Anh/Chị đồng ý với đề xuất, hãy chốt và yêu cầu tạo 3 file tài liệu chuyên sâu:*
```text
Tôi chọn phương án [A]. Hãy đồng ý chốt hướng giải pháp này và xuất Gói Đặc Tả (Spec Pack) cho tôi bao gồm:

1. BAN-DO-HIEN-TRANG.md (Mô tả Nỗi đau cũ, các bước thủ công)
2. BAN-DO-MUC-TIEU.md (Sơ đồ quy trình TO-BE đã tối ưu)
3. HUONG-DAN-VAN-HANH-V1.md (SOP các bước để nhân viên làm theo)
```


### 📍 GIAI ĐOẠN 2 — CÀI ĐẶT, CHUẨN HÓA & THỬ NGHIỆM LẦN 1

**Lệnh 3 — Khởi động phiên & Cài đặt Giải pháp**
*Anh/Chị mở Antigravity, tải file ZIP từ Custom GPT vào `Kho-Du-Lieu/Du-Lieu-Vao/`, rồi gõ 2 lệnh sau:*
```text
/khoi-dong-phien
```

**Lệnh 4 — Kiểm định Workspace (Audit)**
*Đảm bảo các file vừa cài đặt không làm vỡ kiến trúc hệ thống gốc.*
```text
/kiem-dinh-workspace --full-scan
```

**Lệnh 5 — Tự động vá lỗi (Self-Healing)**
*CHỈ DÙNG NẾU Lệnh 2.2a báo có lỗi (Score < 100/100) hoặc bị cảnh báo đỏ.*
```text
/toi-uu-workspace
```

**Lệnh 6 — Khởi tạo Dự án & Khai báo dữ liệu**
*Tạo dự án mới để làm việc và nạp dữ liệu thô vào.*
```text
/khoi-tao-du-an-moi
Tên dự án: quy-trinh-[ten-quy-trinh-khong-dau]
```

**Lệnh 7 — Chuẩn hóa Dữ liệu đầu vào**
*Rác dữ liệu sẽ làm AI báo lỗi sai lệch. Phải làm sạch trước khi test. Vui lòng sử dụng 1 trong 2 lệnh dưới đây tùy theo loại dữ liệu Anh/Chị có.*

**Tùy chọn A: Dành cho file văn bản (Word, PDF, PPTX)**
```text
/chuan-hoa-tai-lieu
Hãy đọc các file văn bản (Word/PDF/PPTX) tôi vừa tải vào thư mục dự án. Trích xuất thông tin, làm sạch rác định dạng và xuất ra một file chuẩn Markdown (.md) để hệ thống dễ dàng truy vấn.
Lưu kết quả vào `Kho-Du-Lieu/Du-Lieu-Vao/[tên-dự-án]/[tên-file-da-chuan-hoa].md`.
```

**Lệnh 8 — Chạy Thử Nghiệm, Đánh Giá & Tự xuất Prompt xin tư vấn**
*Áp dụng phong cách PDCA (Vòng lặp cải tiến liên tục). Không cho Agent chạy ngay mà ép Agent phải lên Kế hoạch chạy thử nghiệm, thực thi, đánh giá, và cuối cùng tự soạn sẵn câu lệnh (Prompt) để mang đi hỏi Custom GPT.*
```text
[BỐI CẢNH]
Tôi cần chạy thử nghiệm quy trình với dữ liệu thực tế tại `Kho-Du-Lieu/Du-Lieu-Vao/`.
- Lệnh kích hoạt quy trình: [Nhập lệnh Slash Command vừa cài, VD: /chay-quy-trinh-xyz]
- Dữ liệu đã chuẩn hóa: [Hãy kéo thả nguyên thư mục chứa các file .md, .csv, .xlsx vừa xử lý ở Lệnh 2.4 vào chatbox này]

[CHỈ THỊ]
Hãy thực hiện theo 4 bước sau (Tuyệt đối không nhảy cóc):
1. [PLAN/ANALYZE] Nghiên cứu file dữ liệu đầu vào, đối chiếu với kiến trúc Quy trình/Kỹ năng. Lên kế hoạch chạy thử nghiệm.
2. [DO/IMPLEMENT] Sau khi tôi duyệt Kế hoạch, hãy tiến hành chạy thử nghiệm quy trình và in log ra màn hình.
3. [CHECK/EVALUATE] Sau khi chạy xong, hãy lập một **Báo cáo phân tích chạy thử nghiệm** (Thực trạng, Vấn đề P0/P1, Nguyên nhân, Hướng giải quyết).
4. [PROMPT GENERATION] Dựa vào Báo cáo trên, TỰ ĐỘNG viết một đoạn Prompt hoàn chỉnh (tóm tắt lỗi và yêu cầu sửa đổi cấu hình) để tôi đem sang Custom GPT xin tư vấn giải pháp.
```

**Lệnh 9 — Nhận giải pháp từ Custom GPT, Phân tích và Lập Kế hoạch vá lỗi**
*Anh/Chị copy phương án mà Custom GPT vừa tư vấn, dán ngược lại vào Antigravity để Agent lên kế hoạch vá lỗi cục bộ.*
```text
[BỐI CẢNH]
Tôi vừa mang báo cáo lỗi đi hỏi và nhận được Phương án Cải tiến từ Trợ lý Phân tích (Custom GPT).

[CHỈ THỊ]
1. Đọc kỹ Phương án Cải tiến bên dưới.
2. TUYỆT ĐỐI KHÔNG ĐƯỢC TỰ ĐỘNG THỰC THI (KHÔNG GHI ĐÈ FILE).
3. Hãy đối chiếu phương án này với kiến trúc 5-Zone hiện tại và các Kỹ năng đang có, sau đó lập một Kế hoạch Thực thi (Implementation Plan) chi tiết.
4. Đợi tôi gõ "Đồng ý" thì mới được bắt đầu thực thi.

[PHƯƠNG ÁN CỦA CUSTOM GPT]
[DÁN TOÀN BỘ CÂU TRẢ LỜI CỦA CUSTOM GPT VÀO ĐÂY]
```

**Lệnh 10 — Duyệt Kế hoạch & Thực thi tối ưu**
> [!CAUTION]
> **💡 HÀNH ĐỘNG GHI ĐÈ FILE HỆ THỐNG**
> Sau khi Antigravity trình bày Kế hoạch Thực thi, hãy đọc kỹ. CHỈ KHI NÀO Anh/Chị gõ lệnh dưới đây, AI mới được phép ghi đè/sửa đổi file. Nếu thấy kế hoạch rủi ro, hãy gõ: "Tôi không đồng ý, hãy làm lại hướng khác".
```text
Đồng ý. Hãy tiến hành cập nhật hệ thống theo đúng Kế hoạch Thực thi.
Sau khi xong, hãy in ra danh sách các file đã được thay đổi.
```


### 📍 GIAI ĐOẠN 3 — CHẠY THỬ, GÓP Ý VÀ CẢI THIỆN QUY TRÌNH

**Lệnh 11 — Chạy thử lần tiếp theo với dữ liệu mới**
*Dùng khi Anh/Chị đã có bộ dữ liệu mới hoặc tình huống mới để kiểm tra quy trình.*
```text
Hãy chạy thử lại quy trình này với dữ liệu mới tôi vừa cung cấp.

Yêu cầu thực hiện theo 4 bước:

1. Kiểm tra dữ liệu đầu vào có đủ để chạy thử chưa.
2. Chạy thử quy trình theo đúng các bước hiện tại.
3. Đánh giá kết quả: bước nào đúng, bước nào sai, bước nào còn thiếu.
4. Đề xuất câu lệnh góp ý để tôi yêu cầu hệ thống sửa quy trình nếu cần.

Khi trả kết quả, hãy trình bày theo bảng:

| **Nội dung kiểm tra** | **Kết quả** | **Vấn đề phát hiện** | **Đề xuất sửa** |
|---|---|---|---|

Nếu dữ liệu chưa đủ, hãy hỏi tôi phần còn thiếu. Không tự đoán.
```

**Lệnh 12 — Bổ sung trường hợp đặc biệt**
*Dùng khi quy trình xử lý sai một tình huống ít gặp, ví dụ khách hủy đơn, hàng lỗi đặc biệt, thiếu chứng từ, sai mã hàng, phát sinh phê duyệt ngoài thông thường.*
```text
Trong lần chạy thử vừa rồi, quy trình xử lý chưa đúng trường hợp đặc biệt sau:

- Tình huống phát sinh:
[Mô tả tình huống thực tế]

- Cách hệ thống đã xử lý:
[Mô tả kết quả sai hoặc chưa phù hợp]

- Cách phòng ban tôi cần xử lý đúng:
[Mô tả cách làm đúng theo nghiệp vụ]

Hãy đề xuất cách bổ sung nhánh xử lý riêng cho tình huống này.

Yêu cầu:
1. Chỉ rõ tình huống này nên được nhận diện bằng dấu hiệu nào.
2. Chỉ rõ ai cần xử lý, ai cần kiểm tra, ai cần duyệt nếu có.
3. Chỉ rõ kết quả cuối cùng cần tạo ra.
4. Cập nhật đề xuất vào bản sửa quy trình, nhưng chưa coi là bản chính thức cho đến khi tôi xác nhận.

Hãy trả lời theo bảng:

| **Phần cần bổ sung** | **Nội dung đề xuất** | **Lý do** | **Cần người duyệt không** |
|---|---|---|---|
```

**Lệnh 13 — Bổ sung chiều sâu phân tích**
*Dùng khi báo cáo chỉ liệt kê số liệu, chưa giải thích nguyên nhân, chưa chỉ ra vấn đề thật, hoặc đánh giá còn nông.*
```text
Kết quả phân tích hiện tại còn nông và chưa giúp quản lý hiểu nguyên nhân phía sau số liệu.

Tôi cần bổ sung chiều sâu phân tích như sau:

- Chỉ số hoặc nội dung cần phân tích sâu hơn:
[Ghi chỉ số, vấn đề hoặc phần báo cáo]

- Tiêu chuẩn đánh giá đúng của phòng ban tôi:
[Ghi rõ mức nào là tốt, mức nào là cần chú ý, mức nào là rủi ro]

- Cách lý giải nguyên nhân mong muốn:
[Ghi cách phòng ban thường phân tích, ví dụ: hỏi nhiều lần “vì sao”, so sánh theo kỳ trước, so sánh theo khu vực, so sánh theo người phụ trách]

Hãy đề xuất bản sửa để kết quả phân tích:
1. Không chỉ nêu số liệu.
2. Có nhận định về nguyên nhân có khả năng cao.
3. Có cảnh báo nếu chỉ số vượt ngưỡng rủi ro.
4. Có 1-3 việc nên làm tiếp theo.

Trình bày theo mẫu:

| **Chỉ số/vấn đề** | **Kết quả hiện tại** | **Tiêu chuẩn đánh giá** | **Nguyên nhân có khả năng cao** | **Việc nên làm tiếp** |
|---|---|---|---|---|
```

**Lệnh 14 — Chuẩn hóa cách trình bày kết quả**
*Dùng khi kết quả khó đọc, dài dòng, giọng văn máy móc, thiếu bảng tóm tắt, hoặc không phù hợp với lãnh đạo/phòng ban.*
```text
Tôi cần chuẩn hóa lại cách trình bày kết quả để người quản lý và nhân sự phòng ban dễ đọc hơn.

Các vấn đề hiện tại:
- [Ghi vấn đề 1: ví dụ quá dài, thiếu bảng tóm tắt, câu văn khó hiểu]
- [Ghi vấn đề 2]
- [Ghi vấn đề 3]

Yêu cầu cách trình bày mới:
1. Mở đầu bằng bảng tóm tắt ngắn cho quản lý.
2. Viết bằng tiếng Việt dễ hiểu, không dùng thuật ngữ kỹ thuật nếu không cần.
3. Mỗi ý không quá 3 dòng.
4. Có bảng “vấn đề — nguyên nhân — đề xuất xử lý”.
5. Có mục “việc cần người quản lý xác nhận” nếu có điểm cần duyệt.

Hãy đề xuất bản định dạng kết quả mới và áp dụng cho các lần trả lời sau của quy trình này.

Trình bày theo mẫu:

| **Phần trong báo cáo** | **Cách trình bày mới** | **Lý do** |
|---|---|---|
```

**Lệnh 15 — Sửa lỗi mất thông tin giữa các bước**
*Dùng khi bước sau quên dữ liệu, quên điều kiện, quên quyết định hoặc quên kết quả đã tạo ở bước trước. Đây là lỗi rất hay gặp, vì ngay cả hệ thống AI cũng có lúc cư xử như nhân viên vừa đổi ca mà không bàn giao.*
```text
Trong lần chạy thử vừa rồi, tôi phát hiện hệ thống bị mất thông tin giữa các bước.

- Bước trước đã tạo ra thông tin sau:
[Ghi rõ thông bảo/kết quả/ràng buộc đã có]

- Bước sau đã quên hoặc dùng sai thông tin này:
[Ghi rõ bước bị sai và sai như thế nào]

- Cách xử lý đúng phải là:
[Ghi rõ bước sau cần kiểm tra hoặc sử dụng lại thông tin nào]

Hãy đề xuất cách sửa quy trình để bước sau luôn kiểm tra lại kết quả của bước trước trước khi thực hiện.

Yêu cầu:
1. Chỉ rõ thông tin nào phải được chuyển tiếp.
2. Chỉ rõ bước nào phải kiểm tra lại thông tin đó.
3. Nếu thiếu thông tin, hệ thống phải dừng lại và hỏi người dùng, không tự đoán.
4. Cập nhật đề xuất vào bản sửa quy trình, chờ tôi xác nhận trước khi coi là bản chính thức.

Trình bày theo mẫu:

| **Bước trước** | **Thông tin cần giữ lại** | **Bước sau cần kiểm tra** | **Cách xử lý khi thiếu thông tin** |
|---|---|---|---|
```

**Lệnh 16 — Tổng hợp các góp ý và tạo bản sửa quy trình**
*Dùng sau khi người dùng đã góp ý bằng một hoặc nhiều mẫu trên.*
```text
Hãy tổng hợp toàn bộ góp ý của tôi trong phiên làm việc này và tạo bản đề xuất sửa quy trình.

Yêu cầu:
1. Nhóm góp ý theo 4 loại:
   - Trường hợp đặc biệt cần bổ sung
   - Phân tích cần sâu hơn
   - Cách trình bày cần chuẩn hóa
   - Thông tin bị mất giữa các bước
2. Với mỗi góp ý, nêu rõ:
   - Vấn đề cũ
   - Cách sửa đề xuất
   - Ảnh hưởng đến quy trình
   - Có cần người quản lý duyệt không
3. Không tự sửa thành bản chính thức nếu chưa có xác nhận của tôi.
4. Cuối cùng, đưa ra 3 lựa chọn:
   A. Tôi đồng ý cập nhật bản sửa này.
   B. Tôi đồng ý một phần, cần sửa thêm.
   C. Tôi chưa đồng ý, cần phân tích lại.

Trình bày theo bảng:

| **Nhóm góp ý** | **Vấn đề cũ** | **Cách sửa đề xuất** | **Ảnh hưởng** | **Cần duyệt** |
|---|---|---|---|---|
```

**Lệnh 17 — Kiểm tra lại sau khi đã sửa**
*Dùng để kiểm tra bản vá có làm hỏng phần khác không. Vì sửa một lỗi rồi tạo thêm ba lỗi mới là truyền thống lâu đời của mọi hệ thống.*
```text
Hãy kiểm tra lại quy trình sau khi áp dụng bản sửa.

Yêu cầu kiểm tra:
1. Trường hợp cũ đã sai có được xử lý đúng chưa.
2. Các trường hợp bình thường có còn chạy đúng không.
3. Kết quả đầu ra có đúng định dạng mới không.
4. Bước sau có còn quên thông tin từ bước trước không.
5. Có phát sinh lỗi mới không.

Trả kết quả theo bảng:

| **Nội dung kiểm tra** | **Đạt/Chưa đạt** | **Bằng chứng** | **Cần sửa thêm** |
|---|---|---|---|

Nếu còn lỗi, hãy đề xuất câu lệnh góp ý tiếp theo cho tôi.
```


### 📍 GIAI ĐOẠN 4 — ĐÓNG GÓI BÁO CÁO & TẠO SLIDE THUYẾT TRÌNH

**Lệnh 18 — Thu thập dữ liệu và tạo báo cáo Trước/Sau**
*Dùng để tổng hợp toàn bộ thông tin từ Giai đoạn 1 đến Giai đoạn 3, đánh giá mức cải thiện tổng thể.*
```text
Tôi cần tạo báo cáo tổng kết so sánh Trước/Sau cho dự án cải tiến quy trình này.

[DỮ LIỆU ĐẦU VÀO]
Hãy thu thập thông tin từ các nguồn sau trong thư mục dự án:
- Bản mô tả hiện trạng ban đầu (AS-IS)
- Bản mô tả quy trình mục tiêu (TO-BE)
- Các kết quả chạy thử từ Giai đoạn 2 và Giai đoạn 3
- Bản sửa quy trình đã được duyệt
- Kết quả mẫu thực tế (nếu có)

[YÊU CẦU BÁO CÁO]
Tạo file `SO-SANH-TRUOC-SAU.md` với các nội dung:
1. Tóm tắt vấn đề ban đầu và giải pháp đã chọn.
2. Bảng so sánh Trước/Sau theo các chỉ số:
   - Số bước thực hiện (trước vs sau)
   - Thời gian ước tính (trước vs sau)
   - Tỷ lệ lỗi hoặc rủi ro (trước vs sau)
   - Mức độ dễ bàn giao cho nhân sự mới
3. Ghi rõ chỉ số nào có dữ liệu thật, chỉ số nào là ước lượng.
4. Liệt kê các bài học rút ra trong quá trình cải tiến.
5. Đề xuất hướng mở rộng tiếp theo.

Trình bày theo bảng:

| **Tiêu chí** | **Trước cải tiến** | **Sau cải tiến** | **Nguồn dữ liệu** | **Ghi chú** |
|---|---|---|---|---|

Nếu thiếu dữ liệu ở mục nào, hãy hỏi tôi. Không tự ước lượng.
```

**Lệnh 19 — Thiết kế dàn ý Slide thuyết trình**
*Dùng để tạo dàn ý slide trình bày trước lãnh đạo và các phòng ban. Prompt được thiết kế theo chuỗi tư duy tuần tự (Chain-of-Thought) để Agent xử lý chặt chẽ từng bước.*
```text
/tao-tai-lieu
Tôi cần tạo bộ slide thuyết trình bảo vệ dự án cải tiến quy trình trước lãnh đạo và 12 phòng ban. Thời gian trình bày tối đa 8 phút + 3 phút hỏi đáp.

[DỮ LIỆU ĐẦU VÀO]
Hãy đọc các file sau trong thư mục dự án:
- SO-SANH-TRUOC-SAU.md (vừa tạo ở Lệnh 4.1)
- Bản mô tả hiện trạng ban đầu
- Bản mô tả quy trình mục tiêu
- Kết quả mẫu thực tế (nếu có)

[YÊU CẦU THỰC HIỆN THEO TỪNG BƯỚC]
Bước 1: Đọc toàn bộ dữ liệu đầu vào và tóm tắt các điểm mấu chốt.
Bước 2: Xác định thông điệp chính (Key Message) mà nhóm muốn truyền tải.
Bước 3: Đề xuất dàn ý slide tối đa 10 trang theo cấu trúc:
   - Slide 1: Tiêu đề + Tên nhóm + Tên quy trình
   - Slide 2: Vấn đề đang gặp (Nỗi đau cũ, bằng chứng cụ thể)
   - Slide 3-4: Giải pháp đã xây dựng (Trước/Sau, sơ đồ quy trình mới)
   - Slide 5-6: Trình diễn thực tế (Ảnh chụp kết quả mẫu, số liệu cải thiện)
   - Slide 7-8: Bảng chỉ số cải thiện (lấy từ SO-SANH-TRUOC-SAU.md)
   - Slide 9: Bài học rút ra + Đề xuất mở rộng
   - Slide 10: Cam kết triển khai thí điểm (Ai làm, Khi nào, Đo gì)
Bước 4: Với mỗi slide, ghi rõ:
   - Tiêu đề slide
   - Nội dung chính (tối đa 5 dòng gạch đầu dòng)
   - Ghi chú cho người trình bày (nên nói gì)
Bước 5: DỪNG LẠI CHỜ TÔI DUYỆT trước khi xuất file.

BẮT BUỘC: Phải có ít nhất 1 slide nhúng kết quả mẫu thật để chứng minh quy trình đã chạy được. Không phóng đại kết quả.
```

**Lệnh 20 — Xuất file Slide thực tế**
*Dùng sau khi đã duyệt dàn ý. Cung cấp thêm yêu cầu thiết kế để slide đẹp và chuyên nghiệp.*
```text
/chuan-hoa-tai-lieu
Dàn ý slide đã được duyệt. Hãy xuất thành file SLIDE-TRINH-BAY-V1.pptx.

[YÊU CẦU THIẾT KẾ]
- Phong cách: Chuyên nghiệp, tối giản, hiện đại (Corporate/Minimal style)
- Bảng màu: [Chọn 1 trong các gợi ý dưới đây hoặc tự mô tả]
  + Xanh dương đậm + Trắng (Chuyên nghiệp, tin cậy)
  + Xanh lá + Xám đậm (Sáng tạo, công nghệ)
  + Đỏ cam + Trắng (Năng động, quyết liệt)
  + Hoặc: [Ghi màu thương hiệu công ty nếu có]
- Font chữ: Dễ đọc, kích thước lớn (tối thiểu 24pt cho nội dung, 36pt cho tiêu đề)
- Mỗi slide tối đa 5 dòng nội dung, không nhồi nhét chữ
- Nếu có file mẫu tham khảo, hãy kéo thả vào đây: [Kéo thả file .pptx mẫu nếu có]

Lưu file vào thư mục dự án.
```


### 📍 GIAI ĐOẠN 5 — TRÌNH BÀY BẢO VỆ TRƯỚC 12 PHÒNG BAN


### 📍 GIAI ĐOẠN 6 — ĐÓNG PHIÊN & CAM KẾT CHẠY THỬ ĐIỂM

**Lệnh 21 — Tạo cam kết chạy thử điểm**

```text
[CHỈ THỊ]
Tạo file CAM-KET-PILOT-2-TUAN.md trong dự án Day 2.

[TIÊU CHÍ ĐẦU RA]
Nội dung gồm:
1. Tên quy trình V1 sẽ chạy thử điểm.
2. Người chịu trách nhiệm (tên thật).
3. Số lần chạy thử trong tuần 1.
4. Chỉ số theo dõi: thời gian, số lỗi, tính dễ dùng.
5. Kế hoạch mở rộng tuần 2.
```

**Lệnh 22 — Đóng gói Giải pháp (Thành quả cuối cùng)**
*Thu gom toàn bộ "chiến lợi phẩm" của ngày hôm nay thành 1 file ZIP duy nhất để mang về phòng ban.*
```text
Hãy đóng gói toàn bộ kết quả thành 1 file ZIP.
Yêu cầu:
1. Thu gom đủ các file sau trong thư mục dự án:
   - BAN-DO-HIEN-TRANG.md
   - BAN-DO-MUC-TIEU.md
   - HUONG-DAN-VAN-HANH-V1.md
   - NHAT-KY-CHAY-THU.md
   - SO-SANH-TRUOC-SAU.md
   - SLIDE-TRINH-BAY-V1.pptx (hoặc file dàn ý slide nếu chưa xuất được PPTX)
   - CAM-KET-PILOT-2-TUAN.md
2. Nếu thiếu file nào, hãy thông báo cho tôi biết. Không tự bỏ qua.
3. Đặt tên file ZIP là: GOI-GIAI-PHAP-[TEN-QUY-TRINH]-V1.zip
4. Nếu môi trường không xuất được ZIP, hãy liệt kê danh sách file đủ để Trainer hỗ trợ đóng gói.
```

**Lệnh 23 — Đóng phiên an toàn**
*Giải phóng bộ nhớ và lưu vết toàn bộ kiến thức của khóa học vào bộ nhớ dài hạn.*
```text
/dong-phien
```
