---
name: s-tao-tai-lieu
description: >
  Universal skill xây dựng synchronized multi-artifact materials (Bộ tài liệu đa định dạng đồng bộ).
  Kiến trúc 5 tầng: Design System + Brand Kit + Content Model + Format Adapters + Workflows.
  Produce deck + workbook + handout + report đồng bộ từ 1 nguồn content duy nhất, apply brand kit per-client.
  Kích hoạt khi user nói "tạo training kit", "deck + workbook đi cùng nhau", "material đa thương hiệu",
  "đồng bộ deck workbook", "training materials cho client X", "brand kit", "swap brand", "tạo slide",
  "viết báo cáo", "tạo báo giá". Sau khi sinh cấu trúc, BẮT BUỘC chuyển giao `chuan-hoa-tai-lieu` render.
version: v2.0
status: Production-Ready
hook_summary:
  - HOOK_DOCUMENT_TYPE: loại tài liệu (executive_report, business_proposal, sop, meeting_minutes, training_handout, quotation, pitch_deck)
  - HOOK_OUTPUT_CHANNEL: kênh đầu ra (docx-ready, marp-slide, google-slides-ready, package)
  - HOOK_STYLE_PROFILE: tone (executive, formal, operational, training, persuasive, client-facing)
  - HOOK_BRAND_PROFILE: brand kit nếu có
---

# Material Studio (Document Artifact Builder)

Universal skill produce **multi-artifact training/presentation/reporting materials** đồng bộ từ 1 nguồn content, apply brand kit per-client.
**Kiến trúc 5 tầng:** 5. Orchestrator -> 4. Use-Case Workflows -> 3. Format Adapters -> 2. Content Model -> 1. Design System & Brand Kit.

## When to use this skill

- **Phòng Đào tạo:** có dàn ý môn học → cần Handout học viên hoặc Slide giáo án
- **Phòng Ops/HR:** có bước làm việc thô → cần SOP chuẩn hoặc Memo nội bộ
- **Phòng Sale:** có tính năng/giá → cần Báo giá (Quotation) hoặc Pitch Deck
- **BOD/Manager:** có meeting notes thô → cần Biên bản họp (Minutes) format chuẩn

**KHÔNG dùng khi:**
- Cần xử lý/clean data raw (dùng `phan-tich-du-lieu` trước)
- Cần research market (dùng `nghien-cuu-thi-truong` trước)
- Cần hợp đồng pháp lý từ zero (chuyển pháp chế)
- Input thiếu — yêu cầu user cung cấp content trước

## How to use it

### Đầu vào bắt buộc

- **Nội dung nguồn:** Bullet points / meeting notes / draft thô / output từ skill khác
- **Intent:** Để báo cáo Sếp / đào tạo nhân viên / gửi báo giá khách / etc
- **Output mong muốn:** DOCX-ready (văn bản) hay SLIDE-ready (thuyết trình)

### Step 1 — Intake & Phân loại (Smart Routing)

Hỏi user 5 câu (skip nếu đã rõ):
1. **Use case?** training / presentation / reporting / proposal
2. **Client là ai?** → Map sang brand_kit_id (vd: mindx, bank_abc). Nếu client mới, gọi Brand Intake.
3. **Source material gì?** PPTX / DOCX / MD / Scratch.
4. **Project metadata?** Title, audience, duration.
5. **Cần artifact nào?** (VD: deck + workbook + handout).

<<HOOK_DOCUMENT_TYPE>>
options:
  - executive_report: Báo cáo điều hành (BOD)
  - business_proposal: Đề xuất/dự án (Marketing/Sale)
  - sop: Quy trình (Ops/HR)
  - meeting_minutes: Biên bản họp (All)
  - training_handout: Tài liệu đào tạo (Training)
  - quotation: Báo giá (Sale)
  - pitch_deck: Hồ sơ năng lực (Sale)
<</HOOK_DOCUMENT_TYPE>>

### Step 2 — Áp Style & Tone

<<HOOK_STYLE_PROFILE>>
options:
  - executive: Ngắn gọn, action-oriented (BOD)
  - operational: Rõ bước, có checklist, có owner (Ops)
  - training: Dễ hiểu, trực quan, có ví dụ (Học viên)
  - persuasive: Thuyết phục, nhấn mạnh value (Sale)
  - formal/client_facing: Trang trọng (Khách hàng)
  - internal: Casual, mộc mạc (Nội bộ)
<</HOOK_STYLE_PROFILE>>

### Step 3 — Xây dựng Content Model (YAML)
Convert source thành Content Model format-agnostic. Đọc schema tại `references/content-model.md`. Cho user review Draft Content Model trước khi render.

### Step 4 — Render Multi-Artifact (Adapters)
Dựa vào lựa chọn ở Step 1, invoke các adapter (đọc `adapter-workbook.md`, `adapter-deck.md`).
- **Deck (Marp):** 1 slide = 1 idea, max 3-4 bullet cấp 1 (Action Title).
- **Workbook / Report (DOCX):** Bảng biểu chặt chẽ, Heading H1/H2 rõ ràng.
- **Handout:** 1-page PDF.
Render order: workbook → deck → handout → facilitator notes.
Tiến hành **Consistency Check** (Đồng bộ số lượng block, tiêu đề, brand màu sắc).

### Step 5 — Mandatory Handoff

> [!IMPORTANT]
> Sau khi sinh Markdown thô (DOCX hay SLIDE), KHÔNG ĐƯỢC DỪNG hoặc tự kết thúc nhiệm vụ.
> BẮT BUỘC chuyển giao dữ liệu cho `chuan-hoa-tai-lieu` để chạy QA 15 tiêu chí + xuất file Binary thực (DOCX/PPTX).

## Edge cases & escalation

1. **User chỉ nói "viết slide" không cho content** → REFUSE, yêu cầu user cung cấp nội dung nguồn
2. **Content thô có conflict** (vd 2 KPI mâu thuẫn) → flag conflict, ask user chọn version canonical
3. **User yêu cầu mix 2 style** (vd executive + training trong cùng 1 doc) → REFUSE, suggest 2 deliverables tách
4. **Quotation có giá trị lớn (>500M VND)** → escalate user verify giá + có signature người phê duyệt
5. **Content có trích dẫn 3rd party (logo, brand)** → ask permission/license trước khi đưa vào slide khách
6. **SOP có data nhạy cảm** (salary, customer PII) → REFUSE inclusion, ask anonymize
7. **Pitch deck >20 slide** → suggest cut về ≤15 slide (rule "less is more" cho Sale)
8. **Meeting minutes >5 trang** → suggest tách thành Executive Summary 1 trang + Full Minutes appendix

## Anti-patterns

- ❌ Tài liệu BOD dài thòng thiếu Executive Summary
- ❌ SOP không gán Owner cho từng step
- ❌ Slide có >12 bullet (bế từ Word qua)
- ❌ Tự bịa data khi content thô sơ sài (phải hỏi user)
- ❌ Bỏ Mandatory Handoff (Markdown thô không phải deliverable cuối)
- ❌ Sale pitch dài >15 slide
- ❌ Training handout không có Bài tập / Practice section

## Output Contract (Idempotent JSON)

```json
{
  "deliverable_file": "path/to/output.md",
  "document_type": "executive_report | business_proposal | sop | meeting_minutes | training_handout | quotation | pitch_deck",
  "style_profile": "executive | formal | operational | training | persuasive | client_facing | internal",
  "output_channel": "docx-ready | marp-slide | google-slides-ready | package",
  "structure": {
    "h1_count": 1,
    "h2_count": 5,
    "h3_count": 8,
    "tables": 2,
    "bullets_total": 24,
    "page_estimate": 4
  },
  "next_steps_section_present": true,
  "ship_decision": "ship | warn | halt",
  "confidence_level": "high | medium | low",
  "escalation_needed": false,
  "next_skill_suggested": "chuan-hoa-tai-lieu (mandatory)"
}
```

## Confidence Calibration

**F1 — Confidence signaling:**
- `high`: Content thô đủ data, intent rõ, style profile match phòng ban, structure check pass (H1/H2 rõ, có Next Steps)
- `medium`: Content thô có gap nhỏ (vd thiếu 1 KPI), nhưng skill có thể fill in template, confidence calibrated trong output
- `low`: Content thô quá sơ sài, skill phải auto-generate >30% content → warning user cần review kỹ

**F2 — Escalation triggers:**
- Content thô thiếu key data → REFUSE, ask user
- Conflict 2 numbers trong source → ask user chọn
- User yêu cầu mix style → REFUSE, suggest split
- Quotation lớn (>500M) → ask verification
- Trích dẫn brand 3rd party → ask permission

**F3 — Self-critique trong output:**
- Section `<!-- skill-notes -->` cuối file Markdown, liệt kê:
  - Assumptions made (vd "Coi target Q2 là 12 tỷ theo content thô")
  - Gaps filled (vd "Bổ sung intro paragraph vì content thô thiếu")
  - User-confirmation-needed items
- Nếu confidence=low → warning đầu file "Tài liệu này cần BOM review trước khi gửi đi"

## Cross-skill chaining

- **Nhận output từ:**
  - `s-phan-tich-du-lieu` (Markdown Pyramid report → render PPTX BOD)
  - `s-nghien-cuu-thi-truong` (Research brief → render DOCX/PPTX)
  - `s-xay-dung-quy-trinh` (5 process deliverables → render bộ SOP DOCX)
  - `s-phan-tich-yeu-cau` (Implementation plan → render DOCX)
- **Truyền output cho:** `chuan-hoa-tai-lieu` (MANDATORY — render Binary thực)
- **Validation handshake:** Output có H1 title rõ, H2 sections, Next Steps section. `chuan-hoa-tai-lieu` parse structure để QA.

## Resources

| Variant | File |
|---------|------|
| Business proposal DOCX | `references/variant-business-proposal-docx.md` |
| Executive report DOCX | `references/variant-executive-report-docx.md` |
| Executive slide deck (Marp) | `references/variant-executive-slide-deck.md` |
| Meeting minutes DOCX | `references/variant-meeting-minutes-docx.md` |
| SOP DOCX | `references/variant-sop-docx.md` |
| Customize prompt scaffold | `references/customize-prompt-scaffold.md` |
| Operator handoff | `references/operator-handoff.md` |
| **(Mới) Skeleton Patterns** | `references/skeleton-patterns.md` |
| **(Mới) Brand Kit Schema** | `references/brand-kit-schema.md` |
| **(Mới) Content Model Schema** | `references/content-model.md` |
| **(Mới) Adapter Workbook** | `references/adapter-workbook.md` |
| **(Mới) Adapter Deck** | `references/adapter-deck.md` |
| **(Mới) Workflow Training** | `references/workflow-training.md` |

**Output templates:**
- `assets/output-templates/docx-business-letter-template.md`
- `assets/output-templates/docx-meeting-minutes-template.md`
- `assets/output-templates/docx-proposal-template.md`
- `assets/output-templates/docx-report-template.md`
- `assets/output-templates/docx-sop-template.md`
- `assets/output-templates/slide-marp-template.md`
- `assets/output-templates/package-report-plus-slide-template.md`

**Scripts:**
- `scripts/export_docx_from_markdown.py` — Helper export DOCX từ Markdown (chain hỗ trợ chuan-hoa-tai-lieu)

## BOM Hands-On Example

**Input từ BOM Sale:**
> "Em có content đề xuất chiến dịch Q2 cho khách ABC: budget 500tr, kỳ vọng ROI 4x, 3 phase deploy. Sếp giúp em làm Pitch Deck"

**Skill xử lý:**
1. Document_type: pitch_deck; style: persuasive client-facing
2. Smart routing: Sale → Vấn đề → Giải pháp → Giá → CTA structure
3. Render Marp Markdown 10 slides:
   - Slide 1: Title + Logo placeholder
   - Slide 2: Vấn đề ABC đang gặp (1 idea)
   - Slide 3: Giải pháp chiến dịch
   - Slides 4-6: 3 Phase deploy
   - Slide 7: Budget breakdown 500tr
   - Slide 8: ROI projection 4x
   - Slide 9: Timeline
   - Slide 10: CTA + contact
4. Mỗi slide ≤4 bullet cấp 1, Action Title style
5. Mandatory handoff → call `chuan-hoa-tai-lieu` render PPTX với brand profile
6. JSON contract: `ship_decision: ship, confidence: high, next_skill: chuan-hoa-tai-lieu`

## Guardrails

- `Empty_Content_Render` → [DENY] Không sinh tài liệu nếu content thô <100 từ
- `Mandatory_Handoff_Skip` → [DENY] Markdown thô không phải deliverable cuối, PHẢI chain qua `chuan-hoa-tai-lieu`
- `Hallucinate_Numbers` → [DENY] Không bịa số liệu, phải dùng từ content nguồn hoặc ask user
- `Style_Mix` → [DENY] Không trộn 2 style trong 1 deliverable

## Rules

- `Executive_Summary_First`: Tài liệu BOD/proposal LUÔN có Executive Summary đầu
- `Owner_Per_Step`: SOP có owner mỗi step
- `One_Idea_Per_Slide`: Slide deck 1 idea/slide, ≤4 bullet
- `Next_Steps_Required`: Mọi tài liệu có Next Steps section
- `Action_Title_Slide`: Slide tiêu đề "Q1 ROAS giảm 30% do channel X" thay vì "Q1 Performance"
