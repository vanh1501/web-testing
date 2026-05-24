# references/yaml-schema.md — YAML Front Matter Schema (Complete Specification)

## Purpose
Complete schema definition for KB doc front matter. Load when validating YAML or designing schema enforcement.

---

## Schema Overview

YAML front matter is structured metadata at the top of each markdown file, separated by `---` delimiters. It enables machine-readable governance: search, filtering, validation, lifecycle automation.

**Why YAML (not JSON, not inline)**:
- Human-readable: SMEs can edit
- Git-friendly diff: line-by-line changes visible
- Tooling standard: every static site generator parses it natively (Jekyll, Hugo, Docusaurus, MkDocs, Astro)
- Conventions established: don't reinvent

---

## Required Fields (6)

These MUST exist on every doc. Validation rejects docs missing any of these.

### 1. `id`
- **Type**: string
- **Format**: kebab-case (lowercase, hyphens, no spaces/underscores/special chars)
- **Constraint**: Must match filename without `.md` extension
- **Uniqueness**: Globally unique across KB
- **Example**: `complaint-wrong-drink-howto`

### 2. `title`
- **Type**: string
- **Format**: Human-readable, quoted if contains special chars
- **Constraint**: Non-empty
- **Example**: `"How to: Xử lý khách phàn nàn đồ uống sai"`

### 3. `type`
- **Type**: enum (string)
- **Allowed values**: `tutorial | how-to | reference | explanation | decision | adr | runbook | sop`
- **Note**: Extensible — domains may add custom types (e.g., `incident-report`)
- **Example**: `how-to`

### 4. `owner`
- **Type**: string (slug)
- **Format**: kebab-case, references entry in `/catalog/owners.yaml`
- **Constraint**: Must be NAMED person, not team/role
- **Resolves to**: Full person record (name, role, email, active status)
- **Example**: `tran-thi-b`

### 5. `status`
- **Type**: enum (string)
- **Allowed values**: `draft | review | published | deprecated | archived`
- **State machine**:
  - `draft` → `review` → `published`
  - `published` → `deprecated` → `archived`
  - Backwards transitions allowed (with audit log)
- **Example**: `published`

### 6. `last_reviewed`
- **Type**: date (ISO 8601: `YYYY-MM-DD`)
- **Constraint**: Not in future
- **Example**: `2026-05-17`

---

## Recommended Fields (6)

Strongly suggested. Auto-populate where possible during STANDARDIZE.

### 7. `created`
- **Type**: date (ISO 8601)
- **Set once**: at doc creation, never updated
- **Example**: `2025-12-01`

### 8. `updated`
- **Type**: date (ISO 8601)
- **Updated**: on any content change (not just metadata refresh)
- **Example**: `2026-05-17`

### 9. `review_due`
- **Type**: date (ISO 8601)
- **Computed**: `last_reviewed + cadence` (cadence depends on `type`)
- **Cadences**:
  - tutorial: 6 months
  - how-to: 6 months
  - reference: 3 months
  - explanation: 12 months
  - decision: null (never expires)
  - sop: 3 months
- **Example**: `2026-08-17`

### 10. `tags`
- **Type**: array of strings
- **Format**: lowercase, kebab-case for multi-word tags
- **Use**: searchability, filtering, batch operations
- **Example**: `[customer-service, complaint, beverages]`

### 11. `depends_on`
- **Type**: array of strings (doc IDs)
- **Constraint**: All referenced IDs must exist in catalog
- **Use**: cascade analysis, dependency tracking
- **Example**: `[refund-policy-explanation, pos-troubleshooting-reference]`

### 12. `audience`
- **Type**: string
- **Format**: role-or-level (e.g., `barista-junior`, `customer-service-rep`, `engineering-senior`)
- **Use**: targeting, role-based access control derivation
- **Example**: `barista-junior`

---

## Advanced Fields (Governance + Lifecycle)

Optional but powerful for KB governance.

### `seci_origin`
- **Type**: enum
- **Allowed values**: `externalization | combination | reconstructed`
- **Use**: tracks how doc was created (helps with quality assessment)
- **Example**: `externalization` (from SME interview)

### `sme_source`
- **Type**: string (slug)
- **Format**: same as `owner` (slug referencing owners table)
- **Use**: when content originated from SME different from current owner
- **Example**: `tran-thi-b`

### `recording_url`
- **Type**: string (path or URL)
- **Use**: link to SME interview recording (if Recording method used)
- **Example**: `./recordings/sme-2025-12-01.mp4`

### `language`
- **Type**: enum
- **Allowed values**: `vi | en | mixed`
- **Use**: filtering by language, translation tracking
- **Default**: `vi` (or organization default)
- **Example**: `vi`

### `compliance`
- **Type**: array of strings (framework names)
- **Use**: regulated industry docs — triggers additional review steps
- **Example**: `[GMP, ISO-9001]`

### `ai_assisted`
- **Type**: enum
- **Allowed values**: `true | false | partial`
- **Use**: track AI involvement, apply higher scrutiny in validation
- **Example**: `partial`

### `ai_note`
- **Type**: string
- **Use**: details on AI involvement (paired with `ai_assisted`)
- **Example**: `"AI drafted body from transcript, SME validated steps 1-3 manually"`

### `breaking_change`
- **Type**: boolean
- **Use**: marks updates that break dependent docs
- **Triggers**: notification protocol, grace period

### `breaking_change_notice`
- **Type**: date (ISO 8601)
- **Use**: end of grace period for breaking change
- **Example**: `2026-12-17`

### `deprecation_target`
- **Type**: string (doc ID)
- **Use**: successor doc when current is deprecated
- **Example**: `complaint-resolution-howto-v2`

### `deprecation_notice`
- **Type**: date (ISO 8601)
- **Use**: when doc will move from deprecated to archived
- **Example**: `2026-09-17`

### `translation_of`
- **Type**: string (doc ID)
- **Use**: links translated versions
- **Example**: `complaint-wrong-drink-howto` (EN version links to VN original)

### `version`
- **Type**: string (semver or simple)
- **Use**: for Reference docs tied to product versions
- **Example**: `2.4.0`

### `product_version`
- **Type**: string
- **Use**: which product version this doc applies to
- **Example**: `>=2.4.0`

---

## Complete Schema Examples

### Example 1: Standard How-to (minimal required + recommended)

```yaml
---
# Required
id: complaint-wrong-drink-howto
title: "How to: Xử lý khách phàn nàn đồ uống sai"
type: how-to
owner: tran-thi-b
status: published
last_reviewed: 2026-05-17

# Recommended
created: 2025-12-01
updated: 2026-05-17
review_due: 2026-11-17
tags: [customer-service, complaint, beverages]
depends_on: [refund-policy-explanation, pos-troubleshooting-reference]
audience: barista-junior
---
```

### Example 2: Reference with governance

```yaml
---
id: order-status-api-reference
title: "Order Status API Reference"
type: reference
owner: nguyen-van-a
status: published
last_reviewed: 2026-05-17

created: 2025-08-15
updated: 2026-05-17
review_due: 2026-08-17  # 3-month cadence for reference
tags: [api, orders, integration]
depends_on: []
audience: engineering-senior

# Governance
language: en
version: 2.4.0
product_version: ">=2.4.0"
seci_origin: combination  # derived from code + design docs
---
```

### Example 3: SOP with compliance

```yaml
---
id: refund-process-sop
title: "SOP: Refund Processing"
type: sop
owner: tran-thi-b
status: published
last_reviewed: 2026-05-17

created: 2025-06-01
updated: 2026-05-17
review_due: 2026-08-17  # 3-month cadence for SOP
tags: [refund, finance, customer-service, sop]
depends_on: [refund-policy-explanation]
audience: customer-service-rep

# Compliance
compliance: [PCI-DSS]
language: vi
---
```

### Example 4: Decision (ADR)

```yaml
---
id: pos-vendor-switch-decision
title: "Decision: Switch POS vendor from X to Y"
type: decision
owner: le-van-c
status: published
last_reviewed: 2026-05-17

created: 2026-02-01
updated: 2026-02-01
review_due: null  # ADRs don't expire
tags: [decision, pos, vendor, infrastructure]
depends_on: []
audience: leadership
---
```

### Example 5: Deprecated doc

```yaml
---
id: old-complaint-process-howto
title: "How to: Process customer complaints (DEPRECATED)"
type: how-to
owner: tran-thi-b
status: deprecated
last_reviewed: 2026-05-17

created: 2024-01-01
updated: 2026-05-17

# Deprecation
deprecation_target: complaint-wrong-drink-howto
deprecation_notice: 2026-08-17  # 90 days from today
breaking_change: true

tags: [customer-service, complaint, deprecated]
audience: customer-service-rep
language: vi
---
```

---

## Validation Rules (Implementation Reference)

### Field-Level

```python
# Pseudo-code for validator
REQUIRED_FIELDS = ['id', 'title', 'type', 'owner', 'status', 'last_reviewed']
VALID_TYPES = ['tutorial', 'how-to', 'reference', 'explanation', 'decision', 'sop']
VALID_STATUS = ['draft', 'review', 'published', 'deprecated', 'archived']

def validate(yaml_dict, filename):
    errors = []

    # Required fields present
    for field in REQUIRED_FIELDS:
        if field not in yaml_dict:
            errors.append(f"Missing required field: {field}")

    # Type enum
    if yaml_dict.get('type') not in VALID_TYPES:
        errors.append(f"Invalid type: {yaml_dict.get('type')}")

    # Status enum
    if yaml_dict.get('status') not in VALID_STATUS:
        errors.append(f"Invalid status: {yaml_dict.get('status')}")

    # ID matches filename
    if yaml_dict.get('id') != filename.replace('.md', ''):
        errors.append(f"id '{yaml_dict.get('id')}' doesn't match filename")

    # ID is kebab-case
    if not re.match(r'^[a-z][a-z0-9-]*$', yaml_dict.get('id', '')):
        errors.append(f"id must be kebab-case: {yaml_dict.get('id')}")

    # Date format
    for date_field in ['last_reviewed', 'created', 'updated', 'review_due']:
        if date_field in yaml_dict:
            try:
                datetime.fromisoformat(yaml_dict[date_field])
            except ValueError:
                errors.append(f"{date_field}: invalid ISO date format")

    # Owner exists in catalog
    if yaml_dict.get('owner') not in owners_catalog:
        errors.append(f"Owner not in catalog: {yaml_dict.get('owner')}")

    # Cross-references resolve
    for dep in yaml_dict.get('depends_on', []):
        if dep not in doc_catalog:
            errors.append(f"depends_on references unknown doc: {dep}")

    return errors
```

### Cross-Doc Validation

- All `depends_on` IDs must exist in catalog
- No circular dependencies (graph cycle detection)
- `deprecation_target` (if set) must exist and be `status: published`
- `translation_of` (if set) must exist

---

## Owners Catalog Schema

`/catalog/owners.yaml`:

```yaml
owners:
  - slug: tran-thi-b
    name: "Trần Thị B"
    role: "Customer Service Lead"
    email: b.tran@company.com
    active: true
    domains_owned: [customer-service]
    last_active: 2026-05-15

  - slug: nguyen-van-a
    name: "Nguyễn Văn A"
    role: "Engineering Manager"
    email: a.nguyen@company.com
    active: true
    domains_owned: [engineering, infrastructure]
    last_active: 2026-05-17

  - slug: le-van-c
    name: "Lê Văn C"
    role: "Operations Director"
    email: c.le@company.com
    active: false  # Left company 2026-04-01
    domains_owned: []
    last_active: 2026-04-01
    successor: tran-thi-b  # Docs reassigned to
```

---

## Migration: Adding New Required Field

When schema is updated (e.g., adding new required field):

1. **Don't break existing docs**: Make field "soft-required" initially
2. **Default value strategy**:
   - If derivable: auto-populate (e.g., `created` from Git history)
   - If not derivable: prompt owner during next review cycle
3. **Migration window**: 90 days to populate
4. **After migration window**: Hard-require for all docs

**Example**: Adding `audience` as required field
- Day 0: Update schema, mark `audience` required for new docs
- Day 0-90: Existing docs without `audience` get warning, but pass validation
- Day 90+: Existing docs without `audience` fail validation (must update before next change)

---

## Anti-Patterns

1. **Inventing custom fields per doc** — schema sprawl. → Stick to defined schema, propose extensions formally.

2. **Storing non-metadata in YAML** — body content should be in body. → Front matter is for governance/searchability metadata.

3. **Optional everything** — no field required → no governance. → 6 required fields are non-negotiable.

4. **Owner = team name** — accountability gap. → Always named person, with successor field if person moves on.

5. **Stale `last_reviewed`** — never updated even when content changes. → Update on every meaningful change.
