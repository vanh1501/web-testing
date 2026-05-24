# references/templates.md — Doc Templates (All 6 Diátaxis + Extensions)

## Purpose
Complete templates for each doc type. Load when creating new doc or restructuring existing.

---

## Template 1: Tutorial (Learning-Oriented)

**For**: Beginner learning a new skill through hands-on doing.
**Tone**: Encouraging, instructor-like, "you will..."
**Length**: Medium (45-90 min reading + doing)

```markdown
---
id: <name-of-tutorial>-tutorial
title: "<Tutorial Title — what learner will accomplish>"
type: tutorial
owner: <owner-slug>
status: draft
last_reviewed: <YYYY-MM-DD>
created: <YYYY-MM-DD>
review_due: <YYYY-MM-DD + 6 months>
tags: [<topic>, <skill-area>]
audience: <beginner-role>
depends_on: []  # Tutorials should be self-contained for newcomer
language: vi  # or en
---

# <Tutorial Title>

## Goal
By the end of this tutorial, bạn sẽ có thể: <specific, observable outcome>.

## Prerequisites
- <prerequisite knowledge or setup>
- <required tools/access>

**Estimated time**: <N> minutes

## Step 1: <Action verb> <noun>
<Brief context: what you're about to do and why>

<Concrete instructions — what to click, type, observe>

**Bạn nên thấy**: <expected result for this step — gives learner confidence>

**Nếu không**: <common error and how to fix>

## Step 2: <Next action>
<...>

## Step N: <Final action>
<...>

## Bạn đã làm được gì
Trong tutorial này, bạn đã:
- <accomplishment 1>
- <accomplishment 2>
- <accomplishment 3>

## Next Steps
Bây giờ bạn có thể:
- Try [<related tutorial>](<path>) to expand the skill
- Read [<explanation doc>](<path>) to understand the why
- Reference [<how-to>](<path>) when you need to do this in production
```

**Quality checks for Tutorial**:
- Does each step have an observable "you should see" outcome?
- Are common errors anticipated?
- Is the learner GAINING SKILL, not just following directions blindly?
- Self-contained (minimal external deps)?

---

## Template 2: How-to Guide (Problem-Oriented)

**For**: Competent user with specific goal, needs steps.
**Tone**: Directive, focused, no hand-holding.
**Length**: Short to medium (10-30 min reading)

```markdown
---
id: <action>-howto
title: "How to: <specific task>"
type: how-to
owner: <owner-slug>
status: draft
last_reviewed: <YYYY-MM-DD>
created: <YYYY-MM-DD>
review_due: <YYYY-MM-DD + 6 months>
tags: [<topic>, <action-area>]
audience: <competent-user-role>
depends_on: [<related-reference-doc>]
language: vi
---

# How to: <task name>

## Problem
<When and why you'd need to do this. 1-2 sentences.>

## Solution

### Step 1: <action>
<Direct instruction. Assume competence.>

### Step 2: <action>
<...>

### Step N: <action>
<...>

## Variations

### Variation A: <when condition X>
<modified steps>

### Variation B: <when condition Y>
<modified steps>

## Related
- [<related how-to>](<path>)
- [<reference doc for details>](<path>)
- [<explanation if user wants to understand why>](<path>)
```

**Quality checks for How-to**:
- Does it solve ONE specific problem (not multi-purpose)?
- Are variations enumerated (not just "depending on context, do X")?
- No hand-holding (reader is competent)?
- No background/theory (that's Explanation)?

---

## Template 3: Reference (Information-Oriented)

**For**: Expert looking up specific facts.
**Tone**: Dry, precise, structured, comprehensive.
**Length**: Variable (can be long, as long as well-organized).

```markdown
---
id: <subject>-reference
title: "<Subject> Reference"
type: reference
owner: <owner-slug>
status: draft
last_reviewed: <YYYY-MM-DD>
created: <YYYY-MM-DD>
review_due: <YYYY-MM-DD + 3 months>  # Reference cadence shorter
tags: [<topic>, <subject>]
audience: <expert-role>
depends_on: []
language: vi
---

# <Subject> Reference

## Summary
<1-2 sentence overview of what this reference covers>

## <Section 1: e.g., Endpoints / Parameters / Fields>

### <Item 1 name>
**Type**: <data type or category>
**Required**: Yes / No
**Default**: <default value>

<Description: what it is, when to use>

**Example**:
```<language>
<code or example>
```

### <Item 2 name>
<...>

## <Section 2: e.g., Examples / Common Patterns>

### Example: <use case>
```<language>
<code>
```

<Brief annotation>

## <Section 3: e.g., Errors / Limits / Constraints>

| Code | Meaning | Resolution |
|------|---------|------------|
| <c1> | <m1>    | <r1>       |
| <c2> | <m2>    | <r2>       |

## See Also
- [<related reference>](<path>)
- [<explanation of design rationale>](<path>)
```

**Quality checks for Reference**:
- Lookup-friendly (tables, lists, scannable)?
- Comprehensive within scope (no "see also for more" gaps in critical areas)?
- No tutorials embedded (no "let's walk through together")?
- No long discursive prose?

---

## Template 4: Explanation (Understanding-Oriented)

**For**: Curious reader wanting to understand "why."
**Tone**: Discursive, reflective, can be opinionated.
**Length**: Medium (15-45 min reading).

```markdown
---
id: <topic>-explanation
title: "<Topic>: <angle of explanation>"
type: explanation
owner: <owner-slug>
status: draft
last_reviewed: <YYYY-MM-DD>
created: <YYYY-MM-DD>
review_due: <YYYY-MM-DD + 12 months>  # Slow drift
tags: [<topic>, <concept-area>]
audience: <interested-reader>
depends_on: []
language: vi
---

# <Topic Title>: <Angle>

## Context
<The situation in which this concept matters. Why should reader care?>

## The Concept
<Discursive explanation. May include analogies, metaphors, historical context.>

<Build understanding progressively. Each paragraph develops the idea.>

## Why <design choice / convention>
<Rationale for choices. Trade-offs considered. What was rejected and why.>

## Implications
<What this means for how readers should think about or do things.>

- <Implication 1>
- <Implication 2>

## Common Misconceptions
**Misconception**: "<wrong understanding>"
**Reality**: <correct understanding + why misconception is appealing>

## See Also
- [<related explanation>](<path>)
- [<tutorial that applies this concept>](<path>)
- [<reference for facts>](<path>)
```

**Quality checks for Explanation**:
- Answers "why" not just "what"?
- Reader gains UNDERSTANDING, not procedure?
- Discursive (not step-by-step)?
- No action items embedded (that's Tutorial/How-to)?

---

## Template 5: Decision (ADR — Architectural Decision Record)

**For**: Historical record of significant decisions.
**Tone**: Factual, neutral, time-stamped.
**Length**: Short to medium.

```markdown
---
id: <decision-topic>-decision
title: "Decision: <Short title of decision>"
type: decision
owner: <decision-maker-slug>
status: published  # ADRs typically published immediately
last_reviewed: <YYYY-MM-DD>
created: <YYYY-MM-DD>
review_due: null  # ADRs don't expire (historical record)
tags: [<topic>, decision]
audience: <stakeholders>
depends_on: [<related-decisions>]
language: vi
---

# Decision: <Title>

## Status
proposed | accepted | superseded by [<new-decision>](<path>) | deprecated

## Context
<Situation that prompted this decision. What problem are we solving?>

<Constraints, forces at play.>

## Options Considered

### Option A: <name>
- Pros: <list>
- Cons: <list>

### Option B: <name>
- Pros: <list>
- Cons: <list>

### Option C: <name>
- Pros: <list>
- Cons: <list>

## Decision
**Chosen**: Option <X>

**Rationale**: <Why this option won, given the trade-offs>

## Consequences

### Positive
- <consequence 1>
- <consequence 2>

### Negative / Trade-offs
- <trade-off 1>
- <trade-off 2>

### Neutral
- <implication 1>

## Date
<YYYY-MM-DD>

## Decision-makers
- <Name, Role>
- <Name, Role>
```

**Quality checks for Decision**:
- Multiple options considered (not just chosen one)?
- Trade-offs explicit (not glossed)?
- Date stamped?
- Decision-makers named?
- Status accurate?

---

## Template 6: SOP (Standard Operating Procedure)

**For**: Operational procedures, often compliance-tied.
**Tone**: Formal, prescriptive, role-aware.
**Length**: Medium.

```markdown
---
id: <process>-sop
title: "SOP: <Process Name>"
type: sop
owner: <process-owner-slug>
status: draft
last_reviewed: <YYYY-MM-DD>
created: <YYYY-MM-DD>
review_due: <YYYY-MM-DD + 3 months>
tags: [<process>, <domain>, sop]
audience: <operator-roles>
depends_on: [<related-policies>, <reference-docs>]
language: vi
compliance: [<framework-if-applicable>]
---

# SOP: <Process Name>

## Purpose
<Why this SOP exists. What outcome it ensures.>

## Scope
- **Applies to**: <which teams, situations, products>
- **Does NOT apply to**: <exclusions>

## Roles & Responsibilities

| Role | Responsibility |
|------|----------------|
| <role 1> | <specific responsibility> |
| <role 2> | <specific responsibility> |

## Prerequisites
- <Required tools, access, training>

## Procedure

### Step 1: <action>
**Performer**: <role>
**Action**: <what to do>
**Verify**: <how to confirm step done correctly>

### Step 2: <action>
<...>

### Step N: <action>
<...>

## Compliance / Audit

**Compliance framework**: <name if applicable>

**Audit method**: <how adherence is verified>

**Audit frequency**: <quarterly / annually / per-event>

**Records to maintain**: <what evidence>

## Exceptions

**When deviations are allowed**: <conditions>

**Authorization required**: <who can approve deviation>

**Escalation path**: <if deviation creates issue>

## Related Documents
- [<Policy this SOP enforces>](<path>)
- [<Reference for tools/parameters>](<path>)
- [<Related SOPs>](<path>)

## Revision History
| Version | Date | Author | Change |
|---------|------|--------|--------|
| 1.0 | <date> | <name> | Initial publication |
```

**Quality checks for SOP**:
- Roles explicit (not "the team does X")?
- Each step has performer + action + verification?
- Compliance section completed if regulated?
- Exception path defined?
- Revision history started?

---

## Template 7: Runbook (Operational / Troubleshooting)

**For**: DevOps, SysAdmins, On-call engineers resolving system issues.
**Tone**: Urgent, precise, step-by-step, symptom-focused.
**Length**: Short to medium.

```markdown
---
id: <system-issue>-runbook
title: "Runbook: <Symptom or Issue Name>"
type: runbook
owner: <oncall-team-lead>
status: draft
last_reviewed: <YYYY-MM-DD>
created: <YYYY-MM-DD>
review_due: <YYYY-MM-DD + 3 months>
tags: [runbook, <system>, <component>]
audience: <oncall-engineer>
depends_on: [<architecture-explanation>, <api-reference>]
language: vi
---

# Runbook: <Issue Name>

## Symptoms
<What the alert looks like, what metrics drop, user reports>
- Alert ID/Name:
- Dashboard Link:

## Impact
<Severity of issue, affected users, data loss potential>

## Initial Triage (Pre-flight checks)
1. Check <service A status>
2. Check <log query B>

## Resolution Steps

### Step 1: <Action>
<Command or script to run>
```bash
$ kubectl restart deployment <name>
```
**Verify**: <Expected output>

### Step 2: <Action>
<...>

## Escalation
If issue persists after above steps:
- **Contact**: <Name or Team>
- **Slack channel**: <#channel>
- **Jira template**: <Link>

## Root Cause Reference
For deep dive into why this component fails, see [<Architecture Explanation>](<path>).
```

**Quality checks for Runbook**:
- Does it start with clear symptoms/alerts?
- Are commands copy-pasteable?
- Is there a clear escalation path if steps fail?
- Is theory/explanation separated out?

---

## Template Selection Guide

| Situation | Template |
|-----------|----------|
| "Bạn lần đầu học/làm việc X" → newcomer skill-building | Tutorial |
| "Bạn cần làm việc X cụ thể, đã biết context" → competent person solving problem | How-to |
| "Tra cứu chi tiết, parameters, API, fields..." → expert lookup | Reference |
| "Hiểu tại sao X được thiết kế thế này" → conceptual understanding | Explanation |
| "Ghi nhận quyết định quan trọng + lý do" → historical record | ADR (Decision) |
| "Quy trình vận hành chuẩn, có roles + compliance" → procedural standard | SOP |
| "Hướng dẫn xử lý sự cố hệ thống, troubleshooting" → operational execution | Runbook |

---

## Common Mistakes in Template Use

1. **Using "blank document" template** — no structure, no Diátaxis classification. → Use type-specific template from start.

2. **Filling Tutorial template for How-to content** — adds unnecessary hand-holding. → Match content to correct template.

3. **SOP without compliance section** when regulated — compliance gap. → Always include compliance section in regulated industries, mark "N/A" only if truly not applicable.

4. **Decision without options considered** — looks like fait accompli, no trace of trade-offs. → Even if only 2 options, document both.

5. **Reference written as prose** — defeats lookup purpose. → Use tables, lists, structured sections. Reference is for scanning.

---

## Custom Templates

If your domain needs a type beyond these 6 (e.g., `incident-report`, `runbook`, `lesson-learned`):

1. Define the new `type` in the schema enum
2. Create the template following same structure (YAML + body sections)
3. Document when to use it (Template Selection Guide entry)
4. Add to STANDARDIZE mode's Diátaxis purity check rules

Most domains can fit into the 6 standard types. Resist creating new types prematurely.
