# adapter-workbook.md — Material Studio Workbook Adapter

> **Tầng 3 — Format Adapter: Workbook (DOCX)** trong Material Studio.
> Render Content Model → workbook DOCX với slide-card-stacked A4 pattern.

**Version:** v1.0 · 2026-05-17
**Depends on:** `skeleton-patterns.md`, `brand-kit-schema.md`, `content-model.md`
**Reference implementation:** `build_workbook_template.js` (docx-js, validated trên MindX Day 2)

---

## 🎯 TL;DR

Workbook adapter biến Content Model thành file `.docx` editable, brand-consistent, in-ready:
- **Stack:** Node.js + `docx-js` library
- **Pattern:** Slide cards stacked dọc trên A4 (1-3 cards/page theo density rule)
- **Output:** Editable DOCX, validate sạch, open được Word/Google Docs/LibreOffice
- **Pages:** ~28 pages cho 50-block content

---

## 📑 Mục lục

1. [Input/Output spec](#1-io-spec)
2. [Render pipeline](#2-pipeline)
3. [Page archetype renderers](#3-archetype-renderers)
4. [Block renderer (4 rows × N variants)](#4-block-renderer)
5. [Brand Kit application](#5-brand-kit-apply)
6. [Helper functions](#6-helpers)
7. [Validation + preview](#7-validate)
8. [Edge cases](#8-edge-cases)

---

## 1. I/O Spec

### Input
```
- content_model: parsed Content Model YAML (Section 2 schema)
- design_system: resolved Brand Kit + Skeleton (after Tầng 1 merge)
- output_path: string (where to write .docx)
- options:
    print_ready: boolean       # If true, apply mirror_margins from brand_kit
    include_note_page: boolean # Default true
    page_numbers: boolean      # Default true
```

### Output
```
- {output_path}/{project_id}_workbook.docx
- Optional: PDF preview render via LibreOffice
- Validation report: list of warnings/errors
```

---

## 2. Pipeline

```
1. Validate inputs
   - Content Model schema valid (per content-model.md § 8)
   - Brand Kit valid (per brand-kit-schema.md § 3)
   - Output path writable

2. Resolve Design System
   - Merge Brand Kit + Skeleton defaults
   - Build token lookup table

3. Compose document children
   For each Page in content_model.project.pages:
     If skip_in includes 'workbook': skip
     Else: dispatch to archetype renderer (Section 3)
   
4. Wrap in Document
   - Apply page setup (A4 + margins from brand_kit.page or skeleton default)
   - Attach header + footer (Section 3.5)
   - Set up section properties

5. Pack to .docx
   - docx.Packer.toBuffer(doc)
   - Write to output_path

6. Validate output
   - Run docx validator (python3 validate.py)
   - Convert PDF preview (LibreOffice headless)
   - Render thumbnails (pdftoppm)

7. Return summary
```

---

## 3. Page Archetype Renderers

### 3.1 Cover (Archetype A)
```javascript
function renderCover(brandKit, projectMeta) {
  return [
    // Top: Brand banner block (red bg)
    brandBannerBlock(brandKit),
    
    // Title block (centered)
    p(brandKit.voice.cover_reflection_prompt, { 
      size: brandKit.typography.size_xxl, 
      bold: true, 
      align: 'center' 
    }),
    p(projectMeta.title, { size: brandKit.typography.size_xl, align: 'center' }),
    p(projectMeta.subtitle, { 
      size: brandKit.typography.size_l, 
      italic: true, 
      align: 'center',
      color: brandKit.color.primary 
    }),
    
    // Cohort info bar (light gray bg)
    cohortInfoBar(projectMeta.program.cohort_info),
    
    // Fill-in section
    fillInSection(brandKit.voice.cover_reflection_prompt),
    
    // Name/Department/Date fields (3 columns)
    fieldRow(brandKit.voice.field_labels),
    
    pageBreak()
  ];
}
```

### 3.2 TOC (Archetype B)
```javascript
function renderTOC(tocData, brandKit) {
  return [
    p(brandKit.voice.toc_label, { 
      size: brandKit.typography.size_xl, 
      bold: true, 
      color: brandKit.color.primary 
    }),
    p(tocData.subtitle, { italic: true, color: brandKit.color.neutral_mid }),
    horizontalRule(brandKit.color.primary, 1),
    
    // Schedule table
    dataTable(
      ['Thời gian', 'Giai đoạn', 'Công cụ', 'Output', 'Trang'],
      tocData.schedule_table.map(r => [r.time, r.stage, r.tool, r.output, r.page_ref || '']),
      [20, 35, 15, 25, 5],  // column widths %
      { headerBg: brandKit.color.neutral_dark, headerText: 'FFFFFF' }
    ),
    
    blank(200),
    
    // Two callouts: deliverable + how-to-use
    twoCalloutsSideBySide(
      { icon: '🎯', label: 'SẢN PHẨM CUỐI NGÀY', body: tocData.final_deliverable, color: brandKit.color.primary },
      { icon: '📖', label: 'CÁCH DÙNG WORKBOOK', body: tocData.how_to_use_text, color: brandKit.color.accent_secondary }
    ),
    
    pageBreak()
  ];
}
```

### 3.3 Block Pages (Archetype C)
```javascript
function renderBlockPage(page, brandKit) {
  const blocks = page.blocks.filter(b => !(b.hints?.skip_in?.includes('workbook')));
  const density = page.density_override || autoPickDensity(blocks);
  
  const children = [];
  blocks.forEach((block, idx) => {
    children.push(renderBlock(block, brandKit));
    if (idx < blocks.length - 1) {
      children.push(blank(brandKit.spacing.inter_block_gap || 120));
    }
  });
  children.push(pageBreak());
  return children;
}

function autoPickDensity(blocks) {
  const totalScore = blocks.reduce((s, b) => s + (b.hints?.height_score || estimateHeight(b)), 0);
  if (totalScore >= 5 && blocks.length === 1) return 1;
  if (totalScore <= 2.5 && blocks.length === 3) return 3;
  return 2;  // default
}

function estimateHeight(block) {
  // Heuristic per skeleton § 7.1
  if (block.body.type === 'code_block' && block.body.content.length > 400) return 5;
  if (block.body.type === 'table' && block.body.rows.length > 6) return 4;
  if (block.body.type === 'table') return 3;
  if (block.body.type === 'concept_callout') return 2.5;
  if (block.body.type === 'paragraphs') return 2;
  if (block.body.type === 'divider') return 1;
  return 2.5;
}
```

### 3.4 Note Page (Archetype D)
```javascript
function renderNotePage(page, brandKit) {
  const children = [
    p('📝 ' + brandKit.voice.notes_label, { 
      size: brandKit.typography.size_xl, 
      bold: true, 
      color: brandKit.color.primary 
    }),
    blank(200)
  ];
  
  page.note_clusters.forEach(cluster => {
    children.push(p(cluster.cluster_label, { size: brandKit.typography.size_m, bold: true }));
    if (cluster.prompt) {
      children.push(p(cluster.prompt, { size: brandKit.typography.size_s, italic: true, color: brandKit.color.neutral_mid }));
    }
    for (let i = 0; i < cluster.line_count; i++) {
      children.push(underlineRule());
    }
    children.push(blank(150));
  });
  
  if (page.next_step_text) {
    children.push(blank(200));
    children.push(p(page.next_step_text, { 
      size: brandKit.typography.size_m, 
      bold: true, 
      color: brandKit.color.primary 
    }));
  }
  
  return children;
}
```

### 3.5 Header + Footer
```javascript
function pageHeader(brandKit, projectMeta) {
  return new Header({
    children: [
      twoColumnRow(
        `${projectMeta.program.name} · ${projectMeta.program.day_label}`,
        `Workbook ${projectMeta.audience.role}`,
        { size: brandKit.typography.size_xs, color: brandKit.color.neutral_mid }
      ),
      horizontalRule(brandKit.color.primary, 1)
    ]
  });
}

function pageFooter(brandKit) {
  return new Footer({
    children: [
      horizontalRule(brandKit.color.border, 1),
      twoColumnRow(
        `© ${brandKit.identity.org_name} · 2026`,
        `${brandKit.voice.page_label} {PAGE} / {NUMPAGES}`,
        { size: brandKit.typography.size_xs, color: brandKit.color.neutral_mid }
      )
    ]
  });
}
```

---

## 4. Block Renderer (4 Rows × Variants)

```javascript
function renderBlock(block, brandKit) {
  // Returns a Table with 1 column, N rows wrapping all components
  
  const rows = [
    // Row 1: Banner (accent bg)
    bannerRow(block.banner, brandKit),
    
    // Row 2: Title
    titleRow(block.title, brandKit),
    
    // Row 3: Subtitle (optional)
    block.subtitle ? subtitleRow(block.subtitle, brandKit) : null,
    
    // Row 4: Body (variant-dispatch)
    bodyRow(block.body, block.variant, brandKit)
  ].filter(Boolean);
  
  return new Table({
    rows,
    width: { size: 9072, type: WidthType.DXA },  // Content width
    borders: thinAllBorders(brandKit.color.border),  // Card outline
    // NO atLeast height on body row (skeleton invariant)
  });
}

function bannerRow(banner, brandKit) {
  const text = banner.custom_text 
    || `${banner.section_label}${banner.slide_number ? ` · SLIDE ${banner.slide_number}` : ''}`;
  
  return new TableRow({
    children: [new TableCell({
      shading: { fill: brandKit.color.primary, type: ShadingType.CLEAR },
      margins: { top: 100, bottom: 100, left: 240, right: 240 },
      children: [p(text.toUpperCase(), {
        size: brandKit.typography.size_s,
        bold: true,
        color: 'FFFFFF',
        letterSpacing: 60
      })]
    })]
  });
}
```

### 4.1 Body Variants

```javascript
function bodyRow(body, variant, brandKit) {
  const cellChildren = (() => {
    switch (body.type) {
      case 'paragraphs':       return renderParagraphs(body, brandKit);
      case 'table':            return [renderDataTable(body, brandKit)];
      case 'list':             return renderList(body, brandKit);
      case 'code_block':       return renderCodeBlock(body, brandKit);
      case 'concept_callout':  return renderConceptCallout(body, brandKit);
      case 'divider':          return renderDivider(body, brandKit);
      case 'mixed':            return body.fragments.flatMap(f => bodyRowChildren(f, variant, brandKit));
      default: throw new Error(`Unknown body type: ${body.type}`);
    }
  })();
  
  return new TableRow({
    children: [new TableCell({
      margins: { top: 120, bottom: 120, left: 240, right: 240 },
      children: cellChildren
      // NO atLeast height — skeleton invariant
    })]
  });
}
```

#### renderDataTable
```javascript
function renderDataTable(body, brandKit) {
  const headerRow = new TableRow({
    children: body.headers.map(h => new TableCell({
      shading: { fill: brandKit.color.neutral_dark, type: ShadingType.CLEAR },
      children: [p(h, { 
        size: brandKit.typography.size_m, 
        bold: true, 
        color: 'FFFFFF' 
      })]
    }))
  });
  
  const dataRows = body.rows.map(r => new TableRow({
    children: r.map(cell => new TableCell({
      children: [p(cell, { size: brandKit.typography.size_m })]
    }))
  }));
  
  return new Table({
    rows: [headerRow, ...dataRows],
    columnWidths: computeColumnWidths(body.column_widths),  // % → DXA
    borders: thinAllBorders(brandKit.color.border)
  });
}
```

#### renderCalloutBox
```javascript
function renderCalloutBox(callout, brandKit) {
  const color = resolveCalloutColor(callout, brandKit);  // semantic_type → hex
  
  return new Table({
    rows: [new TableRow({
      children: [new TableCell({
        shading: { fill: lightenColor(color, 0.95), type: ShadingType.CLEAR },
        borders: {
          left: { style: BorderStyle.SINGLE, size: 16, color },
          top: noBorder, right: noBorder, bottom: noBorder
        },
        children: [
          p(`${callout.icon} ${callout.label}`, { 
            size: brandKit.typography.size_m, 
            bold: true, 
            color 
          }),
          p(callout.body, { size: brandKit.typography.size_m })
        ]
      })]
    })],
    width: { size: 9072, type: WidthType.DXA }
  });
}

function resolveCalloutColor(callout, brandKit) {
  if (callout.semantic_type && brandKit.callout_overrides?.[callout.semantic_type]) {
    return brandKit.callout_overrides[callout.semantic_type];
  }
  // Fallback to skeleton mapping (icon → default semantic)
  const iconMap = {
    '🎯': brandKit.color.primary,
    '💡': brandKit.color.primary,
    '🔑': brandKit.color.primary,
    '⚠️': brandKit.color.primary,
    '🚨': brandKit.color.primary_dark,
    '📖': brandKit.color.accent_secondary
  };
  return iconMap[callout.icon] || brandKit.color.primary;
}
```

---

## 5. Brand Kit Application

### 5.1 Token Resolution
```javascript
function resolveDesignSystem(brandKit) {
  return {
    color: brandKit.color,
    typography: brandKit.typography,
    identity: brandKit.identity,
    voice: brandKit.voice,
    page: brandKit.page || SKELETON_DEFAULTS.page,
    spacing: {
      multiplier: brandKit.spacing?.multiplier || 1.0,
      cell_padding_v: 100 * (brandKit.spacing?.multiplier || 1),
      cell_padding_h: 240 * (brandKit.spacing?.multiplier || 1),
      inter_block_gap: 120 * (brandKit.spacing?.multiplier || 1)
    },
    callout_overrides: brandKit.callout_overrides || {}
  };
}
```

### 5.2 Mirror Margins (Print Binding)
```javascript
function applyPageSetup(brandKit) {
  if (brandKit.page?.mirror_margins?.enabled) {
    return {
      size: A4_DIMENSIONS,
      margin: {
        top: brandKit.page.margins.top,
        bottom: brandKit.page.margins.bottom,
        left: brandKit.page.mirror_margins.inner,
        right: brandKit.page.mirror_margins.outer,
        header: brandKit.page.margins.header,
        footer: brandKit.page.margins.footer
      },
      mirrorMargins: true  // docx-js flag (or write to settings.xml)
    };
  }
  return defaultPageSetup(brandKit);
}
```

---

## 6. Helper Functions

```javascript
// Text run with brand kit defaults
function tx(text, opts = {}) {
  return new TextRun({
    text: String(text),
    font: opts.font || brandKit.typography.font_sans,
    size: (opts.size || brandKit.typography.size_m) * 2,  // half-points
    bold: opts.bold || false,
    italics: opts.italic || false,
    color: opts.color || brandKit.color.neutral_dark
  });
}

// Paragraph helper
function p(text, opts = {}) {
  return new Paragraph({
    children: Array.isArray(text) ? text : [tx(text, opts)],
    alignment: opts.align || AlignmentType.LEFT,
    spacing: { 
      before: opts.before || 0, 
      after: opts.after || 100, 
      line: opts.line || 320 
    }
  });
}

// Empty spacer
function blank(size = 100) {
  return new Paragraph({ 
    children: [new TextRun({ text: '' })], 
    spacing: { before: 0, after: size } 
  });
}

// Page break
function pageBreak() {
  return new Paragraph({ children: [new PageBreak()] });
}

// Underline rule (for fill-in lines)
function underlineRule() {
  return new Paragraph({
    children: [new TextRun({ text: ' '.repeat(80) })],
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: '999999' } },
    spacing: { before: 100, after: 100 }
  });
}

// Border styles
const noBorder = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
function thinAllBorders(color) {
  const b = { style: BorderStyle.SINGLE, size: 4, color };
  return { top: b, bottom: b, left: b, right: b, insideHorizontal: b, insideVertical: b };
}
```

---

## 7. Validation + Preview

### 7.1 Post-Build Validation
```python
# validate.py — run after .docx generation
import zipfile
from lxml import etree

def validate_docx(path):
    issues = []
    with zipfile.ZipFile(path) as z:
        try:
            # Parse main document
            doc = etree.fromstring(z.read('word/document.xml'))
            # Schema validation against OOXML
            # Check no atLeast height on body rows (skeleton invariant)
            # Check color hex format (no #)
            # Check table widths use DXA not pct
        except etree.XMLSyntaxError as e:
            issues.append(f"XML parse error: {e}")
    return issues
```

### 7.2 PDF Preview
```bash
libreoffice --headless --convert-to pdf workbook.docx --outdir /tmp
pdftoppm -jpeg -r 110 /tmp/workbook.pdf /tmp/preview
```

### 7.3 Common Issues Detector
```
- Banner màu không lên → check shading.type=CLEAR not SOLID
- Table cột rộng không đều → check column_widths math
- Content tràn trang → giảm font hoặc split block
- Vietnamese diacritics vỡ → font fallback (Arial Unicode MS)
- Page count quá nhiều → check density rule, merge sparse pages
```

---

## 8. Edge Cases

### 8.1 Long Block Title (>15 words)
- Auto-wrap in title row (don't truncate)
- Increase title row height to accommodate
- WARN in validation log

### 8.2 Empty Body
- FAIL build — block must have body content
- Suggest using Variant 6 Divider with `centered_text` for placeholder pages

### 8.3 Sparse Content (page bottom > 50% empty)
- Auto-suggest merge with next page if applicable
- Or add reflection question to last block
- Configure via `workbook_density: spacious` to accept

### 8.4 Image Embedding
- AVOID for slide content (skeleton anti-pattern)
- ALLOWED for cover logo, callout icons (small decorative)
- If logo required: ensure file path in brand_kit.identity.logo_path

### 8.5 Multi-Language Project
- Brand Kit determines primary language
- Per-block language override: not supported in MVP
- For mixed-language content, use Unicode-capable font

### 8.6 Print-Ready Output
- Set `print_ready: true` option
- Enable mirror_margins in brand kit
- Validate gáy width ≥ 2.5cm
- Generate PDF for printer

---

## 🔗 Dependencies

**Upstream:** `content-model.md`, `brand-kit-schema.md`, `skeleton-patterns.md`
**Reference impl:** `build_workbook_template.js` (in source materials)
**Runtime:** Node.js + `docx-js`

---

## 📋 Change Log

| Version | Date | Changes | By |
|---|---|---|---|
| v1.0 | 2026-05-17 | Initial workbook adapter spec | MAESTRO + Trainer |

---

*Material Studio · Tầng 3 Workbook Adapter · v1.0 · 2026-05-17*
