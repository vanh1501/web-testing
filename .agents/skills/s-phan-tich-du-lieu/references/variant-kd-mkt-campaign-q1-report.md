### 4.1 `variant-kd-mkt-campaign-q1-report.md`

**Context:** Việt Anh (BOM KD MKT) cần báo cáo Q1 campaign performance cho BOD Thursday. Data input: Excel raw từ Facebook Ads Manager + Google Ads + Influencer tracking.

#### HOOK customization

```yaml
HOOK_INPUT_SCHEMA:
  required_columns:
    - date: YYYY-MM-DD
    - campaign_id: string
    - channel: enum (facebook_ads / google_search / influencer / direct)
    - brand_line: enum (line_a / line_b / line_c)
    - impressions: int
    - clicks: int
    - conversions: int
    - spend: float (VND)
    - revenue: float (VND)
  sample_row:
    - 2026-03-15, CAMP-FB-001, facebook_ads, line_a, 125400, 1830, 47, 8250000, 28500000

HOOK_METRIC_CATALOG:
  primary:
    - ROAS: revenue / spend; target: 4.0; warning: <3.5
    - CAC: spend / conversions; target: <280000; warning: >280000
    - CTR: clicks / impressions; target: >1.5%; warning: <1.0%
    - conversion_rate: conversions / clicks; target: >2.0%; warning: <1.5%
  secondary:
    - revenue_share_by_channel
    - cost_share_by_channel
    - brand_line_ROAS_breakdown

HOOK_PYRAMID_ANGLE: ROAS performance vs target + channel decomposition + brand line breakdown

HOOK_OUTPUT_FORMAT:
  length: 15 dòng + 1 chart inline (bar channel ROAS)
  appendix: KPI table full + cleaning log
```

#### Sample output báo cáo

```
BÁO CÁO MKT Q1 — 15 DÒNG

[Conclusion]
ROAS Q1 đạt 3.45x, miss target 4.0x (achievement 86%); root cause
tập trung ở 2 channel Facebook Ads + Influencer, trong khi Google
Search giữ ổn định target.

[Key Finding 1 — ROAS Performance]
- Overall ROAS 3.45x, giảm 18% MoM (Q4: 4.2x)
- Achievement vs target Q1: 86% — miss
- Trong 3 brand line, chỉ Line A đạt target (ROAS 4.1x); Line B
  + C dưới 3.5x warning threshold

[Key Finding 2 — Channel Decomposition]
- Google Search: ROAS 5.8x ↑ (target 4.0x) — outperformer
- Direct: ROAS 4.5x ↑ stable
- Facebook Ads: ROAS 2.8x ↓ (vs Q4: 4.1x, drop 32%) — main drag
- Influencer: ROAS 2.4x ↓ (vs Q4: 3.0x, drop 21%) — second drag

[Key Finding 3 — Brand Line Breakdown]
- Line A (mature): ROAS 4.1x, CAC 245k (within target)
- Line B (Q1 launch): ROAS 3.2x, CAC 312k (vượt 280k threshold)
- Line C (Q1 launch): ROAS 2.9x, CAC 358k (vượt 280k threshold)

[Decision Box]
Cần BOD quyết Q2:
- Option A: Pause Influencer + reallocate 60% budget sang Search
- Option B: Tighten Facebook targeting + A/B test riêng từng brand line
Owner: Việt Anh + Tùng (CEO). Deadline: Thursday meeting 16:00.

[Chart inline — Bar]
ROAS by Channel Q1 2026:
Google Search ████████████████ 5.8x (target line ━━━━ 4.0x)
Direct        ████████████ 4.5x
Facebook Ads  ████████ 2.8x ⚠
Influencer    ███████ 2.4x ⚠
```

---
