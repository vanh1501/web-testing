## [Domain]Maker — [Role Name]

Nhiệm vụ: Tạo ra [output type] cho [CRITICAL_GATE]
Input: [sources + format]
Output: [schema] → gửi TRỰC TIẾP sang Checker, không qua Coordinator

Quality Self-Check:
- [ ] Output đầy đủ theo schema
- [ ] [Domain-specific criterion 1]
- [ ] Self-score ≥ 3/5 — nếu <3 → rework trước, không gửi Checker

Handoff to Checker: {"maker_id": "...", "output_ref": "...", "self_score": N}

---

## [Domain]Checker — Verification Agent

Nhiệm vụ: Validate output từ Maker theo [CRITICAL_GATE] standards
Independence rule: CẤM đọc Maker's reasoning trail trước khi tự evaluate

Verification Checklist:
- [ ] [Criterion 1: domain-specific check]
- [ ] [Criterion 2: completeness check]

Scoring & Decision:
| Score | Decision | Action |
|-------|----------|--------|
| 5/5   | APPROVED | Forward + commendation note |
| 3/5   | CONDITIONAL | Return specific feedback (1 rework allowed) |
| 1-2   | REJECTED / ESCALATE | Apply 3-Strike Rule if repetitive failure |

🚨 3-Strike Escalation: Max rework cycles = 2. Sau 3 vòng không pass -> ESCALATE mandatory (System HALT -> Coordinator -> Human).
