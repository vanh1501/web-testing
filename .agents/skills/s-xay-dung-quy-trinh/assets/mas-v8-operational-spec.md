# Đặc tả chuẩn (Spec) cho Workflow và Skill trên Google Antigravity
*Phiên bản V8.0 - Dành cho môi trường Vận hành (Operations)*

## 1. Nguyên tắc thiết kế cốt lõi
- **Workflow:** Quy trình thao tác do người vận hành gọi bằng slash command. Chỉ điều phối: kiểm đầu vào, gọi Skill phù hợp, rẽ nhánh xử lý, yêu cầu người thật duyệt và đóng gói đầu ra. Không nhét logic tính toán, phân tích vào Workflow.
- **Skill:** Kỹ năng tác vụ chuyên biệt mà agent tự chọn khi yêu cầu khớp mô tả. Làm một việc rõ ràng, tái sử dụng ở nhiều Workflow.

**Công thức tối ưu:**
`Rule = luật bắt buộc | Workflow = đường đi | Skill = năng lực chuyên môn | Business source = tài liệu nghiệp vụ`

## 2. Cấu trúc thư mục tối ưu
- **Workflow:** File phẳng trong `.agents/workflows/<workflow-name>.md`
- **Skill:** Thư mục riêng trong `.agents/skills/<skill-name>/` (Bắt buộc có `SKILL.md`, `references/`, `assets/`, `scripts/`, `evals/`).
- **Tài liệu nghiệp vụ:** Để trong `/business_sources/` (hoặc `Kho-Du-Lieu/`), không nhét vào `.agents/`.

## 3. Spec chuẩn cho Workflow

```markdown
---
name: [workflow-name]
slash_command: /[workflow-name]
purpose: [Workflow này chuẩn hóa quy trình gì]
owner: [role chịu trách nhiệm]
inputs: [input_1, input_2, input_3]
outputs: [output_1, output_2, output_3]
skill_targets: [skill_1, skill_2, skill_3]
version: v1.0
---

👤 **Owner:** [role]  
🛠 **Skill Target:** [skill_1, skill_2, skill_3]

# Workflow: [Tên workflow]

## Purpose
[Mục đích nghiệp vụ của workflow]

## Trigger
Use this workflow when:
- [Tình huống 1]
Do not use this workflow when:
- [Trường hợp không phù hợp]

## Prerequisites
Before running this workflow, ensure:
- [Tài liệu/Template cần có]

## Inputs
| Input | Required? | Owner | Description | Example |
|---|---|---|---|---|
| [input_1] | Yes | [role] | [mô tả] | [ví dụ] |

## Steps
1. **Check source pack:** Kiểm tra input bắt buộc.
2. **Run input validation:** Call skill validation.
3. **Run domain processing:** Call skill xử lý.
4. **Generate draft output:** Call skill xuất bản.
5. **Human checkpoint:** [Role] duyệt.
6. **Package final output:** Đóng gói.

## Validation
- [ ] Trigger đúng.
- [ ] Input bắt buộc đã đủ.
- [ ] Skill đã được gọi đúng vai trò.
- [ ] Human checkpoint đã thực hiện.

## Outputs
| Output | Format | Receiver | Notes |
|---|---|---|---|
| [output_1] | Markdown/Doc/Sheet | [role] | [ghi chú] |

## Human Checkpoint
Require approval from [role] before:
- Gửi output cho lãnh đạo/khách hàng.

## Edge Cases
| Case | Handling |
|---|---|
| Missing input | Dừng và yêu cầu bổ sung |

## Test Prompt
```text
Hãy chạy workflow /[workflow-name] với input sau:
- [input mẫu]
Kỳ vọng: ...
```
(đóng markdown block)

## 4. Spec chuẩn cho Skill
```markdown
---
name: [skill-name]
version: v1.0
description: |
  WHAT: [mô tả năng lực cụ thể]
  WHEN: [khi nào agent nên tự dùng skill này]
trigger: [điều kiện kích hoạt]
license: Internal
owner: [role]
status: active
---

# Skill: [Tên skill]

## Purpose
[Mục đích nghiệp vụ]

## When to Use / When Not to Use
...

## Inputs
| Input | Required? | Description | Example |
|---|---|---|---|
| [input_1] | Yes | [mô tả] | [ví dụ] |

## How to Use
1. Check input completeness.
2. Apply template.
3. Process task.
4. Flag missing/risky data.
5. Return output with assumptions.

## Output Format
# [Output Title]
## 1. Summary
## 2. Main Output
## 3. Assumptions
## 4. QA Checklist

## Human Checkpoint
Require review from [role] before:
- Gửi output ra ngoài.

## Edge Cases
| Case | Handling |
|---|---|
| Missing required input | Dừng và yêu cầu input |

## QA Checklist & Test Prompts
...
```
(đóng markdown block)

## 5. Anti-pattern cần tránh
- Một Skill ôm cả quy trình.
- Workflow chứa công thức tính toán/phân tích dài.
- Thiếu Human checkpoint (đặc biệt với quyết định tài chính/nhân sự).
