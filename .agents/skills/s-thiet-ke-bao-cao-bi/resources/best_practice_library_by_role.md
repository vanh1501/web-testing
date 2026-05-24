# Best Practice Library by Role

**Mục đích**: Template sẵn cho 7 role phổ biến. Skill match inferred role → pull template → propose user. Đây là advisor knowledge — non-tech không biết, skill biết thay họ.

**Cách dùng**: Step 2 của pipeline. Sau khi infer role ở Step 1, mở file này, tìm role match, propose 5 KPI + cadence + layout + drill paths theo template.

---

## TABLE OF CONTENTS

- [A. Sales Manager / Sales Ops](#a-sales-manager--sales-ops)
- [B. Customer Service Lead](#b-customer-service-lead)
- [C. Operations / Manufacturing](#c-operations--manufacturing)
- [D. Finance Manager](#d-finance-manager)
- [E. HR Manager](#e-hr-manager)
- [F. Marketing Manager](#f-marketing-manager)
- [G. E-commerce Manager](#g-e-commerce-manager)
- [Pattern selection logic](#pattern-selection-logic)
- [Cadence-driven layout](#cadence-driven-layout)

---

## A. Sales Manager / Sales Ops

### Core 5 KPIs

| # | KPI | Công thức | Target benchmark | Decision served |
|---|---|---|---|---|
| 1 | **Pipeline Coverage** | Pipeline value ÷ Quota period | >3x = healthy | "Pipeline đủ cho quota Q không?" |
| 2 | **Win Rate by Stage** | Deals won ÷ Deals reached stage | Industry benchmark | "Stage nào funnel rớt nhiều?" |
| 3 | **ASP (Average Selling Price)** | Total revenue ÷ Deals closed | Trend vs target | "Deal size đang shrink không?" |
| 4 | **AE Performance** | Quota attainment per AE | ≥100% | "AE nào cần coaching/recognition?" |
| 5 | **Forecast Accuracy** | Actual ÷ Forecast (period N-1) | 90-110% = good | "Forecast tin được không?" |

### Cadence điển hình
- **Weekly review** (Monday morning) — primary
- Daily quick-check tùy team size

### Layout (Weekly — 2-3 trang)

```
Trang 1 — Executive Summary:
├── Top: 5 KPI cards (actual / target / variance % / 13-week trend sparkline)
├── Middle: Bar chart "AE Leaderboard" (quota attainment %)
└── Right: Slicers [Week] [AE Group]

Trang 2 — Pipeline Detail:
├── Funnel chart: Lead → MQL → SQL → Opp → Closed
├── PivotTable: Pipeline by stage × month
└── Risk flag: deals stuck >30 days in stage

Trang 3 — Forecast vs Actual:
├── Line chart: Forecast vs Actual last 13 weeks
└── Variance table by AE
```

### Drill sheets

- `05_drill_deals` — PivotTable per deal (stage, value, days in stage, AE)
- `05_drill_ae` — Per-AE performance breakdown

### Decisions thường phục vụ
- Thứ Hai sáng standup: "Tuần này focus AE nào? Deal nào sắp close?"
- End-of-quarter: "Forecast Q tới có realistic không?"
- Coaching: "AE nào cần intervention?"

---

## B. Customer Service Lead

### Core 5 KPIs

| # | KPI | Công thức | Target benchmark | Decision served |
|---|---|---|---|---|
| 1 | **Ticket Volume** | Count tickets created | Trend baseline | "Volume tăng đột biến không?" |
| 2 | **First Response Time (FRT)** | Time first reply - Time created | <SLA (vd: <2h) | "SLA miss do đâu?" |
| 3 | **Average Handle Time (AHT)** | Total handle time ÷ Tickets resolved | <industry avg | "Agent nào bottleneck?" |
| 4 | **CSAT (Customer Satisfaction)** | Positive responses ÷ Total responses | >80% | "Trend CSAT đang xấu đi?" |
| 5 | **Agent Utilization** | Active time ÷ Login time | 70-85% sweet spot | "Capacity planning?" |

### Cadence điển hình
- **Daily ops** (morning) — primary cho team lead
- **Weekly review** (Monday) — cho manager
- Monthly review cho leadership

### Layout (Daily ops — 1 trang fit screen)

```
Top: 5 KPI cards (today vs yesterday vs 7-day avg)
Middle: 
├── Line chart: Ticket volume last 7 days (by hour pattern)
└── Bar chart: SLA miss reason breakdown
Bottom:
├── Table: Top 5 tickets aging (priority + days open)
└── Agent leaderboard (tickets resolved today)
Right: Slicers [Date] [Priority] [Channel]
```

### Drill sheets

- `05_drill_tickets` — PivotTable ticket-level (SLA miss reason, agent, channel, priority)
- `05_drill_agents` — Per-agent performance (volume, AHT, CSAT, utilization)

### Decisions thường phục vụ
- Morning standup: "Ticket aging nào cần escalate? Agent nào bottleneck?"
- Weekly: "SLA miss reason top 3? Action gì?"
- Quarterly: "Headcount/capacity planning?"

---

## C. Operations / Manufacturing

### Core 5 KPIs

| # | KPI | Công thức | Target benchmark | Decision served |
|---|---|---|---|---|
| 1 | **OEE (Overall Equipment Effectiveness)** | Availability × Performance × Quality | >85% world-class | "Line nào bottleneck?" |
| 2 | **Defect Rate** | Defects ÷ Total units produced | <industry threshold | "Quality issue ở đâu?" |
| 3 | **Downtime** | Total downtime minutes by cause | <X min/shift | "Downtime reason top?" |
| 4 | **Cycle Time** | Time per unit vs standard | At/below standard | "Process improvement target?" |
| 5 | **Throughput** | Units produced ÷ Time period | ≥plan | "Output đáp ứng demand?" |

### Cadence điển hình
- **Daily shift report** — primary
- **Weekly review** cho plant manager
- Monthly cho operations director

### Layout (Daily shift report — 1 trang)

```
Top: 5 KPI cards (current shift vs prior shift vs 7-day avg)
Middle:
├── Bar chart: OEE by production line
└── Pareto chart: Downtime causes (top 5)
Bottom:
├── Defect rate trend last 14 shifts
└── Throughput vs plan (gauge or progress bar)
Right: Slicers [Shift] [Line]
```

### Drill sheets

- `05_drill_downtime` — Downtime incidents per line × cause × shift
- `05_drill_quality` — Defect detail by product, line, shift

### Decisions thường phục vụ
- Shift handover: "Line nào down? Reason gì? Action ngay?"
- Weekly: "Trend OEE? Improvement initiative impact?"
- Capital expenditure: "Equipment nào ROI thay thế?"

---

## D. Finance Manager

### Core 5 KPIs

| # | KPI | Công thức | Target benchmark | Decision served |
|---|---|---|---|---|
| 1 | **Revenue Waterfall** | Actual vs Budget vs Forecast (variance breakdown) | ±5% budget | "Variance do đâu?" |
| 2 | **Cost Variance** | Actual cost - Budget cost (by category) | ±5% budget | "Department nào over-spend?" |
| 3 | **Cash Position** | Current cash + 13-week forecast | Min runway threshold | "Runway tháng nào risk?" |
| 4 | **AR Aging** | Receivables by 30/60/90+ days bucket | <X% in 90+ | "Customer nào AR risk?" |
| 5 | **Margin** | Gross margin %, Operating margin % | ≥target | "Product/segment nào margin issue?" |

### Cadence điển hình
- **Monthly close** (executive summary tab) — primary
- **Weekly cash flash** — cho CFO/CEO
- Quarterly board report

### Layout (Monthly close — Executive summary 1 trang + detail tabs)

```
Trang 1 — Executive Summary:
├── Revenue waterfall chart (budget → actual decomposition)
├── 5 KPI cards (top): Revenue, Gross Margin, Operating Margin, Cash, AR Aging
├── Top 3 variance commentary box (user-edited)
└── Slicers [Month] [Department]

Trang 2 — Cost detail:
├── PivotTable: Cost by category × department (variance %)
└── Bar chart: Top 10 variance items

Trang 3 — Cash & AR:
├── 13-week cash forecast (line chart)
├── AR aging bucket bar chart
└── Top 10 AR overdue (customer × amount × days)
```

### Drill sheets

- `05_drill_revenue` — Revenue by product × customer × month
- `05_drill_cost` — Cost by GL account × department × month
- `05_drill_ar` — Customer-level AR aging

### Decisions thường phục vụ
- Monthly close: "Variance reason? Forecast adjust?"
- Weekly cash: "Cash flow risk? Collection priority?"
- Board: "Performance vs plan? Outlook?"

---

## E. HR Manager

### Core 5 KPIs

| # | KPI | Công thức | Target benchmark | Decision served |
|---|---|---|---|---|
| 1 | **Headcount Movement** | Start + Hires - Leavers = End (monthly) | Aligned with plan | "Headcount vs plan?" |
| 2 | **Attrition Rate** | Leavers ÷ Avg headcount (annualized) | <industry avg | "Team nào attrition spike?" |
| 3 | **Recruitment Funnel** | Apply→Screen→Interview→Offer→Hire (conversion %) | Each stage threshold | "Funnel stage nào bottleneck?" |
| 4 | **Engagement Score** | Survey avg score | >benchmark | "Team nào engagement risk?" |
| 5 | **Cost per Hire** | Total recruitment cost ÷ Hires | <industry avg by role | "Channel nào ROI tốt?" |

### Cadence điển hình
- **Monthly business review** — primary
- Quarterly board report

### Layout (Monthly — Executive summary + detail)

```
Trang 1 — Executive Summary:
├── 5 KPI cards (current month vs prior month vs YTD)
├── Headcount waterfall chart (Start + Hire - Leave = End)
├── Bar chart: Attrition by department
└── Slicers [Month] [Department]

Trang 2 — Recruitment Detail:
├── Funnel chart: Apply → Screen → Interview → Offer → Hire
├── Time-to-hire by role
└── Cost per hire by channel

Trang 3 — Engagement:
├── Score trend last 4 surveys
├── Heat map by department × topic
└── Comment cluster (qualitative)
```

### Drill sheets

- `05_drill_headcount` — Per-department, per-role detail
- `05_drill_attrition` — Leaver detail (department, tenure, reason)
- `05_drill_pipeline` — Recruitment pipeline by role

### Decisions thường phục vụ
- Monthly: "Team nào attrition cần intervention?"
- Quarterly: "Workforce plan adjust?"
- Recruitment: "Channel pause/scale?"

---

## F. Marketing Manager

### Core 5 KPIs

| # | KPI | Công thức | Target benchmark | Decision served |
|---|---|---|---|---|
| 1 | **MQL → SQL Conversion** | SQLs ÷ MQLs (funnel) | >industry avg | "Lead quality issue?" |
| 2 | **CAC (Customer Acquisition Cost)** | Total marketing spend ÷ New customers | <target by channel | "Channel nào efficient?" |
| 3 | **Channel Attribution** | Revenue contribution per channel | Mix vs plan | "Budget allocation?" |
| 4 | **Campaign ROI** | (Revenue - Spend) ÷ Spend | >threshold per campaign | "Campaign nào scale/kill?" |
| 5 | **Pipeline Sourced** | % pipeline value from marketing | ≥target % | "Marketing impact on revenue?" |

### Cadence điển hình
- **Weekly campaign review** — primary
- **Monthly marketing review** — cho CMO/CEO

### Layout (Weekly — 2 trang)

```
Trang 1 — Campaign Performance:
├── 5 KPI cards (this week vs last 4-week avg)
├── Bar chart: Spend vs Revenue by channel
└── Slicers [Week] [Channel]

Trang 2 — Funnel & Attribution:
├── Funnel chart: Impressions → Clicks → MQL → SQL → Customer
├── Stacked bar: Revenue attribution by channel
└── ROI table per active campaign
```

### Drill sheets

- `05_drill_campaign` — Campaign-level (spend, leads, conversion, ROI)
- `05_drill_channel` — Channel performance over time

### Decisions thường phục vụ
- Weekly: "Channel nào pause/scale? Campaign nào extend?"
- Monthly: "Budget reallocation? CAC target adjust?"
- Quarterly: "Channel mix strategy?"

---

## G. E-commerce Manager

### Core 5 KPIs

| # | KPI | Công thức | Target benchmark | Decision served |
|---|---|---|---|---|
| 1 | **GMV (Gross Merchandise Value)** | Total order value | Trend/target | "GMV trend? Promo impact?" |
| 2 | **Conversion Rate** | Orders ÷ Sessions | >benchmark by source | "Source nào convert tốt?" |
| 3 | **AOV (Average Order Value)** | GMV ÷ Orders | Trend/target | "Bundle/upsell working?" |
| 4 | **Repeat Purchase Rate** | Repeat customers ÷ Total customers (cohort) | >benchmark | "Retention by cohort?" |
| 5 | **Cart Abandonment Rate** | Carts not converted ÷ Carts created | <industry avg | "Funnel last step issue?" |

### Cadence điển hình
- **Daily ops** (morning) — primary
- **Weekly review** — cho ecommerce director

### Layout (Daily ops — 1 trang)

```
Top: 5 KPI cards (today vs yesterday vs 7-day avg)
Middle:
├── Line chart: GMV last 30 days
└── Bar chart: Conversion rate by traffic source
Bottom:
├── Top 10 products by GMV today
├── Cart abandonment by step (funnel)
└── Slicers [Date] [Channel]
```

### Drill sheets

- `05_drill_products` — Product-level (units, GMV, conversion)
- `05_drill_cohort` — Customer cohort retention

### Decisions thường phục vụ
- Daily: "Product nào push? Promo impact?"
- Weekly: "Channel mix? Cart abandonment fix?"
- Monthly: "Cohort retention pattern? CRM strategy?"

---

## Pattern selection logic

```
IF inferred role match EXACTLY 1 trong library 
  → propose template đó

IF inferred role match 2+ (vd: "Sales-Marketing hybrid") 
  → propose blend: 7 KPI core (4 từ primary + 3 từ secondary)
  → 2 dashboard riêng trong cùng file (nếu cadence khác nhau)

IF inferred role NOT in library 
  → ask multiple-choice: "Role gần nhất của bạn: A/B/C trong 7 role này?"
  → Hoặc user mô tả 1 dòng → re-infer

IF blind design (no file) 
  → ask role với 7-option multiple choice + "Khác" option
```

---

## Cadence-driven layout reference

| Cadence | Layout | KPI count | Time horizon | Drill depth |
|---|---|---|---|---|
| **Daily ops** | 1 trang fit screen | 3-5 | Today vs Y'day + 7-day trend | 1 level |
| **Weekly review** | 2-3 trang | 5-7 | WoW + 4-week trend + breakdown | 2 levels |
| **Monthly BR** | Exec summary tab + detail tabs | 7 | MoM + YoY + YTD vs target + commentary | 2-3 levels |
| **Quarterly** | Deck-style, 1 KPI/trang | 5-7 | QoQ + YoY + plan vs actual | 3 levels + variance analysis |

**Quan trọng**: Layout sai cadence = không ai đọc. Monthly review mà chỉ có today vs yesterday → không có context. Daily ops mà 3 trang chi tiết → không ai đọc kịp.
