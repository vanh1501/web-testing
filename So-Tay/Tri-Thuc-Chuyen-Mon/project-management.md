---
title: "Project Management Methodology"
domain_tags: ["PM", "planning", "tracking"]
summary: "Lean PM methodology, artifact types, right-sizing framework"
keywords: ["project", "WBS", "RACI", "timeline", "status", "risk", "retro"]
applicable_agents: ["PRO-W04"]
last_updated: "2026-04-22"
version: "1.0.0"
---

# Project Management — PRO-W04 Domain Knowledge

## TL;DR
Lean PM: chỉ làm đủ ceremony cần thiết. Decompose → Assign → Track → Close. Right-size mọi thứ theo complexity. Output phải actionable, không phải giấy tờ.

## Complexity Auto-Sizing

| Signal | Size | Artifacts cần | Timeline |
|--------|------|---------------|----------|
| 1-3 tasks, 1-2 người, <1 tuần | **Mini** | Checklist only | Ngay |
| 4-10 tasks, 2-5 người, 1-4 tuần | **Small** | Brief + Task list + Status | Weekly check |
| 10-30 tasks, 5-10 người, 1-3 tháng | **Medium** | Brief + WBS + RACI + Timeline + Status + Risk | Weekly report |
| >30 tasks, >10 người, >3 tháng | **Large** | Full suite + Steering committee + Phase gates | Bi-weekly report |

## Artifact Templates (reference tại `.context/templates/`)

### Project Brief
Required fields: Objective (1-2 câu) → Scope (in/out) → Team (roles) → Timeline (milestones) → Budget (nếu có) → Risks (top 3) → Success criteria

### WBS (Work Breakdown Structure)
Level 1: Phases (3-5) → Level 2: Work packages → Level 3: Tasks (actionable)
Rule: task ở level cuối phải assignable cho 1 người, estimate được thời gian

### RACI Matrix
R = Responsible (làm), A = Accountable (chịu trách nhiệm cuối cùng, chỉ 1 người/task), C = Consulted (hỏi ý kiến), I = Informed (thông báo kết quả)
Rule: Mỗi task phải có đúng 1 chữ A. Nếu 0 hoặc >1 → flag

### Timeline
Format: Task → Owner → Start → End → Dependencies → Status
Visual: Gantt-style nếu >10 tasks, simple list nếu ≤10
Milestones: Đánh dấu rõ 3-5 milestones chính

### Status Report
Structure: Period → Overall RAG → Completed → In Progress → Blocked → Risks → Next Period
Rule: ≤1 trang. Sếp đọc 30 giây phải hiểu tình hình
Template: `.context/templates/status-report.md`

### Risk Register
Format: Risk → Probability (H/M/L) → Impact (H/M/L) → Score → Mitigation → Owner → Status
Rule: Top 5 risks minimum. Review weekly cho Medium+Large projects

### Retrospective
Format: What went well → What to improve → Action items (who + what + when)
Rule: Action items phải specific và có owner. "Làm tốt hơn" không phải action item

## Project Folder Convention
Khi user tạo project mới, tự động setup folder trong `projects/`:
```
projects/{epic-name}/{project-name}/
├── brief.md          # Project brief
├── tasks.md          # Task list / WBS
├── status/           # Status reports theo period
├── artifacts/        # Deliverables của project
└── notes.md          # Meeting notes, decisions
```

## Quality Rules
- PHẢI right-size: không áp framework nặng lên việc nhẹ
- PHẢI có 1 chữ A duy nhất trong mỗi row RACI
- CẤM tạo task không assignable (quá lớn hoặc quá mơ hồ)
- PHẢI estimate effort cho mỗi task level cuối
- NÊN close bằng 1 câu: "Bước tiếp theo bạn muốn [A], [B], hay [C]?"
