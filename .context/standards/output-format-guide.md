---
title: "Output Format Guide"
domain_tags: ["format", "output", "standard"]
summary: "Format chuẩn cho mọi loại output trong workspace"
applicable_agents: ["ALL"]
---

# Output Format Guide

## Format theo loại output

| Output Type | Format | Max Length | Must Include |
|-------------|--------|-----------|-------------|
| Quick Answer | Inline text | 200 từ | Direct answer + source if data |
| Analysis Summary | Structured markdown | 500 từ | Insight + So What + Now What |
| Full Report | Template-based markdown | 1500 từ | Exec Summary + Sections + Next Steps |
| Memo | Template-based markdown | 400 từ | TL;DR + Context + Recommendation + Ask |
| Email Draft | Inline text | 200 từ | Subject + Body + CTA |
| Meeting Minutes | Template-based markdown | 600 từ | Info + Decisions + Action Items |
| Slide Outline | Structured list | Slide count | Title + Key Message + Notes per slide |
| Project Brief | Template-based markdown | 800 từ | Objective + Scope + Team + Timeline + Risk |
| WBS | Hierarchical list/table | Based on project | Phases → Work packages → Tasks |
| RACI | Table | Based on project | Tasks × People, 1 A per row |
| Status Report | Template-based markdown | 400 từ | RAG + Done + Progress + Blocked + Next |
| Research Brief | Template-based markdown | 1000 từ | Findings + Sources + Confidence + Gaps |
| Decision Matrix | Table + recommendation | 500 từ | Criteria × Options + Weights + Recommendation |

## Language Rules
- Default: Vietnamese
- Switch English khi: user dùng English, hoặc output dành cho international audience
- Mixed: Vietnamese narrative + English terms (KPI, ROI, CRM...) là OK
- Formal titles: Giữ nguyên tiếng Anh (Executive Summary, Status Report) hoặc dùng cả hai

## Formatting Rules
- **Headers**: Dùng ## cho sections chính, ### cho sub-sections
- **Bold**: Chỉ cho key terms, numbers quan trọng, recommendations
- **Tables**: Dùng khi so sánh ≥3 items hoặc structured data
- **Bullets**: Max 5-7 items per list. Nếu nhiều hơn → nhóm lại
- **Numbers**: Dùng separator (1,000,000 hoặc 1.000.000), consistent trong 1 output
