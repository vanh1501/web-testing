# Process Design Document (PDD)
> **Template version:** v1.0 | Dùng cho: Thiết kế quy trình mới (TO-BE) hoặc tài liệu hóa quy trình hiện có (AS-IS)
> Thay thế mọi `{{PLACEHOLDER}}` trước khi giao nộp. Xóa dòng hướng dẫn in nghiêng.

---

## Header

| Trường | Giá trị |
|--------|---------|
| **Tên quy trình** | {{TEN_QUY_TRINH}} |
| **Process ID** | {{PROCESS_ID}} |
| **Phòng ban chủ sở hữu** | {{PHONG_BAN_OWNER}} |
| **Process Owner** | {{PROCESS_OWNER}} |
| **Phiên bản** | {{PHIEN_BAN}} |
| **Ngày hiệu lực** | {{NGAY_HIEU_LUC}} |
| **Ngày review tiếp theo** | {{NGAY_REVIEW}} |
| **Trạng thái** | Draft ☐ / Review ☐ / Approved ☐ / Deprecated ☐ |
| **Loại tài liệu** | AS-IS ☐ / TO-BE ☐ / SOP ☐ |

---

## 1. Tổng quan quy trình

### 1.1 Mục đích
> *Giải thích tại sao quy trình này tồn tại — nó giải quyết vấn đề gì / tạo ra giá trị gì cho ai.*

{{MUC_DICH_QUY_TRINH}}

### 1.2 Phạm vi áp dụng

- **Áp dụng cho:** {{AP_DUNG_CHO}}
- **Trigger (Sự kiện kích hoạt):** {{TRIGGER}}
- **Điều kiện kết thúc:** {{DIEU_KIEN_KET_THUC}}
- **Không áp dụng cho:** {{NGOAI_PHAM_VI}}

### 1.3 SIPOC Summary

| Supplier | Input | Process Name | Output | Customer |
|----------|-------|-------------|--------|----------|
| {{SUPPLIER}} | {{INPUT}} | {{TEN_QUY_TRINH}} | {{OUTPUT}} | {{CUSTOMER}} |

---

## 2. Đo lường & KPI

| KPI | Công thức | Baseline (AS-IS) | Target (TO-BE) | Review cycle |
|-----|-----------|-----------------|----------------|-------------|
| Cycle Time | End - Start | {{BASELINE_CT}} | {{TARGET_CT}} | {{REVIEW}} |
| Error / Rework Rate | Lỗi / Tổng × 100% | {{BASELINE_ER}} | {{TARGET_ER}} | {{REVIEW}} |
| Wait Time Ratio | Wait / Cycle × 100% | {{BASELINE_WT}} | {{TARGET_WT}} | {{REVIEW}} |
| Output Quality Score | Per Effectiveness Audit | {{BASELINE_OQ}} | {{TARGET_OQ}} | {{REVIEW}} |
| {{KPI_CUSTOM_1}} | {{CONG_THUC_1}} | {{BASELINE_C1}} | {{TARGET_C1}} | {{REVIEW}} |

**ESOAR Ratio hiện tại:** {{ESOAR_RATIO}}% (Target: ≥60%)
**Value-Add Ratio hiện tại:** {{VALUE_ADD_RATIO}}% (Target: ≥50%)
**Process Health Score:** {{HEALTH_SCORE}}/100 — Verdict: {{VERDICT}}

---

## 3. Process Map (Bước chi tiết)

> *Điền đầy đủ mỗi bước. Bắt đầu bằng động từ hành động. Thêm/xóa hàng theo số bước thực tế.*

| Step # | Tên bước | Owner | Trigger / Điều kiện vào | Input | Hành động (chi tiết) | Output | SLA | ESOAR tag |
|--------|---------|-------|------------------------|-------|---------------------|--------|-----|-----------|
| 1 | {{TEN_1}} | {{ROLE_1}} | {{TRIGGER_1}} | {{INPUT_1}} | {{ACTION_1}} | {{OUTPUT_1}} | {{SLA_1}} | E/S/O/A/R |
| 2 | {{TEN_2}} | {{ROLE_2}} | {{TRIGGER_2}} | {{INPUT_2}} | {{ACTION_2}} | {{OUTPUT_2}} | {{SLA_2}} | E/S/O/A/R |
| 3 | {{TEN_3}} | {{ROLE_3}} | {{TRIGGER_3}} | {{INPUT_3}} | {{ACTION_3}} | {{OUTPUT_3}} | {{SLA_3}} | E/S/O/A/R |
| *(thêm hàng)* | | | | | | | | |

---

## 4. RACI Matrix

> *R = Responsible (người làm), A = Accountable (người chịu trách nhiệm), C = Consulted (cần hỏi ý kiến), I = Informed (cần thông báo)*

| Bước | {{ROLE_A}} | {{ROLE_B}} | {{ROLE_C}} | {{ROLE_D}} |
|------|-----------|-----------|-----------|-----------|
| Bước 1: {{TEN_1}} | R | A | C | I |
| Bước 2: {{TEN_2}} | | | | |
| Bước 3: {{TEN_3}} | | | | |
| *(thêm hàng)* | | | | |

---

## 5. Exception Handling

| # | Tình huống exception | Xảy ra ở bước | Người xử lý | Hành động xử lý | Escalate khi nào | Deadline xử lý |
|---|---------------------|--------------|------------|----------------|-----------------|---------------|
| 1 | {{EXCEPTION_1}} | Step {{N}} | {{ROLE_1}} | {{ACTION_1}} | {{ESCALATE_1}} | {{DEADLINE_1}} |
| 2 | {{EXCEPTION_2}} | Step {{N}} | {{ROLE_2}} | {{ACTION_2}} | {{ESCALATE_2}} | {{DEADLINE_2}} |
| 3 | {{EXCEPTION_3}} | Step {{N}} | {{ROLE_3}} | {{ACTION_3}} | {{ESCALATE_3}} | {{DEADLINE_3}} |

---

## 6. Automation Map

> *Dùng khi quy trình có automation component. Xóa section này nếu toàn manual.*

| Bước được tự động hóa | Loại automation | Tool / System | Trigger | Fallback khi lỗi | ROI estimate |
|----------------------|----------------|--------------|---------|-----------------|-------------|
| Step {{N}}: {{TEN}} | Rule-based / AI-assisted / RPA | {{TOOL}} | {{TRIGGER}} | {{FALLBACK}} | {{ROI}} |

---

## 7. Risk Register

| # | Rủi ro | Loại | Likelihood (1-5) | Impact (1-5) | Risk Score | Mitigation | Owner |
|---|-------|------|-----------------|-------------|-----------|-----------|-------|
| 1 | {{RIRI_1}} | SPOF/Data/Compliance/Dep/Knowledge | {{L_1}} | {{I_1}} | {{L×I}} | {{MITIGATION_1}} | {{OWNER_1}} |
| 2 | {{RIRI_2}} | | {{L_2}} | {{I_2}} | {{L×I}} | {{MITIGATION_2}} | {{OWNER_2}} |

**Risk Score tổng:** {{RISK_SCORE_TOTAL}} / 25 — Level: HIGH ☐ / MED ☐ / LOW ☐

---

## 8. AS-IS vs TO-BE Comparison (nếu là redesign)

> *Xóa section này nếu đây là quy trình hoàn toàn mới.*

| Chiều so sánh | AS-IS (Hiện tại) | TO-BE (Đề xuất) | Cải thiện |
|--------------|-----------------|-----------------|----------|
| Số bước | {{STEPS_AS_IS}} | {{STEPS_TO_BE}} | {{DELTA_STEPS}} |
| Cycle Time trung bình | {{CT_AS_IS}} | {{CT_TO_BE}} | {{PCT_IMPROVEMENT}}% |
| Error Rate | {{ER_AS_IS}} | {{ER_TO_BE}} | {{PCT_IMPROVEMENT}}% |
| Value-Add Ratio | {{VAR_AS_IS}} | {{VAR_TO_BE}} | {{DELTA_VAR}} pp |
| Chi phí nhân công/tháng | {{COST_AS_IS}} | {{COST_TO_BE}} | {{SAVINGS}}/tháng |

**Process_Improvement_Index:** {{PII}}%
**Payback Period (nếu có automation):** {{PAYBACK}} tháng

---

## 9. Implementation Plan

| Phase | Hành động | Owner | Start | End | Success Criteria |
|-------|----------|-------|-------|-----|-----------------|
| P1 — Pilot | {{ACTION_P1}} | {{OWNER_P1}} | {{START}} | {{END}} | {{SUCCESS_P1}} |
| P2 — Rollout | {{ACTION_P2}} | {{OWNER_P2}} | {{START}} | {{END}} | {{SUCCESS_P2}} |
| P3 — Optimize | {{ACTION_P3}} | {{OWNER_P3}} | {{START}} | {{END}} | {{SUCCESS_P3}} |

---

## 10. References & Biểu mẫu đính kèm

| # | Tên tài liệu | Loại | Link / Path | Phiên bản |
|---|-------------|------|------------|----------|
| 1 | {{TAI_LIEU_1}} | Form / Template / System / Policy | {{LINK_1}} | {{VER_1}} |
| 2 | {{TAI_LIEU_2}} | Form / Template / System / Policy | {{LINK_2}} | {{VER_2}} |

---

## 11. Change Log

| Version | Ngày | Người cập nhật | Nội dung thay đổi |
|---------|------|---------------|-----------------|
| {{VER}} | {{DATE}} | {{AUTHOR}} | {{CHANGES}} |
