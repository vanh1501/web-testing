---
id: "WF-DOC-PRODUCTION-01"
name: "w-san-xuat-tai-lieu"
description: "Pipeline End-to-End sản xuất và chuẩn hóa tài liệu doanh nghiệp đa loại (Báo cáo, Đề xuất, SOP, Slide Deck, Biên bản họp, Báo giá). Routing theo document type. Mandatory chain `s-tao-tai-lieu` → `s-chuan-hoa-tai-lieu` để xuất Binary thực."
version: v2.0
status: Production-Ready
semantic_triggers: ['soạn tài liệu', 'viết báo cáo', 'làm slide', 'chuẩn hóa format', 'format file', 'tạo biên bản', 'pitch deck', 'đề xuất', 'báo giá', 'quotation', 'SOP doc']
owner: "PRO-W03"
skill_target: "s-tao-tai-lieu, s-chuan-hoa-tai-lieu"
hitl_timeout: "24h"
retry_policy: {max_attempts: 3, backoff: exponential_1s_2s_4s, fallback: "log_to_ACTION-LOG_and_report_human"}
---

- **👤 Owner:** `[@PRO-W03]`
- **🛠 Skill Target:** `[s-tao-tai-lieu, s-chuan-hoa-tai-lieu]`
- **⏱ HITL Timeout:** 24h
- **🔄 Circuit Breaker:** retry 3 lần, fallback → ACTION-LOG + human

# Quy Trình: /w-san-xuat-tai-lieu (v2.0 — Document Production Pipeline)

## Purpose & Scope

**Purpose:** Hỗ trợ Operator tạo tài liệu doanh nghiệp chuyên nghiệp từ nội dung thô. Chuẩn hóa format (Heading, Bullet, Table) + văn phong (Tone & Voice). Output: file Binary (DOCX/PPTX) ready-to-share.

**Scope:** Từ Outline đến xuất xưởng Binary. KHÔNG bao gồm: phân tích data (dùng `/w-phan-tich-va-bao-cao`), nghiên cứu market (dùng skill `00-nghien-cuu-thi-truong`), hợp đồng pháp lý.

## Trigger

User: "viết báo cáo X", "làm slide", "soạn SOP", "tạo pitch deck", "format tài liệu", "biên bản họp Q1".

## Prerequisites

- [ ] Nội dung nguồn ≥100 từ (bullet points / meeting notes / draft / output từ skill khác)
- [ ] Intent rõ (đối tượng: BOD? khách? nhân viên? đào tạo?)
- [ ] Output channel mong muốn (DOCX-ready? Slide Marp? Package?)

## Routing — Step 0

| Document Type | Route | Style mặc định |
|---------------|-------|----------------|
| executive_report, business_proposal | **Route A: Executive** | executive style, Pyramid structure |
| sop, memo | **Route B: Operational** | operational style, step-by-step + checklist |
| meeting_minutes | **Route C: Meeting** | formal, action-item focus |
| training_handout | **Route D: Training** | training style, có ví dụ + bài tập |
| quotation, pitch_deck | **Route E: Sale** | persuasive, client-facing |

**Decision:** Operator chọn route hoặc system auto-detect từ keyword. Sai route có thể switch giữa chừng.

## Steps

> [!IMPORTANT] KARPATHY VERIFICATION MANDATE
> Mỗi Step: `[Step] -> verify: [Tiêu chí]`. CẤM Blind Looping.

### Step 1 — Brief Intake
**Action:** Hỏi Operator 3 thông tin tối thiểu: (a) Document type + audience, (b) Mục đích cốt lõi, (c) Output channel (DOCX/Slide/Both).
**Verify:** 3 thông tin clear. Nếu thiếu, hỏi tối đa 2 câu rồi default theo Route.

### Step 2 — Outline Generation
**Action:** Gọi `s-tao-tai-lieu` (sub-mode: outline_only) với route mapping (Route A → Pyramid; B → SCQA; E → AIDA). Output: Markdown outline H1/H2.
**Verify:** Outline có ≥3 section H1/H2, không bullet thô.

### Step 3 — Outline Approve (HITL Gate 1)
**Action:** Trình bày Outline cho Operator.
**Decision:** Approve → Step 4 | Modify → re-render Outline | Reject → quay Step 1 lấy thêm Brief.
**HITL Timeout:** 24h. Sau timeout: pause + reminder; sau 48h archive draft.

### Step 4 — Content Render
**Action:** Gọi `s-tao-tai-lieu` (full content render) — viết chi tiết từng H2 section theo style profile. Apply principle:
- MECE (no overlap)
- 1 idea/slide (cho Slide route)
- Action Title (cho Slide BOD)
- Owner per step (cho SOP route)
**Verify:** Output Markdown đầy đủ section + có Next Steps section cuối.

### Step 5 — Quality Self-Check
**Action:** Gọi `s-tao-tai-lieu` (sub-mode: self_qa) — check confidence, list assumptions, identify gaps.
**Verify:** Output JSON có `confidence_level` + `<!-- skill-notes -->` block.

### Step 6 — Mandatory Chain → chuan-hoa
**Action:** Tự động chain `s-chuan-hoa-tai-lieu` để xuất Binary thực:
- Truyền tham số Metadata Style (e.g., `modern-minimal`, `mckinsey`) để script tự động generate DOCX bằng `python-docx`.
- DOCX/PPTX path: `Kho-Du-Lieu/Ket-Qua/{filename}.{ext}`
- QA 15 tiêu chí chạy tự động
**Verify:** Output Contract từ s-chuan-hoa-tai-lieu có `ship_decision: ship` + file exists.

### Step 7 — Final Confirm (HITL Gate 2 — optional)
**Action:** Trình bày Binary file path + JSON QA report.
**Decision:** Nếu Route E (Sale) hoặc Route A (BOD/khách) → ask final confirm trước khi declared "done".
**HITL Timeout:** 24h. Sau timeout: auto-finalize (file đã xuất, không rollback).

## HITL Gates Summary

| Gate | Step | Timeout | Action on timeout |
|------|------|---------|-------------------|
| Gate 1 — Outline Approve | Step 3 | 24h | Pause + reminder; 48h archive |
| Gate 2 — Final Confirm (Route A, E only) | Step 7 | 24h | Auto-finalize, file đã xuất |

## Circuit Breaker Policy

| Failure mode | Detection | Retry | Fallback |
|--------------|-----------|-------|----------|
| Skill `s-tao-tai-lieu` timeout | 60s no response | 3 lần | ACTION-LOG + ask human review |
| Skill `s-chuan-hoa-tai-lieu` QA fail >2 vòng | QA report halt_count >0 | 1 lần fix | REFUSE ship, escalate human |
| Content thô <100 từ | Step 1 validate | 0 | REFUSE, ask Operator cung cấp thêm |
| Document type mâu thuẫn style | Skill detect | 0 | REFUSE, ask Operator choose 1 |

## Edge Cases & Recovery

1. **Content thô quá sơ sài (<100 từ)** → REFUSE Step 4, ask Operator cung cấp thêm; KHÔNG tự bịa data
2. **Tài liệu đầu vào >20 trang** → DỪNG, báo User chia nhỏ để tránh Hallucination. KHÔNG âm thầm tóm tắt làm mất dữ liệu gốc
3. **Conflict 2 numbers trong source** (vd 2 KPI mâu thuẫn) → Flag, ask Operator chọn canonical
4. **User muốn mix 2 style** (vd executive + training) → REFUSE, suggest split 2 deliverables tách biệt
5. **Quotation lớn (>500M VND)** → Escalate Operator verify giá + có signature người phê duyệt trước ship
6. **Brand asset 3rd party (logo, trademark)** → Ask permission/license, KHÔNG tự thêm vào slide khách
7. **SOP có data nhạy cảm (PII, salary)** → REFUSE inclusion, ask anonymize trước
8. **Pitch deck >20 slide** → Suggest cut về ≤15 (rule "less is more" cho Sale)

## Output Contract (Idempotent JSON)

```json
{
  "workflow_id": "WF-DOC-PRODUCTION-01",
  "route_executed": "A | B | C | D | E",
  "run_status": "success | halt_at_gate | halt_at_failure",
  "document_metadata": {
    "type": "executive_report",
    "style": "executive",
    "audience": "BOD",
    "output_channel": "package (docx + pptx)"
  },
  "skills_invoked": ["s-tao-tai-lieu", "s-chuan-hoa-tai-lieu"],
  "deliverable_files": [
    {"path": "Kho-Du-Lieu/Ket-Qua/report-q1-2026.md", "type": "markdown"},
    {"path": "Kho-Du-Lieu/Ket-Qua/report-q1-2026.docx", "type": "docx"},
    {"path": "Kho-Du-Lieu/Ket-Qua/report-q1-2026.pptx", "type": "pptx"}
  ],
  "qa_summary": {
    "qa_passed": 14,
    "qa_total": 15,
    "ship_decision": "ship | warn | halt",
    "confidence_level": "high | medium | low"
  },
  "hitl_gates_triggered": ["Gate 1"],
  "circuit_breaker_activated": false,
  "next_workflow_suggested": "none (deliverable ship)"
}
```

## Cross-Workflow Chaining

- **Receives from:** `00-phan-tich-va-bao-cao` (Route 3, 4 — báo cáo tuần/tháng cần format chuẩn hóa)
- **Hands off to:** Không có downstream — deliverable ship cuối
- **Internal chain:** Step 6 MANDATORY chain `s-tao-tai-lieu` → `s-chuan-hoa-tai-lieu`

## Validation

- [ ] Document type + style xác định trước Step 2
- [ ] Outline approved bởi Operator (Gate 1) trước Step 4
- [ ] Content có Next Steps section
- [ ] Mandatory chain chuan-hoa-tai-lieu đã chạy
- [ ] QA 15 tiêu chí pass ≥12/15 (ship hoặc warn, no halt)
- [ ] File Binary tồn tại đúng path
- [ ] JSON Output Contract đầy đủ

## Resources

- Skill: `s-tao-tai-lieu` (sub-modes: outline_only, content_render, self_qa)
- Skill: `s-chuan-hoa-tai-lieu` (QA 15 tiêu chí + xuất Binary)
- Output path: `Kho-Du-Lieu/Ket-Qua/`
- Brand kit (optional): `assets/BO-NHAN-DIEN.md` nếu Route E cần brand profile
