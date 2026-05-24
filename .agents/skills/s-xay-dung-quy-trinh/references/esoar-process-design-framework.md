# ESOAR Process Design Framework
> **Phiên bản:** v1.0 | **Áp dụng cho:** Xây dựng và tối ưu hóa quy trình — Mới / Cải tiến / Audit
> **Loại:** Process Engineering Framework — Design + Redesign + Audit

---

## 1. Tổng quan ESOAR

ESOAR là phương pháp thiết kế quy trình theo trình tự bắt buộc:

```
E — Eliminate   → Loại bỏ bước không tạo giá trị
S — Standardize → Chuẩn hóa bước còn lại
O — Optimize    → Tối ưu thứ tự, tài nguyên, thời gian
A — Automate    → Tự động hóa bước đã chuẩn hóa + tối ưu
R — Robotize    → Đưa lên AI / agent / RPA đầy đủ
```

**Quy tắc tối thượng:** **S trước A** — không Automate bước chưa Standardize.
Vi phạm quy tắc này = automate sai quy trình = lãng phí gấp đôi.

---

## 2. Kiến trúc 5 Phase ESOAR

```
Phase 1: PROCESS CAPTURE       (AS-IS)  → Ghi nhận quy trình hiện tại
Phase 2: WASTE AUDIT           (E)      → Phát hiện và loại bỏ lãng phí
Phase 3: STANDARDIZE & DESIGN  (S + O)  → Thiết kế TO-BE chuẩn hóa
Phase 4: AUTOMATION DESIGN     (A + R)  → Xác định điểm tự động hóa
Phase 5: VALIDATION            (ALL)    → Kiểm tra trước triển khai
```

---

## 3. Phase 1 — PROCESS CAPTURE (AS-IS)

### 3.1 SIPOC Capture

Điền bảng SIPOC cho quy trình đang phân tích:

| Supplier | Input | Process | Output | Customer |
|----------|-------|---------|--------|----------|
| Ai cung cấp đầu vào? | Dữ liệu / vật liệu đầu vào | Các bước chính (5-7 bước) | Kết quả đầu ra | Ai nhận kết quả? |

**Quy tắc SIPOC:**
- Process: ghi 5-7 bước, mỗi bước bắt đầu bằng động từ hành động
- Output: phải đo lường được (không được viết "thông tin được xử lý")
- Customer: phân biệt Internal Customer và External Customer

### 3.2 Process Map OIPO

Với mỗi bước trong Process, lập bảng OIPO:

| Step # | Bước | Owner | Input | Process (chi tiết) | Output | SLA / Thời gian |
|--------|------|-------|-------|-------------------|--------|----------------|
| 1 | {{TEN_BUOC}} | {{OWNER}} | {{INPUT}} | {{CHI_TIET}} | {{OUTPUT}} | {{SLA}} |

**Đo lường bắt buộc cho mỗi bước:**
- **Actual Time:** Thời gian thực tế (hỏi người thực hiện, không ước tính)
- **Wait Time:** Thời gian chờ giữa các bước (thường bị bỏ sót)
- **Error Rate:** % lần thực hiện phải làm lại hoặc escalate

```
Total Process Time = Σ(Actual_Time_i) + Σ(Wait_Time_i)
Value-Add Ratio = Σ(Actual_Time của bước Value-Add) / Total Process Time × 100%
Target: Value-Add Ratio ≥ 50% (quy trình hiệu quả)
```

### 3.3 Pain Matrix

Phỏng vấn ≥2 người thực hiện quy trình và ≥1 người nhận output. Điền bảng:

| Pain Point | Bước xảy ra | Frequency (lần/tuần) | Impact (H/M/L) | Nguyên nhân gốc rễ |
|-----------|-------------|--------------------|----|-------------------|
| {{PAIN_1}} | Step {{N}} | {{FREQ}} | H/M/L | {{ROOT_CAUSE}} |

---

## 4. Phase 2 — WASTE AUDIT (E — Eliminate)

### 4.1 8 Loại Lãng phí (TIMWOODS)

Kiểm tra mỗi bước trong OIPO map với checklist sau:

| # | Loại lãng phí | Câu hỏi kiểm tra | Indicator |
|---|--------------|-----------------|-----------|
| T | **Transport** | Thông tin/vật liệu di chuyển không cần thiết không? | Email forward nhiều lần, file copy nhiều nơi |
| I | **Inventory** | Có task tồn đọng / queue chờ xử lý không? | Hộp thư đến đầy, file chưa xử lý >2 ngày |
| M | **Motion** | Người thực hiện phải tra cứu / tìm kiếm nhiều không? | >2 lần switch app/tab để hoàn thành 1 bước |
| W | **Waiting** | Có thời gian chờ phê duyệt / phản hồi không? | Wait Time >30% Actual Time của bước đó |
| O | **Over-processing** | Có bước nào làm kỹ hơn mức khách hàng cần không? | Report 20 trang khi khách cần 2 trang |
| O | **Overproduction** | Có output tạo ra nhưng không dùng không? | Báo cáo không ai đọc, data không dùng |
| D | **Defects** | Có lỗi phải làm lại không? | Error Rate >5% = đáng lo ngại |
| S | **Skills** | Có công việc được giao sai người không? | Senior làm việc của junior |

### 4.2 Eliminate Decision Matrix

Với mỗi bước phát hiện lãng phí, ra quyết định:

| Bước | Loại lãng phí | Value-Add? | Quyết định | Lý do |
|------|--------------|-----------|----------|-------|
| Step N | T/I/M/W/O/D/S | Có / Không | **ELIMINATE** / KEEP / REDUCE | {{LY_DO}} |

**Quy tắc Eliminate:**
- ELIMINATE ngay: bước không tạo giá trị + không bắt buộc (compliance/safety)
- REDUCE: bước tạo ít giá trị nhưng vẫn cần thiết → tối thiểu hóa
- KEEP: bước Value-Add hoặc bắt buộc (không thể loại)

```
Sau Phase 2: tính lại Value-Add Ratio với tập bước đã loại
Target improvement: Value-Add Ratio tăng ≥15 percentage points
```

---

## 5. Phase 3 — STANDARDIZE & DESIGN (S + O)

### 5.1 Standardize — 5 thành phần bắt buộc

Với mỗi bước còn lại (đã qua Eliminate), chuẩn hóa:

1. **Trigger** — Sự kiện / điều kiện kích hoạt bước này (VD: "Nhận email request từ Sales")
2. **Input rõ** — Tên file / form / dữ liệu đầu vào cụ thể (không viết chung "thông tin cần thiết")
3. **Execution steps** — Hướng dẫn từng bước con (số thứ tự, động từ hành động)
4. **Output rõ** — Tên file / form / dữ liệu đầu ra cụ thể + format chuẩn
5. **Exception handling** — Làm gì khi input thiếu / lỗi / edge case

### 5.2 TO-BE Process Map

Vẽ lại OIPO map cho TO-BE với các bước đã Eliminate + Standardize. Tính:

```
Process_Improvement_Index = (AS_IS_Total_Time - TO_BE_Total_Time) / AS_IS_Total_Time × 100%
Error_Reduction_Index     = (AS_IS_Error_Rate - TO_BE_Error_Rate) / AS_IS_Error_Rate × 100%
```

**Benchmark:**
- Process_Improvement_Index ≥ 20% → cải tiến đáng kể
- Error_Reduction_Index ≥ 30% → giảm lỗi đáng kể

### 5.3 Optimize — Sắp xếp lại thứ tự

Với TO-BE map, kiểm tra:
- Bước nào có thể thực hiện song song (parallel) thay vì tuần tự?
- Bước nào phụ thuộc vào bước nào? (Dependency mapping)
- Bước có Wait Time cao → có thể trigger async không?

---

## 6. Phase 4 — AUTOMATION DESIGN (A + R)

### 6.1 Automation Readiness Checklist

Trước khi đưa vào Automate, bước phải đạt **tất cả** tiêu chí sau:

- [ ] Đã Standardize đầy đủ (5 thành phần Phase 3)?
- [ ] Input có format nhất quán (không ambiguous)?
- [ ] Business rule rõ ràng, không cần judgment chủ quan?
- [ ] Error Rate AS-IS < 5% (đủ stable để automate)?
- [ ] Volume đủ lớn để ROI dương trong ≤12 tháng?

**Nếu bất kỳ checkbox nào chưa đạt → KHÔNG automate. Quay lại S.**

### 6.2 Automation Type Selection

| Loại | Khi nào dùng | Tool example | ROI Horizon |
|------|-------------|-------------|-------------|
| **Rule-based trigger** | If-then đơn giản, 1 điều kiện | Zapier, Make, Power Automate | ≤3 tháng |
| **Form → Workflow** | Thu thập thông tin → route đến người xử lý | Jotform, Google Forms + Sheets | ≤3 tháng |
| **Document generation** | Template fill từ data | Doc merge, Canva API | ≤6 tháng |
| **AI-assisted** (R tier) | Judgment cần, nhưng có pattern | Claude Agent, GPT-4o | 6-12 tháng |
| **Full RPA** | Lặp lại 100%, không exception | UiPath, Power Automate Desktop | 12+ tháng |

### 6.3 ROI Calculation

```
Manual_Cost_Monthly = (Thời_gian_bước/60) × Hourly_rate × Volume_tháng
Automation_Cost_Monthly = Setup_cost / Payback_months + License_monthly
ROI = (Manual_Cost_Monthly - Automation_Cost_Monthly) / Automation_Cost_Monthly × 100%
Payback_period = Setup_cost / (Manual_Cost_Monthly - License_monthly)
```

**Cấm automate** nếu Payback_period > 18 tháng với điều kiện bình thường.

---

## 7. Phase 5 — VALIDATION

### 7.1 Process Validation Checklist trước Go-Live

- [ ] TO-BE map được review bởi người thực hiện (không chỉ quản lý)?
- [ ] Exception handling đã test với ≥3 edge case thực tế?
- [ ] SLA TO-BE được stakeholder chấp nhận?
- [ ] Rollback plan nếu TO-BE phát sinh lỗi?
- [ ] Training material cho người thực hiện?
- [ ] Measurement framework: ai đo, đo gì, bao giờ review?

### 7.2 KPI Tracking Framework

| KPI | Công thức | Baseline (AS-IS) | Target (TO-BE) | Review cycle |
|-----|-----------|-----------------|----------------|-------------|
| Cycle time | Tổng thời gian từ trigger → output | {{BASELINE}} | {{TARGET}} | Tuần đầu |
| Error rate | Lỗi / Tổng lần thực hiện × 100% | {{BASELINE}} | {{TARGET}} | Hàng tuần |
| Cost per unit | Chi phí nhân công / đơn vị | {{BASELINE}} | {{TARGET}} | Hàng tháng |
| Satisfaction | Score từ Customer (nội bộ) | {{BASELINE}} | {{TARGET}} | Hàng tháng |

---

## 8. ESOAR Ratio Rule

```
ESOAR_Ratio = (Count_E + Count_S + Count_O) / Total_steps × 100%
Target: ESOAR_Ratio ≥ 60%

Exception allowed: Workspace "Concierge Assistant" board — must document
reason in meta: {"esoar_exception": "concierge_board", "justification": "..."}
```

Vi phạm ESOAR Ratio mà không có exception document → WARN tới người thiết kế.
