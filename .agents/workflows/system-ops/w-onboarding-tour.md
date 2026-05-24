---
description: "System component: w-onboarding-tour.md"
semantic_triggers: ['w-onboarding-tour']
---

﻿---
description: "Tour khám phá workspace do Cố vấn AI dẫn dắt từ A-Z cho người dùng mới. User làm theo hướng dẫn và quan sát, Agent thực hiện toàn bộ 9 chặng trong 10-15 phút."
semantic_triggers: ['onboarding', 'lần đầu', 'first time', 'khám phá workspace', 'làm quen', 'hướng dẫn sử dụng', 'dẫn tôi khám phá', 'mới sử dụng', 'bắt đầu từ đâu', 'onboarding tour']
---

# Quy Trình: /w-onboarding-tour

- **👤 Owner:** `[@Cố vấn AI MindX]`
- **🛠 Skill Target:** `[workspace-orchestrator]`
- **⏱ Thời lượng:** 10–15 phút

---

## Triết lý vận hành

> [!IMPORTANT] CONCIERGE AGENT PATTERN (Bắt buộc)
> Agent đóng vai **Cố vấn chuyên môn** — ngắn gọn, trọng tâm, uy tín.
> - Agent **LÀM** toàn bộ thao tác kỹ thuật. User **LÀM THEO HƯỚNG DẪN** và **QUAN SÁT** kết quả.
> - **CẤM** dump nhiều chặng cùng lúc. Mỗi lần 1 chặng, đợi user xác nhận.
> - **CẤM** giải thích dài dòng. User là BOM/Key Person cấp cao — nói ngắn, nói đúng, nói trọng tâm.
> - Khi mô tả thao tác UI, **BẮT BUỘC** chỉ rõ vị trí nút bấm trên giao diện.

---

## Step 0: Context Boundary Lock 🛡️

**[IDE Cross-Contamination Block]:** Disregard ALL open IDE tab metadata.
`TARGET_ROOT = managed_workspaces/mindx-agent_v1/`

**[Strict Read/Write Isolation]:**
- Hardcoded scope. CẤM đọc luật/file từ Master Repo hoặc workspace khác.

---

## Chặng 0 — Chào Đón & Kiểm Tra Sẵn Sàng

**Mục tiêu:** Xác nhận workspace + kiểm tra công cụ + tạo ấn tượng chuyên nghiệp.

**Agent thực hiện:**

1. **Xác nhận workspace:** Đọc `GEMINI.md` để xác minh đúng workspace target. Sai → dừng.

2. **Kiểm tra môi trường (chạy ngầm):**

   | Hạng mục | Lệnh kiểm tra | Nếu thiếu |
   |----------|--------------|-----------|
   | Python | `python --version` | Cài qua `winget install --id Python.Python.3.11 -e --silent` |
   | Thư viện phân tích | `pip show pandas openpyxl` | `pip install pandas openpyxl matplotlib` |
   | Thư viện tài liệu | `pip show python-docx python-pptx markitdown pdfplumber` | `pip install python-docx python-pptx markitdown pdfplumber` |
   | File demo | Kiểm tra `Kho-Du-Lieu/Du-Lieu-Vao/DEMO_BAO_CAO_MAU.csv` | Cảnh báo nếu thiếu |

   Chỉ hiển thị bảng trạng thái gọn:
   ```
   ✅ Python 3.11 — OK
   ✅ Thư viện phân tích — OK
   ✅ Thư viện tài liệu — OK
   ✅ File demo — Có sẵn
   ```

3. **Mẹo nhanh (không bắt buộc):**
   > **Xem file đầu ra:** Cài extension **Office Viewer** (cweijan) từ biểu tượng Extensions (hình ô vuông, thanh bên trái) để mở file `.docx`, `.xlsx` trực tiếp trong Antigravity.
   >
   > **Theo dõi quota:** Bấm vào phần chọn Model (góc trên bên phải khung chat) — quota hiển thị ngay tại đó.

4. **Lời chào:**

> "Chào mừng Anh/Chị đến với Văn phòng AI của MindX trên Google Antigravity.
>
> Tôi là Cố vấn giúp Anh/Chị điều phối AI Agent trên workspace này hiệu quả. Hành trình gồm 9 chặng, mất khoảng 10-15 phút. Anh/Chị chỉ cần làm theo hướng dẫn của tôi và quan sát.
>
> [Bảng trạng thái môi trường]
>
> Sẵn sàng bắt đầu chứ ạ?"

**User:** Xác nhận bắt đầu.

---

## Chặng 1 — Chọn Model & Chế Độ Làm Việc

**Mục tiêu:** User biết cách chọn Model/Mode phù hợp từng loại công việc.

**Agent thực hiện:**

1. **Hướng dẫn vị trí:** "Anh/Chị nhìn góc trên bên phải khung chat — có nút chọn **Model** (tên model hiện tại) và nút chọn **Mode** (Fast/Planning)."

2. **Khuyến nghị thực chiến:**

| Tình huống | Model | Mode | Lý do |
|-----------|-------|------|-------|
| Lập kế hoạch, phân tích chiến lược | **Gemini Pro** | Planning | Tư duy sâu, chi phí hợp lý |
| Thực thi task, soạn tài liệu, chạy workflow | **Gemini Flash** | Planning | Nhanh, tiết kiệm quota |
| Gemini Pro không giải quyết được | **Claude Sonnet** | Planning | Năng lực mạnh hơn |
| Bài toán phức tạp nhất, cần chất lượng tối đa | **Claude Opus** | Planning | Đắt nhất nhưng xịn nhất |

3. **Tóm gọn:** "Nguyên tắc: **Pro để nghĩ, Flash để làm**. Chỉ leo thang lên Claude khi Gemini không đáp ứng."

**Chuyển tiếp:** "Tiếp theo tôi sẽ demo cho Anh/Chị thấy hệ thống tự động hoạt động như thế nào."

---

## Chặng 2 — Demo Workflow: Khởi Động Phiên

**Mục tiêu:** User thấy workflow là chuỗi việc tự động, không phải chat đơn lẻ.

**Agent thực hiện:**

1. **Giới thiệu ngắn:** "Mỗi ngày bắt đầu làm việc, Anh/Chị gõ `/w-khoi-dong-phien`. Hệ thống sẽ tự mở bảng điều khiển, kiểm tra tiến độ, và tóm tắt tình hình."

2. **Tự thực thi logic `/w-khoi-dong-phien`:**
   - Đọc `Bang-Dieu-Khien/TIEN-DO.md` + `BANG-DIEU-KHIEN.md`.
   - Tóm tắt ngắn gọn cho user.

3. **Giải thích:** "Vừa rồi tôi chạy 3 bước tự động: mở bảng điều khiển → kiểm tra tiến độ → tóm tắt. Đó là 1 **workflow** — chuỗi việc chạy tự động thay vì gõ từng lệnh."

**Chuyển tiếp:** "Tiếp theo tôi giới thiệu các workflow quan trọng mà Anh/Chị sẽ dùng hàng ngày."

---

## Chặng 3 — Các Workflow Khởi Đầu Công Việc

**Mục tiêu:** User biết các workflow cốt lõi và chọn thử 1 cái.

**Agent thực hiện:**

1. **Giới thiệu nhóm workflow khởi đầu:**

| Workflow | Khi nào dùng |
|----------|-------------|
| `/w-khoi-tao-du-an-moi` | Tạo dự án mới — hệ thống tự tạo cấu trúc thư mục chuẩn |
| `/w-phan-tich-nhiem-vu` | Nhận yêu cầu thô → Agent phân rã thành kế hoạch hành động |
| `/w-san-xuat-tai-lieu` | Soạn báo cáo, đề xuất, SOP từ dữ liệu/outline |
| `/w-phan-tich-va-bao-cao` | Phân tích dữ liệu số liệu → xuất báo cáo |

2. **Gợi ý trải nghiệm:** "Anh/Chị muốn thử workflow nào? Tôi khuyến nghị `/w-phan-tich-nhiem-vu` — Anh/Chị chỉ cần nêu 1 yêu cầu bất kỳ, tôi sẽ phân rã thành kế hoạch chi tiết ngay."

3. **Demo theo lựa chọn của user:** Agent chạy workflow được chọn với input thực tế từ user (hoặc input mẫu nếu user không có sẵn).

**Chuyển tiếp:** "Tiếp theo tôi demo kỹ năng phân tích dữ liệu — từ file thô ra báo cáo chuyên nghiệp."

---

## Chặng 4 — Demo Kỹ Năng: Phân Tích Dữ Liệu → Báo Cáo

**Mục tiêu:** User thấy pipeline dữ liệu thô → phân tích → báo cáo DOCX hoàn chỉnh.

**Agent thực hiện:**

1. **Đọc file demo:** Mở `Kho-Du-Lieu/Du-Lieu-Vao/DEMO_BAO_CAO_NHAN_SU.xlsx`.
   - Giới thiệu: "Đây là bộ dữ liệu nhân sự mẫu gồm 150 nhân viên, 13 cột thông tin — từ mã nhân viên, chi nhánh, phòng ban đến trình độ, hợp đồng, trạng thái nghỉ việc."
   - Mở sheet `HUONG_DAN` để chỉ cho user thấy cấu trúc IPO (Input → Process → Output) đã được thiết kế sẵn.

2. **Phân tích và tạo báo cáo Markdown (dùng kỹ năng `phan-tich-du-lieu`):**
   - Chạy pipeline 3 bước: Làm sạch → Tính 10 Chỉ số → Viết báo cáo Pyramid.
   - 10 Chỉ số cần tính: Tổng nhân sự, Tỷ lệ nghỉ việc, Phân bổ chi nhánh, Phân bổ phòng ban, Tỷ lệ giới tính, Trình độ học vấn, Nhóm tuổi, Thâm niên, Lý do nghỉ việc, Loại hợp đồng.
   - Lưu kết quả vào `Kho-Du-Lieu/Ket-Qua/BAO-CAO-TONG-QUAN-NHAN-SU.md`.

3. **Demo chuyển đổi MD → DOCX:**
   - Giới thiệu: "File Markdown đọc tốt trong Antigravity. Để gửi cho đồng nghiệp, tôi dùng kỹ năng `chuan-hoa-tai-lieu` để chuyển thành file Word."
   - Thực thi chuyển đổi → lưu `Kho-Du-Lieu/Ket-Qua/BAO-CAO-TONG-QUAN-NHAN-SU.docx`.

4. **Chỉ dẫn:** "Kết quả nằm tại `Kho-Du-Lieu/Ket-Qua/`. Đây là toàn bộ pipeline: **file thô → phân tích → báo cáo chuyên nghiệp** — Anh/Chị chỉ cần quăng file, tôi lo phần còn lại."

**Chuyển tiếp:** "Vừa rồi tôi dùng file mẫu có sẵn. Tiếp theo tôi hướng dẫn cách đưa file của Anh/Chị vào workspace."

---

## Chặng 5 — Nạp Dữ Liệu Từ Máy Tính Vào Workspace

**Mục tiêu:** User hiểu rõ: dữ liệu phải đưa vào workspace THỦ CÔNG trước, Agent mới tiếp quản được.

**Agent thực hiện:**

1. **Giải thích nguyên tắc:** "Agent chỉ đọc được file **nằm trong workspace**. File trên Desktop, ổ D, hay bất kỳ đâu bên ngoài — tôi không thấy được. Anh/Chị cần tự di chuyển file vào trước."

2. **Hướng dẫn từng bước:**

   > **Bước 1:** Mở cửa sổ quản lý file trên máy tính (Windows: `Win + E` mở File Explorer / Mac: mở Finder).
   >
   > **Bước 2:** Tìm đến file cần đưa vào (thường nằm ở Desktop hoặc thư mục Document).
   >
   > **Bước 3:** Copy file đó (Windows: `Ctrl+C` / Mac: `Cmd+C`).
   >
   > **Bước 4:** Trong cây thư mục bên trái Antigravity, tìm đến thư mục `Kho-Du-Lieu/Du-Lieu-Vao/` → Paste (Windows: `Ctrl+V` / Mac: `Cmd+V`).
   >
   > **Gợi ý:** Nên lưu workspace folder ở vị trí dễ tìm (ổ D hoặc Desktop) để việc di chuyển file tiện lợi.

3. **Nếu user thực hành:**
   - Agent phát hiện file mới → đọc, mô tả nội dung, đề xuất bước phân tích tiếp theo.

4. **Nếu user chưa có file:** Xác nhận OK, chuyển tiếp ngay. Không ép.

5. **Nhấn mạnh:** "Ghi nhớ: **file vào workspace trước → Agent tiếp quản sau**. Đây là nguyên tắc xuyên suốt."

**Chuyển tiếp:** "Tiếp theo, tôi sẽ hướng dẫn Anh/Chị tạo một dự án thực tế trên workspace."

---

## Chặng 6 — Tạo Dự Án Thực Tế

**Mục tiêu:** User tạo 1 dự án/bài toán thực → hiểu cách quy hoạch lưu trữ trong Du-An/.

**Agent thực hiện:**

1. **Gợi ý:** "Anh/Chị hãy nghĩ đến 1 bài toán hoặc dự án đang cần xử lý — ví dụ: 'Xây dựng SOP phòng kinh doanh', 'Phân tích hiệu suất Q2', 'Lập kế hoạch tuyển dụng'. Nêu tên dự án, tôi sẽ khởi tạo ngay."

2. **Chạy `/w-khoi-tao-du-an-moi`** với tên dự án từ user:
   - Tạo cấu trúc thư mục chuẩn trong `Du-An/`.
   - Tạo file brief, tasks, status theo template PMBOK.
   - Đăng ký vào Bảng Điều Khiển.

3. **Giải thích cấu trúc vừa tạo:** Liệt kê ngắn gọn các file/thư mục, mỗi cái 1 dòng giải thích.

4. **Educate:** "Mọi task và project nên được quy hoạch vào `Du-An/` ngay từ đầu. Cách này giúp tôi quản lý thông tin, theo dõi tiến độ, và không để dữ liệu rải rác khắp nơi."

**Chuyển tiếp:** "Gần xong rồi. Chặng tiếp tôi sẽ tổng hợp lại toàn bộ kiến trúc workspace."

---

## Chặng 7 — Tổng Quan Workspace & 5 Cấp Độ Agent

**Mục tiêu:** User có bức tranh toàn cảnh sau khi đã trải nghiệm thực tế.

**Agent thực hiện:**

1. **Bảng cấu trúc workspace (6 vùng):**

| Vùng | Thư Mục | Chức năng | Anh/Chị được sửa? |
|------|---------|-----------|-------------------|
| 📋 Bảng Điều Khiển | `Bang-Dieu-Khien/` | Xem tổng quan, danh sách kỹ năng/quy trình | ⚠️ Chỉ xem |
| 📁 Dự Án | `Du-An/` | Quản lý dự án phòng ban | ✅ Có |
| 📥 Kho Dữ Liệu | `Kho-Du-Lieu/` | Nạp file vào `Du-Lieu-Vao/`, lấy kết quả tại `Ket-Qua/` | ✅ Có |
| 📓 Sổ Tay | `So-Tay/` | Bài học, quyết định, thuật ngữ | ✅ Có |
| 🏛️ Quản Trị | `Quan-Tri/` | Chính sách, audit log | ⚠️ Chỉ xem |
| ⚙️ Bộ Não Agent | `.agents/` | Kỹ năng, quy tắc, quy trình | 🚫 Cấm |

2. **5 cấp độ Agent (tóm gọn):**

| Cấp | Năng lực | Ví dụ Anh/Chị vừa thấy |
|-----|---------|------------------------|
| 1 | Trả lời câu hỏi đơn lẻ | Khi tôi giải thích Model/Mode |
| 2 | Dùng kỹ năng chuyên biệt | Khi tôi phân tích file CSV |
| 3 | Chạy workflow tự động | Khi tôi chạy `/w-khoi-dong-phien` |
| 4 | Tuân thủ quy tắc, biết từ chối | Khi tôi cấm ghi đè file hệ thống |
| 5 | Điều phối nhiều Agent | Tầm nhìn cho dự án phức tạp |

3. **Tóm gọn:** "Anh/Chị vừa trải nghiệm cấp 1-4 trong tour này. Workspace đã trang bị đầy đủ — Anh/Chị chỉ cần nêu yêu cầu."

**Chuyển tiếp:** "Chặng cuối — tôi đóng phiên và tổng kết."

---

## Chặng 8 — Đóng Phiên & Tổng Kết

**Mục tiêu:** Lưu trạng thái + cung cấp tài liệu tham khảo.

**Agent thực hiện:**

1. **Đóng phiên:**
   - Cập nhật `TIEN-DO.md`: `[x] Hoàn thành Onboarding Tour.`
   - Tạo Workspace Map tại `Kho-Du-Lieu/Ket-Qua/WORKSPACE-MAP.md`.

2. **Tạo Mini Cheat Sheet** lưu tại `Kho-Du-Lieu/Ket-Qua/CHEAT-SHEET-LENH.md`:

| Lệnh | Khi nào dùng |
|------|-------------|
| `/w-khoi-dong-phien` | Bắt đầu ngày làm việc |
| `/w-dong-phien` | Kết thúc ngày |
| `/w-tro-giup` | Không biết làm gì |
| `/w-khoi-tao-du-an-moi` | Tạo dự án mới |
| `/w-phan-tich-nhiem-vu` | Phân rã yêu cầu thành kế hoạch |
| `/w-san-xuat-tai-lieu` | Soạn báo cáo/slide |

3. **Lời kết:**

> "Hoàn thành! Tôi đã lưu toàn bộ kết quả:
> - 📋 [Bản đồ Workspace](Kho-Du-Lieu/Ket-Qua/WORKSPACE-MAP.md)
> - 📝 [Cheat Sheet](Kho-Du-Lieu/Ket-Qua/CHEAT-SHEET-LENH.md)
> - 📊 [Báo cáo mẫu](Kho-Du-Lieu/Ket-Qua/TOM-TAT-FILE-MAU.docx)
> - 📁 [Dự án vừa tạo](Du-An/)
>
> Lần tới quay lại, gõ `/w-khoi-dong-phien` — tôi sẽ nhớ mọi thứ. Chúc Anh/Chị làm việc hiệu quả!"

---

## Quy tắc An toàn (Áp dụng toàn bộ workflow)

- **KHÔNG** upload dữ liệu nhạy cảm (nhân sự, lương, tài chính nội bộ).
- **KHÔNG** chỉnh sửa thư mục `.agents/`.
- **KHÔNG** tự ý cài phần mềm ngoài whitelist.
- Gặp lỗi → báo ngắn gọn + đề xuất giải pháp, KHÔNG dump stack trace.
- Script tạm → chỉ tạo trong `tmp/`. CẤM tạo ở root workspace.

---

## Fallback Protocol

Nếu user gõ prompt tự nhiên thay vì `/w-onboarding-tour` (ví dụ: "Đây là lần đầu tôi sử dụng workspace này"), Agent PHẢI tự động kích hoạt workflow này qua semantic_triggers.

Nếu sub-workflow bị lỗi, Agent fallback bằng cách thực thi logic tương đương thủ công và thông báo: "Tôi đã xử lý bằng cách khác nhưng kết quả tương đương."
