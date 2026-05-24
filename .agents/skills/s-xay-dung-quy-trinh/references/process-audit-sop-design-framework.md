# Process Audit & SOP Design Framework
> **Phiên bản:** v1.0 | **Áp dụng cho:** Kiểm toán quy trình hiện có + thiết kế SOP chuẩn
> **Loại:** Audit Framework + Documentation Standard

---

## 1. Mục đích & Phân biệt với ESOAR

Framework này **không thiết kế quy trình mới** — đây là công cụ **kiểm toán quy trình đang chạy** và **viết SOP chuẩn hóa**. Dùng khi:

- Quy trình đang hoạt động nhưng chưa có tài liệu
- Quy trình có sẵn SOP nhưng cần audit xem có đang được tuân thủ không
- Cần baseline measurement trước khi cải tiến (đầu vào cho ESOAR)

**Chuỗi kết hợp điển hình:**
```
Process Audit Framework (đây) → AS-IS baseline
        ↓
ESOAR Framework → TO-BE thiết kế
        ↓
SOP Writing Section (đây) → SOP tài liệu hóa TO-BE
```

---

## 2. Module 1 — Process Audit (4 Dimension)

### 2.1 Kiến trúc Audit

Mọi cuộc kiểm toán quy trình phải đánh giá đủ 4 Dimension:

```
D1: COMPLIANCE     → Quy trình có đang được thực hiện đúng như thiết kế?
D2: EFFICIENCY     → Quy trình có đang được thực hiện hiệu quả về thời gian / chi phí?
D3: EFFECTIVENESS  → Quy trình có đang tạo ra output đúng như kỳ vọng?
D4: RISK           → Quy trình có điểm mù / rủi ro / single point of failure?
```

### 2.2 D1 — Compliance Audit

**Bước 1:** Thu thập SOP / quy trình chính thức hiện tại (nếu có)
**Bước 2:** Shadow observation — quan sát người thực hiện thực tế (≥3 lần thực hiện)
**Bước 3:** Điền Compliance Gap Matrix:

| Bước SOP chính thức | Thực tế đang làm | Có tuân thủ? | Lý do lệch (nếu có) | Severity |
|---------------------|-----------------|-------------|---------------------|----------|
| {{BUOC_SOP}} | {{THUC_TE}} | Có / Không / Partial | {{LY_DO}} | H/M/L |

**Compliance Score:**
```
Compliance_Score = Count_Có / Total_steps × 100%
≥ 80%: PASS
60-79%: WARN — cần retraining hoặc SOP review
< 60%: FAIL — quy trình hoặc SOP cần redesign ngay
```

### 2.3 D2 — Efficiency Audit

**Đo lường 4 chỉ số:**

| Chỉ số | Công thức | Benchmark |
|--------|-----------|-----------|
| **Cycle Time** | End time - Start time (tính từ khi nhận trigger đến khi output) | Tùy ngành |
| **Processing Time** | Tổng thời gian người thực sự làm việc (loại wait time) | ≥50% Cycle Time = tốt |
| **Wait Time Ratio** | (Cycle Time - Processing Time) / Cycle Time × 100% | ≤40% = chấp nhận được |
| **Rework Rate** | Số lần làm lại / Tổng lần thực hiện × 100% | ≤5% = ổn |

**Time Study Protocol:**
1. Chọn 10 lần thực hiện quy trình (không thông báo trước)
2. Ghi thời gian bắt đầu và kết thúc mỗi bước
3. Tính trung bình và độ lệch chuẩn
4. Nếu Std_Dev > 30% của Mean → quy trình thiếu nhất quán → cần Standardize

### 2.4 D3 — Effectiveness Audit

**Xác định Output Quality Criteria:**
- Hỏi Internal/External Customer: "Output tốt theo tiêu chí nào?"
- Liệt kê 3-5 tiêu chí đo lường được

**Điền bảng:**

| Tiêu chí output | Trọng số | Đo bằng cách nào | Kết quả đo | Đánh giá |
|----------------|----------|-----------------|-----------|----------|
| {{TIEU_CHI_1}} | {{W_1}} | {{CACH_DO_1}} | {{KQ_1}} | Pass/Fail |
| {{TIEU_CHI_2}} | {{W_2}} | {{CACH_DO_2}} | {{KQ_2}} | Pass/Fail |

```
Effectiveness_Score = Σ(W_i × Score_i) / Σ(W_i) × 100
≥85: Hiệu quả cao
70-84: Chấp nhận được
<70: Cần cải tiến đáng kể
```

### 2.5 D4 — Risk Audit

**Kiểm tra 5 loại rủi ro:**

| Loại rủi ro | Câu hỏi kiểm tra | Indicator nguy hiểm |
|------------|-----------------|---------------------|
| **Single Point of Failure** | Có bước chỉ 1 người làm được không? | "Chỉ có anh/chị X biết làm" |
| **Data Loss** | Dữ liệu quan trọng được lưu ở đâu? Backup? | File trên máy cá nhân, không backup |
| **Compliance Risk** | Có bước nào liên quan đến PII / pháp lý không? | Không có audit trail |
| **Dependency Risk** | Quy trình phụ thuộc vào hệ thống ngoài nào? | Third-party SLA không có |
| **Knowledge Risk** | Quy trình có documented không? | Chỉ trong đầu người thực hiện |

**Risk Rating:**
```
Risk_Score = Σ(Likelihood_i × Impact_i) / Total_risks
Likelihood: 1 (hiếm) đến 5 (thường xuyên)
Impact: 1 (nhẹ) đến 5 (nghiêm trọng)
Risk_Score ≥ 15: HIGH → cần action plan ngay
```

---

## 3. Module 2 — SOP Writing Standard

### 3.1 Cấu trúc SOP bắt buộc (7 Section)

Mỗi SOP phải có đủ 7 section sau theo thứ tự:

```
Section 1: HEADER          → Metadata quản lý tài liệu
Section 2: PURPOSE         → Tại sao SOP này tồn tại
Section 3: SCOPE           → Áp dụng cho ai, quy trình nào, giới hạn
Section 4: DEFINITIONS     → Thuật ngữ + viết tắt
Section 5: PROCEDURE       → Hướng dẫn từng bước (nội dung chính)
Section 6: EXCEPTION HANDLING → Xử lý khi exception / lỗi
Section 7: REFERENCES      → Biểu mẫu, hệ thống, tài liệu liên quan
```

### 3.2 Section 5 — PROCEDURE Writing Rules

**Quy tắc viết từng bước:**

1. Mỗi bước bắt đầu bằng **động từ hành động** (Nhập / Gửi / Kiểm tra / Phê duyệt / Tải lên)
2. Mỗi bước có **1 hành động duy nhất** — không ghép 2 hành động
3. Mỗi bước có tên người/role thực hiện (không để "ai đó")
4. Mỗi bước có **điều kiện chuyển tiếp** (khi nào sang bước tiếp theo)
5. Screenshot hoặc ví dụ với bước có giao diện phức tạp

**Cấu trúc từng bước:**
```markdown
## Bước [N]: [Động từ] + [Đối tượng hành động]
**Người thực hiện:** [Role/Tên]
**Trigger:** [Khi nào thực hiện bước này]
**Action:**
  1. [Hành động con 1]
  2. [Hành động con 2]
**Output:** [Kết quả cụ thể sau khi hoàn thành]
**Chuyển tiếp:** [Sang Bước N+1 / Nếu X thì → Bước N+3]
```

### 3.3 Exception Handling Matrix (Section 6)

| Tình huống exception | Bước xảy ra | Người xử lý | Hành động | Escalate khi nào |
|---------------------|-------------|------------|-----------|-----------------|
| {{EXCEPTION_1}} | Step {{N}} | {{ROLE_1}} | {{ACTION_1}} | {{ESCALATE_1}} |
| {{EXCEPTION_2}} | Step {{N}} | {{ROLE_2}} | {{ACTION_2}} | {{ESCALATE_2}} |

### 3.4 SOP Quality Checklist

Trước khi publish SOP, kiểm tra:

- [ ] Mỗi bước có 1 động từ hành động duy nhất?
- [ ] Mỗi bước có người thực hiện rõ ràng?
- [ ] Mỗi bước có output đo được?
- [ ] Tất cả exception phổ biến đã được xử lý?
- [ ] Người thực hiện thực tế đã review và xác nhận SOP khả thi?
- [ ] Tài liệu liên quan đã liệt kê đầy đủ?
- [ ] Ngày hiệu lực và version control đã ghi?

---

## 4. Module 3 — Process Health Score

### 4.1 Tổng hợp 4 Dimension

Tính Process Health Score sau khi audit xong:

```
Process_Health_Score = 
  D1_Compliance_Score × 0.30
  + D2_Efficiency_Score × 0.25
  + D3_Effectiveness_Score × 0.30
  + (100 - D4_Risk_Score_normalized) × 0.15

Trọng số tổng: 1.00
```

**D2_Efficiency_Score formula:**
```
D2 = (1 - Wait_Time_Ratio/100) × 50 + (1 - Rework_Rate/100) × 50
```

**D4_Risk_Score_normalized:**
```
D4_normalized = (D4_Risk_Score / 25) × 100  [capping max 25 = full risk]
```

### 4.2 Health Score Verdict

| Score | Verdict | Hành động bắt buộc |
|-------|---------|-------------------|
| ≥ 80 | **HEALTHY** | Duy trì, review hàng quý |
| 65-79 | **NEEDS IMPROVEMENT** | Lập kế hoạch cải tiến trong 60 ngày |
| 50-64 | **CRITICAL** | Ưu tiên redesign trong 30 ngày |
| < 50 | **BROKEN** | Stop + redesign ngay, không chờ lịch |

---

## 5. Anti-Patterns khi Audit & Viết SOP

| Anti-pattern | Hệ quả | Fix |
|---|---|---|
| Audit chỉ hỏi quản lý, không quan sát thực tế | Compliance Gap bị che giấu | Bắt buộc shadow observation ≥3 lần |
| SOP viết bởi người không làm quy trình | SOP thiếu edge case, không thực tế | Co-write với người thực hiện thực tế |
| Bước SOP quá dài, ghép nhiều hành động | Người đọc không hiểu, bỏ qua bước | Enforce 1 bước = 1 hành động |
| SOP không có version control | Người dùng version cũ | Header bắt buộc Version + Ngày hiệu lực + Owner |
| Audit 1 lần rồi không review | SOP lỗi thời trong 6 tháng | Lịch review định kỳ: quy trình quan trọng = 6 tháng/lần |
