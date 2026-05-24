---
id: "WF-BPM-LIFECYCLE-01"
name: "w-s-xay-dung-quy-trinh"
description: "Pipeline End-to-End hỗ trợ BOM thiết kế quy trình mới, kiểm định quy trình hiện hành, và tối ưu quy trình kém hiệu quả. 3 luồng: CREATE / AUDIT / OPTIMIZE. Output SOP Package 6 thành phần chuẩn doanh nghiệp. Áp dụng BPM Lifecycle (Plan-Do-Check-Act) + Socratic Scaffolding."
version: v2.0
status: Production-Ready
semantic_triggers: ['xây quy trình', 'chuẩn hóa SOP', 'thiết kế quy trình', 'audit quy trình', 'kiểm định SOP', 'tối ưu quy trình', 'cải tiến workflow', 'PDCA', 'BPM', 'ESOAR', 'AS-IS TO-BE', 'process design']
owner: "PRO-W06"
skill_target: "00-xay-dung-quy-trinh, 00-tao-tai-lieu, 00-chuan-hoa-tai-lieu"
hitl_timeout: "24h"
retry_policy: {max_attempts: 3, backoff: exponential_1s_2s_4s, fallback: "log_to_ACTION-LOG_and_report_human"}
---

- **👤 Owner:** `[@PRO-W06]`
- **🛠 Skill Target:** `[00-xay-dung-quy-trinh, 00-tao-tai-lieu, 00-chuan-hoa-tai-lieu]`
- **⏱ HITL Timeout:** 24h
- **🔄 Circuit Breaker:** retry 3 lần, fallback → ACTION-LOG + human

# Quy Trình: /w-xay-dung-quy-trinh (v2.0 — BPM Lifecycle Pipeline)

## Purpose & Scope

**Purpose:** Hỗ trợ BOM (Business Operations Manager) thiết kế quy trình mới, kiểm định quy trình hiện hành, tối ưu quy trình kém hiệu quả. Mỗi lượt vận hành xuất ra **SOP Package 6 thành phần** chuẩn doanh nghiệp.

**Scope:** BPM Lifecycle (Plan → Do → Check → Act). KHÔNG bao gồm: viết policy pháp lý (chuyển pháp chế), xây tool tự động hóa hoàn chỉnh, tự ý đổi KPI/quyền phê duyệt phòng ban.

## Trigger

BOM gõ `/w-xay-dung-quy-trinh` hoặc nói: "tạo quy trình mới", "audit SOP", "tối ưu quy trình", "cải tiến workflow", "PDCA quy trình".

## Prerequisites

- [ ] BOM cung cấp tên quy trình + phòng ban + vấn đề đang gặp (Luồng 1, 3) hoặc đường dẫn SOP cũ (Luồng 2)
- [ ] Workspace có folder `Kho-Du-Lieu/Ket-Qua/` để lưu SOP Package

## Routing — Step 0 (Bộ Điều Phối 3 luồng)

| Tín hiệu từ BOM | Luồng |
|-----------------|-------|
| "Tạo quy trình mới", "Xây SOP", "Thiết kế workflow" | **Luồng 1: CREATE (Tạo mới)** |
| "Kiểm định quy trình", "Audit SOP", "Đánh giá quy trình hiện tại" | **Luồng 2: AUDIT (Kiểm định)** |
| "Tối ưu quy trình", "Quy trình X chậm/lỗi", "Cải tiến workflow" | **Luồng 3: OPTIMIZE (Tối ưu)** |

**Auto-clarify:** Nếu BOM nói chung chung ("Giúp tôi về quy trình tuyển dụng"), Agent ask: "Anh/Chị muốn TẠO MỚI, KIỂM ĐỊNH, hay TỐI ƯU quy trình này?"

---

## Luồng 1: CREATE (Tạo mới)

> [!IMPORTANT] KARPATHY VERIFICATION MANDATE
> Mỗi Bước: `[Step] -> verify: [Tiêu chí]`. CẤM Blind Looping.

### Bước 1.1 — Scaffolding (IPO Intake)
**Action:** Gọi `00-xay-dung-quy-trinh` (sub-mode: ipo_intake) hỏi BOM theo bộ khung **IPO**:
- **Input:** Quy trình bắt đầu từ đâu? Data/tài liệu nào cần có?
- **Process:** Ai làm gì, theo thứ tự nào? (liệt kê sơ bộ)
- **Output:** Kết quả cuối cùng mong đợi (Biên bản, báo cáo, sản phẩm)
**Verify:** Có Input + Output rõ. Process có thể sơ bộ. Hỏi tối đa 3 câu, không thẩm vấn.

### Bước 1.2 — Socratic Challenge (HITL Gate 1)
**Action:** Gọi `00-xay-dung-quy-trinh` (sub-mode: socratic_challenge) đặt **MỘT (01) câu hỏi** thách thức logic dựa trên IPO. Ví dụ:
- *"Nếu người phụ trách chính nghỉ phép, ai thay thế ở bước X?"*
- *"Bước Y hiện tại mất bao lâu? KPI nào đo hiệu quả?"*
**HITL Timeout:** 24h. BOM trả lời challenge.
**Decision:** Đủ context → Bước 1.3 | BOM không trả lời được → log gap, proceed với assumption ghi rõ.

### Bước 1.3 — Technical Design (SOP Package 6 thành phần)
**Action:** Gọi `00-xay-dung-quy-trinh` (sub-mode: full_design) build 5 deliverables theo skill + 1 Executive README:

| # | Thành phần | Skill sub-action |
|---|------------|------------------|
| 1 | IPO Map (AS-IS) | as_is_mapper |
| 2 | ESOAR Matrix | esoar_evaluator |
| 3 | TO-BE Design | to_be_designer |
| 4 | SOP 7 mục | sop_writer |
| 5 | Pilot Plan | pilot_planner |
| 6 | Executive README 1 trang | (chain `00-tao-tai-lieu` document_type: executive_report) |

**Verify:** Skill return Output Contract với 5 deliverable_files + eso_ratio ≥0.60 (hoặc exception documented).

### Bước 1.4 — Approve & Publish (HITL Gate 2)
**Action:** Trình bày SOP Package draft cho BOM.
**Decision:** Approve → publish | Modify → áp feedback resubmit.
**HITL Timeout:** 24h. Sau timeout: pause + reminder, không auto-publish.

**Action sau approve:** Chain `00-chuan-hoa-tai-lieu` xuất DOCX file `Kho-Du-Lieu/Ket-Qua/{ten-quy-trinh}/06-SOP-PACKAGE.docx`. Update Bảng Điều Khiển registry.

**Guidance cuối:** Gợi ý BOM lên lịch chạy Luồng 2 AUDIT sau 30 ngày vận hành.

---

## Luồng 2: AUDIT (Kiểm định)

### Bước 2.1 — Scope Definition
**Action:** Hỏi BOM: "Audit quy trình nào? Hay toàn bộ?"
**Verify:** Có path SOP hoặc tên quy trình cụ thể.

### Bước 2.2 — PDCA Assessment
**Action:** Gọi `00-xay-dung-quy-trinh` (sub-mode: pdca_audit) đánh giá quy trình theo 4 tiêu chí PDCA:

| Tiêu chí | Câu hỏi kiểm định | Phương pháp |
|----------|-------------------|-------------|
| **Plan** | SOP đủ 7 mục? Có IPO Map? | File check |
| **Do** | Nhân sự tuân thủ? Biểu mẫu có dùng? | Interview / file usage check |
| **Check** | KPI Framework có theo dõi? Số liệu gần nhất? | Data check |
| **Act** | Lần cập nhật gần nhất? Có feedback từ nhân sự? | Version history |

**Verify:** Skill return Process Health Scorecard A-F + evidence per criterion.

### Bước 2.3 — Report & Routing (HITL Gate 3)
**Action:** Trình bày Scorecard cho BOM.
**Decision:**
- Đạt **A hoặc B** → quy trình khỏe mạnh, hẹn audit tiếp theo (30-60 ngày)
- Đạt **C trở xuống** → đề xuất chuyển Luồng 3 OPTIMIZE
- BOM phê duyệt next step.
**HITL Timeout:** 24h.

---

## Luồng 3: OPTIMIZE (Tối ưu)

### Bước 3.1 — Pain Point Diagnosis
**Action:** Hỏi BOM: "Vấn đề lớn nhất với quy trình này là gì?" (vd chậm, thiếu người, sai sót lặp lại).
**Verify:** BOM cung cấp ≥1 pain point cụ thể.

### Bước 3.2 — Socratic Root Cause Challenge
**Action:** Gọi `00-xay-dung-quy-trinh` (sub-mode: socratic_root_cause) đặt **MỘT câu hỏi** thách thức root cause. Ví dụ:
- *"Bước duyệt chậm là do thiếu nhân sự hay quá nhiều tầng phê duyệt?"*
**Verify:** Xác định Root Cause trước khi đề xuất giải pháp.

### Bước 3.3 — Before/After Delta Design
**Action:** Gọi `00-xay-dung-quy-trinh` (sub-mode: optimize_delta) sinh **Bảng So sánh Trước/Sau**:
- Bước nào bỏ/gộp?
- KPI nào thay đổi?
- Ai chịu trách nhiệm mới?
**Verify:** Output có Delta table + tuân ESOAR 60/40.

### Bước 3.4 — Approve Optimization (HITL Gate 4)
**Action:** Trình bày Delta plan cho BOM.
**Decision:** Approve → Bước 3.5 | Reject → quay 3.3 với feedback.
**HITL Timeout:** 24h.

### Bước 3.5 — Update & Monitor
**Action:** Update SOP Package (tăng version, ghi lịch sử thay đổi). Chain `00-chuan-hoa-tai-lieu` để xuất bản version mới. Update Bảng Điều Khiển registry.
**Guidance:** Gợi ý BOM theo dõi KPI mới trong 2 tuần, sau đó chạy lại Luồng 2 AUDIT để đo hiệu quả (vòng lặp PDCA).

---

## HITL Gates Summary

| Gate | Luồng | Step | Timeout | Action on timeout |
|------|-------|------|---------|-------------------|
| Gate 1 | L1 | 1.2 Socratic | 24h | Log gap + proceed với assumption |
| Gate 2 | L1 | 1.4 Approve Publish | 24h | Pause + reminder, không auto-publish |
| Gate 3 | L2 | 2.3 Routing decision | 24h | Default = ship Scorecard, không auto-route Luồng 3 |
| Gate 4 | L3 | 3.4 Approve Delta | 24h | Pause + reminder |

## Circuit Breaker Policy

| Failure mode | Detection | Retry | Fallback |
|--------------|-----------|-------|----------|
| Skill timeout | 60s no response | 3 lần | ACTION-LOG + human |
| ESOAR ratio <0.60 (Luồng 1) | Skill validate | 0 (immediate) | Flag exception, BOM phải document lý do + người phê duyệt |
| SOP cũ không parse được (Luồng 2) | File format error | 1 lần (try alternative parser) | REFUSE audit, ask BOM cung cấp SOP chuẩn hóa |
| Root cause không identify được (Luồng 3) | Skill return null | 1 lần (ask BOM thêm context) | Log "Root cause unknown", suggest external consultant |

## Edge Cases & Recovery

1. **BOM yêu cầu viết policy pháp lý** → REFUSE, chuyển pháp chế (policy ≠ process)
2. **BOM muốn tự động hóa bước chưa standardize** → REFUSE automate, yêu cầu Luồng 1 standardize trước
3. **Quy trình liên phòng ban** → Yêu cầu BOM confirm các đầu mối liên quan trước Bước 1.3
4. **Data nhạy cảm trong quy trình** (PII, salary, contract) → Skill flag, ask ẩn danh hoặc giảm scope
5. **BOM muốn redesign >20% số bước** (Luồng 3) → Yêu cầu manager approval trước Bước 3.4
6. **ESOAR E+S+O <60%** → Cảnh báo, yêu cầu BOM document exception với lý do + người phê duyệt
7. **Bước không rõ người phụ trách** → Tạm dừng, hỏi xác định 1 person (không chấp nhận "team")
8. **Quy trình ad-hoc (shadow process) không có tài liệu chính thức** → HALT, yêu cầu chuẩn hóa và confirm với manager

## Output Contract (Idempotent JSON)

```json
{
  "workflow_id": "WF-BPM-LIFECYCLE-01",
  "luong_executed": "L1_CREATE | L2_AUDIT | L3_OPTIMIZE",
  "run_status": "success | halt_at_gate | halt_at_failure",
  "process_metadata": {
    "name": "Quy trình tuyển dụng v2",
    "department": "HR",
    "version": "v2.0"
  },
  "deliverables": {
    "ipo_map": "...",
    "esoar_matrix": "...",
    "to_be_design": "...",
    "sop": "...",
    "pilot_plan": "...",
    "executive_readme": "..."
  },
  "luong_specific_data": {
    "L1": {"eso_ratio": 0.875, "step_count_to_be": 8},
    "L2": {"pdca_scorecard": "B", "passed_criteria": 3, "failed_criteria": 1},
    "L3": {"root_cause": "Phê duyệt 3 tầng dư thừa", "delta_steps_removed": 2}
  },
  "skills_invoked": ["00-xay-dung-quy-trinh", "00-tao-tai-lieu", "00-chuan-hoa-tai-lieu"],
  "hitl_gates_triggered": ["Gate 2"],
  "circuit_breaker_activated": false,
  "next_workflow_suggested": "L2 AUDIT (sau 30 ngày) | L3 OPTIMIZE (nếu Scorecard ≤C)"
}
```

## Chuẩn Đầu Ra — SOP Package 6 thành phần (Luồng 1, 3)

```
Kho-Du-Lieu/Ket-Qua/{ten-quy-trinh}/
├── 01-IPO-MAP.md              ← Sơ đồ Input-Process-Output
├── 02-SOP.md                  ← Tài liệu SOP 7 mục chuẩn
├── 03-BIEU-MAU.md             ← Biểu mẫu thực thi (Forms/Checklist)
├── 04-KPI-FRAMEWORK.md        ← Khung chỉ số đo lường
├── 05-AUDIT-CHECKLIST.md      ← Bảng kiểm cho kiểm định định kỳ
└── 06-EXECUTIVE-README.md     ← Tóm tắt 1 trang cho lãnh đạo
```

> [!IMPORTANT] Hard-Gate
> Nếu bất kỳ thành phần nào bị thiếu, Agent KHÔNG ĐƯỢC báo hoàn thành. Phải quay lại bổ sung.

## Cross-Workflow Chaining

- **Receives from:** `00-phan-tich-nhiem-vu` (sub-task "chuẩn hóa quy trình")
- **Hands off to:** `00-san-xuat-tai-lieu` (format SOP Package thành DOCX/PPTX cuối cùng)
- **Internal chain:** Luồng 2 → Luồng 3 nếu Scorecard ≤C (Gate 3)

## Validation

- [ ] Luồng 1: 6 deliverables đầy đủ
- [ ] Luồng 1: ESOAR E+S+O ≥60% hoặc có exception document
- [ ] Luồng 2: Scorecard có evidence per PDCA criterion
- [ ] Luồng 3: Delta plan có before/after rõ
- [ ] Mọi Hard-Gate có HITL timeout declared
- [ ] Mandatory chain `00-chuan-hoa-tai-lieu` đã chạy cho final ship
- [ ] JSON Output Contract đầy đủ

## Resources

- Skill: `00-xay-dung-quy-trinh` (sub-modes: ipo_intake, socratic_challenge, full_design, pdca_audit, optimize_delta)
- Skill: `00-tao-tai-lieu` (cho Executive README + Slide deck nếu cần)
- Skill: `00-chuan-hoa-tai-lieu` (mandatory final ship)
- Output path: `Kho-Du-Lieu/Ket-Qua/{ten-quy-trinh}/`
- Templates: `assets/output-templates/` của skill `00-xay-dung-quy-trinh`
