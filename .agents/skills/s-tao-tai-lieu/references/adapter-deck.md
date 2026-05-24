# adapter-deck.md — Material Studio Deck Adapter

> **Tầng 3 — Format Adapter: Deck (PPTX)** trong Material Studio.
> Render Content Model → slide deck với McKinsey-style action titles + brand consistency.

**Version:** v1.0 · 2026-05-17
**Depends on:** `skeleton-patterns.md`, `brand-kit-schema.md`, `content-model.md`

---

## 🎯 TL;DR

Deck adapter biến Content Model thành slide deck (.pptx hoặc Marp .md):
- **Stack:** Marp (Markdown-based, recommended) hoặc python-pptx
- **Pattern:** 1 Block = 1 slide (default), với 6 slide layouts mapping 6 block variants
- **Output:** .pptx editable trong PowerPoint/Keynote/Google Slides, hoặc .pdf export
- **Slide count:** ~50-60 slides cho 50-block content (1:1) hoặc compressed (1:2)

---

## 📑 Mục lục

1. [Stack choice: Marp vs python-pptx](#1-stack-choice)
2. [I/O spec](#2-io-spec)
3. [Render pipeline](#3-pipeline)
4. [6 slide layouts (per block variant)](#4-slide-layouts)
5. [Cross-artifact hints application](#5-hints)
6. [Brand Kit → Marp theme](#6-marp-theme)
7. [Export pipeline](#7-export)
8. [Edge cases](#8-edge-cases)

---

## 1. Stack Choice: Marp vs python-pptx

**Recommend: Marp** (cho MVP). Fallback: python-pptx for advanced layouts.

| Aspect | Marp | python-pptx |
|---|---|---|
| Authoring | Markdown (editable) | Python code |
| Templates | CSS-based theme | XML-based |
| Speed to build | Fast (declarative) | Slower (imperative) |
| Editability after build | High (re-render from .md) | Medium (edit .pptx directly) |
| Layout control | Themes + slide directives | Full XML access |
| Best for | Standard training decks | Custom-layout decks |

**MVP:** Marp-based pipeline. Advanced: hybrid (Marp for body, python-pptx for cover + special slides).

---

## 2. I/O Spec

### Input
```
- content_model: parsed Content Model
- design_system: resolved Brand Kit + Skeleton
- output_path: string
- options:
    format: marp_md | pptx | pdf      # Default: pptx
    block_to_slide_ratio: 1_to_1 | compressed   # 1:1 = each block = 1 slide; compressed = merge sparse blocks
    include_speaker_notes: boolean    # Default true (from block.subtitle + hints)
```

### Output
```
- {output_path}/{project_id}_deck.pptx (or .md / .pdf)
- Marp source: {output_path}/{project_id}_deck.md (for re-rendering)
- Validation report
```

---

## 3. Render Pipeline

```
1. Validate inputs (Content Model + Brand Kit valid)

2. Generate Marp theme CSS from Brand Kit
   - color.primary → --primary
   - typography.* → --font-*
   - sizes → CSS rem scale
   - Save: /tmp/{project_id}_theme.css

3. Build Marp .md file
   - Front matter (theme, size, paginate, headers/footers)
   - For each Page in content_model:
       - cover archetype → cover slide(s)
       - toc archetype → TOC slide(s)
       - block_pages archetype → 1 slide per block
       - note archetype → SKIP (note pages typically workbook-only)
       - divider archetype → divider slide

4. Render via Marp CLI
   marp --theme {project_id}_theme.css \
        --pptx \
        {project_id}_deck.md \
        -o {project_id}_deck.pptx

5. Validate output
   - Open via python-pptx, check slide count, basic structure
   - Optional: PDF preview

6. Return summary
```

---

## 4. 6 Slide Layouts (per block variant)

### 4.1 Layout SIMPLE (V1)
```markdown
<!-- _class: slide-simple -->

# {block.title}

*{block.subtitle}*

{body.paragraphs[0].text}

{body.paragraphs[1].text}

{if body.callout:}
> {callout.icon} **{callout.label}** — {callout.body}
```

CSS:
```css
.slide-simple h1 { font-size: 2.2rem; color: var(--neutral-dark); }
.slide-simple em { font-size: 1.1rem; color: var(--neutral-mid); }
.slide-simple p { font-size: 1.5rem; line-height: 1.5; }
.slide-simple blockquote { 
  border-left: 4px solid var(--primary);
  background: var(--neutral-light);
  padding: 1rem;
}
```

### 4.2 Layout COMPARISON (V2)
```markdown
<!-- _class: slide-comparison -->

# {block.title}

*{block.subtitle}*

<table>
<tr><th>{headers[0]}</th><th>{headers[1]}</th></tr>
{for row in rows:}
<tr><td>{row[0]}</td><td>{row[1]}</td></tr>
{endfor}
</table>
```

CSS: Table header `bg: var(--neutral-dark); color: white;`. Rows alternating subtle bg.

### 4.3 Layout PROCESS (V3 — Steps Table)
Similar to comparison but typically 3-5 columns. CSS adjusts table column widths.

### 4.4 Layout PROMPT (V4 — Code Block)
```markdown
<!-- _class: slide-prompt -->

# {block.title}

*{body.description}*

```text
{body.content}
```

> {callout.icon} **{callout.label}** — {callout.body}
```

CSS:
```css
.slide-prompt pre { 
  background: var(--neutral-light);
  font-family: var(--font-mono);
  font-size: 1.1rem;
  padding: 1.5rem;
  border-radius: 4px;
}
```

### 4.5 Layout CONCEPT_CALLOUT (V5)
```markdown
<!-- _class: slide-concept -->

# {block.title}

*{block.subtitle}*

{body.concept_paragraph}

> {callout.icon} **{callout.label}**
> {callout.body}

{if body.reflection_question:}
*🤔 {body.reflection_question}*
```

### 4.6 Layout DIVIDER (V6)
```markdown
<!-- _class: slide-divider -->

# {body.centered_text}

*{body.description}*

{if body.upcoming_items:}
{for item in upcoming_items:}
- {item}
{endfor}
```

CSS: Centered hero text, large font (3rem+), brand accent color.

---

## 5. Cross-Artifact Hints Application

### 5.1 deck_emphasis
```
hints.deck_emphasis = 'hero'
  → Block renders as standalone HERO slide
  → Larger title font, sparse layout, prominent callout
  → Use for key takeaways, hero messages

hints.deck_emphasis = 'takeaway'
  → Block renders as small TAKEAWAY footer slide
  → Compact, summarizes key point
  → Use for recap/closing blocks

hints.deck_emphasis = 'normal' (default)
  → Standard layout per variant
```

CSS classes added: `.slide-hero`, `.slide-takeaway` on top of variant class.

### 5.2 skip_in
```
hints.skip_in includes 'deck'
  → Skip this block entirely in deck output
```

Typically used for:
- Note slides (workbook-only)
- Reflection scaffolds

### 5.3 source_slide_ref
```
hints.source_slide_ref = 5
  → Used in speaker notes as provenance
  → Helps trainer find source if updates needed
```

### 5.4 Block-to-Slide Compression Mode
```
options.block_to_slide_ratio = 'compressed':
  - If 2 consecutive blocks have height_score ≤ 2 each → merge into 1 slide with split layout
  - Useful for short presentations where 1:1 ratio yields too many slides
```

---

## 6. Brand Kit → Marp Theme

### 6.1 CSS Variable Generation
```javascript
function generateMarpTheme(brandKit) {
  return `
/* @theme ${brandKit.metadata.client_id}-theme */

:root {
  --primary: #${brandKit.color.primary};
  --primary-dark: #${brandKit.color.primary_dark};
  --accent-secondary: #${brandKit.color.accent_secondary};
  --neutral-dark: #${brandKit.color.neutral_dark};
  --neutral-mid: #${brandKit.color.neutral_mid};
  --neutral-light: #${brandKit.color.neutral_light};
  --border: #${brandKit.color.border};
  --bg: #${brandKit.color.background};
  
  --font-sans: ${brandKit.typography.font_sans}, sans-serif;
  --font-mono: ${brandKit.typography.font_mono}, monospace;
  
  --size-xs: ${brandKit.typography.size_xs}pt;
  --size-s: ${brandKit.typography.size_s}pt;
  --size-m: ${brandKit.typography.size_m}pt;
  --size-l: ${brandKit.typography.size_l}pt;
  --size-xl: ${brandKit.typography.size_xl}pt;
  --size-xxl: ${brandKit.typography.size_xxl}pt;
}

section {
  background: var(--bg);
  font-family: var(--font-sans);
  color: var(--neutral-dark);
  padding: 50px 80px;
}

section h1 {
  color: var(--neutral-dark);
  font-size: var(--size-xl);
  font-weight: bold;
  margin-bottom: 0.5rem;
}

section h1 + em {
  color: var(--primary);
  font-size: var(--size-l);
  font-style: italic;
  display: block;
  margin-bottom: 2rem;
}

section header {
  font-size: var(--size-xs);
  color: var(--neutral-mid);
  border-bottom: 2px solid var(--primary);
  padding-bottom: 4px;
}

section footer {
  font-size: var(--size-xs);
  color: var(--neutral-mid);
}

/* Cover slide */
section.slide-cover {
  text-align: center;
  background: var(--primary);
  color: white;
}

/* Divider slide */
section.slide-divider {
  text-align: center;
  background: linear-gradient(135deg, var(--primary), var(--primary-dark));
  color: white;
}

section.slide-divider h1 {
  color: white;
  font-size: 3rem;
}

/* Hero emphasis */
section.slide-hero h1 {
  font-size: 3rem;
  text-align: center;
  margin-top: 2rem;
}

/* Tables */
section table {
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0;
}

section th {
  background: var(--neutral-dark);
  color: white;
  padding: 0.8rem;
  text-align: left;
}

section td {
  padding: 0.8rem;
  border: 1px solid var(--border);
}

/* Callouts (blockquote styling) */
section blockquote {
  border-left: 4px solid var(--primary);
  background: var(--neutral-light);
  padding: 1rem 1.5rem;
  margin: 1.5rem 0;
}

/* Code blocks */
section pre {
  background: var(--neutral-light);
  font-family: var(--font-mono);
  padding: 1rem;
  border-radius: 4px;
  font-size: 1.1rem;
  overflow-x: auto;
}
`;
}
```

### 6.2 Header/Footer Marp Directives
```markdown
---
marp: true
theme: {client_id}-theme
size: 16:9
paginate: true
header: '{program.name} · {program.day_label}'
footer: '© {brandKit.identity.org_name} · 2026'
---
```

---

## 7. Export Pipeline

### 7.1 Marp CLI (Node-based)
```bash
# Install
npm install -g @marp-team/marp-cli

# Build
marp \
  --theme {project_id}_theme.css \
  --pptx \
  --pdf \
  {project_id}_deck.md \
  -o {project_id}_deck

# Outputs:
#   {project_id}_deck.pptx
#   {project_id}_deck.pdf
```

### 7.2 Speaker Notes
```markdown
# Slide title

Slide body content...

<!--
Speaker notes from block.subtitle + hints.source_slide_ref:
- "Slide source: PPTX slide #5"
- Talking points...
-->
```

Notes extracted from `block.subtitle` (primary) + custom notes field (if Content Model extended).

### 7.3 Output Variants
```
Standard:        .pptx (editable in PowerPoint)
Read-only:       .pdf (for distribution)
Web-embeddable:  .html (Marp HTML export)
Source:          .md  (for version control + re-rendering)
```

---

## 8. Edge Cases

### 8.1 Block Too Dense for 1 Slide
- Auto-split: if estimated content height > slide capacity, split into "Title" + "Title (cont.)"
- WARN in validation: "Block {id} split across 2 slides"
- Alternative: hint `workbook_density: spacious` and accept multi-slide

### 8.2 Code Block Too Long
- Limit: ~25 lines per slide for mono content (readability)
- Auto-split with `(cont.)` suffix
- Or hint `deck_emphasis: hero` to dedicate larger slide

### 8.3 Image Embedding
- Marp supports `![alt](path)` directly
- For brand logo: `![bg fit](logo.png)` on cover slide
- Skeleton anti-pattern: don't embed slide content AS image (text vỡ)

### 8.4 Language + Font
- Vietnamese diacritics: ensure font supports (Arial, Roboto, Inter OK)
- For mixed CJK content: use font fallback chain

### 8.5 No Cover/TOC Mode
- Some short presentations don't need cover/TOC
- Option: `skip_archetypes: [cover, toc]` → deck starts at first block_pages
- Useful for embedded section presentations

### 8.6 Vertical (Portrait) Slides
- Marp supports `size: 9:16` for portrait
- Use for mobile-first presentations (rare)
- Default: 16:9 landscape

---

## 🔗 Dependencies

**Upstream:** `content-model.md`, `brand-kit-schema.md`, `skeleton-patterns.md`
**Runtime:** Marp CLI (Node) or python-pptx + LibreOffice (Python)

---

## 📋 Change Log

| Version | Date | Changes | By |
|---|---|---|---|
| v1.0 | 2026-05-17 | Initial deck adapter spec (Marp primary) | MAESTRO + Trainer |

---

*Material Studio · Tầng 3 Deck Adapter · v1.0 · 2026-05-17*
