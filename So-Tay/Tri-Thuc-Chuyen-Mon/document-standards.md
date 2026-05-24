---
title: "Document Standards"
domain_tags: ["writing", "report", "memo", "email", "minutes"]
summary: "Chuẩn viết report/memo/email/minutes, tone guide, format quan-ly-quy-tac"
keywords: ["report", "memo", "email", "minutes", "writing", "format", "tone"]
applicable_agents: ["PRO-W03"]
last_updated: "2026-04-22"
version: "1.0.0"
---

# Document Standards — PRO-W03 Domain Knowledge

## TL;DR
Detect genre trước → load đúng format → viết theo Pyramid → self-check quality. Mỗi loại văn bản có structure riêng, tone riêng, length riêng. KHÔNG one-size-fits-all.

## Genre Detection & Format

### 1. Business Report (báo cáo tuần/tháng/quý)
**Structure**: Executive Summary (3-5 câu, KẾT LUẬN trước) → Key Metrics (RAG status) → Details by Section → Recommendations → Next Steps
**Tone**: Professional, data-driven, objective
**Length**: 1-3 trang tùy frequency (weekly ngắn hơn quarterly)
**Template**: `.context/templates/report-template.md`

### 2. Memo (đề xuất, thông báo cho leadership)
**Structure**: TL;DR (1-2 câu) → Context (tại sao viết) → Recommendation → Supporting Arguments → Ask (cần approval gì?)
**Tone**: Concise, persuasive, respect time
**Length**: 1 trang MAX. Nếu dài hơn → chuyển thành report
**Template**: `.context/templates/memo-template.md`

### 3. Email (professional)
**Structure**: Subject line clear → Opening (purpose) → Body (key points, max 3) → CTA → Closing
**Tone**: Warm-professional, adapt theo relationship
**Length**: <200 từ ideal. >300 từ → suggest chuyển thành attachment

### 4. Meeting Minutes (biên bản họp)
**Structure**: Meeting info (date, attendees, objective) → Key Discussions → Decisions Made → Action Items (who, what, when) → Next Meeting
**Tone**: Factual, neutral, action-oriented
**Length**: 1-2 trang. Focus decisions + actions, KHÔNG transcript
**Template**: `.context/templates/meeting-minutes.md`

### 5. Executive Summary
**Structure**: Recommendation (1-2 câu) → 3 supporting arguments → Key data points → Next step
**Tone**: Confident, strategic, no hedge words
**Length**: 200-400 từ. Phải đứng độc lập (đọc chỉ summary vẫn hiểu đủ)

## Tone Guide

| Audience | Tone | Avoid |
|----------|------|-------|
| C-level / BGĐ | Strategic, concise, numbers-driven | Jargon kỹ thuật, detail quá sâu |
| Manager / Team lead | Action-oriented, clear expectations | Vague requests, passive voice |
| Cross-functional | Neutral, explain context, define terms | Assume shared knowledge |
| External (đối tác, khách) | Professional, warm, benefit-focused | Internal acronyms |

## Writing Quality Checklist (self-check trước deliver)
- [ ] Pyramid: Kết luận ở đầu, không phải cuối?
- [ ] Mỗi paragraph có 1 main point rõ ràng?
- [ ] Không có câu >30 từ?
- [ ] Action items có rõ WHO, WHAT, WHEN?
- [ ] Số liệu có source/date range?
- [ ] Đúng tone cho audience?
- [ ] Length phù hợp genre?
