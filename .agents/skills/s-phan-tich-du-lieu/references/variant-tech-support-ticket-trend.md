### 4.3 `variant-tech-support-ticket-trend.md`

**Context:** Tech Leader (Mind team) cần báo cáo support ticket tuần cho weekly với CTO Huy. Data: JIRA export 2 sprint cuối.

#### HOOK customization

```yaml
HOOK_INPUT_SCHEMA:
  required_columns:
    - ticket_id: string
    - severity: enum (P1 / P2 / P3 / P4)
    - category: enum (auth / data_sync / ui_bug / feature_request / other)
    - opened_at: ISO datetime
    - resolved_at: ISO datetime | null
    - reporter: string
    - assignee: string
    - status: enum (open / in_progress / resolved / closed / wontfix)

HOOK_METRIC_CATALOG:
  primary:
    - total_tickets: count(*)
    - MTTR_overall: avg(resolved_at - opened_at) hours
    - MTTR_by_severity: avg per P1/P2/P3/P4
    - severity_mix: count(P1+P2) / total
  trend:
    - volume_trend: tickets_per_day moving_avg_7
    - repeat_rate: tickets_with_same_category_within_30days / total
  SLA:
    - P1_SLA: target 4h; warning >6h
    - P2_SLA: target 24h; warning >48h
    - P3_SLA: target 7 days
    - P4_SLA: target 30 days

HOOK_PYRAMID_ANGLE: Ticket volume trend + severity mix + MTTR vs SLA + repeat issue pattern

HOOK_OUTPUT_FORMAT:
  length: 14 dòng + trend line chart inline
  appendix: top 5 repeat issues
```

#### Sample output báo cáo

```
BÁO CÁO TICKET TRACK — 2 SPRINT CUỐI — 14 DÒNG

[Conclusion]
Ticket volume tăng 28% (sprint 22→24), MTTR P1 vượt SLA 4h (actual
6.5h trung bình); root cause là 2 incident production (auth + data
sync) cùng 4 ticket carryover do thiếu E2E test coverage.

[Key Finding 1 — Volume Trend]
- Sprint 22: 38 ticket, sprint 23: 46, sprint 24: 49 (tăng 28%)
- Tickets per day moving avg 7d: từ 2.7 → 3.5
- 4 ticket carryover sprint 23 → 24, trong đó 2 ticket carryover
  2 sprint liên tiếp ⚠

[Key Finding 2 — Severity & MTTR]
- Severity mix: P1+P2 = 18% (vs healthy <12%) ⚠
- MTTR P1: 6.5h (target ≤4h, vượt SLA 62%)
- MTTR P2: 22h (target ≤24h, within SLA)
- 2 incident production: P1 auth flow (MTTR 4h), P2 data sync (18h)

[Key Finding 3 — Category & Repeat Pattern]
- Top category: auth (28%), data_sync (22%), ui_bug (18%)
- Repeat rate: 24% — top 3 issue lặp:
  - "auth token expired" (5 tickets/30d) — same root cause
  - "data sync delay >30s" (4 tickets/30d)
  - "FE form validation off" (3 tickets/30d)
- Repeat rate cao = thiếu permanent fix, chỉ fix triệu chứng

[Decision Box]
Cần CTO Huy quyết sprint 25:
- Option A: Hire Senior FE Q2 (align Thuỷ recruitment)
- Option B: Fast-track 1 mid-level dev → Senior + E2E Test Champion
Owner: Tech Lead + Huy. Deadline: D+3.
Đề xuất sprint 25 bắt buộc E2E coverage check trước merge.

[Chart inline — Line]
Tickets/day (7d MA): Sprint 22 ▁▂▂▂ Sprint 23 ▂▃▃▄ Sprint 24 ▄▅▆▆
```

---
