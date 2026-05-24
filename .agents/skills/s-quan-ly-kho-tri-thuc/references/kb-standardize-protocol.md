# references/standardize.md — STANDARDIZE Mode Protocol (Full)

## Purpose
Detailed protocol for Mode 2 (STANDARDIZE). Load when entering STANDARDIZE mode.

## SECI Mapping
Combination (explicit → explicit). Refine, restructure, validate explicit knowledge for consistency and discoverability.

---

## Validation Pipeline (7 Checks)

Run in order. Fail-fast on Check 1-2 (return errors). Auto-fix on Check 3-4. Flag on Check 5-6. Update on Check 7.

### Check 1: YAML Front Matter Validation

**Required fields (6) — fail if missing or wrong type:**

```yaml
id: <kebab-case string, matches filename>
title: <string, non-empty>
type: <enum: tutorial | how-to | reference | explanation | adr | runbook | sop>
owner: <string, must exist in /catalog/owners.yaml>
status: <enum: draft | review | published | deprecated | archived>
last_reviewed: <ISO 8601 date>
```

**Validation rules**:
- `id` must match filename without `.md` extension
- `id` must be kebab-case (lowercase, hyphens only, no spaces/underscores/special chars)
- `type` must be in enum
- `status` must be in enum
- `last_reviewed` must be valid ISO 8601 date, not in future
- `owner` must resolve to entry in owners table

**Common errors**:
- Missing `id` field (auto-fix: derive from filename)
- `type: howto` instead of `how-to` (auto-fix or reject)
- `last_reviewed: 2025/12/01` (wrong format — must be `2025-12-01`)
- `owner: customer-service-team` (must be named person, not team)

### Check 2: Diátaxis Purity (CRITICAL — mandatory, not advisory)

Scan body for type-mixing signals based on declared `type`:

**If `type: tutorial`**, flag if body contains:
- Lookup tables (signal: Reference content)
- "Background context" sections discussing why (signal: Explanation)
- Multiple unrelated parameter lists (signal: Reference)

**If `type: how-to`**, flag if body contains:
- Long explanatory paragraphs about concept history (signal: Explanation)
- Multiple endpoint/API tables (signal: Reference — possibly should split)

**If `type: reference`**, flag if body contains:
- "Let me explain why..." passages (signal: Explanation)
- Step-by-step procedures with hand-holding (signal: Tutorial or How-to)
- Narrative storytelling (signal: Explanation)

**If `type: explanation`**, flag if body contains:
- Numbered step-by-step procedures (signal: How-to or Tutorial)
- Tables of parameters/fields (signal: Reference)

**If `type: adr` (Architecture Decision Record)**, flag if body contains:
- Hướng dẫn cài đặt chi tiết (signal: Tutorial)
- Bảng API endpoints (signal: Reference)

**If `type: runbook`**, flag if body contains:
- Thuyết minh lý do tại sao chọn công nghệ này (signal: ADR/Explanation)
- Giải thích nguyên lý hệ thống dài dòng (signal: Explanation)

**Action on flag**:
1. Identify the embedded type (which doesn't match declared `type`)
2. Suggest split: extract embedded content to new doc with cross-link
3. Reject doc until split done (do not auto-merge)

### Check 3: Markdown Structure Validation

**Rules**:
- H1: 0 or 1 (depending on whether title is auto-generated from YAML)
- H2 → H3 → H4 hierarchy (never skip levels: H2 → H4 is error)
- H4 and deeper discouraged (suggest restructure)
- Code blocks must specify language: `` ```python `` not `` ``` ``
- Tables: pipe-delimited with header row + alignment row
- Line length: soft wrap ~80 chars (warn if >120, for diff-friendliness)
- No trailing whitespace
- Blank line before/after headers, lists, code blocks

**Auto-fixes**:
- Add missing language to code blocks (infer from content)
- Normalize whitespace
- Fix common heading hierarchy issues

### Check 4: Filename and Folder Placement

**Rules**:
- Filename = `<id>.md` (must match YAML `id` exactly)
- Folder path follows taxonomy: `/docs/<domain>/<type>/<id>.md` (e.g., `/docs/architecture/adr/adr-001.md`)
- Domain must exist in taxonomy registry (or flagged as new domain)

**Auto-fix**: Move file to correct path if domain + type known.

### Check 5: Cross-Reference Validation

**Rules**:
- All IDs in `depends_on` must exist in catalog
- All inline markdown links `[text](path)` must resolve
- No circular dependencies (A depends_on B, B depends_on A)
- Orphan check: doc has no inbound links AND not in entry-point list → flag (may be lost in KB)

**Algorithm for circular detection**:
```
visited = set()
stack = set()

def has_cycle(doc_id):
    if doc_id in stack: return True
    if doc_id in visited: return False
    visited.add(doc_id)
    stack.add(doc_id)
    for dep in get_depends_on(doc_id):
        if has_cycle(dep): return True
    stack.remove(doc_id)
    return False
```

**Action on broken cross-ref**:
- Missing target doc → flag, suggest creating stub or removing reference
- Circular dependency → reject, require human resolution
- Orphan → warn, suggest adding to navigation/entry-points

### Check 6: Taxonomy MECE Check (for new doc additions)

**ME check (Mutually Exclusive)**: Does this doc's topic overlap with existing doc(s)?
- Compute content similarity (simple: TF-IDF or keyword overlap)
- If >70% similarity with existing doc → flag potential redundancy

**CE check (Collectively Exhaustive)**: Does this fill a known gap?
- Check against KB gap analysis (if available)

**Action**:
- ME violation → suggest merge or differentiation
- CE pass → confirm addition fills gap

### Check 7: Catalog + Index Update

After all checks pass:
- Add/update entry in `/catalog/index.yaml`
- Build inverse index (who links to this doc)
- Update cross-reference graph
- Transition status: `review` → `published`

---

## Validation Report Format

After running checks, present to user:

```
## Validation Report: <doc-id>

### ✅ Passed
- YAML schema: valid (6/6 required fields)
- Markdown structure: valid (heading hierarchy clean)
- Folder placement: correct (/docs/customer-service/how-to/)

### ⚠️ Auto-fixes Applied
- Language specifier added to 2 code blocks
- Trailing whitespace removed (3 lines)

### ❌ Manual Review Required
- Diátaxis purity: 1 violation
  - Lookup table in tutorial doc → suggested split to new Reference doc
  - File: /docs/backend/tutorial/inventory-setup-tutorial.md
  - Lines 45-62
- Cross-reference: 1 broken link
  - depends_on: [pos-troubleshooting-reference] — target not found
  - Suggestion: create stub or remove reference

### Status
- Cannot transition to `published` until manual items resolved
- Current status: `review`
```

---

## Batch Mode (for imports, audits)

When processing >10 docs at once:

1. **First pass**: Run Check 1 + 2 (schema + Diátaxis) on all docs. Fail-fast list.
2. **Second pass**: Run Check 3 + 4 (structure + placement) with auto-fix.
3. **Third pass**: Build complete catalog first, THEN run Check 5 (cross-refs) — needs full catalog state.
4. **Fourth pass**: Check 6 (MECE) requires full corpus.
5. **Fifth pass**: Update index, commit.

**Report aggregation**:
```
## Batch Validation Report
- Total docs: 120
- Passed all checks: 87 (72%)
- Auto-fixes applied: 25 docs
- Manual review needed: 33 docs
  - Diátaxis violations: 18
  - Cross-ref errors: 12
  - Taxonomy questions: 3
- Estimated rework: 4-8 hours
```

---

## Legacy Import Special Handling

When docs imported without metadata (e.g., from Notion, wiki):

1. **Provisional status**: Set `status: needs_review` (not `draft` — different state)
2. **Diátaxis inference**: Analyze content to suggest type
   - Numbered step procedures + "you will" language → tutorial
   - Numbered steps without hand-holding → how-to
   - Tables + lookup tables → reference
   - Discursive prose, "why" focus → explanation
3. **Owner stub**: Set `owner: [TODO: assign]`
4. **Tags inference**: Extract from content keywords
5. **Cross-ref**: Extract inline links, populate `depends_on` (mark unresolved if target doesn't exist)

Then escalate to human curator for:
- Owner assignment
- Diátaxis type confirmation
- Splitting if mixed type
- Folder placement decision

---

## Anti-Patterns in STANDARDIZE

1. **"Format check only"** — Validator only runs Check 1 + 3, skips Diátaxis purity. Result: compliant but confusing docs. → Fix: Make Check 2 mandatory.

2. **"Auto-merge on overlap"** — When two docs cover similar topic, auto-merge without human review. Lossy. → Fix: ME check flags for human decision, never auto-merge.

3. **"Single-pass batch"** — Running all checks doc-by-doc in 1 pass. Cross-refs fail because catalog incomplete. → Fix: Multi-pass (build catalog first).

4. **"Strict reject on draft"** — Rejecting `status: draft` docs for missing optional fields. Drafts are work-in-progress. → Fix: Only enforce required fields on `draft`; full validation on `review` → `published` transition.

---

## Edge Cases

### 1. Doc has both inline link and `depends_on` entry for same target
Inline link `[guide](path/to/guide.md)` + `depends_on: [other-guide]` (different).
**Action**: Reconcile. Inline link target should appear in `depends_on`. Either add to `depends_on` (canonical) or remove inline link.

### 2. Cross-language cross-references
VN doc references EN doc via `depends_on`.
**Action**: Valid. Check both exist. Language mismatch is OK for reference (often regulatory docs are EN-only).

### 3. Deprecated doc still has dependents
Doc A `deprecated`, doc B `published` with `depends_on: [A]`.
**Action**: Flag. B needs update — either remove dependency or migrate to successor. Don't auto-archive A while B still depends.

### 4. Schema migration (new required field added)
Schema updated to require new field X. Existing docs missing X.
**Action**: Batch migration mode. Auto-populate X with default values where possible. Flag where manual entry needed. Don't reject all existing docs.

### 5. Custom doc types (industry-specific)
Pharma KB needs `protocol` type beyond standard Diátaxis 6.
**Action**: Extend `type` enum in schema. Define template for new type. Document the extension.
