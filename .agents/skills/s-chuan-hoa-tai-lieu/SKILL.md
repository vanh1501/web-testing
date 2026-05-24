---
name: s-chuan-hoa-tai-lieu
description: >
  Tạo, sửa, chuyển đổi file văn phòng (Word, Excel, PPT, PDF) và chuẩn hóa Markdown thành query-ready cho hệ thống RAG.
  Hỗ trợ 4 chuẩn dàn trang DOCX: vn-gov (NĐ 30), mckinsey, modern-minimal, classic-corporate.
  Tích hợp thiết kế slide Marp Markdown chuẩn B2B MindX với 12 cấu trúc layout trực quan.
  Đầu ra: file Binary chuyên nghiệp hoặc query-ready Markdown với YAML Frontmatter + Semantic Chunking.
  Kích hoạt khi user nói "soạn công văn", "tạo báo cáo", "cắt file", "chuyển sang Word", "chuẩn hóa MD",
  "format file markdown", "tinh chỉnh cấu trúc để truy vấn", hoặc yêu cầu "chuẩn hóa văn bản hành chính", "chuẩn McKinsey".
  Không dùng cho: viết nội dung sáng tạo, lập trình phần mềm, thiết kế đồ họa.
version: v3.0
status: Production-Ready
hook_summary:
  - HOOK_DOCUMENT_STANDARD: chuẩn áp dụng (NĐ 30 nhà nước / doanh nghiệp hiện đại / RAG ready)
  - HOOK_DOC_PRESET: 4 preset hỗ trợ (vn-gov, mckinsey, modern-minimal, classic-corporate)
  - HOOK_OUTPUT_CHANNEL: định dạng đầu ra (DOCX / XLSX / PPTX / MD)
  - HOOK_QA_STRICTNESS: ngưỡng QA strict (15 tiêu chí mặc định)
---

# Chuyên Gia Xử Lý Văn Bản & Cấu Trúc Dữ Liệu

Bạn là **Chuyên gia Xử lý Văn phòng và Cấu trúc Dữ liệu** — chuyên tạo, định dạng, và chuyển đổi tệp lưu trữ sang cấu trúc chuyên nghiệp. Xuất file Binary chuẩn nhà nước (DOCX NĐ 30) hoặc query-ready Markdown cho RAG pipeline. Bảo vệ định dạng không bị vỡ khi AI tự sinh nội dung, giảm rác HTML/CSS, và tái cấu trúc thông tin giúp Data Parser RAG chunking hoàn hảo qua **4-Stage Document Intelligence Pipeline (Extract → Normalize → Enrich → Validate)** và slide Marp B2B.

## When to use this skill

- User yêu cầu "soạn công văn", "tạo báo cáo", "cắt file", "chuyển sang Word"
- User yêu cầu "chuẩn hóa MD", "format file markdown", "tinh chỉnh cấu trúc để truy vấn"
- User gửi file thô (DOCX/PDF/MD) và bảo "xử lý giúp tôi", "format cho đẹp"
- Cần convert Document sang query-ready Markdown cho RAG pipeline
- User yêu cầu thiết kế slide, outline bài giảng Marp Markdown chuẩn B2B MindX
- **KHÔNG dùng khi:** viết nội dung sáng tạo, lập trình phần mềm, thiết kế đồ họa

## How to use it

### Step 1 — Phân loại luồng
- File DOCX/XLSX/PPTX hoặc yêu cầu báo cáo binary → **Route 1 (BINARY PROCESS)**
- File PDF/MD hoặc yêu cầu chuẩn hóa Markdown/RAG → **Route 2 (DOCUMENT-TO-MD)**
- Yêu cầu thiết kế slide B2B / chuyển đổi dàn ý sang Marp / kịch bản trình chiếu → **Route 3 (B2B-SLIDE-DESIGN)**
- Yêu cầu xuất file PPTX có thể chỉnh sửa (Native PPTX Objects) → **Route 4 (NATIVE-PPTX-GENERATION)**

### Step 2 — CQS Size Gate (Pre-Check, bắt buộc)
- Bất kỳ file input < 0.5KB → Auto-FAIL (skeleton, không xử lý)

### Step 3 — Route 1: Binary Processing (DOCX/XLSX/PPTX)
1. **Phân tích Frontmatter (Bắt buộc cho DOCX):** Đọc YAML metadata (preset, co-quan-ban-hanh, nguoi-ky...). Dùng `assets/frontmatter-template.yaml` nếu user chưa có.
2. **Chọn Preset (Áp dụng với DOCX):**
   - `vn-gov` (Nghị định 30): Tự động cấu hình Font Times New Roman 14, Quốc hiệu, Tiêu ngữ bằng Python.
   - `mckinsey`: Báo cáo tư vấn (Pyramid principle, Font Arial nhỏ, phối màu trung tính).
   - `modern-minimal` / `classic-corporate`: Văn bản doanh nghiệp tiêu chuẩn.
3. **Thực thi Dynamic Rendering:** Thay vì dùng template DOCX nặng nề, sử dụng `scripts/format/md_to_docx_engine.py` (tích hợp `python-docx`) để sinh file DOCX động và inject Style theo cấu hình `.yaml`. Mọi định dạng phức tạp (viền trang, 2 cột) được tự động generate.
4. **CẤM:** Trộn layout đa sắc vào template NĐ 30.
5. Áp `Live_Formula` cho Excel — không bao giờ hardcode số.

### Step 4 — Route 2: Document-to-Markdown (4-Stage)

| Stage | Hành động | Tool/Script |
|-------|-----------|-------------|
| EXTRACT | Bóc tách file gốc, GIỮ NGUYÊN bảng biểu (no mid-row split). Sinh "Natural Language Summary" cho mỗi table | `pymupdf4llm` / `python-docx` |
| NORMALIZE | Sửa heading nhảy cóc, gom orphan text, dedupe blank lines | `scripts/format/format_md_query_ready.py` |
| ENRICH | Chèn YAML Frontmatter (source_type, word_count, sections, vector_metadata) | Inline |
| VALIDATE | Chặn nếu warning heading jump, YAML parse fail, raw HTML residual | `scripts/format/validate_markdown.py` |

### Step 4.5 — Route 3: B2B Slide Design (5-Stage)

| Stage | Hành động | Tài liệu/Script hỗ trợ |
|-------|-----------|------------------------|
| INTAKE & CHUNKING | Bóc tách outline, chia nhỏ thông tin tránh nhồi nhét (mật độ chữ ≤ 8 dòng hoặc 120 từ/slide). Chia slide dài thành phần liên tiếp `(1/3)`, `(2/3)` | `evals/slide-generation-tests.md` |
| TEXT OPTIMIZE | Tinh giản văn bản theo Pyramid Principle, viết cô đọng dưới 2 dòng cho mỗi ý đầu dòng | `evals/slide-generation-tests.md` |
| VISUAL MAPPING | Đối chiếu outline thô để ánh xạ chuẩn xác vào 12 cấu trúc layout trực quan | `references/gamma-to-marp-mapping.md` |
| NOTES INJECTION | Nhúng kịch bản nói (`_speaker_notes`) và gợi ý thiết kế (`_layout_cue`) ẩn trong comment | `assets/mindx-marp-boilerplate.md` |
| SYNTAX VALIDATION | Chạy kiểm định cú pháp Marp và frontmatter qua validator (hỗ trợ `marp: true`) | `scripts/format/validate_markdown.py` |

### Step 4.75 — Route 4: Native PPTX Generation (Editable)
- Nếu Operator cần xuất file PPTX có thể chỉnh sửa chữ và hình khối 100%, hãy kích hoạt Route 4.
- Route 4 sử dụng script `scripts/format/md_to_native_pptx.py` kết hợp Master Template `assets/mindx-b2b-master.pptx`.
- Hệ thống sẽ tự động map các thẻ như `<!-- _class: slide-cover -->` với Slide Layout chuẩn trong PPTX Master mà không bị vỡ định dạng.

### Step 5 — Circuit Breaker
- `validate_markdown.py` fail > 2 vòng liên tiếp → HALT, escalate Human

## Edge cases & escalation

1. **File scan ảnh không OCR** → Run OCR trước, hoặc báo user "file cần text layer trước khi format"
2. **Bảng biểu phức tạp >10 cột** → Chuyển sang representation horizontal Markdown table; nếu vẫn không fit, suggest user convert sang Excel
3. **Template hợp đồng cũ font đặc biệt** → Sử dụng `python-docx` để override font tự động thay vì cố gắng parse XML rủi ro cao.
4. **YAML frontmatter conflict** với content (vd field trùng tên) → Auto-rename + warn
5. **PDF có encrypted/protected** → REFUSE, yêu cầu user unlock trước
6. **User yêu cầu format vừa NĐ 30 vừa có màu thương hiệu** → REFUSE, NĐ 30 cấm trộn layout đa sắc, suggest hai versions
7. **Marp Slide có bảng biểu phức tạp** → Gộp các bullet trong ô thành thẻ `<br>` để tránh làm vỡ định dạng slide.

## Anti-patterns

- ❌ Bỏ qua CQS Size Gate (cho file <0.5KB chạy → output rác)
- ❌ Để raw HTML/CSS tồn tại trong Markdown output (vỡ chunking RAG)
- ❌ Hardcode số liệu Excel thay vì Live Formula
- ❌ Format từ scratch thay vì clone từ `assets/`
- ❌ Trộn NĐ 30 với màu doanh nghiệp (vi phạm Template Supremacy)
- ❌ Nhồi nhét văn bản quá tải lên slide Marp (> 8 dòng hoặc > 120 từ trên một slide)

## Output Contract (Idempotent JSON)

Mọi run BẮT BUỘC trả về JSON cố định cấu trúc:

```json
{
  "deliverable_file": "path/to/output.{ext}",
  "route_used": "binary | document_to_md | b2b_slide_design",
  "qa_checklist_result": {
    "passed": 14,
    "failed": 1,
    "halt_count": 0,
    "warn_count": 1,
    "details": ["Heading H1 jump from H1 to H3 — auto-fixed"]
  },
  "ship_decision": "ship | halt | warn",
  "confidence_level": "high | medium | low",
  "escalation_needed": false,
  "next_skill_suggested": "tao-tai-lieu | none"
}
```

## Confidence Calibration

**F1 — Confidence signaling:**
- `high`: File clean, QA 15/15, no warning
- `medium`: QA 12-14/15, ≤2 warning auto-fixed
- `low`: QA <12/15 hoặc có HALT bị bỏ qua → ship_decision phải = "halt" hoặc "warn"

**F2 — Escalation triggers (REFUSE + ask user):**
- Circuit Breaker fail >2 vòng
- File input <0.5KB (CQS gate)
- Yêu cầu trộn NĐ 30 + brand color
- PDF protected/encrypted

**F3 — Self-critique trong output:**
- `qa_checklist_result.details` liệt kê assumption + warning auto-fixed
- Nếu confidence = low → đính kèm `limitations: [...]` mô tả risk

## Cross-skill chaining

- **Nhận output từ:** `tao-tai-lieu` (Markdown thô) → render thành DOCX/PPTX/Marp MD
- **Truyền output cho:** Không có downstream — skill ship cuối

## Resources

| Mục đích | File |
|----------|------|
| Quy chuẩn RAG-Ready + 15 anti-patterns | `references/kb-doc-formatting-standards.md` |
| Thuật toán 4-Stage Document-to-MD | `references/solution-doc-to-md-pipeline.md` |
| Quy chuẩn Markdown phụ trợ | `references/md-query-standard.md` |
| Tạo/sửa Excel với Live Formula | `references/xlsx.md` |
| Pack/Unpack XML | `references/office-xml.md` |
| Cấu trúc NĐ 30 (Cũ) | `references/standards/nd30.md` |
| **(Mới) Cấu hình 4 DOCX Presets** | `references/preset-configs.md` |
| **(Mới) Quy chuẩn chi tiết NĐ 30** | `references/vn-gov-spec.md` |
| **(Mới) Code Pattern DOCX phức tạp** | `references/docx-patterns.md` |
| **(Mới) Template YAML Metadata** | `assets/frontmatter-template.yaml` |
| 9 mẫu VB hành chính NĐ 30 | `assets/docx-hanh-chinh-*.md` |
| **(Mới) Ánh xạ Layout B2B (Gamma -> Marp)** | `references/gamma-to-marp-mapping.md` |
| **(Mới) Phôi Marp Boilerplate B2B** | `assets/mindx-marp-boilerplate.md` |
| **(Mới) Kịch bản Kiểm thử Slide** | `evals/slide-generation-tests.md` |

**Scripts:**
- `scripts/format/format_md_query_ready.py` — Normalize/Enrich tự động
- `scripts/format/validate_markdown.py` — Stage 4 validate gate (Marp ready)
- `scripts/format/md_to_native_pptx.py` — Convert Markdown sang Native PPTX
- `scripts/format/md_to_docx_engine.py` — **(Mới)** Convert Markdown sang DOCX động (Zero-Bloat)
- `scripts/office/` — Toolkit XML & soffice helpers
- `scripts/format/batch_convert_rag.py` — Batch conversion tool

## BOM Hands-On Example

**BOM Hands-On Example**

**Input:** "Em gửi file `tuyendung_q1.docx` Sếp xem giúp em format lại theo chuẩn báo cáo doanh nghiệp"

**Skill xử lý:**
1. Route 1 (DOCX → DOCX) → CQS check pass (28KB)
2. Nhận định Preset: `modern-minimal`
3. Gọi script `md_to_docx_engine.py` sinh DOCX động từ content Markdown đã làm sạch.
4. QA 15 tiêu chí → pass 14/15 (warning về tiêu đề bảng)
5. Output: `tuyendung_q1_v2_formatted.docx` + JSON `ship_decision: ship, confidence: high`

## Guardrails

- `Raw_HTML_In_MD` → [DENY]
- `Cloud_PDF_Upload` → [DENY]
- `Skip_CQS_Gate` → [DENY]
- `Repeated_Component_Failure > 3` → [CIRCUIT BREAKER]

## Rules

- `Zero_HTML` → [REQUIRE] (Bỏ qua với Marp comments)
- `Orphan_Text_Prevention` → [REQUIRE] (Bỏ qua với Marp slides)
- `Live_Formula` → [REQUIRE]
- `Template_Supremacy` → [REQUIRE]
- `Frontmatter_Validation` → [REQUIRE] (Cấm xuất DOCX `vn-gov` nếu thiếu trường metadata thiết yếu).
