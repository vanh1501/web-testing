# Tech Variant — K12 Content Review

> Ghi chú cho người đọc không chuyên kỹ thuật: Đây là ví dụ mẫu để tham khảo cách skill tạo 5 tài liệu đầu ra. Khi dùng cho phòng ban thật, cần thay tên người, dữ liệu, chỉ số và công cụ theo thực tế.


**Bối cảnh:** Anh Hiếu (BOM Tech Product K12) cần process kiểm tra nội dung K12 từ ad-hoc kiểm traer riêng lẻ → workflow chuẩn có age-appropriate check + STEM accuracy + parent communication compliance. Hiện defect rate post-release 12% (parent complaints), kiểm tra time 8h/lesson không nhất quán.

#### Tùy chỉnh theo phòng ban

```yaml
HOOK_DOMAIN_TAXONOMY:
  registry: K12 content kiểm tra 5 stage
  stages: [intake, draft_check, age_check, stem_check, approve_release]

HOOK_ESOAR_THRESHOLD: 60/40 default

HOOK_SOP_TEMPLATE:
  base_sections: [Purpose, Scope, Roles, Procedure, Checklist, Escalation, Glossary]
  added_section: Quality Gate (rubric / test / parent comm compliance)

HOOK_PILOT_DURATION: 2 tuần (test 2 lesson sample)
```

#### Tài liệu đầu ra 1 — AS-IS Map (6 step)

| Step | Người phụ trách chính | Thời lượng | Vấn đề |
|------|-------|----------|------|
| 1. Receive draft lesson | Hiếu | 5p | Email scattered |
| 2. Assign kiểm traer | Hiếu | 10p | Pick ad-hoc, no load balancing |
| 3. Reviewer 1 thủ công check | Junior Reviewer | 3h | No rubric → kiểm tra style khác nhau |
| 4. Reviewer 2 senior check | Senior Reviewer | 3h | Duplicate Step 3 effort |
| 5. Parent communication check | Hiếu (thủ công) | 1h | Hay miss |
| 6. Approve + release | Hiếu | 1h | No automated compliance keyword scan |

**Vấn đề:** 8h/lesson, defect 12%, parent complaints chủ yếu about age-inappropriate vocabulary slip through.

#### Tài liệu đầu ra 2 — ESOAR Matrix

| Step | ESOAR | Lý do |
|------|-------|-----------|
| 1. Receive draft | **S** | Submission portal chuẩn 1 format thay email |
| 2. Assign kiểm traer | **O** | Load balancing logic dựa kiểm traer capacity |
| 3. Junior thủ công | **S** | Rubric checklist chuẩn (age + content) |
| 4. Senior thủ công | **E** | Eliminate khi rubric Junior pass; chỉ Senior khi escalation |
| 5. Parent comm check | **A** | Compliance keyword scan auto (đã có S rubric Step 3) |
| 6. Approve + release | **S** | Checklist gate phê duyệt |

**ESOAR Ratio:** E=1, S=3, O=1, A=1, R=0 → E+S+O = 5/6 = **83% ✅ strong pass**
**S-trước-A:** Step 5 A có S precedent (Step 3 rubric) ✅

#### Tài liệu đầu ra 3-5 — TO-BE + SOP + Pilot

[Condensed: TO-BE 5 step down từ 6, kiểm tra time per lesson 8h → 4h (saving 50%), defect target 12% → 5%. SOP added Quality Gate section với 3 rubric (Age-appropriate vocabulary list per grade / STEM accuracy fact-check list / Parent communication tone guide). Pilot 2 tuần với 2 lesson sample (1 elementary + 1 middle school), success criteria: kiểm tra time ≤4h, defect post-release ≤5%, 0 parent complaint.]
