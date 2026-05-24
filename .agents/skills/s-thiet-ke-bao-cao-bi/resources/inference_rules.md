# Inference Rules — Đoán role/domain/intent từ file signals

**Mục đích**: Skill quan sát file Excel + infer thay vì hỏi. Đây là consultant capability — nhìn file 5 phút biết user đang làm gì.

**Cách dùng**: Step 1 của pipeline. Sau khi đọc file structure + column headers + formulas + charts, apply rules dưới để build Internal Inference Brief.

---

## TABLE OF CONTENTS

- [Rule 1: Domain identification](#rule-1-domain-identification)
- [Rule 2: Cadence identification](#rule-2-cadence-identification)
- [Rule 3: Decision focus inference](#rule-3-decision-focus-inference)
- [Rule 4: User Excel capability](#rule-4-user-excel-capability)
- [Rule 5: Pain point inference](#rule-5-pain-point-inference)
- [Composite inference example](#composite-inference-example)

---

## Rule 1: Domain identification

Match column names trong sheets với keyword sets dưới:

| Keywords trong columns | Inferred domain | Confidence |
|---|---|---|
| "AE", "Deal", "Pipeline", "Close Date", "Quota", "Stage", "Lead Source" | **SALES** | 90% |
| "Ticket", "Agent", "SLA", "CSAT", "AHT", "FRT", "Channel" (support) | **CUSTOMER SERVICE** | 90% |
| "OEE", "Downtime", "Defect", "Yield", "Shift", "Line", "Cycle Time" | **MANUFACTURING / OPS** | 90% |
| "Revenue", "Cost", "AR", "AP", "Margin", "Cash", "GL", "Budget" | **FINANCE** | 85% |
| "Headcount", "Attrition", "Hire", "Engagement", "FTE", "Tenure" | **HR** | 90% |
| "Campaign", "Channel" (marketing), "CAC", "ROAS", "Impressions", "CTR" | **MARKETING** | 90% |
| "GMV", "Conversion", "AOV", "Cart", "Sessions", "SKU" | **E-COMMERCE** | 90% |
| "Inventory", "Stock", "Reorder", "Lead Time" | **SUPPLY CHAIN** | 85% |
| "Project", "Milestone", "Sprint", "Velocity", "Story Points" | **PROJECT MGMT** | 80% |

**Logic**:
- Nếu ≥3 keywords match 1 domain → confidence high
- Nếu ≥2 domains match (vd: Sales + Marketing keywords trộn) → flag multi-domain → Step 3 clarify
- Nếu <2 keywords match bất cứ domain nào → flag "domain unclear" → trigger Step 3

**Bonus signals**:
- Sheet/file name có "sales", "revenue", "pipeline" → boost SALES confidence
- Sheet name có "T01_2024", "T02_2024" → tracking by month (cadence signal — see Rule 2)
- Currency formatting heavy → FINANCE bias

---

## Rule 2: Cadence identification

Match sheet naming + date patterns:

| Pattern | Inferred cadence |
|---|---|
| Sheet names: "T01, T02, T03, ..., T12" hoặc "Jan, Feb, ..., Dec" | **Monthly** |
| Sheet names: "W01, W02, ..." hoặc "Week 1, Week 2..." | **Weekly** |
| Date column có entries hằng ngày recent (last 30 days dense) | **Daily ops** |
| Sheet names: "Q1, Q2, Q3, Q4" hoặc "QTD" | **Quarterly** |
| Single sheet với date range ≥6 months continuous | Continuous (any cadence) — check date column granularity |
| Multiple files: "report_Jan.xlsx, report_Feb.xlsx" | **Monthly** với Save-As anti-pattern |

**Logic**:
- Nếu detect "Monthly" pattern + last-modified date của file ~end-of-month → confirm monthly review cycle
- Nếu detect "Weekly" + last-modified Monday morning → confirm weekly review (Monday standup)
- Nếu data có timestamp daily entries last 7 days dense → daily ops

**Cadence ambiguous?**: Apply default theo domain (Sales/CS → weekly, Finance/HR → monthly, Ops/Ecom → daily).

---

## Rule 3: Decision focus inference

Đoán user đang care gì từ chart type + formula type:

| Signal | Inferred decision focus |
|---|---|
| Chart type = **line + time series** | "Track trend over time" — pattern detection |
| Chart type = **bar grouped by entity** (AE/agent/region/product) | "Compare performers" — ranking/leaderboard |
| Chart type = **funnel / waterfall** | "Conversion analysis" — step-by-step drop-off |
| Chart type = **pie / donut** | (Often misused) — usually mean "breakdown/composition" — propose stacked bar instead |
| Chart type = **gauge / KPI card** | "Single number vs target" — status check |
| Heavy use **conditional formatting on threshold** | "Anomaly detection" — spot outliers |
| Formula heavy **SUMIF/SUMIFS** | "Aggregation/totaling" — sum by dimension |
| Formula heavy **VLOOKUP/XLOOKUP** | "Joining data" — often bad architecture |
| Formula heavy **AVERAGEIF, MEDIAN, PERCENTILE** | "Distribution analysis" — central tendency |
| **Filter/Sort applied to specific column** (saved in file) | "Drill into X dimension" — user actively slices |
| **PivotTable present** | "Multi-dimensional analysis" — competent user |
| **Slicer present** | "Interactive exploration" — modern Excel user |

**Logic**:
- Combine 2-3 signals → triangulate decision focus
- Vd: Line chart + heavy SUMIFS + filter saved on "AE" → "Track AE performance trend over time" = AE performance management

---

## Rule 4: User Excel capability

Đoán level user để adapt build approach:

| Signal | Inferred capability |
|---|---|
| Uses **Power Query** (Data > Get Data > ...) | **Advanced** — comfortable with M language, can handle complexity |
| Uses **Tables** (Ctrl+T) consistently | **Intermediate** — understands structured references |
| Uses **PivotTable + Slicer** | **Intermediate** — knows interactive analysis |
| **VBA macros** present | **Advanced** but careful about dependencies — possibly fragile |
| Uses **XLOOKUP/INDEX-MATCH** | **Intermediate to Advanced** |
| Uses **only SUM, AVERAGE, COUNT, VLOOKUP** | **Beginner to Intermediate** |
| **Hardcoded range references** (A1:A100 fixed) | **Beginner** — doesn't know Tables |
| **Merged cells everywhere** | **Cosmetic-focused** — not data-thinking, beginner |
| **VLOOKUP chain ≥4 levels** | Tried but doesn't know better pattern — educate gently |
| **No formulas, all hardcoded numbers** | **Pure entry-level** — needs heavy coaching |
| **Multiple files like "report_v1.xlsx, v2, v3..."** | **No template discipline** — needs guidance on template approach |

**Logic**:
- Beginner → BUILD with Tables + XLOOKUP + manual refresh (skip Power Query)
- Intermediate → BUILD with Power Query if data source allows
- Advanced → Full Power Query + advanced features OK
- Adjust coaching depth accordingly (beginner = Kỳ 1 step-by-step screenshot-level)

---

## Rule 5: Pain point inference

Đoán pain mà user không articulate được:

| Signal trong file | Inferred pain |
|---|---|
| Same data appears in 3+ sheets | **Manual sync burden** — user copy-paste between sheets |
| Files "T01.xlsx, T02.xlsx" pattern (separate files) | **No template** — rebuild every cycle, lose Power Query connection |
| Charts showing `#N/A` or `#REF!` | **Refresh fragility** — data range không update đúng |
| Heavy color-coding without legend | **Tribal knowledge dependency** — only user understands |
| Many "TEMP", "DELETE LATER", "Backup" sheets | **No maintenance discipline** — file decay over time |
| Merged cells in data range | **Pivot/Filter brittleness** — broken sorting/filtering |
| Blank rows in data range | **Table auto-expand broken** — adding new data requires manual range adjustment |
| Manual override values overwriting formulas (formula bar shows hardcoded) | **Audit trail loss** — user "fix" numbers without documentation |
| 20+ hidden columns/sheets | **Dead code accumulation** — never cleaned |
| External links broken (`#REF!`) | **Lost data source** — file moved/deleted |
| Last modified date pattern shows "weekend overtime" | **Process inefficiency** — user struggling with manual work |

**Logic**:
- Count pain signals → severity assessment
- 0-2 signals = Acceptable
- 3-4 signals = Refactor (skill builds TO-BE on top of cleaned AS-IS)
- ≥5 signals = Recommend Rebuild (start fresh)

---

## Composite inference example

**Input**: User upload file `bao_cao_sales_v37.xlsx`. Skill observes:

```
Sheets:
- T01_2024, T02_2024, T03_2024, ..., T12_2024 (12 sheets, monthly cadence)
- Dashboard (1 sheet with charts)
- Master_Data
- Lookup_AE
- TEMP (hidden)
- Test (hidden)

Columns common: "Mã KH", "Tên KH", "AE", "Pipeline Value", "Close Date", "Stage", "Doanh thu"
Charts: Line chart "Doanh thu theo tháng", Bar chart "AE performance"
Formulas: VLOOKUP chain 4 levels in Dashboard
Conditional formatting: Heavy on Pipeline Value column
Slicer: Not present
Power Query: Not used
Tables: Not used (range A1:Z500 hardcoded)
```

**Inference output**:

```yaml
inferred_role: Sales Manager hoặc Sales Ops
inferred_domain: SALES (confidence 95% — "AE", "Pipeline", "Stage", "Doanh thu")
inferred_cadence: Monthly (sheet T01-T12 pattern)
  → BUT consider: user mentions weekly review? Check.
inferred_decision_focus: 
  - Track revenue trend over time (line chart)
  - Compare AE performance (bar chart)
  - Anomaly detection on Pipeline Value (conditional formatting heavy)
inferred_excel_level: Beginner-Intermediate
  - No Power Query, no Tables, hardcoded ranges → Beginner pattern
  - But uses VLOOKUP + charts → Intermediate basics
  → Adjust BUILD: skip Power Query, use Tables + XLOOKUP + PivotTable
inferred_pain:
  - Manual sync burden (12 separate monthly sheets)
  - Save-As anti-pattern (v37 suffix shows version proliferation)
  - VLOOKUP chain 4 levels (lag risk)
  - TEMP/Test sheets (no maintenance discipline)
file_health: REFACTOR (4 pain signals, no CRITICAL)
preserved_vocab: "Doanh thu", "AE", "Mã KH" (giữ tiếng Việt)
```

**Step 2 Propose dựa trên inference**:
"Tôi đã xem file `bao_cao_sales_v37.xlsx`. Bạn đang là Sales Manager làm monthly review.
Đề xuất 5 KPI core cho role: Pipeline Coverage, Win Rate by Stage, ASP, AE Performance, Forecast Accuracy.
Layout monthly: Executive summary tab + 2 detail tabs.
File structure: 6 sheets thay vì 12 monthly + helpers.
Cải thiện: eliminate 11 monthly sheets cũ (gộp 1 sheet master), simplify VLOOKUP chain → XLOOKUP, time saved ~3h/tháng.
**OK build?**"
