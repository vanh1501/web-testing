### 4.2 `variant-back-hr-recruitment-monthly.md`

**Context:** Thuỷ (BOM BACK HR) cần báo cáo recruitment tháng 4 cho 1:1 với CEO Hà. Data: pipeline tracker Excel + interview feedback form Google.

#### HOOK customization

```yaml
HOOK_INPUT_SCHEMA:
  required_columns:
    - candidate_id: string
    - source: enum (linkedin_paid / referral / vietnamworks / cold_apply)
    - role: enum (senior_fe / ml_engineer / business_analyst / ...)
    - stage: enum (sourced / screen / interview / final / offer / hired / declined)
    - stage_date: YYYY-MM-DD
    - status: enum (active / passed / rejected / accepted / declined)
  sample_row:
    - C-1247, linkedin_paid, senior_fe, final, 2026-04-18, declined

HOOK_METRIC_CATALOG:
  primary:
    - hires: count(stage=hired)
    - target_achievement: hires / target * 100
    - time_to_hire: avg(hire_date - sourced_date) days
  funnel:
    - sourced_to_screen: count(screen) / count(sourced)
    - screen_to_interview: count(interview) / count(screen)
    - interview_to_final: count(final) / count(interview)
    - final_to_offer: count(offer) / count(final)
    - offer_to_hire: count(hired) / count(offer)
  source:
    - source_effectiveness: hires_per_source / cost_per_source

HOOK_PYRAMID_ANGLE: Hiring target achievement + funnel drop-off + source effectiveness

HOOK_OUTPUT_FORMAT:
  length: 12 dòng + funnel visual ASCII
  appendix: source comparison table
```

#### Sample output báo cáo

```
BÁO CÁO RECRUITMENT THÁNG 4 — 12 DÒNG

[Conclusion]
Hire 8/12 (achievement 67%, miss 33%); root cause tập trung ở 2 vị
trí Tech (Senior FE + ML Engineer) — final stage drop-off 44%
chủ yếu do salary mismatch.

[Key Finding 1 — Target Achievement]
- Hire 8 (target 12), miss 4 slot
- Time-to-hire trung bình 28 ngày (target ≤21 ngày, vượt 33%)
- 4 slot miss đều Tech roles; 8 slot hired đều Non-Tech

[Key Finding 2 — Funnel Drop-off]
Pipeline tháng 4:
Sourced 320 → Screen 142 (44%) → Interview 64 (45%) → Final 18 (28%)
→ Offer Accept 8 (44% drop ⚠)
- Drop lớn nhất: Final → Offer Accept (44% rớt)
- Reason chính (Tech): salary mismatch (75% candidate rejected
  offer cite "below market")

[Key Finding 3 — Source Effectiveness]
- LinkedIn paid: 35% hire, cost 12M/hire — best
- Referral: 28% hire, cost 5M/hire — most cost-effective
- Vietnamworks: 22% hire, cost 18M/hire ⚠ (4.5x LinkedIn cost)
- Cold apply: 15% hire, cost 0 — supplementary

[Decision Box]
Cần CEO Hà quyết tháng 5:
- Option A: +15% salary range Tech (align market p50 2026)
- Option B: Giữ range + extend timeline thêm 4 tuần
Owner: Thuỷ + Hà. Deadline: 03/05.
Phụ: Cắt Vietnamworks Q2 (cost 4.5x), reallocate referral incentive.
```

---
