# content-model.md — Material Studio Content Model

> **Tầng 2 — Content Model (format-agnostic)** trong kiến trúc Material Studio.
> Định nghĩa cấu trúc dữ liệu trung gian: source content → Content Model → format adapters.
> 1 nguồn content → N artifact (deck + workbook + report + handout) đồng bộ.

**Version:** v1.0 · 2026-05-17
**Depends on:** `skeleton-patterns.md` (block anatomy + variants)

---

## 🎯 TL;DR

Content Model = **biểu diễn YAML/JSON của 1 project** (training, presentation, report) trước khi render ra format cuối.

```
Source (PPTX/markdown/freeform)
        │
        ▼
   Content Model (YAML)  ← Format-agnostic. Anh edit ở đây.
        │
        ├──→ Workbook adapter → workbook.docx
        ├──→ Deck adapter     → deck.pptx
        ├──→ Report adapter   → report.docx
        └──→ Handout adapter  → handout.pdf
```

**Edit Content Model 1 chỗ** → mọi artifact phía dưới tự cập nhật (sau khi rebuild).

---

## 📑 Mục lục

1. [Schema overview](#1-schema-overview)
2. [Project metadata](#2-project-metadata)
3. [Page node](#3-page-node)
4. [Block node](#4-block-node)
5. [Body content types](#5-body-content-types)
6. [Cross-artifact hints](#6-cross-artifact-hints)
7. [Example: minimal project](#7-example-minimal)
8. [Validation rules](#8-validation)

---

## 1. Schema Overview

```yaml
# Top-level project structure
project:
  metadata: {...}              # Project info (client, title, audience, etc.)
  brand_kit: string             # client_id → load brand-kit-{id}.yaml
  pages: [Page]                 # Ordered list of pages

# Page = atomic unit on physical paper / slide
Page:
  archetype: enum               # cover | toc | block_pages | note | divider
  blocks: [Block]               # 1-3 blocks if archetype = block_pages

# Block = atomic content unit (= "slide card" in MindX terminology)
Block:
  id: string                    # Stable ID for cross-references
  variant: enum                 # simple | comparison | process | prompt | concept_callout | divider
  banner: Banner                # Section/slide indicator
  title: string                 # Action title (verb-first)
  subtitle: string?             # Optional 1-liner
  body: Body                    # Variant-specific content
  hints: BlockHints?            # Cross-artifact rendering hints

# Body = polymorphic content
Body:
  type: enum                    # paragraphs | table | list | callout | code_block | mixed
  # Type-specific fields...
```

---

## 2. Project Metadata

```yaml
project:
  metadata:
    project_id: string          # snake_case (vd: "mindx_day2", "bank_abc_q1_training")
    title: string               # Display title
    subtitle: string?           # Tagline
    use_case: enum              # training | presentation | report | proposal
    audience:
      role: string              # vd: "BOM", "Senior Manager", "Investor"
      count: integer?           # # of attendees (optional)
      level: enum               # executive | manager | individual_contributor
    duration:
      total_minutes: integer    # Total session length
      per_day: integer?         # If multi-day
    language: string            # ISO 639-1 (override brand_kit if needed)
    program:
      name: string              # vd: "Agentic Workspace Day 2"
      day_label: string?        # vd: "DAY 2"
      day_of: string?           # vd: "of 2"
      cohort_info: string?      # vd: "12 BOM · Core team"
    created_at: YYYY-MM-DD
    updated_at: YYYY-MM-DD
  
  brand_kit: string             # client_id → resolve to brand-kit-{id}.yaml
  
  pages: [...]                  # See Section 3
```

---

## 3. Page Node

```yaml
Page:
  archetype: cover | toc | block_pages | note | divider
  page_id: string?              # Stable ID (auto-gen if not provided)
  
  # Archetype-specific fields:
  
  # ── cover ──
  cover_fields:
    reflection_prompt: string?  # Override brand_kit voice.cover_reflection_prompt
    additional_fields: [string]?  # Extra form fields (override default Name/Dept/Date)
  
  # ── toc ──
  toc_data:
    schedule_table: [ScheduleRow]
    final_deliverable: string
    how_to_use_text: string
  
  # ── block_pages ──
  blocks: [Block]               # 1-3 blocks (skeleton density rule)
  density_override: integer?    # Override auto-pick (1, 2, or 3)
  
  # ── note ──
  note_clusters: [NoteCluster]
  next_step_text: string?
  
  # ── divider ──
  divider_text: string          # Big centered text (vd: "BUỔI CHIỀU", "BREAK")
  divider_description: string?

ScheduleRow:
  time: string                  # vd: "08:00 — 08:30"
  stage: string                 # vd: "GĐ 1 — Khảo sát Mindset"
  tool: string                  # vd: "Workbook"
  output: string                # vd: "Ghi chú Why-What-How"
  page_ref: string?             # vd: "p. 3" — auto-filled by adapter

NoteCluster:
  cluster_label: string         # vd: "Cụm 1 (sau GĐ 1 sáng)"
  prompt: string?               # Optional reflection prompt
  line_count: integer           # # underline rules to render (default 3-4)
```

---

## 4. Block Node

Block = atomic content unit. Skeleton anatomy: Banner → Title → Subtitle → Body.

```yaml
Block:
  id: string                    # Stable ID (vd: "blk_5_tools_comparison")
  variant: simple | comparison | process | prompt | concept_callout | divider
  
  banner:
    section_label: string       # vd: "DAY 2 · SECTION 0.2"
    slide_number: integer?      # # in source deck (if applicable)
    custom_text: string?        # Override default banner format
  
  title: string                 # ACTION title (verb-first). Skeleton enforces.
  subtitle: string?             # Optional 1-line
  
  body: Body                    # Variant-specific (Section 5)
  
  hints:                        # Cross-artifact rendering hints (Section 6)
    height_score: number?       # 1-5 for density calc (auto if not set)
    deck_emphasis: enum?        # normal | hero | takeaway (for deck adapter)
    workbook_density: enum?     # compact | normal | spacious
    skip_in: [enum]?            # Artifacts to skip this block: [report, handout]
```

### 4.1 Banner Format Rules
Default banner text (skeleton-defined): `"{section_label} · SLIDE {slide_number}"`

Examples:
```yaml
banner:
  section_label: "DAY 2 · SECTION 0.2"
  slide_number: 5
# Renders: "DAY 2 · SECTION 0.2 · SLIDE 5"
```

Custom override:
```yaml
banner:
  custom_text: "OPENING · WELCOME"   # Use as-is, ignore section_label/slide_number
```

### 4.2 Title Rule (Skeleton-enforced)
- Must be **verb-first action statement**
- ≤ 15 words preferred
- Validator FAIL if title starts with topic noun ("Phạm vi", "Tổng quan", "Giới thiệu")

---

## 5. Body Content Types

6 body types map 1:1 to 6 block variants (skeleton Section 6).

### 5.1 `paragraphs` (V1 — Simple Statement)
```yaml
body:
  type: paragraphs
  paragraphs:
    - text: string              # Body paragraph
      emphasis: [string]?       # Words to bold (lookup in text)
    - text: "..."
  callout: Callout?             # Optional callout after paragraphs
```

### 5.2 `table` (V2 — Comparison, V3 — Process)
```yaml
body:
  type: table
  headers: [string]             # Column headers
  rows: [[string]]              # Rows of cell content
  column_widths: [number]?      # Relative widths (vd: [50, 50] or [30, 30, 40])
  comparison_mode: boolean?     # true = V2 (compare), false = V3 (process)
```

### 5.3 `list` (V1 variant — bullets/checklist)
```yaml
body:
  type: list
  list_style: bullet | numbered | checklist
  items:
    - text: string
      sub_items: [string]?      # Optional nesting (1 level)
      checked: boolean?         # For checklist
```

### 5.4 `code_block` (V4 — Prompt/Code)
```yaml
body:
  type: code_block
  language: string?             # vd: "text", "python", "bash" — affects syntax in deck
  content: string               # Multi-line text, preserved verbatim
  description: string?          # Pre-code description paragraph
  callout: Callout?             # Optional post-code callout (context/explanation)
```

### 5.5 `concept_callout` (V5 — Concept + Callout Combo)
```yaml
body:
  type: concept_callout
  concept_paragraph: string     # 1-2 sentence explanation
  callout: Callout              # Highlight callout (required)
  reflection_question: string?  # Optional fill-in question
```

### 5.6 `divider` (V6 — Section Opener)
```yaml
body:
  type: divider
  centered_text: string         # Big text (vd: "BUỔI SÁNG")
  description: string?          # Brief description below
  upcoming_items: [string]?     # List to fill sparse divider
```

### 5.7 `mixed` (escape hatch — multiple body fragments)
```yaml
body:
  type: mixed
  fragments: [Body]             # Sequence of typed bodies
```

Use sparingly — most slides fit cleanly into 1 of the 6 single types.

### 5.8 Callout Sub-Schema
```yaml
Callout:
  icon: string                  # Emoji (🎯 💡 🔑 ⚠️ 🚨 📖)
  label: string                 # UPPERCASE label
  body: string                  # Callout content
  semantic_type: enum?          # goal | insight | principle | warning | critical | reference
                                # If omitted, derived from icon
```

Color resolved at adapter time: `brand_kit.callout_overrides.{semantic_type}` → fallback to skeleton mapping.

---

## 6. Cross-Artifact Hints

Some content renders differently per artifact. `hints` on Block provide adapter-specific guidance.

```yaml
hints:
  height_score: 4               # 1-5 scale for density (auto-calc if omitted)
                                # See skeleton Section 7.1
  
  deck_emphasis: hero           # normal | hero (1-slide deck takeaway) | takeaway (small footer)
                                # Influences font sizes in deck adapter
  
  workbook_density: spacious    # compact | normal | spacious
                                # Adjusts inter-block gap in workbook
  
  skip_in: [report]             # This block won't appear in report adapter
                                # Useful for divider/break blocks
  
  source_slide_ref: 5           # Reference to source PPTX slide number (provenance)
  source_section: "0.2"         # Source section ID (provenance)
```

### 6.1 Skip Rules
```yaml
skip_in: [handout]              # Workbook + deck + report include this block, handout skips.
skip_in: [report, handout]      # Only deck + workbook include.
skip_in: []                     # (Default) all artifacts include.
```

Common patterns:
- Note slides (`archetype: note`): typically `skip_in: [deck, report, handout]` (workbook only)
- Divider blocks: typically `skip_in: [report]` (report doesn't need section breaks)
- Hero callouts: typically `deck_emphasis: hero` → 1-slide hero in deck

---

## 7. Example — Minimal Project

```yaml
project:
  metadata:
    project_id: mindx_day2_sample
    title: "Agentic Workspace · Day 2"
    subtitle: "Trải nghiệm điều phối AI Agent · Thiết kế Quick Win V1"
    use_case: training
    audience:
      role: "BOM"
      count: 12
      level: manager
    duration:
      total_minutes: 480
      per_day: 480
    language: vi
    program:
      name: "MindX Agentic Workspace"
      day_label: "DAY 2"
      day_of: "of 2"
      cohort_info: "12 BOM · AI Lead Core team"
    created_at: 2026-05-17
    updated_at: 2026-05-17
  
  brand_kit: mindx
  
  pages:
    # Page 1: Cover
    - archetype: cover
    
    # Page 2: TOC
    - archetype: toc
      toc_data:
        schedule_table:
          - time: "08:00 — 08:30"
            stage: "GĐ 1 — Khảo sát Mindset"
            tool: "Workbook"
            output: "Ghi chú Why-What-How"
          - time: "08:30 — 09:00"
            stage: "GĐ 2 — Kích hoạt + Phân tích"
            tool: "Workspace"
            output: "WBS + Dự án mới"
        final_deliverable: "Gói Quick Win V1 (.zip) chuẩn bị Hackathon"
        how_to_use_text: "Mỗi trang gồm 2 slide trình bày liên tục từ deck. Đọc song song khi trainer trình bày. Ghi chú tại các trang Reflection."
    
    # Page 3: Block page (2 blocks)
    - archetype: block_pages
      blocks:
        - id: blk_3_why_day2
          variant: concept_callout
          banner:
            section_label: "DAY 2 · OPENING"
            slide_number: 4
          title: "Day 2 chốt 1 quick win nhỏ-nhưng-thật, KHÔNG xây toàn hệ thống"
          subtitle: "Mục tiêu rõ ràng → kết quả đo được"
          body:
            type: concept_callout
            concept_paragraph: "Day 2 không phải để thiết kế lý tưởng. Day 2 là để chứng minh AI agent có thể giải 1 bài toán cụ thể của phòng ban anh chị trong 4 giờ."
            callout:
              icon: "🎯"
              label: "MỤC TIÊU CUỐI NGÀY"
              body: "Mỗi BOM có 1 Quick Win V1 — workspace chạy được + file MD đặc tả + báo cáo demo."
              semantic_type: goal
          hints:
            deck_emphasis: hero
        
        - id: blk_4_tools
          variant: comparison
          banner:
            section_label: "DAY 2 · SECTION 0.2"
            slide_number: 5
          title: "Day 2 dùng 2 AI chuyên biệt: ChatGPT thiết kế, Antigravity thi công"
          subtitle: "Thay vì gò mọi thứ vào một hệ thống"
          body:
            type: table
            headers: ["Công cụ", "Vai trò", "Khi dùng"]
            rows:
              - ["ChatGPT", "Thiết kế logic, viết spec", "GĐ 1, 3"]
              - ["Antigravity", "Thi công workspace, vá lỗi", "GĐ 2-4"]
            column_widths: [30, 40, 30]
          hints:
            height_score: 3
    
    # Page 4: Note page (final)
    - archetype: note
      note_clusters:
        - cluster_label: "Cụm 1 (sau GĐ 1 sáng) — Mindset shifts"
          line_count: 4
        - cluster_label: "Cụm 2 (sau GĐ 2 sáng) — Workspace setup"
          line_count: 4
        - cluster_label: "Cụm 3 (sau GĐ 3 chiều) — Quick Win design"
          line_count: 4
      next_step_text: "→ Mang về phòng ban + chuẩn bị Hackathon"
```

**Note:** Example trên minimal (4 pages, 2 blocks total). Real MindX Day 2 = 28 pages, ~50 blocks. Cấu trúc giữ nguyên, scale up content.

---

## 8. Validation Rules

Run trên Content Model trước khi pass cho adapters.

### 8.1 Schema Conformance
```
- project.metadata required keys present? FAIL.
- project.brand_kit references existing brand-kit-{id}.yaml? FAIL.
- pages array non-empty? FAIL.
- Each page has valid archetype? FAIL.
- block_pages archetype has 1-3 blocks? FAIL if 0 or >3.
```

### 8.2 Block Validation
```
- Block.id unique within project? FAIL if duplicate.
- Block.variant matches body.type compatibility?
  - variant=simple → body.type in [paragraphs, list]
  - variant=comparison → body.type=table, comparison_mode=true
  - variant=process → body.type=table, comparison_mode=false
  - variant=prompt → body.type=code_block
  - variant=concept_callout → body.type=concept_callout
  - variant=divider → body.type=divider
- Block.title verb-first (heuristic)? WARN if starts with noun (topic-style).
- Block.title ≤ 15 words? WARN if longer.
- Banner.section_label UPPERCASE preferred? WARN.
```

### 8.3 Density Validation
```
For each block_pages page:
  total_height_score = sum(block.hints.height_score for block in page.blocks)
  block_count = len(page.blocks)
  
  Per skeleton Section 7:
  - block_count=1 + total_score<3 → WARN (page too sparse)
  - block_count=2 + total_score>9 → WARN (likely overflow)
  - block_count=3 + total_score>7.5 → WARN (likely overflow)
```

### 8.4 Cross-Artifact Validation
```
- skip_in references valid artifact names? FAIL.
- deck_emphasis values valid? FAIL.
- workbook_density values valid? FAIL.
```

### 8.5 Reference Integrity
```
- Callout.semantic_type matches Callout.icon (if both provided)? WARN on mismatch.
- TOC schedule_table.page_ref values valid? Auto-fill by adapter.
- NoteCluster.cluster_label unique within page? WARN.
```

---

## 🔗 Dependencies

**Upstream:**
- `skeleton-patterns.md` — block anatomy, variants, density rule
- `brand-kit-schema.md` — `project.brand_kit` references brand-kit-{id}.yaml

**Downstream:**
- `adapter-workbook.md` — consumes Content Model → DOCX
- `adapter-deck.md` — consumes Content Model → PPTX
- `adapter-report.md` (future) — consumes Content Model → executive DOCX
- `adapter-handout.md` (future) — consumes Content Model → 1-page PDF

---

## 📋 Change Log

| Version | Date | Changes | By |
|---|---|---|---|
| v1.0 | 2026-05-17 | Initial schema + MindX Day 2 minimal example | MAESTRO + Trainer |

---

*Material Studio · Tầng 2 Content Model · v1.0 · 2026-05-17*
