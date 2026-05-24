# Workflow Anatomy — 4-Tier Architecture Reference

## Purpose
Chuẩn cấu trúc bắt buộc cho MỌI domain workflow trong hệ thống MAS 4.0.

## Mandatory 4-Tier Governance Structure

Mỗi workflow PHẢI có đủ 4 hạng mục sau (Chuẩn BPM Governance). Nếu thiếu bất kỳ hạng mục nào, `audit_workflows_bpm.py` sẽ đánh FAIL.

### 1. Frontmatter (T1)

```yaml
---
description: [Short definition]
---
```
*(Bắt buộc đối với CLI visibility và slash-command routing)*

### 2. Goal & Governance Context (T2)

```markdown
## Goal & Governance Context
- **Purpose:** [Why does this workflow exist?]
- **Scope:** [What boundaries does it operate within?]
```

**Anti-pattern:** ❌ Khai báo "Goal" khơi khơi nhưng không có Governance Scope → dẫn đến agent vượt quyền hạn.

### 3. Execution Steps (T3)

```markdown
## Execution Steps

### Step 1: [Action Name]
1. [Concrete imperative instruction]
2. [Next instruction]

### Step 2: [Action Name]
```

**Rules:**
- Dùng imperative form: "Load X", "Calculate Y" — KHÔNG dùng "You should..."
- Header các bước lớn phải dùng H3 (`###`).

### 4. Audit & Metrics (Quality Gates) (T4)

```markdown
## Audit & Metrics (Quality Gates)
- **Gate 1 ([Name]):** [Criteria for passing the gate]
- **Metrics:** [What numeric or Boolean metric defines success]
```

**Quy tắc Cốt Tử:** Mỗi pha hoàn thành đều phải có Gate để chặn trước khi sang pha tiếp theo hoặc kết thúc quy trình.

## Epistemic Wiring Block (Mandatory If Skills Needed)

Insert BEFORE Section 1 if the workflow uses any skills:

```markdown
## Assigned Skills
> [!IMPORTANT]
> Bắt buộc phải Load các kỹ năng sau trước khi chạy luồng:
> - **`[canonical-skill-id]`**: [Purpose — WHY this skill is needed here]
```

**Rule:** Canonical Skill ID MUST match exact folder name in `.agents/skills/`.
