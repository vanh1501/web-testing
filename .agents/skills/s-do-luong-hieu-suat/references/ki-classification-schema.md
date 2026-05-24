# KI Classification Schema

This schema defines the allowed taxonomy values when extracting Telemetry Insights.

## 1. Domain Tags (`domain_tag`)
- `platform`: MAS Architecture, workflows, quan-ly-quy-tac, prompts, UI.
- `ops`: Project management, session loops, handoffs, error recovery.
- `quality`: Audit findings, scorecards, testing results, evals.
- `[custom]`: Specific business domains like `marketing`, `finance`, `hr`, `education`.

## 2. KI Types (`ki_type`)
- `pattern`: A recurring success factor or efficient method discovered.
- `failure`: A systemic break, hallucination, or error encountered.
- `decision`: An architectural or structural decision approved by the user.
- `standard`: A new metric, KPI, or checklist established.
- `config`: Environment settings, variable adjustments, or thresholds.

## 3. Confidence Levels (`confidence`)
- `HIGH`: Confirmed by user approval or passed automated evaluation.
- `MEDIUM`: Observed consistently across multiple turns, but not explicitly verified.
- `LOW`: A hypothesis or single-occurrence anomaly.

## 4. Synergy Data
- `handoff_reverts`: Number of times a task was returned to the maker.
- `critique_count`: Number of critical alerts or corrections issued.
