# brand-kit-schema.md — Material Studio Brand Kit

> **Tầng 1b — Brand Kit (per-client)** trong kiến trúc Material Studio.
> Plug-and-play layer fill các token mà Skeleton (Tầng 1a) expose qua Token Surface.
> 1 file YAML per client. Swap brand → re-render mọi artifact.

**Version:** v1.0 · 2026-05-17
**Depends on:** `skeleton-patterns.md` § 13 (Token Surface)

---

## 🎯 TL;DR

Brand Kit = file YAML chứa **mọi thông tin brand-specific** của 1 client:
- Colors (primary, neutral, accent)
- Typography (font family, sizes, scale)
- Identity (org name, tagline, logo)
- Voice (language, formality, labels)
- Optional: page setup overrides, spacing scale

**Onboarding:** Client mới → upload brand guideline → skill extract → user review → save YAML.
**Usage:** Mọi project sau cho client đó → tự load YAML đúng, không hỏi lại.

---

## 📑 Mục lục

1. [YAML Schema (full structure)](#1-yaml-schema)
2. [Required vs Optional Tokens](#2-required-vs-optional)
3. [Validation Rules](#3-validation-rules)
4. [Intake Workflow](#4-intake-workflow)
5. [Examples (MindX + 2 hypothetical)](#5-examples)
6. [Application Flow (Brand Kit → Skeleton)](#6-application-flow)
7. [File Naming + Versioning](#7-file-naming)

---

## 1. YAML Schema

```yaml
# Material Studio Brand Kit
# Schema version: 1.0
# Client: [client_id]

metadata:
  client_id: string          # snake_case, used in file naming (vd: mindx, bank_abc)
  client_display_name: string # Full name for human readability (vd: "MindX Technology School")
  schema_version: "1.0"      # Brand Kit schema version this YAML conforms to
  created_at: YYYY-MM-DD
  updated_at: YYYY-MM-DD

# ───── REQUIRED SECTIONS ─────

color:
  primary: "RRGGBB"          # 6-char hex, NO # prefix. Banner/accent/CTA color.
  primary_dark: "RRGGBB"     # Darker shade of primary (hover, pressed states)
  accent_secondary: "RRGGBB" # Alternative callout color (vd: 📖 reference type)
  neutral_dark: "RRGGBB"     # Body text + headings (typically near-black)
  neutral_mid: "RRGGBB"      # Captions, subtitles, muted text
  neutral_light: "RRGGBB"    # Subtle backgrounds (vd: callout bg)
  border: "RRGGBB"           # Table borders, card outlines
  background: "RRGGBB"       # Page background (typically white FFFFFF)

typography:
  font_sans: string          # Primary font name (must exist in target render env)
  font_mono: string          # Mono font for code/prompt blocks
  size_xs: number            # Pt absolute. Body min 9pt (skeleton invariant).
  size_s: number             # Pt
  size_m: number             # Pt (body)
  size_l: number             # Pt
  size_xl: number            # Pt
  size_xxl: number           # Pt
  # NOTE: skeleton enforces XS < S < M < L < XL < XXL

identity:
  org_name: string           # Display name for cover banner (uppercase capable)
  org_tagline: string        # Short tagline (vd: "TECHNOLOGY SCHOOL")
  logo_path: string?         # Optional. Relative path to logo image. Skip = use text-only.

voice:
  language: string           # ISO 639-1 (vd: vi, en, ja)
  formality: enum            # formal | semi_formal | casual | technical
  cover_reflection_prompt: string  # Vd: "TÔI THAM GIA KHÓA HỌC NÀY ĐỂ:"
  page_label: string         # "Trang" (vi) | "Page" (en) | etc.
  notes_label: string        # "GHI CHÚ" (vi) | "NOTES" (en) | etc.
  toc_label: string          # "MỤC LỤC" (vi) | "TABLE OF CONTENTS" (en) | etc.
  field_labels:              # For cover form fields
    name: string             # "TÊN" | "NAME"
    department: string       # "PHÒNG BAN" | "DEPARTMENT"
    date: string             # "NGÀY" | "DATE"

# ───── OPTIONAL SECTIONS ─────

page:                        # Override skeleton defaults if needed
  format: enum               # A4_portrait (default) | A4_landscape | letter_portrait
  margins:
    top: number              # DXA. Default 1134.
    bottom: number
    left: number             # Or use mirror_margins.inner for binding
    right: number            # Or use mirror_margins.outer for binding
    header: number
    footer: number
  mirror_margins:            # For book-style binding
    enabled: boolean
    inner: number            # DXA, gáy side
    outer: number            # DXA, mép side

spacing:
  multiplier: number         # 1.0 default. 0.85 = tighter, 1.15 = looser.

typography_scale:
  ratio: number              # 1.25 default geometric scale between sizes

callout_overrides:           # If brand wants specific colors per semantic icon
  goal: "RRGGBB"             # 🎯 Goal/target — defaults to color.primary
  insight: "RRGGBB"          # 💡 Insight — defaults to color.primary_light
  principle: "RRGGBB"        # 🔑 Principle — defaults to color.primary
  warning: "RRGGBB"          # ⚠️ Warning — defaults to color.primary (strong)
  critical: "RRGGBB"         # 🚨 Critical — defaults to red
  reference: "RRGGBB"        # 📖 Reference — defaults to color.accent_secondary

content_hooks:               # Per-client content customization
  program_title_default: string?    # Default program name if not provided per-project
  field_default_values:             # Pre-fill cover fields
    organization: string?
```

---

## 2. Required vs Optional

### Required (Brand Kit MUST provide)
- `metadata.client_id`, `metadata.client_display_name`, `metadata.schema_version`
- All of `color.*` (8 keys)
- All of `typography.*` (8 keys — font + 6 sizes)
- All of `identity.*` (org_name, org_tagline minimum; logo_path optional)
- All of `voice.*` (language, formality, all labels + field_labels)

**Total required keys:** ~28

### Optional (skeleton uses defaults if not provided)
- `page.*` — skeleton uses A4 portrait + default margins
- `spacing.multiplier` — default 1.0
- `typography_scale.ratio` — default 1.25
- `callout_overrides.*` — defaults derived from color.primary/accent_secondary
- `content_hooks.*` — set at project level if not in Brand Kit

---

## 3. Validation Rules

Run on Brand Kit load. Block project build if any FAIL.

### 3.1 Schema Conformance
```
- All required keys present? FAIL if missing.
- Schema version matches supported? WARN if older minor, FAIL if older major.
- YAML syntax valid? FAIL on parse error.
```

### 3.2 Color Validation
```
- Every color value matches /^[0-9A-Fa-f]{6}$/ (6-char hex, NO #)? FAIL otherwise.
- color.primary != color.neutral_light (not invisible)? WARN if too similar.
- color.background contrast with color.neutral_dark ≥ WCAG AA (4.5:1)? WARN.
```

### 3.3 Typography Validation
```
- typography.size_xs ≤ size_s ≤ size_m ≤ size_l ≤ size_xl ≤ size_xxl? FAIL if order broken.
- typography.size_m ≥ 9 (body readability floor)? FAIL.
- typography.font_sans non-empty string? FAIL if empty.
```

### 3.4 Voice Validation
```
- voice.language is ISO 639-1 code? WARN if unknown.
- voice.formality in [formal, semi_formal, casual, technical]? FAIL if other.
- All label strings non-empty? FAIL if empty.
```

### 3.5 Skeleton Invariant Check
```
- Brand Kit does NOT attempt to override skeleton invariants (Section 13.3 of skeleton-patterns.md)?
  - block_anatomy_order? IGNORE + WARN if present.
  - page_archetypes count? IGNORE + WARN.
  - block_variants count? IGNORE + WARN.
  - anti_pattern_list? IGNORE + WARN.
  - action_title_rule? IGNORE + WARN.
```

### 3.6 Page Setup Validation (if override provided)
```
- page.margins values reasonable (200 ≤ x ≤ 3000 DXA)? FAIL if out of range.
- mirror_margins.enabled requires both inner + outer present? FAIL.
- page.format in supported list? FAIL if unknown.
```

---

## 4. Intake Workflow

How to onboard a new client → produce their Brand Kit YAML.

### 4.1 Path A — Client Has Brand Guideline Document

```
Input: PDF / DOCX / image / URL / website screenshot of brand guideline

Step 1: Upload to skill
Step 2: Auto-extract via LLM analysis:
  - OCR if image/scan
  - Identify color hex from style guide
  - Identify font names
  - Identify logo placement, tagline, org name
Step 3: Skill propose draft Brand Kit YAML with extracted values + skeleton defaults
Step 4: User review → adjust any wrong/missing values
Step 5: Run validation (Section 3) → pass = save as brand-kit-{client_id}.yaml
Step 6: Save to: examples/brand-kit-{client_id}.yaml
```

### 4.2 Path B — Client Has No Formal Brand Guideline

```
Input: Free-form description / brand assets / verbal preferences

Step 1: Skill ask guided intake questions:
  - "Tên tổ chức + tagline?"
  - "Có logo không? Upload nếu có."
  - "Màu chủ đạo? (upload sample hoặc tả: 'navy blue đậm', 'red MindX', etc.)"
  - "Font preferred? (Arial, Roboto, Calibri, Times, etc.)"
  - "Ngôn ngữ workbook? Mức formal?"
Step 2: Skill propose Brand Kit YAML based on answers
Step 3: User review → confirm
Step 4: Validate → save
```

### 4.3 Path C — Client Same Industry / Use Existing Brand Kit as Base

```
Input: "Client mới giống Client X về style, chỉ đổi tên + màu chính"

Step 1: User specify base brand kit
Step 2: Skill clone → apply diff (new colors, new identity)
Step 3: User confirm → save as new client_id
```

### 4.4 Intake Output

Final artifact per client:
```
material-studio/
├── references/
│   └── brand-kit-examples/
│       ├── mindx-brand-kit.yaml          ← MindX
│       ├── bank_abc-brand-kit.yaml       ← Bank ABC
│       ├── tech_startup_x-brand-kit.yaml ← Tech Startup X
│       └── ...
```

---

## 5. Examples

### 5.1 MindX Brand Kit (extracted from existing guideline)

See: `examples/mindx-brand-kit.yaml`

Key values:
- Primary color: `E30613` (MindX red)
- Font: Arial
- Language: vi, formality: semi_formal
- Org: "MindX" / "TECHNOLOGY SCHOOL"

### 5.2 Hypothetical: Bank ABC

```yaml
metadata:
  client_id: bank_abc
  client_display_name: "Bank ABC"
  schema_version: "1.0"

color:
  primary: "003D7A"        # Navy
  primary_dark: "002E5C"
  accent_secondary: "C9A961" # Gold
  neutral_dark: "1A1A1A"
  neutral_mid: "5C5C5C"
  neutral_light: "F0F2F5"
  border: "D5D5D5"
  background: "FFFFFF"

typography:
  font_sans: "Roboto"
  font_mono: "Roboto Mono"
  size_xs: 9
  size_s: 11
  size_m: 11
  size_l: 16
  size_xl: 22
  size_xxl: 28

identity:
  org_name: "BANK ABC"
  org_tagline: "PROFESSIONAL FINANCIAL SOLUTIONS"

voice:
  language: en
  formality: formal
  cover_reflection_prompt: "MY LEARNING OBJECTIVES:"
  page_label: "Page"
  notes_label: "NOTES"
  toc_label: "TABLE OF CONTENTS"
  field_labels:
    name: "NAME"
    department: "DEPARTMENT"
    date: "DATE"
```

### 5.3 Hypothetical: Tech Startup X (vibrant brand)

```yaml
metadata:
  client_id: techstartup_x
  client_display_name: "TechStartup X"

color:
  primary: "6E45E2"        # Vivid purple
  primary_dark: "5232BE"
  accent_secondary: "00C896" # Mint
  neutral_dark: "111827"
  neutral_mid: "6B7280"
  neutral_light: "F9FAFB"
  border: "E5E7EB"
  background: "FFFFFF"

typography:
  font_sans: "Inter"
  font_mono: "JetBrains Mono"
  size_xs: 10
  size_s: 12
  size_m: 12
  size_l: 18
  size_xl: 26
  size_xxl: 32

identity:
  org_name: "TechStartup X"
  org_tagline: "Build · Ship · Iterate"

voice:
  language: en
  formality: casual
  cover_reflection_prompt: "What I want to learn:"
  page_label: "Page"
  notes_label: "Notes"
  toc_label: "Contents"
  field_labels:
    name: "Name"
    department: "Team"
    date: "Date"

spacing:
  multiplier: 0.9          # Tighter for modern feel

typography_scale:
  ratio: 1.5               # Bolder hierarchy contrast
```

**Observation:** Same skeleton, 3 vastly different visual identities by swapping Brand Kit only.

---

## 6. Application Flow

```
┌──────────────────────┐
│ User invokes project │  "Tạo training kit cho Bank ABC"
└──────────┬───────────┘
           │
           ▼
┌──────────────────────────────────────────┐
│ Material Studio Orchestrator (Tầng 5)    │
└──────────┬───────────────────────────────┘
           │ Lookup client → load brand-kit-bank_abc.yaml
           ▼
┌──────────────────────────────────────────┐
│ Brand Kit Loader                         │
│  1. Parse YAML                           │
│  2. Validate (Section 3 rules)           │
│  3. Merge with skeleton defaults         │
│     (for optional tokens not provided)   │
│  4. Reject any attempted invariant override
└──────────┬───────────────────────────────┘
           │ Resolved Design System object
           ▼
┌──────────────────────────────────────────┐
│ Content Model (Tầng 2)                   │
│  Uses Design System for resolved tokens  │
│  when composing blocks                   │
└──────────┬───────────────────────────────┘
           │ Block tree (format-agnostic)
           ▼
┌──────────────────────────────────────────┐
│ Format Adapters (Tầng 3)                 │
│  Apply Design System tokens during render│
│  Output: branded artifacts               │
└──────────────────────────────────────────┘
```

### Resolution Order (for any token)
```
1. Brand Kit value? Use it.
2. Skeleton default? Use it.
3. Computed default (vd: callout color derives from color.primary)? Use it.
4. Error: token unresolved → block build.
```

---

## 7. File Naming + Versioning

### 7.1 File Naming Convention
```
brand-kit-{client_id}.yaml

Examples:
  brand-kit-mindx.yaml
  brand-kit-bank_abc.yaml
  brand-kit-techstartup_x.yaml
```

Constraints:
- `client_id`: lowercase, snake_case, no spaces, no special chars (a-z, 0-9, _)
- Filename matches `metadata.client_id` in YAML

### 7.2 Versioning Per Client
```
brand-kit-mindx.yaml          ← current version
brand-kit-mindx.v1.yaml       ← archived previous (optional)
brand-kit-mindx.v2.yaml
```

Update `metadata.updated_at` mỗi lần edit. Keep history if brand evolves over time.

### 7.3 Schema Version Migration
Khi `skeleton-patterns.md` evolve (major version bump), Brand Kits may need migration:
```
skeleton v1.0 → v2.0:
  - New required token added → migration script auto-fill from defaults + flag
  - Token removed → migration script remove + warn
  - Token renamed → migration script rename
```

Brand Kit `metadata.schema_version` tracks compatibility. Validator warn on mismatch.

---

## 🔗 Dependencies

**Upstream (Brand Kit depends on):**
- `skeleton-patterns.md` § 13 (Token Surface contract)

**Downstream (depends on Brand Kit):**
- `content-model.md` (Tầng 2) — uses resolved Design System
- `adapter-*.md` (Tầng 3) — applies tokens during render
- Orchestrator (Tầng 5) — loads correct Brand Kit per project

---

## 📋 Change Log

| Version | Date | Changes | By |
|---|---|---|---|
| v1.0 | 2026-05-17 | Initial schema + MindX example + 2 hypothetical examples | MAESTRO + Trainer |

---

*Material Studio · Tầng 1b Brand Kit Schema · v1.0 · 2026-05-17*
