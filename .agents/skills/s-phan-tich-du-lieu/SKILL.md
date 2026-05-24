---
name: s-phan-tich-du-lieu
description: >
  Phân tích dữ liệu thô end-to-end cho BOM phòng ban MindX. Pipeline 4 bước:
  Suy luận bối cảnh từ file → Làm sạch & Chẩn đoán → Tính chỉ số thông minh → Viết báo cáo Pyramid.
  Đầu ra là báo cáo Markdown chuẩn McKinsey, chain sang skill tao-tai-lieu để xuất DOCX/PPTX.
  Dùng khi user nói "phân tích", "Excel", "CSV", "data", "trend", "MoM", "YoY",
  "breakdown", "báo cáo từ file", "tại sao chỉ số tăng/giảm", "performance vs target".
  Cũng kích hoạt khi user upload file Excel/CSV kèm yêu cầu mơ hồ như "xem giúp tôi".
  KHÔNG dùng cho thiết kế dashboard định kỳ (route sang thiet-ke-bao-cao-bi).
version: v3.1
status: Production-Ready
---

# Data Analyzer — Phân Tích Dữ Liệu & Báo Cáo Pyramid

Pipeline 4 bước: **suy luận bối cảnh → làm sạch & chẩn đoán → tính chỉ số thông minh → viết báo cáo Pyramid (Markdown)** cho BOM phòng ban MindX. Đầu ra cuối cùng là báo cáo Markdown chuẩn mực, sẵn sàng chain sang skill `tao-tai-lieu` để tạo Word (DOCX) hoặc Slide (PPTX) trình BOD.

## When to use this skill

- BOM cần **báo cáo tuần/tháng/quý** từ data thô (Excel, CSV, sao kê)
- BOM cần **performance review vs target** (chỉ số thực tế vs kế hoạch)
- BOM cần **trend analysis** (so sánh tháng trước, năm trước, cùng kỳ)
- BOM cần **funnel/conversion analysis** (phân tích rơi rụng theo bước)
- **Tier 1 (non-tech):** paste Excel raw + 1 câu yêu cầu → output báo cáo Markdown
- **Tier 3 (tech-savvy):** custom chỉ số + chain với `tao-tai-lieu` xuất Word/PPTX

**KHÔNG dùng khi:**
- User muốn **thiết kế hệ thống báo cáo định kỳ / dashboard Excel** → route `thiet-ke-bao-cao-bi`
- User muốn **soạn văn bản từ nội dung có sẵn** → route `tao-tai-lieu`

## How to use it

> **[EXECUTION MANDATE]:** KHÔNG ĐƯỢC tự tính nhẩm hoặc đoán kết quả. BẮT BUỘC viết script Python (lưu vào `tmp/`) và chạy qua `run_command`, xử lý dữ liệu bằng `pandas`. Nếu thiếu thư viện, auto `pip install`.
>
> **[FALLBACK POLICY]:** Nếu môi trường không có Python, agent ĐƯỢC PHÉP dùng built-in code execution của IDE hoặc xuất Python code kèm hướng dẫn để user tự chạy. TUYỆT ĐỐI không halt giữa chừng.

---

### Step 0: OBSERVE & INFER (Suy luận bối cảnh — chạy ngầm)

**Mục tiêu**: Đọc file, suy luận Ngành/Phòng ban, Chu kỳ, Trọng tâm ra quyết định TRƯỚC khi phân tích.

**Hành động:**
1. Đọc file bằng Python (pandas/openpyxl), kiểm kê tất cả sheets + columns
2. Nếu file có sheet HUONG_DAN (metadata IPO) → đọc trước, dùng làm chỉ dẫn phân tích
3. Áp dụng 5 bộ quy tắc suy luận theo `resources/inference-rules.md`:
   - Quy tắc 1: Nhận diện Domain từ tên cột
   - Quy tắc 2: Nhận diện Cadence từ tên sheet + pattern ngày
   - Quy tắc 3: Suy luận Decision Focus từ biểu đồ + công thức
   - Quy tắc 4: Đánh giá năng lực Excel của user
   - Quy tắc 5: Phát hiện Pain Point trong file
4. Biên soạn Internal Inference Brief (nội bộ, chưa show user)

**Quyết định logic:**
- File có sheet HUONG_DAN chứa công thức/chỉ số → ƯU TIÊN dùng hướng dẫn trong file
- File >20 sheets → focus 3 sheet được dùng nhiều nhất
- Không có file (mô tả bằng lời) → skip forensics, infer từ mô tả user
- Pain signals ≥5 → đề xuất chuẩn hóa file gốc trước (route `thiet-ke-bao-cao-bi`)

---

### Step 1: DATA CLEANING + DIAGNOSE (Làm sạch & Chẩn đoán)

**Mục tiêu**: Làm sạch dữ liệu + chẩn đoán cột/dòng nào nên giữ, bỏ, hoặc đơn giản hóa.

**Cleaning logic (auto-run):**
1. **Header normalize:** lowercase, bỏ ký tự đặc biệt, trim khoảng trắng
2. **Date parse:** detect DD/MM/YYYY vs MM/DD/YYYY vs ISO → chuẩn hóa ISO 8601
3. **Number parse:** bỏ ký hiệu tiền tệ (đ, ₫, $), chuyển dấu phẩy thành dấu chấm thập phân
4. **Missing values:** đánh dấu NA rõ ràng; >20% missing ở 1 cột trọng yếu → cảnh báo user
5. **Outlier detection:** giá trị >3σ → cờ cảnh báo, hỏi user xác nhận trước khi bỏ
6. **Duplicate rows:** key columns trùng → loại bỏ, giữ dòng cập nhật gần nhất

**Diagnose logic (MỚI v3.0):**
Phân loại từng cột/sheet vào 1 trong 4 nhóm:
- **GIỮ (Keep):** Phục vụ phân tích trực tiếp, dữ liệu sạch
- **ĐƠN GIẢN (Simplify):** Cần nhưng format lộn xộn → chuẩn hóa trước khi tính
- **GỘP (Consolidate):** Nhiều cột cùng ý nghĩa → gộp thành 1
- **BỎ QUA (Eliminate):** Không phục vụ phân tích → loại khỏi pipeline

Thông báo user: "Tôi phát hiện [N] cột không cần thiết cho phân tích ([liệt kê]). Cho phép bỏ qua?"

**Output Step 1:** cleaned dataframe + cleaning log

---

### Step 2: KPI CALCULATION (Tính chỉ số thông minh)

**Mục tiêu**: Tính toán bộ chỉ số phù hợp nhất cho dữ liệu, dựa trên kết quả Inference Step 0.

**Logic đề xuất chỉ số (MỚI v3.0):**
1. Tra `resources/metric-catalog-by-domain.md` theo domain đã suy luận
2. Nếu file có sheet HUONG_DAN chứa công thức cụ thể → ƯU TIÊN dùng, bỏ qua catalog
3. Nếu không có HUONG_DAN → đề xuất 5 chỉ số core cho user:
   "Dựa trên dữ liệu [domain], tôi đề xuất 5 chỉ số: [1]...[5]. Phù hợp không?"
4. User confirm → tính toán. User adjust → điều chỉnh rồi tính

**Calculation logic:**
1. Compute primary metrics (chỉ số chính)
2. Compute trend vs kỳ trước (nếu có dữ liệu đa kỳ)
3. Highlight 3-5 chỉ số đạt ngưỡng cảnh báo (KHÔNG quá 5 để tránh nhiễu)

<<HOOK_METRIC_CATALOG>>
default catalog (universal MindX):
  - Volume: count(distinct id)
  - Growth %: (current - previous) / previous * 100
  - Achievement %: actual / target * 100
override: xem `resources/metric-catalog-by-domain.md` cho catalog chi tiết 7 domains
each metric requires: formula, target, warning_threshold
<</HOOK_METRIC_CATALOG>>

---

### Step 3: PYRAMID NARRATIVE REPORT (Báo cáo Pyramid + Câu hỏi Đào sâu)

Apply McKinsey Pyramid Principle kết hợp Descriptive-Diagnostic Analytics:

**Pyramid structure (MỚI v3.1):**
1. **Kết luận điểm (Executive Summary)** — 1 câu trả lời "vậy rốt cuộc thế nào?"
2. **Bức tranh tổng quan (Descriptive Statistics)** — Trả lời câu hỏi "What happened?". Liệt kê các thống kê mô tả (mean, median, tần suất, phân bổ) để thiết lập baseline cho người đọc.
3. **Phân tích chẩn đoán (Diagnostic Findings)** — Trả lời câu hỏi "Why did it happen?". Bóc tách nguyên nhân, chỉ ra tương quan từ bức tranh tổng quan. Bao gồm 3 luận điểm chính.
4. **Gợi Ý Hướng Đào Sâu (Deep-Dive Areas)** — 3 hướng gợi mở phân tích tiếp theo đi từ Vĩ mô xuống Vi mô. **MANDATE:** Sử dụng ngôn ngữ tư vấn ("Be Curious, Not Presumptive"), gợi mở hợp tác (VD: "Làm thế nào để..."), TUYỆT ĐỐI KHÔNG dùng câu hỏi chất vấn ("Tại sao lại...").
5. **Hành động đề xuất (Next Steps)** — Gợi ý bước tiếp theo cụ thể.

**Định dạng Visual Formatting BẮT BUỘC:** 
- Markdown chặt chẽ (H1, H2, Bullet points).
- **Hệ thống Emoji:** Dùng 🟢/🟡/🔴 để chỉ báo trạng thái của các Phát hiện.
- **Biểu đồ Unicode:** Dùng thanh tiến trình ngang `████░░` trong bảng để hiển thị tỷ trọng thay vì chỉ dùng số.
- **Callout Blocks:** Dùng `> [!IMPORTANT]` cho Kết luận điểm và `> [!WARNING]` cho Gợi ý hướng đào sâu.
(Xem kỹ `assets/output-templates/pyramid-report-template.md` để lấy format chuẩn).

**Validation handshake:** Output Markdown phải có `## 1. Kết Luận Điểm` H2 đầu tiên + `## 2. Bức Tranh Tổng Quan` H2 + `## 3. Phân Tích Chẩn Đoán` H2 + `## 4. Gợi Ý Hướng Đào Sâu` H2 + `## 5. Hành Động Đề Xuất` H2. Skill `tao-tai-lieu` parse các section này.

---

## Edge cases & escalation

1. **Missing data >20% key column** → cảnh báo + đề xuất nguồn bổ sung. Confidence = low.
2. **Multiple data source format khác** → yêu cầu merge schema rõ ràng trước khi proceed
3. **Yêu cầu out-of-scope ("present slide")** → auto chain `tao-tai-lieu` để render PPTX
4. **Data <30 ngày** → MoM/YoY không ý nghĩa, cảnh báo user và suggest snapshot hiện tại
5. **Outlier ngoài 5σ** → LUÔN hỏi user xác nhận, không tự bỏ
6. **Conflicting metric definitions** → TỪ CHỐI tính, hỏi user chọn nguồn nào chính thức
7. **Period boundary chưa rõ** ("quý 1" = Jan-Mar hay fiscal year?) → hỏi user
8. **Pain signals ≥5** → Đề nghị route sang `thiet-ke-bao-cao-bi` để chuẩn hóa file gốc trước

## Anti-patterns

- ❌ **Kết luận ở cuối báo cáo** (sai Pyramid — phải đặt đầu)
- ❌ **Liệt kê 20+ chỉ số** trong 1 báo cáo (highlight 3-5 thôi)
- ❌ **Plain text output** (làm gãy chuỗi tạo tài liệu sau đó)
- ❌ **Tự tính nhẩm** thay vì chạy script Python
- ❌ **Bỏ outlier ngầm** không hỏi user
- ❌ **Bỏ qua Step 0 Inference** — chạy máy móc không hiểu bối cảnh dữ liệu

## Confidence Calibration

- `high`: data sạch (<5% missing), 0 outlier >5σ, period đủ dài, chỉ số khớp schema
- `medium`: data có warning (5-20% missing, outliers 3-5σ), nhưng vẫn phân tích được
- `low`: data >20% missing 1 cột trọng yếu, hoặc period <30 ngày cho MoM, hoặc conflicting metrics

## Cross-skill chaining

- **Nhận output từ:** `phan-tich-yeu-cau` (sub-task định tính → định lượng)
- **Truyền output cho:** `tao-tai-lieu` (Markdown report → DOCX/PPTX render)
- **Routing đồng cấp:** Nếu phát hiện user cần BI system design → route `thiet-ke-bao-cao-bi`

## Resources

| File | Mục đích |
|------|----------|
| `resources/inference-rules.md` | 5 bộ quy tắc suy luận Domain/Cadence/Pain từ file (Step 0) |
| `resources/metric-catalog-by-domain.md` | Catalog chỉ số cho 7 domains — tra cứu ở Step 2 |
| `references/variant-kd-mkt-campaign-q1-report.md` | Ví dụ báo cáo Kinh doanh Marketing |
| `references/variant-back-hr-recruitment-monthly.md` | Ví dụ báo cáo Nhân sự hàng tháng |
| `references/variant-tech-support-ticket-trend.md` | Ví dụ báo cáo Tech Support |
| `references/customize-prompt-scaffold.md` | Scaffold cho user customize prompt |
| `references/operator-handoff.md` | Hướng dẫn bàn giao cho operator |

**Output templates:**
- `assets/output-templates/pyramid-report-template.md`
- `assets/output-templates/kpi-table-template.md`
- `assets/output-templates/cleaning-log-template.md`

**Scripts:**
- `scripts/clean_data.py` — Cleaning pipeline (Python pandas)
- `scripts/calc_kpi.py` — Chỉ số calculator với catalog

## BOM Hands-On Example

**Input từ BOM HR:**
> "Tôi có file danh sách nhân sự, phân tích tổng quan giúp tôi"

**Skill xử lý:**
1. **Step 0 Infer**: Đọc file → phát hiện cột "ma_nhan_vien", "phong_ban", "trang_thai", "ngay_sinh" → Domain: HR (90%). Cadence: Snapshot. Sheet HUONG_DAN có sẵn → ưu tiên dùng.
2. **Step 1 Clean + Diagnose**: 150 rows, 13 cols. Cột "ly_do_nghi" missing 92% (chỉ người nghỉ mới có) → bình thường, không cảnh báo. Diagnose: Giữ 12 cột, bỏ qua 0.
3. **Step 2 KPI**: Dùng công thức trong HUONG_DAN → tính 10 chỉ số. Turnover 8.0% (tốt), Ban GĐ 15.2% (cảnh báo: cao bất thường).
4. **Step 3 Pyramid**: Kết luận: "Nhân sự ổn định, turnover 8%". Bức tranh tổng quan: Trình bày cơ cấu tuổi, giới tính, tỷ lệ phòng ban. Phân tích chẩn đoán: Finding 1: Retention xuất sắc; Finding 2: Lực lượng trưởng thành; Finding 3: Phân bổ đồng đều nhưng khối GĐ phình to. Deep Dive: "Ban GĐ 15.2% có top-heavy?", "Gen-Z chỉ 28.3% — rủi ro kế thừa?"

## Quality checklist
- [ ] Step 0 Inference đã chạy (có Internal Inference Brief)
- [ ] 3-5 chỉ số được highlight, không quá 5
- [ ] Kết luận ở ĐẦU báo cáo (Pyramid)
- [ ] Mọi phát hiện có ≥2 data point bằng chứng
- [ ] Có section Gợi Ý Hướng Đào Sâu sử dụng ngôn ngữ tư vấn (Vĩ mô -> Vi mô)
- [ ] Output là Markdown chuẩn H1/H2 (chain-ready)
- [ ] Báo cáo đã ứng dụng đầy đủ 4 kỹ thuật Visual Formatting (Emoji, Bảng, Unicode Bar, Callouts)
