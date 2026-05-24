# BACK Variant — Budget Aggregation

> Ghi chú cho người đọc không chuyên kỹ thuật: Đây là ví dụ mẫu để tham khảo cách skill tạo 5 tài liệu đầu ra. Khi dùng cho phòng ban thật, cần thay tên người, dữ liệu, chỉ số và công cụ theo thực tế.


**Bối cảnh:** Anh Đình Anh (BOM BACK Kế toán) cần gom budget quý từ 12 phòng ban (Excel/Word/Sheet khác format) → 1 master budget thống nhất. Hiện mất 4 ngày/quý, discrepancy phát hiện muộn sau khi consolidate.

#### Tùy chỉnh theo phòng ban

```yaml
HOOK_DOMAIN_TAXONOMY:
  registry: Budget cycle 4 phase
  phases: [collect, normalize, consolidate, kiểm tra]

HOOK_ESOAR_THRESHOLD: 60/40 default

HOOK_SOP_TEMPLATE:
  base_sections: [Purpose, Scope, Roles, Procedure, Checklist, Escalation, Glossary]
  added_section: Compliance Check (PII / audit trail / phê duyệt)

HOOK_PILOT_DURATION: 1 quý (1 chu kỳ budget = scope-aligned)
```

#### Tài liệu đầu ra 1 — AS-IS Map (rút gọn 10 step → 5 key)

| Step | Người phụ trách chính | Thời lượng | Vấn đề |
|------|-------|----------|------|
| 1. Email request budget 12 phòng ban | Đình Anh | 30p | Send 12 email khác |
| 2-3. Phòng ban submit Excel/Word/Sheet | 12 BOM khác | 5-15p/phòng | Format inconsistent 12 cách |
| 4. Đình Anh download + organize | Đình Anh | 4h | Multi-format, version control loạn |
| 5. Normalize format (thủ công paste) | Đình Anh | 8h | Tedious, error-prone |
| 6. Validate currency unit + sum | Đình Anh | 2h | Phát hiện discrepancy muộn |
| 7. Consolidate master spreadsheet | Đình Anh | 4h | Manual paste 12 phòng |
| 8. Cross-check vs previous quarter | Đình Anh | 2h | Manual compare |
| 9. Generate kiểm tra packet | Đình Anh | 2h | Layout thủ công |
| 10. BOD kiểm tra meeting | CFO + Đình Anh | 1.5h | Discrepancy phát hiện late → rework |

**Vấn đề summary:** 4 ngày/quý cycle time, discrepancy phát hiện sau Step 6 → rework 30% case.

#### Tài liệu đầu ra 2 — ESOAR Matrix (10 step compact)

| Step | ESOAR | Lý do |
|------|-------|-----------|
| 1. Email request | **S** | Template email chuẩn + scheduled send |
| 2-3. Submit | **S** | Excel template chuẩn 1 format thay 12 cách |
| 4. Download organize | **E** | Cloud folder chuẩn → eliminate thủ công organize |
| 5. Normalize | **A** | Auto-parse từ template chuẩn (S Step 2-3 satisfied) |
| 6. Validate currency + sum | **A** | Auto-check validation quan-ly-quy-tac trong template |
| 7. Consolidate master | **A** | Auto-aggregate từ folder cloud (S+A satisfied) |
| 8. Cross-check quarter | **O** | Side-by-side view auto-rendered |
| 9. Generate kiểm tra packet | **O** | Template packet auto-fill |
| 10. BOD kiểm tra | **R** | Async pre-kiểm tra trước meeting → meeting chỉ decide |

**ESOAR Ratio:** E=1, S=2, O=2, A=3, R=1 → E+S+O = 5/10 = **50% ❌ fail 60/40**

→ **Action:** Document exception trong meta vì:
- Phòng ban Kế toán có 60% bước repeatable rule-based (validation, aggregation, parsing) phù hợp Automate sau khi S template chốt
- Exception rationale: "Internal aggregation process, low judgment requirement, 3 step Automate đều có S precedent (template form chuẩn Step 2-3)"
- BOM Đình Anh + Trainer phê duyệt bypass

**S-trước-A check:** Step 5,6,7 Automate → đều có S precedent ở Step 2-3 ✅

#### Tài liệu đầu ra 3 — TO-BE Design (7 step)

| Step | Người phụ trách chính | Thời lượng |
|------|-------|----------|
| 1. Scheduled email request (template) | Skill (auto) | 0p |
| 2. Phòng ban submit Excel chuẩn 1 format | 12 BOM | 5p/phòng |
| 3. Auto-parse + validate vào cloud | Skill (auto) | <5p |
| 4. Auto-aggregate master | Skill (auto) | <5p |
| 5. Auto-cross-check vs Q-1 | Skill (auto) | <5p |
| 6. Async pre-kiểm tra by CFO | CFO | 30p |
| 7. Decision meeting (short) | CFO + Đình Anh | 30p |

**Thời gian hoàn thành quy trình:** 4 ngày → **1.5 ngày** (saving 62%) | Discrepancy detect: Step 3 (immediate vs Step 6 trong AS-IS) | Đình Anh thủ công time: 22h → 4h/quý

#### Tài liệu đầu ra 4-5 — SOP + Pilot Plan

[Tương tự variant 1, condensed cho readability — SOP có added "Compliance Check" section yêu cầu PII redact + audit trail + 2-signature phê duyệt cho amount >100M VND. Pilot 1 quý = 1 chu kỳ budget, 3 phòng ban thử trước (MKT + HR + Tech) trước rollout 12 phòng ban Q3.]

**Tiêu chí thành công khi chạy thử:**
1. Thời gian hoàn thành quy trình ≤2 ngày (vs 4 hiện tại)
2. Discrepancy detect rate >80% trước Step 6
3. 3 phòng ban thử template không cần >1 vòng support
4. Audit trail 100% transactions
5. CFO satisfaction ≥4/5 với kiểm tra packet auto

---
