---
title: "Data Analysis Methodology"
domain_tags: ["data", "analysis", "visualization"]
summary: "Pipeline phân tích, chart selection guide, insight narrative framework"
keywords: ["excel", "csv", "analysis", "chart", "insight", "variance", "trend"]
applicable_agents: ["PRO-W01"]
last_updated: "2026-04-22"
version: "1.0.0"
---

# Data Analysis — PRO-W01 Domain Knowledge

## TL;DR
Pipeline: RECEIVE → AUDIT → ANALYZE → NARRATE → DELIVER. Kết luận trước (Pyramid), trả lời "So what?" và "Now what?". Chọn chart theo data type, không theo thói quen.

## Analysis Pipeline

### Step 1: RECEIVE & AUDIT
- Đọc file (pandas), profile: shape, types, missing%, duplicates, date range
- Auto-fix nếu đơn giản (<5% missing, format issues, duplicates)
- Báo cáo audit 3-5 dòng — chỉ flag vấn đề nghiêm trọng

### Step 2: ANALYZE — Route theo intent

| User Intent | Pattern | Kỹ thuật |
|-------------|---------|----------|
| So sánh MoM/YoY/vs target | COMPARISON | Variance decomposition, Index 100, waterfall |
| Cơ cấu / tỷ trọng | BREAKDOWN | ABC-Pareto, pie/treemap, top-N analysis |
| Tại sao tăng/giảm | ANOMALY | Outlier detection, correlation, decomposition |
| Xu hướng / dự báo | TREND | Moving averages, seasonality detection |
| Phân khúc | SEGMENTATION | RFM, cohort, clustering |

### Step 3: NARRATE (Insight Framework)
Mỗi insight PHẢI có 3 phần:
1. **Observation**: "Doanh thu tháng 3 giảm 15% so với tháng 2"
2. **So What**: "Nguyên nhân chính từ segment B2B giảm 23%, trong khi B2C tăng 5%"
3. **Now What**: "Cần deep-dive nguyên nhân B2B giảm — kiểm tra pipeline deals tháng 3"

### Step 4: DELIVER — Format theo audience
- **Cho sếp**: Executive summary 5-7 bullets, top 3 insights, 1 recommended action
- **Cho team**: Chi tiết hơn, bảng data, multiple charts, action items per team
- **Cho meeting**: Talking points format, highlight surprises

## Chart Selection Guide

| Data Type | Best Chart | Khi nào KHÔNG dùng |
|-----------|-----------|-------------------|
| So sánh categories | Bar/Column | >12 categories → dùng horizontal bar |
| Trend theo thời gian | Line | <3 data points → dùng bar |
| Tỷ lệ / phần trăm | Stacked bar, Pie (≤5 slices) | >5 slices → dùng bar sorted |
| Phân bố | Histogram, Box plot | Audience non-technical → dùng bar + percentile labels |
| Mối quan hệ 2 biến | Scatter | <10 points → dùng table |
| Actual vs Target | Bullet chart, Waterfall | Audience muốn simplicity → dùng bar + target line |

## Quality Rules
- PHẢI cite data source và date range trong mọi output
- CẤM hallucinate số liệu — nếu data không có thì nói rõ
- PHẢI flag cỡ mẫu nhỏ (n<30) hoặc data quality issues
- NÊN suggest next analysis nếu phát hiện pattern thú vị
