# Domain: Finance & Accounting — Process Standards

Reference file cho Finance & Accounting (FA) department processes. Load khi:
- CREATE mode + domain = Finance/Accounting
- AUDIT mode + FA portfolio
- CATALOG mode + FA scope

---

## FA Process Catalog (Standard cấp 1 + cấp 2)

### Nhóm 1: Accounting Operations

| Mã | Quy trình cấp 1 | Quy trình con | Bộ phận chính | Đầu ra | KPI |
|----|-----------------|---------------|---------------|--------|-----|
| FA-01 | Month-end close | Subledger close (AR/AP/Inventory/Payroll) | Sub-area accountants | Subledger reports | Close on time |
| FA-01.02 | | Journal entries + accruals | GL Accountant | JE entries posted | Accuracy, completeness |
| FA-01.03 | | Reconciliation (Bank, AR, AP, Inventory) | Accountants | Reconciliation files | All accounts reconciled |
| FA-01.04 | | Trial balance review | Chief Accountant | TB reviewed | TB approved |
| FA-01.05 | | Financial statements prep | Chief Accountant | BS/PL/CF | FS finalized day 5-7 |
| FA-01.06 | | Management reporting | FP&A | MIS reports | Reports distributed |
| FA-01.07 | | Close sign-off | CFO | Close memo | Sign-off completed |

### Nhóm 2: Accounts Receivable (AR)

| Mã | Quy trình cấp 1 | Quy trình con | Bộ phận chính | Đầu ra | KPI |
|----|-----------------|---------------|---------------|--------|-----|
| FA-02 | Order-to-cash | Credit application + check | Sales/Credit | Credit approval | Approval cycle time |
| FA-02.02 | | Invoice generation | AR Accountant | Invoice issued | Invoice accuracy |
| FA-02.03 | | Collection follow-up | AR/Sales | Collection log | DSO, aging |
| FA-02.04 | | Cash application | AR Accountant | Payments applied | Application timing |
| FA-02.05 | | Bad debt provision | AR/Finance | Provision JE | Provision accuracy |
| FA-02.06 | | Dispute resolution | AR/Sales/Customer | Dispute log | Resolution time |

### Nhóm 3: Accounts Payable (AP)

| Mã | Quy trình cấp 1 | Quy trình con | Bộ phận chính | Đầu ra | KPI |
|----|-----------------|---------------|---------------|--------|-----|
| FA-03 | Procure-to-pay | PR + PO creation | Buyer/Department | PR/PO docs | PO accuracy |
| FA-03.02 | | Goods receipt verification | Warehouse/Buyer | GR docs | GR matching rate |
| FA-03.03 | | Invoice 3-way match | AP Accountant | Match results | Match success rate |
| FA-03.04 | | Payment approval | Department Head/CFO | Approved payment batch | Approval on time |
| FA-03.05 | | Payment execution | AP/Treasury | Bank transfer | DPO, on-time payment |
| FA-03.06 | | Vendor reconciliation | AP Accountant | Recon statement | Vendor satisfaction |

### Nhóm 4: Treasury & Cash Management

| Mã | Quy trình cấp 1 | Quy trình con | Bộ phận chính | Đầu ra | KPI |
|----|-----------------|---------------|---------------|--------|-----|
| FA-04 | Treasury | Cash flow forecasting | Treasury/FP&A | CF forecast | Forecast accuracy |
| FA-04.02 | | Bank account management | Treasury | Bank statements | Reconciliation rate |
| FA-04.03 | | Short-term investment | Treasury/CFO | Investment decisions | Yield achieved |
| FA-04.04 | | Loan management | Treasury/CFO | Loan schedule | Covenants compliance |
| FA-04.05 | | FX exposure management | Treasury | FX policy + hedging | FX P&L vs benchmark |

### Nhóm 5: Budgeting & Planning

| Mã | Quy trình cấp 1 | Quy trình con | Bộ phận chính | Đầu ra | KPI |
|----|-----------------|---------------|---------------|--------|-----|
| FA-05 | Annual budget cycle | Strategic direction setting | CEO/CFO/Mgmt | Strategic guidance | Approval on time |
| FA-05.02 | | Department budget submission | Dept Heads/FP&A | Dept budgets | Submission quality |
| FA-05.03 | | Budget consolidation + review | FP&A/CFO | Consolidated budget | Iteration count |
| FA-05.04 | | Board approval | CFO/CEO/Board | Approved budget | Approval timeline |
| FA-05.05 | | Budget upload + tracking | FP&A | Budget in ERP | Setup accuracy |
| FA-05.06 | | Variance analysis (monthly) | FP&A | Variance reports | Insights delivered |
| FA-05.07 | | Reforecast (quarterly) | FP&A/CFO | Reforecast | On time |

### Nhóm 6: Tax Compliance

| Mã | Quy trình cấp 1 | Quy trình con | Bộ phận chính | Đầu ra | KPI |
|----|-----------------|---------------|---------------|--------|-----|
| FA-06 | Tax compliance | VAT (monthly/quarterly) | Tax Accountant | VAT declaration filed | On time, accurate |
| FA-06.02 | | CIT (Corporate Income Tax) provisional + annual | Tax Accountant/Chief | CIT filings | Compliance rate |
| FA-06.03 | | PIT (employee — coord HR) | Tax/HR | PIT settlement | On time |
| FA-06.04 | | FCT (Foreign Contractor Tax) | Tax Accountant | FCT declared | When applicable |
| FA-06.05 | | Tax audit support | Tax/Chief Accountant | Audit responses | Audit findings minimized |

### Nhóm 7: Audit & Compliance

| Mã | Quy trình cấp 1 | Quy trình con | Bộ phận chính | Đầu ra | KPI |
|----|-----------------|---------------|---------------|--------|-----|
| FA-07 | Audit support | Internal audit cycle | Internal Audit/Finance | Audit reports | Findings closed |
| FA-07.02 | | External audit (annual) | External Auditor/Finance | Audited FS | Audit opinion |
| FA-07.03 | | Internal control testing | Internal Audit | Control test results | Control effectiveness |
| FA-07.04 | | SOX/regulatory compliance (if applicable) | Compliance | Compliance reports | Compliance rate |

---

## FA KPI Library

### Close cycle metrics
- **Days to close**: working days từ month-end → FS finalized
- **Days to management reporting**: working days → MIS distributed
- **Accuracy**: # corrections post-close / total entries
- **First-time close rate**: % accounts reconciled without manual fix

### AR metrics
- **DSO** (Days Sales Outstanding): AR balance / (daily revenue) — target <45 days standard
- **Aging buckets**: % AR in 0-30/30-60/60-90/90+ days
- **Bad debt ratio**: bad debt / total revenue
- **Cash collection rate**: collected / billed (monthly)

### AP metrics
- **DPO** (Days Payable Outstanding): AP balance / (daily COGS) — leverage payment terms
- **On-time payment rate**: % paid by due date
- **Discount captured**: early payment discounts taken
- **3-way match success rate**: % invoices matched first-attempt

### Liquidity metrics
- **Cash position**: end-of-day cash balance
- **Cash conversion cycle**: DSO + DIO − DPO
- **Working capital ratio**: current assets / current liabilities
- **Burn rate** (cho startups): monthly cash burn

### Budget & Planning metrics
- **Budget variance** (actual vs budget): % deviation per line item
- **Forecast accuracy**: |actual − forecast| / actual
- **Reforecast frequency**: # times reforecast per year (over 4 = signal underlying issues)

### Compliance metrics
- **Tax filing on-time rate**: 100% target
- **Audit findings**: count, severity, repeat findings
- **Statutory deadline adherence**: filings before due date

---

## FA RACI Patterns

### Standard FA roles
- **CFO**: A on strategy, FS, M&A, capital, treasury policy
- **Chief Accountant (KTT)**: A on accounting accuracy, statutory compliance, close
- **FP&A Lead**: A on budget, forecasting, analysis
- **Tax Lead**: A on tax compliance + tax planning
- **Treasury Lead**: A on cash, FX, banking, loans
- **GL Accountant**: R on entries, R on reconciliation
- **AR/AP Accountant**: R on subledger
- **Tax Accountant**: R on tax filings
- **Internal Auditor**: R on testing controls

### Cross-functional partners
- **HR**: C on payroll JE, A on payroll execution
- **Sales**: C on revenue recognition issues, R on AR collection
- **Procurement**: C on AP issues, R on PO management
- **CEO**: A on major financial decisions, capex
- **Board**: A on budget approval, capital decisions

### Common RACI patterns

**Month-end close** (typical day 1-7):
- Day 1-3: Subledger close (R: respective accountants, A: Chief Accountant)
- Day 3-4: JE + reconciliation (R: GL Accountant, A: Chief Accountant)
- Day 4-5: FS prep (R: Chief Accountant)
- Day 5-6: FP&A review + MIS (R: FP&A, A: CFO)
- Day 7: CFO sign-off (A: CFO)

**Payment approval** (tiered):
- AP Accountant (R) prepares batch
- Dept Head (C/A depending on amount):
  - <50M VND: Dept Head A
  - 50M-500M: CFO A
  - >500M: CEO A
- Treasury (R) executes payment
- Bank (I) processes
- Vendor (I) notified

**Budget cycle**:
- CFO/CEO (A) set strategic direction (Aug-Sep)
- Dept Heads (R) submit dept budgets (Oct)
- FP&A (R) consolidates (Nov)
- CFO (A) reviews + iterates (Nov-Dec)
- Board (A) approves (Dec)
- FP&A (R) uploads to ERP (Dec)
- All depts (I) informed

---

## VN Context — FA-Specific Patterns

### Vietnamese Accounting Standards (VAS) vs IFRS
- **VAS mandatory**: cho local entities (FDI có thể IFRS supplementary)
- **VAS vs IFRS differences**:
  - Revenue recognition timing (VAS more cash-based)
  - Lease accounting (VAS less strict on operating leases)
  - Fair value measurement (VAS limited)
- **Implication for processes**: VN companies có FDI parent thường maintain dual books → close cycle longer

### Tax Filing Deadlines (Critical Calendar)
- **VAT** (Thuế GTGT):
  - Monthly: 20th of following month
  - Quarterly: 30th of month after quarter-end
- **CIT provisional** (Tạm tính TTNDN): quarterly, 30th of month after quarter-end
- **CIT annual** (Quyết toán TTNDN): 90 days from year-end (typically March 31)
- **PIT** (Thuế TNCN):
  - Withhold monthly, file with VAT
  - Annual settlement: 90 days from year-end
- **Statutory contributions** (BHXH/BHYT/BHTN): monthly, no later than last day of following month

### Tết Closing Pattern
- **Q1 close challenging**: month-end + Tết overlap. Plan capacity.
- **Pre-Tết payment push**: vendors expect payment before Tết → AP volume spike
- **Tết bonus accruals**: end of fiscal year (often Dec 31), bonus paid pre-Tết (Feb) → accrual JE careful
- **Q1 reporting lag**: results often delayed because Tết absence + complex closing
- **CIT settlement crunch**: March deadline + post-Tết ramp → tax team overloaded

### Audit Culture VN
- **External audit**: required for companies above certain size (LE Decree). Big 4 vs local firms.
- **Internal audit maturity**: VN private companies underdeveloped. Compliance-focused, not advisory.
- **Tax audit**: tax authority audits every 3-5 years typical. Documentation critical (sĩ diện sai = penalty).
- **Audit report timing**: external audit Q1 → significant Finance team pressure overlap with Tết.

### Family Business Finance Quirks
- **Owner withdrawals**: family owners take cash informally → reconciliation nightmare. Solution: formal "loan to owner" tracking.
- **Personal expense bleed**: family expenses (cars, family events) booked as company expense → tax + audit issue. Separate accounts.
- **Cash vs accrual mindset**: family-owned businesses think cash; accrual accounting feels artificial → educate Department Heads.
- **Successor planning**: 2nd-gen takeover phase requires Finance restructure (governance, controls, transparency).

### Cash Management VN
- **VND-USD dual currency**: imports + exports common → FX exposure
- **Cash heavy economy**: VN still uses significant physical cash → cash handling SOPs needed
- **Multiple bank accounts**: standard practice, easier reconciliation but more complex consolidation
- **Vendor payment culture**: vendors expect cash or fast bank transfer; check-based slow

---

## Common FA Process Pitfalls

1. **Close cycle drift**: target 5 days → actual 7-10 days → no improvement effort. Solution: track close cycle KPI explicitly, root cause delays.

2. **Reconciliation deferral**: small bank account discrepancies "fix next month" → accumulates → year-end nightmare. Mandatory: reconcile within month.

3. **AR aging blindness**: AR aged >90 days grows silently → bad debt surprise → P&L hit. Weekly aging report mandatory, action triggers automatic.

4. **AP payment timing politics**: CFO holds payments to manage cashflow → vendors irritated → supply disruption. Better: transparent payment cadence + early-warning.

5. **Budget vs reality drift**: budget set Q4 last year, never revised → first quarter halfway through and variances ignored. Quarterly reforecast mandatory.

6. **Tax compliance shortcuts**: small filing errors accumulate → audit penalty disproportionate to original error. Zero-tolerance on filing accuracy.

7. **Manual JE reliance**: month-end has 50+ manual JE → high error rate, audit findings. Automate recurring JE.

8. **Owner override on controls**: family business owner approves payments outside SOP → audit weakness. Document override with rationale, escalate to audit committee.

---

## Example: Worked SOP for FA-01 (Month-end Close)

Khi user request enterprise-grade close SOP:

- **Section V Glossary**: GAAP terms, system codes (GL/SL/Tax accounts), abbreviations (JE/AR/AP/AP)
- **Section VIII Approval**: tiered close milestones (Chief Accountant for subledger close, CFO for FS sign-off)
- **Section XI RACI**: 7 sub-processes × 10 roles (CFO/Chief Accountant/GL/AR/AP/Inventory/Payroll/FP&A/Tax/Treasury)
- **Section XIII SLA**: standard 5-7 working days, with checkpoint at day 3 (subledger), day 5 (FS draft), day 7 (sign-off)
- **Section XVI Forms**: BM-FA01-01 Close calendar, BM-FA01-02 Reconciliation template, BM-FA01-03 JE approval, BM-FA01-04 Close memo
- **Section XVII Compliance**: External auditor, internal audit, tax authority, BCC for foreign-invested entities
- **Section XVIII Sanctions**: missed statutory deadline = automatic CFO escalation, repeated breach = disciplinary action per labor contract
