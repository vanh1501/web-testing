# Domain: HR — Process Standards

Reference file cho HR (Human Resources) department processes. Load khi:
- CREATE mode + domain = HR
- AUDIT mode + HR portfolio
- CATALOG mode + HR scope

---

## HR Process Catalog (Standard cấp 1 + cấp 2)

### Nhóm 1: Talent Acquisition

| Mã | Quy trình cấp 1 | Quy trình con | Bộ phận chính | Đầu ra | KPI |
|----|-----------------|---------------|---------------|--------|-----|
| HR-01 | Hire-to-onboard | Manpower planning | HR Lead/Department | MP plan | Plan approval đúng hạn |
| HR-01.02 | | Job requisition | Hiring Manager/HR | JD + JR form | JR turnaround |
| HR-01.03 | | Sourcing + screening | Recruiter | Candidate pipeline | Sourcing volume, quality |
| HR-01.04 | | Interview process | Hiring panel/HR | Interview feedback forms | Interview cycle time |
| HR-01.05 | | Offer + negotiation | HR/Hiring Mgr | Offer letter | Offer-to-accept rate |
| HR-01.06 | | Pre-employment | HR/HSE | Background check, contract | Compliance rate |
| HR-01.07 | | Onboarding (day 1-90) | HR/Manager | Onboarding plan + check-ins | 90-day retention, ramp time |

### Nhóm 2: Performance Management

| Mã | Quy trình cấp 1 | Quy trình con | Bộ phận chính | Đầu ra | KPI |
|----|-----------------|---------------|---------------|--------|-----|
| HR-02 | Performance review | Goal setting (KPI) | Manager/HR | KPI form per employee | KPI submission rate |
| HR-02.02 | | Mid-year check-in | Manager/Employee | Check-in notes | Completion rate |
| HR-02.03 | | Annual performance review | Manager/HR | Performance rating | Calibration completion |
| HR-02.04 | | Performance improvement plan (PIP) | Manager/HR/Employee | PIP doc | PIP success rate |
| HR-02.05 | | Promotion/bonus decisions | HR/Mgmt/Finance | Decision letter | Promotion equity |

### Nhóm 3: Compensation & Benefits

| Mã | Quy trình cấp 1 | Quy trình con | Bộ phận chính | Đầu ra | KPI |
|----|-----------------|---------------|---------------|--------|-----|
| HR-03 | Payroll cycle | Timesheet collection | HR/Manager | Verified timesheet | Submission on time |
| HR-03.02 | | Payroll calculation | HR/Payroll Specialist | Payroll register | Calc accuracy |
| HR-03.03 | | Payroll approval | HR Lead/Finance | Approved payroll | Approval timeline |
| HR-03.04 | | Salary disbursement | Finance/Bank | Bank transfer | Disbursement on time |
| HR-03.05 | | Statutory contributions | HR/Finance | BHXH, BHYT, BHTN paid | Compliance 100% |
| HR-03.06 | | Personal income tax (PIT) | HR/Finance | PIT filing | Filing on time |
| HR-03.07 | | Annual settlement (PIT) | HR | Quyết toán thuế | Timely settlement |

### Nhóm 4: Talent Development

| Mã | Quy trình cấp 1 | Quy trình con | Bộ phận chính | Đầu ra | KPI |
|----|-----------------|---------------|---------------|--------|-----|
| HR-04 | Talent development | Training needs analysis | HR/Manager | TNA report | Coverage of roles |
| HR-04.02 | | Training program design | HR/L&D | Training curriculum | Program quality |
| HR-04.03 | | Training delivery | L&D/Trainer | Training records | Completion rate, NPS |
| HR-04.04 | | Skill assessment | HR/Manager | Skill matrix | Assessment frequency |
| HR-04.05 | | Career development planning | HR/Manager/Employee | IDP doc | IDP coverage |

### Nhóm 5: Employee Relations & Offboarding

| Mã | Quy trình cấp 1 | Quy trình con | Bộ phận chính | Đầu ra | KPI |
|----|-----------------|---------------|---------------|--------|-----|
| HR-05 | Employee relations | Grievance handling | HR/Manager | Grievance log + resolution | Resolution time |
| HR-05.02 | | Disciplinary action | HR/Manager/Legal | Disciplinary record | Process compliance |
| HR-05.03 | | Exit interview | HR | Exit interview report | Completion rate |
| HR-05.04 | | Offboarding (resignation/termination) | HR/IT/Finance | Offboarding checklist | Process completion |
| HR-05.05 | | Knowledge handover | Manager/Employee | Handover document | Handover quality |

---

## HR KPI Library

### Acquisition metrics
- **Time-to-hire**: days từ JR open → offer accepted
- **Cost-per-hire**: total cost / # hired
- **Source-of-hire**: % per channel (referral, agency, direct, university)
- **Offer-to-accept rate**: % offers accepted
- **90-day retention**: % new hires still employed at day 90

### Workforce metrics
- **Headcount**: total + by department/level
- **Turnover rate**: # leavers / avg headcount (annual)
- **Voluntary vs involuntary turnover**: breakdown
- **Regrettable turnover**: % leavers HR wanted to keep
- **Tenure**: average years in company

### Engagement metrics
- **eNPS** (Employee NPS): -100 to +100
- **Engagement survey score**: % engaged (typically Gallup format)
- **Pulse survey response rate**: % completing
- **Internal mobility rate**: % roles filled internally

### Development metrics
- **Training hours per employee**: avg per year
- **Training completion rate**: % required training done
- **Promotion rate**: % promoted in period
- **Bench strength**: # ready successors per critical role

### Productivity metrics
- **Revenue per employee**: revenue / headcount
- **Profit per employee**: profit / headcount
- **HR cost % of revenue**: HR opex / revenue

### Compliance metrics
- **Payroll accuracy**: % cycles error-free
- **Statutory compliance**: BHXH/BHYT/BHTN/PIT on-time filing
- **Audit findings**: HR-related findings count

---

## HR RACI Patterns

### Standard HR roles
- **CHRO/HR Director**: A on strategy, exec hires, comp framework
- **HR Lead/Manager**: A on operations, A on standard hires
- **HRBP** (HR Business Partner): R on department support, C on performance
- **Recruiter/Talent Acquisition**: R on sourcing, R on screening
- **L&D Specialist**: R on training programs
- **Payroll Specialist**: R on payroll execution, A on accuracy
- **HR Admin**: R on document management, R on data entry

### Cross-functional partners
- **Hiring Manager**: R on interviewing, A on hire decision
- **Finance/Kế toán**: C on budget, A on payment execution
- **Legal**: C on contract, disciplinary
- **IT**: R on access provisioning (onboard/offboard)
- **Department Head**: A on team decisions

### Common RACI patterns

**Hire decision**:
- Recruiter (R) sources + screens
- Hiring Manager (R) interviews + selects
- HR (C) advises on compensation, fit
- Hiring Manager (A) for individual hires
- HR Lead (A) for sensitive cases (replacement, fast-track)
- Department Head (I) on standard, (A) on senior hires

**Disciplinary action**:
- Manager (R) documents incident
- HR (R) investigates
- Legal (C) reviews
- HR Lead (A) for verbal/written warning
- HR Director (A) for suspension/termination
- Employee (I) on process, (R) on response

**Payroll**:
- Manager (R) approves timesheet
- Payroll Specialist (R) calculates
- HR Lead (C) reviews exceptions
- HR Director (A) for approval
- Finance (R) for disbursement
- Employee (I) on payslip

---

## VN Context — HR-Specific Patterns

### Lunar Calendar Bonus Timing (Critical)
- **13th-month salary (lương tháng 13)**: standard in VN, paid before Tết
- **Tết bonus**: separate from 13th-month, performance-based, expected by employees
- **Timing matters**: payment AFTER Tết = mass complaints + flight risk. Pay BEFORE.
- **Year-end calculation pressure**: Q4 calc all bonuses, performance ratings, promotion decisions → HR overloaded. Plan capacity.
- **KPI scoring window**: VN performance review thường Jan-Feb (post-Tết). Avoid Tết week itself.

### Vietnamese Labor Law Specifics
- **Probation period**: max 60 days (most roles), 30 days for some, 180 for senior management
- **Notice period**: 30 days standard (employee resignation), 45 days for non-fixed term
- **Severance pay (trợ cấp thôi việc)**: 0.5 month / year service for pre-2009 service period
- **Overtime cap**: max 200 hours/year (special cases 300h with approval)
- **Female-specific protections**: maternity leave 6 months, breastfeeding break 1h/day until child 1 year
- **Termination grounds**: strict list of legal grounds. Cannot terminate at-will.

### Statutory Contributions (BHXH/BHYT/BHTN)
- **BHXH** (social insurance): 25.5% total (employee 8% + employer 17.5%)
- **BHYT** (health insurance): 4.5% (employee 1.5% + employer 3%)
- **BHTN** (unemployment insurance): 2% (employee 1% + employer 1%)
- **Maximum base**: capped at 20x minimum wage (changes annually)
- **Filing monthly + annual reconciliation**: deadline strict, penalties significant

### Personal Income Tax (PIT)
- **Progressive rates**: 5%-35% across 7 brackets
- **Family deductions**: 11M/month for self + 4.4M per dependent
- **Annual settlement (quyết toán)**: Mar of following year — major HR work
- **Foreign employees**: different rules (resident vs non-resident)

### Family Hiring Bias (Common VN Pitfall)
- Family-owned businesses thường có family members trong key positions
- Issue: standard RACI assumes merit-based; family override breaks this
- Mitigation: explicit "family-related employment policy" + separate performance review track if needed
- AUDIT flag: if HR ownership maturity = 5 but actual family overrides exist → score down

### Cultural Patterns in Performance Review
- **Sĩ diện (face-saving)**: direct negative feedback can damage relationship → manager avoids → underperformance unaddressed for years
- **Mitigation**: structured PIP với explicit timeline + HR involvement formal (không chỉ manager-employee)
- **Calibration sessions**: VN managers tend to give "tốt" ratings uniformly → calibration meetings critical
- **Promotion-by-tenure trap**: long tenure expects promotion regardless of performance → set clear capability gates

### Exit Interview Quality (Common Issue)
- **Surface answers**: leavers don't share real reasons (e.g., "vì nhà xa") to avoid burning bridges
- **Real reasons hidden**: manager problem, comp issue, growth gap → revealed in alumni surveys 3-6 months later
- **Solution**: 2-stage exit (immediate + 90-day follow-up) for valuable departures

---

## Common HR Process Pitfalls

1. **JR delay cascade**: HR slow on JR → manager gives up + freelancer hire informal → no HR record → liability later. SLA on JR critical (24-48h).

2. **Onboarding cliff**: day 1 great, day 8 abandoned. 90-day retention dies. Solution: scheduled 30/60/90 check-ins mandatory.

3. **PIP weaponization**: PIP used to manage out instead of develop → legal risk. PIP MUST be development-focused first, termination only after fair process.

4. **Bonus secrecy backfire**: bonuses kept secret → grapevine learns → unfair compared to imagined → resentment. Transparent framework better than secrecy.

5. **Compliance theater**: payroll done on time but accuracy poor → corrections cycle next month → trust eroded. Accuracy KPI as important as timing.

6. **Tribal HR knowledge**: HR admin knows all the workarounds, no documentation → admin leaves, everything breaks. Force codification.

7. **Manager-as-HR vacuum**: small departments, manager handles HR informally → no records, no compliance trail. Build minimum SOPs even small teams.

---

## Example: Worked SOP for HR-01 (Hire-to-Onboard)

Khi user request enterprise-grade hire-to-onboard SOP:

- **Section V Glossary**: role levels (M1-M5, IC1-IC5), employment types (full-time, contract, internship), VN labor law terms (HĐLĐ vô thời hạn, HĐLĐ xác định, HĐLĐ thử việc)
- **Section VIII Approval**: tiered by level (Hiring Mgr for IC1-IC3, HR Lead + Dept Head for IC4-M3, CEO for M4+)
- **Section XI RACI**: 7 sub-processes × 9 roles (HR/Recruiter/Hiring Mgr/Dept Head/Finance/Legal/IT/HSE/Employee)
- **Section XIII SLA**: typical 30-45 days end-to-end (JR → onboard day 1), 90 days to first checkpoint
- **Section XVI Forms**: BM-HR01-01 Manpower plan, BM-HR01-02 JR form, BM-HR01-03 Interview feedback, BM-HR01-04 Offer letter, BM-HR01-05 Onboarding checklist, BM-HR01-06 90-day review
- **Section XVII Compliance**: HR audit, labor inspector (annual), tax authority
- **Section XVIII Sanctions**: missed BHXH filing = financial penalty per Decree 28
