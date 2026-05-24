# references/update.md — UPDATE Mode Protocol (Full)

## Purpose
Detailed protocol for Mode 3 (UPDATE). Load when entering UPDATE mode.

## SECI Mapping
Externalization + Combination revisited. Capture new tacit knowledge (when system/process changes) + recombine with existing explicit knowledge.

---

## Update Triggers — 4 Types

Each trigger initiates UPDATE mode differently.

### Trigger Type 1: Time-Based

Doc's `review_due` ≤ today.

**Action**:
1. Notify owner: "Doc X is due for review. Verify still accurate?"
2. Owner runs Refresh OR Revise based on findings
3. Update `last_reviewed`, recompute `review_due`

**Cadence per type** (default):
- Tutorial: 6 months
- How-to: 6 months
- Reference: 3 months (high downstream impact)
- Explanation: 12 months (slow drift)
- Decision (ADR): never (historical record)
- SOP: 3 months (operational, compliance)

### Trigger Type 2: Event-Based

External event invalidates doc content:
- Dependency doc changed (cascade)
- System/product changed (e.g., new feature, API change)
- Regulation changed
- Org structure changed (process owner moved)
- User reported error

**Action**:
1. Identify scope of impact (which docs affected?)
2. Apply changes per affected doc
3. Cascade check (see below)
4. Notify dependent doc owners

### Trigger Type 3: Audit-Based

Quarterly ROT audit flags doc.

**Action**:
1. Run ROT classification (Keep / Consolidate / Archive)
2. Execute decision

### Trigger Type 4: Manual

Owner initiates update voluntarily (knew change was coming).

**Action**:
1. Classify update type
2. Apply changes
3. Cascade check

---

## ROT Analysis (for Audit-Triggered Updates)

ROT = Redundant + Obsolete + Trivial.

### Per-Doc Assessment

For each doc, evaluate:

| Dimension | Signal | Threshold |
|---|---|---|
| **Redundant** | Content duplicates elsewhere | Similarity >70% with another doc |
| **Obsolete** | Outdated, no longer accurate | `last_reviewed` > 12 months AND system_changed |
| **Trivial** | Low value | Views <5/quarter AND no inbound links |
| **Link rot** | Broken outbound links | Any 404 in inline links |
| **Contradiction** | Conflicts with newer doc | Detected during audit |

### Verdict per doc

- **Keep**: No ROT signals. Refresh metadata only.
- **Consolidate** (Redundant): Merge with canonical, redirect.
- **Revise** (Obsolete + still needed): Update content.
- **Archive** (Obsolete + not needed, OR Trivial): Remove from active KB, retain in archive.
- **Reconcile** (Contradiction): Decision needed on which is canonical.

### Aggregate Metrics

```
ROT % = (Consolidate + Archive + Reconcile) / Total docs in audit scope

Healthy KB: < 15%
Typical unmanaged KB: 30-50%
Sick KB: > 50%
```

Track quarter-over-quarter. Trend matters more than absolute number.

---

## Cascade Analysis (Systems Thinking)

**Critical**: Never point-fix. Always trace upstream + downstream.

### Upstream Trace

For doc X being updated:
1. Read `depends_on` field — these are upstream deps
2. For each upstream doc:
   - Is the issue we're fixing in X actually rooted upstream?
   - If yes → fix upstream FIRST
3. Recursively check upstream of upstream (max depth 3)

**Example**: User reports `complaint-howto` says 30% discount, should be 20%.
- Upstream: `refund-policy-explanation`
- Check: does it also say 30%?
- If yes → ROOT CAUSE upstream. Fix `refund-policy-explanation` first. `complaint-howto` may auto-resolve if it references upstream rather than hardcoding.

### Downstream Trace

For doc X being updated:
1. Query inverse index — which docs depend on X?
2. For each downstream doc:
   - Will my change to X break their assumptions?
   - Do they need notification?
3. If breaking change → notify owners + add `breaking_change_notice`

**Example**: Updating `refund-policy-explanation` from 30% to 20%.
- Downstream: `complaint-howto`, `customer-service-training-tutorial`, `refund-process-sop`
- All need review.
- Notify owners.

---

## Update Type Classification

| Type | Scope | Cascade Risk | Process |
|---|---|---|---|
| **Refresh** | Metadata only (no body change) | None | Update `last_reviewed`, commit |
| **Revise** | Partial body change, structure preserved | Low-medium | Apply change, cascade check, commit |
| **Rewrite** | Substantial change, may affect cross-refs | High | Apply change, cascade check, re-validate, notify dependents |
| **Deprecate** | Lifecycle: mark for sunset | High | Set `status: deprecated`, add `deprecation_target` (successor doc), notify dependents, grace period 30-90 days |
| **Archive** | Lifecycle: remove from active KB | Medium | After deprecation grace period, move to archive folder, remove from index |

### Refresh

When: audit confirms still accurate, just needs cadence reset.

Steps:
1. Update `last_reviewed: <today>`
2. Update `updated: <today>`
3. Recompute `review_due: <today + cadence>`
4. Commit with message: `refresh(doc-id): quarterly review, no changes`
5. No cascade needed

### Revise

When: partial content needs update.

Steps:
1. Apply content changes (preserve YAML structure)
2. Update `last_reviewed`, `updated`, `review_due`
3. Cascade check:
   - Upstream: is root cause upstream? Fix there first.
   - Downstream: who depends? Notify if breaking.
4. Re-validate per STANDARDIZE Mode 2
5. Structured commit message: `revise(doc-id): <what changed and why>`
6. Log update in change log

### Rewrite

When: substantial change (>50% of body, or core meaning changes).

Steps:
1. **Branch first** (don't edit in place if production-published)
2. Apply changes
3. Re-validate per Mode 2 (more rigorous — structure may have changed)
4. **Mandatory** cascade check
5. **Mandatory** dependent notification
6. Decide: replace or version (if doc supports versioning)
7. Update `updated`, optionally bump version field
8. Commit + log

### Deprecate

When: doc is being replaced or retired.

Steps:
1. Set `status: deprecated`
2. Add `deprecation_target: <successor-doc-id>` (if there's a replacement)
3. Add `deprecation_notice: <date when archive will happen>`
4. Add breaking change notice to body header:
   ```markdown
   > ⚠️ **DEPRECATED 2026-MM-DD**: This document is no longer maintained.
   > **Successor**: [<new-doc-title>](path/to/successor.md)
   > **Will be archived**: 2026-MM-DD (90 days from deprecation)
   ```
5. Notify all dependents (use inverse index)
6. Grace period: 30 days minimum, 90 days for high-impact docs
7. After grace period, transition to Archive

### Archive

When: deprecation grace period expired, OR doc has no value (Trivial).

Steps:
1. Move file to `/archive/<year>/<id>.md`
2. Set `status: archived`
3. Remove from active catalog index
4. Keep in inverse index (so future audits can detect orphan references)
5. Inbound links should now 404 or redirect (depending on KB platform)

---

## Hypothesis-Test Updates

**Critical**: After applying update, validate it actually fixes the issue.

### Process
1. Identify the trigger scenario (e.g., user reported error)
2. Re-run that scenario against updated doc
3. Does updated doc resolve the issue?
   - Yes → update complete
   - No → update is incomplete, investigate further (may be cascade root cause not addressed)

**Example**:
- Trigger: User report "Step 3b says 30%, should be 20%"
- Update: Changed `complaint-howto` step 3b to 20%
- Test: Read doc as new barista, does it say 20%? ✅
- Cascade: But also check `refund-policy-explanation` — does it say 20% or still 30%?
- If still 30% → update incomplete. Same user (or different one) will hit same problem from upstream doc.

---

## Breaking Change Protocol

A change is **breaking** if:
- Procedural step removed or substantially changed
- Data format/schema in Reference doc changed
- Decision (ADR) superseded
- SOP compliance requirement changed

A change is **non-breaking** if:
- Typo fix
- Clarification (same meaning, better words)
- New example added
- Cross-reference added

### Breaking Change Steps

1. Add to YAML: `breaking_change: true` + `breaking_change_notice: <30-day-from-now date>`
2. Notify all dependents (use inverse index)
3. Add prominent warning to doc body
4. If possible, provide migration guide:
   ```markdown
   > ### Migration from previous version
   > If you previously followed Step 3 with X, now do Y because [reason].
   ```
5. Wait grace period before treating as canonical

---

## Change Log Format

Maintain `/audit-logs/changes-<year>.md`:

```markdown
## 2026-11-17 | UPDATE | complaint-wrong-drink-howto
- **Type**: Revise
- **Trigger**: User report (Q3 incident #4521)
- **Change**: Step 3b discount 30% → 20%
- **Cascade**: refund-policy-explanation also updated (root cause)
- **Dependents notified**: customer-service-training-tutorial (owner: Lê Văn C)
- **Hypothesis validated**: re-tested with reporting user — issue resolved
- **Owner**: Trần Thị B
```

---

## Anti-Patterns in UPDATE

1. **Symptom-fix only**: Update doc A without checking upstream root cause. Same issue reappears from other docs. → Fix: mandatory cascade check.

2. **Auto-archive obsolete**: Auto-archive after 12 months without review. Breaks downstream consumers. → Fix: deprecation notice + grace period, never auto-archive.

3. **Batch update without cascade**: Bulk-update 50 docs for policy change, but skip dependent notifications. Downstream docs still reference old policy. → Fix: batch mode with mandatory dependent traversal.

4. **No hypothesis test**: Apply update, declare done, move on. Issue not actually resolved. → Fix: re-test trigger scenario after update.

5. **Vague commit messages**: "Updated doc" tells nothing in retrospect. → Fix: structured commits — `<type>(<doc-id>): <what changed and why>`.

---

## Edge Cases

### 1. SME for doc no longer at company
**Action**: Reassign owner. May need re-Externalization (Mode 1 partial) with current practitioners to validate doc.

### 2. Two SMEs disagree on current truth
**Action**: Don't auto-update. Escalate to Knowledge Steward. Create Decision (ADR) recording resolution. Then update doc.

### 3. Regulatory change → batch update needed
**Action**: Query catalog by `compliance: [framework]` tag. Identify all impacted. Batch revise with mandatory dependent traversal. Add compliance officer review step.

### 4. High-traffic Reference doc with breaking change
**Action**: 90-day grace period (max). Provide migration guide. Notify all dependents explicitly with deadline. Consider parallel publishing both versions during transition.

### 5. Update conflicts with parallel update
**Action**: Git-merge resolution. If semantic conflict (two contradictory changes), escalate to Knowledge Steward.

### 6. Archive request for doc with active consumers
**Action**: Cannot archive directly. Must deprecate first with grace period. Document the request in audit log.
