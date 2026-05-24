# KD Variant — Space Customer Journey

> Ghi chú cho người đọc không chuyên kỹ thuật: Đây là ví dụ mẫu để tham khảo cách skill tạo 5 tài liệu đầu ra. Khi dùng cho phòng ban thật, cần thay tên người, dữ liệu, chỉ số và công cụ theo thực tế.


**Bối cảnh:** Chị Thơ (BOM KD Space) cần thiết kế process tracking khách hàng Space từ ad-hoc (3 nhân viên làm khác Excel cá nhân) → SOP team-wide thống nhất. No-show rate hiện tại 18% (mục tiêu ≤8%).

#### Tùy chỉnh theo phòng ban

```yaml
HOOK_DOMAIN_TAXONOMY:
  registry: Space customer journey 6 stage
  stages: [booking, setup, onsite, checkout, followup, repeat]

HOOK_ESOAR_THRESHOLD: 60/40 default

HOOK_SOP_TEMPLATE:
  base_sections: [Purpose, Scope, Roles, Procedure, Checklist, Escalation, Glossary]
  added_section: Customer Touchpoint (script + tone)

HOOK_PILOT_DURATION: 2 tuần (simple-moderate scope)
```

#### Tài liệu đầu ra 1 — AS-IS Map

| Step | Người phụ trách chính | Thời lượng | Công cụ | Kết quả đầu ra | Vấn đề |
|------|-------|----------|------|--------|------|
| 1. Receive booking call/online | Space staff (3 người khác) | 5p | Excel cá nhân + giấy | Booking note | 3 nhân viên dùng template khác → data inconsistent |
| 2. Confirm booking qua Zalo | Same staff | 10p | Zalo + Excel | Confirm msg | Có khi quên confirm → no-show |
| 3. Setup space pre-arrival | Cleaner | 30p | Checklist tay | Space ready | Checklist mỗi người khác |
| 4. Onsite greeting + walkthrough | Space staff | 20p | — | KH check-in | Greeting script không nhất quán |
| 5. Checkout + collect feedback | Space staff | 10p | Giấy survey | Feedback note | Feedback hay mất, không enter system |
| 6. Followup post-checkout (1 ngày) | BOM Thơ (thủ công) | 15p/KH | Zalo cá nhân | Thank you msg | Thơ làm thủ công, hay miss |
| 7. Update tracker | Space staff | 5p | Excel cá nhân | Updated row | Update 2 trackers riêng = duplicate |
| 8. Quarterly kiểm tra (BOM) | Thơ | 4h/quý | — | Pattern note | Khó analyze vì data scattered |

**Vấn đề summary:** No-show rate 18%, customer satisfaction 4.1/5 (mục tiêu ≥4.5), data scattered 3 Excel.

#### Tài liệu đầu ra 2 — ESOAR Matrix

| Step | ESOAR | Lý do | Kiểm tra nguyên tắc bắt buộc |
|------|-------|-----------|------------------|
| 1. Receive booking | **S** | Cần template chuẩn 1 form thay 3 Excel khác nhau | ✅ |
| 2. Confirm qua Zalo | **S** | Cần script chuẩn + checklist gửi | ✅ |
| 3. Setup pre-arrival | **S** | Cần checklist chuẩn cleaner all dùng | ✅ |
| 4. Onsite greeting | **S** | Cần greeting script chuẩn brand tone | ✅ |
| 5. Checkout + feedback | **O** | Survey enter trực tiếp tablet vs giấy → save thời gian | ✅ |
| 6. Followup post-checkout | **A** | Automate thank-you Zalo broadcast 24h sau checkout — đã Standardize trong S Step 4 voice | ✅ S-trước-A satisfied |
| 7. Update tracker | **E** | Eliminate duplicate Excel; data đã enter Step 1 form chuẩn flows tự động | ✅ |
| 8. Quarterly kiểm tra | **O** | BI report tự gen từ tracker chuẩn → BOM kiểm tra 1h thay 4h | ✅ |

**ESOAR Ratio:** E=1, S=4, O=2, A=1, R=0 → E+S+O = 7/8 = **87% ✅ pass 60/40**
**S-trước-A check:** Step 6 A có S precedent (Step 4 voice chuẩn) ✅

#### Tài liệu đầu ra 3 — TO-BE Design

Pipeline 6 step (down từ 8):

| Step | Người phụ trách chính | Thời lượng | Công cụ | Kết quả đầu ra |
|------|-------|----------|------|--------|
| 1. Receive booking | Space staff | 5p | Form Google chuẩn (1 form thay 3 Excel) | Booking entry |
| 2. Auto-confirm + reminder schedule | Skill (automated) | <1p | Zalo broadcast scheduled | Confirm + reminder |
| 3. Setup pre-arrival | Cleaner | 30p | Checklist chuẩn in cứng | Space ready |
| 4. Onsite greeting + walkthrough | Space staff | 20p | Script card | KH check-in |
| 5. Checkout + e-feedback | Space staff | 8p | Tablet survey | Feedback in system |
| 6. Auto-followup 24h | Skill (automated) | 0p (auto) | Zalo broadcast | Thank-you msg |

**Thời gian hoàn thành quy trình:** Booking → Checkout 48h (no change) | Manual time BOM Thơ: 4h/quý → 1h/quý (saving 75%) | No-show rate target: 18% → 8% (-55%)
**Complexity check:** 6 step vs 8 step ✅ | Người phụ trách chính clear per step ✅

#### Tài liệu đầu ra 4 — SOP doc (rút gọn 4 dòng/section)

```
SOP — Space Customer Journey v1.0

1. PURPOSE
   Chuẩn hóa quy trình tracking khách hàng Space, giảm no-show
   rate từ 18% xuống ≤8% và đồng đều trải nghiệm KH bất kể nhân
   viên nào phục vụ.

2. SCOPE
   In: tất cả booking Space MindX 3 chi nhánh.
   Out: corporate booking >10 người (escalate BOM trực tiếp).

3. ROLES
   - Space Staff (3 người): Step 1, 4, 5
   - Cleaner: Step 3
   - Skill automation: Step 2, 6
   - BOM Thơ: kiểm tra quarterly + handle escalation

4. PROCEDURE
   [6 step như TO-BE bảng trên — chi tiết script + form link]

5. CHECKLIST (gate per step)
   Step 1: ☐ Form đầy đủ 6 field bắt buộc
   Step 2: ☐ Confirm Zalo sent <5p sau Step 1
   Step 3: ☐ 12 item checklist setup tick hết
   Step 4: ☐ Greeting script delivered + walkthrough <20p
   Step 5: ☐ 5-question survey filled before KH leave
   Step 6: ☐ Thank-you Zalo delivered + KH read receipt

6. ESCALATION
   - Form data thiếu/sai → Space staff → BOM Thơ <2h
   - Customer complaint onsite → BOM Thơ ngay
   - System down (form/Zalo) → Tech Leader

7. CUSTOMER TOUCHPOINT (added section per HOOK)
   Greeting script v1.0: "Chào anh/chị [TÊN], em là [NAME] từ
   Space MindX. Em sẽ walkthrough nhanh 3 phút..."
   Tone: ấm áp, không robot, không quá thân mật.

8. GLOSSARY
   - Walkthrough: tour giới thiệu space 3-5 phút
   - No-show: KH booked không đến trong 30p sau giờ booking
```

#### Tài liệu đầu ra 5 — Pilot Plan

```
PILOT PLAN — Space Customer Journey v1.0

DURATION: 2 tuần (T+0 → T+14)
PARTICIPANTS: 2 nhân viên Space chi nhánh quận 1 (test cùng input
- R6 mode-uniform)

SUCCESS CRITERIA (5 measurable):
1. Thời gian hoàn thành quy trình booking → checkout ≤48h (current: 48h, maintain)
2. No-show rate ≤12% (current: 18%, intermediate target trước
   final ≤8%)
3. Customer satisfaction ≥4.3/5 (current: 4.1)
4. Form data completeness ≥95% (vs Excel cũ ~70%)
5. 2 nhân viên cùng KH input → 2 SOP execution >85% match
   (Standardize Test)

SCHEDULE:
- D0: Kick-off + train 2 nhân viên (1.5h)
- D7: Mid-pilot checkpoint (kiểm tra 10 KH first)
- D14: Retrospective + final metrics

TOP 3 RISK + MITIGATION:
1. Nhân viên cũ resist form mới
   → daily standup 5p Week 1 support + ưu tiên form ease-of-use
2. Zalo automation fail (Step 2/6)
   → fallback thủ công confirm Space staff trong 10p
3. Survey tablet not engaging
   → A/B test 2 design tablet vs paper-with-QR

GO/NO-GO CRITERIA (D14 retrospective):
- GO full deploy 3 chi nhánh: ≥4/5 success criteria PASS
- ITERATE: 3/5 PASS → tinh chỉnh script/form 1 tuần → re-pilot
- ABANDON: <3/5 PASS → BOM Thơ + Trainer kiểm tra root cause
```

---
