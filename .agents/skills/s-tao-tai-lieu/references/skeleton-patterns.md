# skeleton-patterns.md — Material Studio Universal Skeleton

> **Tầng 1a — Skeleton (universal)** trong kiến trúc Material Studio.
> Quy định **CẤU TRÚC + LAYOUT MATH** cho workbook/training materials. Brand-agnostic.
> Brand Kit (Tầng 1b) plug vào qua **Token Surface** ở Section 13.

**Version:** v1.0 · 2026-05-17 · Đúc từ MindX Workbook Pattern (validate trên Day 2: 58 slides → 28 trang)

---

## 🎯 TL;DR

Universal skeleton định nghĩa **cấu trúc bất biến** cho mọi workbook block-based (1-3 block / trang A4):
- 4 **page archetypes** (Cover · TOC · Block Pages · Note Page)
- 6 **block variants** (Simple · Comparison · Process · Prompt · Concept+Callout · Divider)
- **Block anatomy 4 thành phần** (Banner → Title → Subtitle → Body)
- **Density rule 1-3 block/page** (auto-pick theo content density)
- **Anti-pattern list** (CẤM tuyệt đối)

Brand Kit (Tầng 1b) plug vào để fill: colors, fonts, sizes, logo, voice, naming. Skeleton KHÔNG biết về brand.

---

## 📑 Mục lục

1. [Page Setup](#1-page-setup)
2. [Spacing Tokens (relative)](#2-spacing-tokens)
3. [Typography Hierarchy (labels only)](#3-typography-hierarchy)
4. [Page Archetypes](#4-page-archetypes)
5. [Block Anatomy](#5-block-anatomy)
6. [Block Variants](#6-block-variants)
7. [Blocks-per-Page Density Rule](#7-blocks-per-page)
8. [Content Mapping (Source → Block)](#8-content-mapping)
9. [Block Height Behavior](#9-block-height)
10. [Header / Footer Pattern](#10-header-footer)
11. [Anti-Patterns (CẤM)](#11-anti-patterns)
12. [Quality Checklist](#12-quality-checklist)
13. [Brand Kit Token Surface](#13-token-surface)

---

## 1. Page Setup

### 1.1 Page Dimensions
| Format | Width (DXA) | Height (DXA) | Real size |
|---|---|---|---|
| A4 portrait (default) | 11906 | 16838 | 21.0 × 29.7 cm |
| A4 landscape | 16838 | 11906 | 29.7 × 21.0 cm |
| US Letter portrait | 12240 | 15840 | 8.5 × 11 in |

Brand Kit có thể override page format. Skeleton default = **A4 portrait**.

### 1.2 Margins (default)
| Side | DXA | Cm |
|---|---|---|
| Top / Bottom | 1134 | 2.0 |
| Left / Right | 1417 | 2.5 |
| Header pad | 720 | 1.27 |
| Footer pad | 720 | 1.27 |

Brand Kit MAY override (vd: mirror margins cho in đóng quyển — inner 1701 / outer 1134).

### 1.3 Content Width Formula
```
content_width = page_width - left_margin - right_margin
```
A4 default: `11906 - 1417 - 1417 = 9072 DXA ≈ 16.0 cm`

Mọi block, table, callout PHẢI fit trong `content_width`. Skeleton enforce ràng buộc này.

---

## 2. Spacing Tokens

Relative units (DXA). Brand Kit MAY scale toàn bộ với `spacing_multiplier` (default = 1.0).

### 2.1 Inside Block Padding
```
cell.padding.top/bottom:  100-220 DXA  (~0.7-1.5 mm)
cell.padding.left/right:  240 DXA      (~4 mm)
```

### 2.2 Between Paragraphs
```
paragraph.spacing.small:    60-100 DXA
paragraph.spacing.default:  120-160 DXA
paragraph.spacing.section:  200-280 DXA
paragraph.line_height:      320 (1.45x) — for body text
```

### 2.3 Between Blocks (same page)
```
inter_block_gap:  100-150 DXA  (~2-3 mm vertical)
```

### 2.4 Page Break
```
After last block on page: PageBreak inside Paragraph wrapper
```

---

## 3. Typography Hierarchy

Skeleton định nghĩa **labels + relative weight/style**. Brand Kit fill colors, fonts, absolute sizes.

| Label | Purpose | Weight | Style | Relative size | Notes |
|---|---|---|---|---|---|
| `cover_title` | Cover page main title | Bold | — | XXL | Centered |
| `cover_subtitle` | Cover page tagline | — | Italic | L | Centered |
| `toc_heading` | TOC heading | Bold | — | XL | Letter-spacing +100 |
| `banner_text` | Block banner | Bold | UPPERCASE | S | Letter-spacing +60, on accent bg |
| `block_title` | Block action title | Bold | — | L | Verb-first action statement |
| `block_subtitle` | Block subtitle (optional) | — | Italic | M-L | 1 line max |
| `block_body` | Block main text | — | — | M | line height 320 (1.45x) |
| `table_header` | Table column header | Bold | — | M | On accent bg, white text |
| `table_body` | Table cell content | — | — | M | — |
| `callout_label` | Callout type label | Bold | UPPERCASE | M | With icon prefix |
| `callout_body` | Callout body text | — | — | M | — |
| `page_header_text` | Page header L/R | — | — | XS | Subtle, doesn't compete |
| `page_footer_text` | Page footer L/R | — | — | XS | Same as header |

**Relative size scale (Brand Kit fills absolute pt):**
```
XS  < S  < M  < L  < XL  < XXL
(default A4 pt mapping: 9, 11, 11-13, 16, 22, 26)
```

**Rule:** banner < page text < body ≤ table = callout < title < toc < cover_subtitle < cover_title

Brand Kit có thể tăng/giảm scale, NHƯNG phải giữ thứ tự hierarchy.

**Minimum readability:** body ≥ 9pt absolute. Skeleton enforce.

---

## 4. Page Archetypes

4 loại trang. Số lượng mỗi loại tùy source deck.

### 4.1 Archetype A — Cover Page (1 trang, đầu workbook)
```
Structure (top → bottom):
  1. Brand banner block (accent bg)
     - Org name + tagline (uppercase)
     - Program day label (vd: "DAY 2 of 2")
  2. Title block (center)
     - Cover title (XXL bold)
     - Program name (L)
     - Tagline (italic, subtitle color)
  3. Cohort info bar (light bg, M text)
     - "[cohort_size] · [audience_role] · [day_X / day_total]"
  4. Fill-in section: prompt + 2 underline rules
     - "[reflection_prompt]" (vd: "TÔI THAM GIA KHÓA HỌC NÀY ĐỂ:")
  5. Field row (3 columns): label + underline rule each
     - Name | Department | Date
```

**Brand Kit hooks:** banner content, cover_title text, cover_subtitle, cohort_info, reflection_prompt, field labels.

### 4.2 Archetype B — TOC / Mục lục (1 trang, vị trí thường là trang 2)
```
Structure:
  1. Heading (XL bold, accent color)
  2. Subtitle (italic, muted)
  3. Thin accent rule (horizontal divider)
  4. Schedule table (5 cols):
     [Time | Stage | Tool | Output | Page]
  5. Two callouts side-by-side or stacked:
     - Callout A: "Final deliverable" (accent color)
     - Callout B: "How to use this workbook" (secondary accent)
```

**Brand Kit hooks:** heading text, schedule data, deliverable description, how-to-use text.

### 4.3 Archetype C — Block Pages (N trang, body của workbook)
```
Structure (per page): 1-3 block(s) stacked dọc + page break
Density rule: see Section 7.
Each block: see Section 5 (anatomy) + Section 6 (variants).
```

### 4.4 Archetype D — Note Page (1 trang, cuối workbook)
```
Structure:
  1. Heading "📝 NOTES / GHI CHÚ" (or brand equivalent)
  2. N mini-sections with fill-in scaffold:
     - Cluster heading (M bold)
     - 3-4 underline rules for handwriting
  3. Footer note (optional): "→ [next step instruction]"
```

**Brand Kit hooks:** heading, cluster labels, next-step text.

---

## 5. Block Anatomy

Block (= "slide card" trong MindX terminology) là đơn vị nội dung cơ bản trong Archetype C.

### 5.1 Visual Structure
```
┌─────────────────────────────────────────┐
│ ███ BANNER · UPPERCASE BOLD ███         │   ← Row 1: Banner (accent bg, white text)
├─────────────────────────────────────────┤
│ Block Title (action statement)          │   ← Row 2: Title (L bold)
│ Block subtitle, italic optional         │   ← Row 3: Subtitle (M italic, OPTIONAL)
│ ─────────────────────────────────────── │
│ Body content (variant — see Section 6)  │   ← Row 4: Body (variant)
│  [table / paragraph / callout / mixed]  │
└─────────────────────────────────────────┘
                                              ← Border thin around entire card
```

### 5.2 4 Required Components
| Row | Component | Required? | Notes |
|---|---|---|---|
| 1 | Banner | YES | Banner text format (Section 8.2) |
| 2 | Title | YES | Action title (verb-first) |
| 3 | Subtitle | NO | 1-line context, italic |
| 4 | Body | YES | One of 6 variants |

### 5.3 Implementation Pattern (format-agnostic)
```
Block = Table with 1 column, 3-4 rows:
  Row 1 (Banner):    accent bg, white text, padding 100/240
  Row 2 (Title):     transparent bg, padding 120/240
  Row 3 (Subtitle):  transparent bg, padding 60/240, OPTIONAL
  Row 4 (Body):      transparent bg, padding 120/240, NO atLeast height
  
Table-level border: thin (1pt) on all 4 sides
```

---

## 6. Block Variants

6 variants. Source content type → variant mapping ở Section 8.

### V1 — Simple Statement
Body:
- 1-2 paragraph (body size, line-height 320)
- Optional 1 callout below

Use case: Key message, principle, mindset.

### V2 — Comparison Table (2-3 cols)
Body:
- Data table 2-3 columns
- Column ratio: 50/50 (compare equals), 30/70 (concept/explain), 33/33/33 (3-way)

Use case: A vs B, Trước vs Sau, Cũ vs Mới.

### V3 — Process / Steps Table
Body:
- Table 3-5 columns: [Step | Description | Tool | Output | Time]
- Optional icon column

Use case: Process steps, checklist, procedure.

### V4 — Prompt / Code Block
Body:
- Mono-font paragraph với light bg
- 1 callout explaining context

Use case: AI prompt, code snippet, command line.

### V5 — Concept + Callout Combo
Body:
- 1-2 sentence explanation
- 1 callout highlighting key insight
- Optional: 1 reflection question

Use case: Intro slide, mindset shift, concept introduction.

### V6 — Divider / Section Opener
Body:
- Big centered text (XL-XXL)
- Brief description
- List of upcoming items (to prevent sparse card)

Use case: Section break, time marker (Morning / Afternoon), closing.

---

## 7. Blocks-per-Page Density Rule

**Auto-pick rule** based on block content density:

| Blocks per page | When to use | Reason |
|---|---|---|
| **1 block** | High-density content | Block tự nhiên cao, fill ~80%+ trang |
| **2 blocks** (default) | Mixed content | Standard rhythm, 2 cards stacked |
| **3 blocks** | Low-density content | Each block sparse (~25% trang), 3 = full |

### 7.1 Decision Logic
```
For each block, estimate height_score:
  - Prompt-heavy (>150 words mono): 5
  - Large table (>8 rows, >3 cols): 4
  - Comparison table 2-3 rows: 3
  - Concept+callout combo: 2.5
  - Simple statement 1-2 para: 2
  - Divider (just title + brief): 1

Per page: sum of height_scores
  - sum ≥ 5: → 1 block/page
  - sum 3-4.5: → 2 blocks/page (default)
  - sum ≤ 2.5: → 3 blocks/page

Adjust: never split a logical pair (vd: "SẼ" / "KHÔNG" comparison stays together).
```

### 7.2 Override
User có thể override: "Tôi muốn trang này có 1 block thôi" / "Gộp 3 block lại".

### 7.3 Page Bottom Margin Behavior
- Block dùng natural height (NO atLeast). Page bottom có thể có khoảng trống.
- Acceptable: 0-30% page bottom empty.
- Nếu >30%: thử merge thêm 1 block hoặc thêm reflection question vào block cuối.

---

## 8. Content Mapping (Source → Block)

Source = slide (PPTX), markdown, or freeform content. Skeleton định nghĩa rules map content type → block component.

### 8.1 Title Mapping
- Lấy SLIDE TITLE (action title — câu khẳng định, không phải chủ đề)
- Giữ verb-first 100% trường hợp
- Quá dài (>15 words) → rút gọn nhưng vẫn verb-first
- **NEVER** đổi action title thành topic noun

✅ ĐÚNG: `"Day 2 chốt 1 quick win nhỏ-nhưng-thật, KHÔNG xây toàn hệ thống"`
❌ SAI: `"Phạm vi Day 2"` (mất action, thành chủ đề)

### 8.2 Banner Mapping
Format: `[SECTION_LABEL] · SLIDE [N]`

Examples:
```
"DAY 2 · SECTION 0.2 · SLIDE 5"
"WORKSHOP · MODULE 3 · SLIDE 12"
"DAY 1 · OPENING · SLIDE 7"
```

Rules:
- UPPERCASE
- Use `·` as separator
- Concise, no redundant words

### 8.3 Body Content Mapping

| Source type | Maps to Body |
|---|---|
| Slide has table | `dataTable` (preserve column count + ratios) |
| Slide has bullet list | `bulletList` (1 paragraph each) |
| Slide has prompt block (mono-spaced, long) | `codeBlock` (mono, light bg, padding) |
| Slide has callout/highlight | `calloutBox` (icon + label + body) |
| Slide has paragraph >2 sentences | `Paragraph` (line height 320) |
| Slide is divider (big text only) | Variant 6 (Divider) |
| Slide is note slide | **SKIP** — content gộp vào Note Page (Archetype D) |

### 8.4 Semantic Icon → Callout Type

Skeleton định nghĩa **semantic categories** (universal). Brand Kit fill exact color cho mỗi category.

| Icon | Semantic | Suggested callout color (Brand Kit override) |
|---|---|---|
| 🎯 | Goal / target / final deliverable | `accent_primary` |
| 💡 | Insight / key message | `accent_primary_light` |
| 🔑 | Principle / rule / key point | `accent_primary` |
| ⚠️ | Warning / caution | `accent_primary` (strong) |
| 🚨 | Critical / urgent | `accent_warning` |
| 📖 | Reference / how-to | `accent_secondary` |
| ✅ | Checklist done | (no callout, inline checkbox) |
| ☐ | Checklist todo | (no callout, inline checkbox empty) |
| ☕🍱 | Break / meal | (no callout, plain text) |
| 📝 | Note / scaffold | (no callout, used in Note Page) |

---

## 9. Block Height Behavior

### 9.1 Core Rule
```
Body row: NO atLeast height        ← chìa khóa tránh whitespace bên trong block
Block height: = sum of all rows naturally
Block border: visible at content's natural end
```

### 9.2 Whitespace Philosophy
- ❌ KHÔNG dùng atLeast để force block height
- ✅ Cho block auto-size, accept page bottom margin
- ✅ Tăng font sizes (relative) để content tự nhiên fill nhiều hơn
- ✅ Cho slide sparse, thêm 1 reflection question hoặc takeaway mini để fill thêm
- ✅ Apply density rule (Section 7) để tự decide 1/2/3 blocks per page

### 9.3 Expected Block Heights
```
Sparse block (V1, V6):        ~3000-4000 DXA
Medium block (V2, V5):        ~4000-5500 DXA
Dense block (V3, V4):         ~5500-7500 DXA

Page content area (A4):       ~13150 DXA usable
2 medium blocks + gap:        ~9000-11000 DXA (fits, page bottom = 2000-4000 DXA empty)
1 dense block:                ~7500 DXA (fits, page bottom = 5650 DXA empty — OK)
3 sparse blocks + 2 gaps:     ~9000-12000 + 300 = ~12300 DXA (tight but fits)
```

---

## 10. Header / Footer Pattern

Universal structure. Brand Kit fills text, color, rule style.

### 10.1 Page Header (every page)
```
[LEFT_TEXT]                            [RIGHT_TEXT]
─────────────────────────────────────────────────  ← accent color rule (1pt)
```

Brand Kit hooks:
- `header_left`: typically program/day name
- `header_right`: typically workbook/audience name
- `header_rule_color`: typically `accent_primary`

### 10.2 Page Footer (every page)
```
─────────────────────────────────────────────────  ← neutral rule (1pt)
[FOOTER_LEFT_TEXT]                  Trang X / Y
```

Brand Kit hooks:
- `footer_left`: typically copyright + year
- `footer_rule_color`: typically `neutral_border`

### 10.3 Page Numbers
- Format: `"Trang X / Y"` (default Vietnamese) — Brand Kit MAY override (vd: `"Page X of Y"` English)
- X = current page number (bold), Y = total pages
- Position: footer right

---

## 11. Anti-Patterns (CẤM)

Skeleton-level constraints. Mọi adapter PHẢI tuân theo.

```
❌ Body row có atLeast height (gây internal whitespace)
❌ Footer line redundant với banner (banner đã có slide #)
❌ Image embedding cho slide content (text vỡ khi zoom + không edit)
❌ Color hex có ký tự # (skeleton/brand kit dùng 6-char hex no prefix)
❌ Cell shading dùng SOLID (tạo black bg, phải dùng CLEAR)
❌ Table width dùng PERCENTAGE (breaks in Google Docs — phải DXA absolute)
❌ Line spacing trên paragraph chứa image (clip image)
❌ Stand-alone PageBreak (phải wrap trong Paragraph)
❌ Font kích thước < 9pt cho body (khó đọc — minimum readability)
❌ Title đổi action thành chủ đề (mất verb-first)
❌ Note slides render thành block riêng (phải gộp vào Note Page)
❌ Banner thiếu UPPERCASE hoặc thiếu SLIDE# (banner anatomy yêu cầu cả 2)
❌ Block không có border (mất visual containment)
❌ >3 blocks per page (vi phạm density rule, content quá nhỏ để đọc)
```

---

## 12. Quality Checklist

Run trước khi giao deliverable.

### 12.1 Layout
- [ ] Page archetypes đúng thứ tự (Cover → TOC → Block Pages → Note Page)
- [ ] Density rule tuân thủ (1/2/3 blocks/page theo content)
- [ ] Inter-block gap 100-150 DXA
- [ ] Page header + footer present mọi trang
- [ ] Header có accent rule, footer có neutral rule
- [ ] Page numbers chạy đúng (X / Y)
- [ ] Note page cuối có scaffold đầy đủ

### 12.2 Content
- [ ] Block title verb-first (action statement, không phải topic)
- [ ] Banner format đúng (`[SECTION] · SLIDE [N]` UPPERCASE)
- [ ] Tables có data đầy đủ, không cắt cụt
- [ ] Callouts có icon + label + body (3 thành phần)
- [ ] Vietnamese (or target language) diacritics render đúng
- [ ] No placeholders `[TBD]` / `[TODO]` / `[insert here]`
- [ ] No `<<HOOK:...>>` markers (đã resolve qua Brand Kit)

### 12.3 Technical
- [ ] File validate passed (per format adapter's validator)
- [ ] PDF convert thành công (no errors)
- [ ] File size hợp lý
- [ ] Open được trong target apps (Word + Google Docs + LibreOffice cho .docx)
- [ ] Edit text vẫn được
- [ ] Print preview OK (no orphaned content, no awkward breaks)

---

## 13. Brand Kit Token Surface

**Định nghĩa contract giữa Skeleton và Brand Kit** — handshake interface.

### 13.1 Tokens Brand Kit MUST Fill (required)

```yaml
# Color tokens
color:
  primary:           # Accent for banners, callouts, headers
  primary_dark:      # Hover/pressed states (digital)
  accent_secondary:  # Alternative callout color
  neutral_dark:      # Body text, headings
  neutral_mid:       # Captions, subtitles
  neutral_light:     # Subtle backgrounds
  border:            # Table borders, card outlines
  background:        # Page background (typically white)

# Typography tokens
typography:
  font_sans:         # Body, titles, banners
  font_mono:         # Code blocks, prompts
  size_xs: 9         # Page header/footer
  size_s: 11         # Banner
  size_m: 11         # Body, table, callout body
  size_l: 16         # Block title
  size_xl: 22        # TOC heading
  size_xxl: 26       # Cover title

# Brand identity
identity:
  org_name:          # Display name (vd: "MindX Technology School")
  org_tagline:       # Short tagline
  logo_path:         # Optional, for cover banner

# Voice & language
voice:
  language:          # vi / en / etc.
  formality:         # formal / casual / technical
  cover_reflection:  # "I am taking this course to:" prompt
  page_label:        # "Trang" / "Page" / etc.
  notes_label:       # "Ghi chú" / "Notes" / etc.
```

### 13.2 Tokens Brand Kit MAY Override (optional)

```yaml
# Page setup
page:
  format: A4_portrait     # Override to letter / A4_landscape if needed
  margins:
    top: 1134
    bottom: 1134
    left: 1417            # Or use mirror: inner/outer for binding
    right: 1417
    header: 720
    footer: 720

# Spacing scale
spacing:
  multiplier: 1.0         # Scale all spacing tokens (tighter 0.85, looser 1.15)

# Hierarchy size ratios (if brand wants different scale)
typography_scale:
  ratio: 1.25             # Default geometric scale between sizes
```

### 13.3 Skeleton Invariants (Brand Kit CANNOT override)

```
- Block anatomy order (banner → title → subtitle → body)
- 4 page archetypes (Cover, TOC, Block Pages, Note Page)
- 6 block variants
- Block height behavior (no atLeast on body)
- Density rule (1-3 blocks per page)
- Anti-pattern list
- Typography hierarchy ORDER (banner < body < title < cover_title)
- Body minimum 9pt (readability floor)
- Action title rule (verb-first)
```

### 13.4 Brand Kit Application Flow

```
1. Brand Kit YAML loaded → validate against Skeleton Token Surface
2. Required tokens missing → error (block build)
3. Optional tokens missing → use Skeleton defaults
4. Invariant token attempted override → ignore + warn
5. Mount Brand Kit onto Skeleton → resolved Design System (Tầng 1 complete)
6. Pass to Content Model (Tầng 2) for block composition
7. Pass to Format Adapters (Tầng 3) for render
```

---

## 🔗 Dependencies

**Upstream (Skeleton depends on):**
- Nothing — Skeleton is foundation layer

**Downstream (depends on Skeleton):**
- `brand-kit-schema.md` (Tầng 1b) — fills Token Surface
- `content-model.md` (Tầng 2) — uses Block + Archetype definitions
- `adapter-*.md` (Tầng 3) — implements Skeleton patterns in specific format

---

## 📋 Change Log

| Version | Date | Changes | By |
|---|---|---|---|
| v1.0 | 2026-05-17 | Initial skeleton extracted from MindX guideline v1.0 | MAESTRO + Trainer |

---

*Material Studio · Tầng 1a Skeleton · v1.0 · 2026-05-17*
*Universal patterns. Brand-agnostic. Validated on MindX Workbook (28 trang, 58 slides).*
