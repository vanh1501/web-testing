# workflow-training.md — Material Studio Training Workflow

> **Tầng 4 — Use-Case Workflow: Training** trong Material Studio.
> Orchestration logic cho training/đào tạo use case — produce deck + workbook + (optional) facilitator notes đồng bộ.

**Version:** v1.0 · 2026-05-17
**Depends on:** All Tầng 1-3 references

---

## 🎯 TL;DR

Training workflow = recipe để biến source training material (deck/notes/outline) thành **bundle artifact đồng bộ** cho 1 chương trình đào tạo:

```
Input → [Training Workflow] → Output bundle:
  ├── deck.pptx       (trainer-facing, slide-by-slide)
  ├── workbook.docx   (learner-facing, takes home)
  ├── facilitator.md  (trainer notes, optional)
  └── handout.pdf     (1-page summary, optional)
```

Tất cả từ 1 Content Model, brand-consistent qua 1 Brand Kit.

---

## 📑 Mục lục

1. [Workflow input/output](#1-io)
2. [Pipeline 6 phases](#2-pipeline)
3. [Source → Content Model conversion](#3-conversion)
4. [Multi-artifact rendering](#4-multi-artifact)
5. [Cross-artifact consistency rules](#5-consistency)
6. [Decision tree: artifact selection](#6-decision-tree)
7. [Output bundle structure](#7-output-bundle)
8. [Iteration + revision flow](#8-iteration)

---

## 1. Workflow I/O

### Input (any combination)
```
- source_material: file path(s)
    - existing .pptx (most common — convert to content model)
    - markdown outline
    - .docx draft
    - freeform notes
    - blank (build from scratch)
- brand_kit_id: string (vd: "mindx", "bank_abc")
- project_metadata:
    - title, audience, duration, language, etc. (per content-model.md § 2)
- artifact_selection:
    - deck: boolean (default true)
    - workbook: boolean (default true for training)
    - facilitator_notes: boolean (default false)
    - handout: boolean (default false)
- options:
    - print_ready_workbook: boolean (apply mirror_margins)
    - speaker_notes_in_deck: boolean (default true)
```

### Output
```
project_output/
├── content_model.yaml              # Persisted source of truth
├── deck.pptx                       # If artifact_selection.deck=true
├── deck.pdf                        # Auto-generated preview
├── workbook.docx                   # If artifact_selection.workbook=true
├── workbook.pdf                    # Auto-generated preview
├── facilitator_notes.md            # If facilitator_notes=true
├── handout.pdf                     # If handout=true
├── validation_report.md            # All warnings/errors across adapters
└── README.md                       # Bundle overview + how to update
```

---

## 2. Pipeline 6 Phases

### Phase 1 — INTAKE (5 minutes)
Skill ask user 5-7 questions to gather:
- Project metadata (title, audience, duration)
- Source material location + format
- Client (which Brand Kit to use)
- Artifact selection (which to produce)
- Special requirements (print binding, speaker notes, etc.)

**Output:** Project metadata + plan (= "Intake Summary")

### Phase 2 — SOURCE PARSING (5-15 min, depends on source)
Convert source → Content Model:
- PPTX source → use `python-pptx` to extract per-slide content
- Markdown outline → parse heading hierarchy
- Freeform notes → structured intake (interview-style with user)

**Output:** Draft Content Model YAML (no Brand Kit applied yet)

### Phase 3 — CONTENT REVIEW (10-30 min, user-driven)
User reviews draft Content Model:
- Block titles verb-first?
- Banner structure correct?
- Body variants appropriate?
- Block density (hints.height_score) tuned?
- Cross-artifact hints (skip_in, deck_emphasis) set?

**Output:** Confirmed Content Model

### Phase 4 — MULTI-ARTIFACT RENDER (~10 min)
For each selected artifact, invoke adapter:
```
For artifact in artifact_selection:
  If artifact = 'deck':       invoke adapter-deck
  If artifact = 'workbook':   invoke adapter-workbook
  If artifact = 'handout':    invoke adapter-handout
  If artifact = 'facilitator': invoke facilitator-notes-gen
```

Each adapter:
- Loads Brand Kit
- Applies cross-artifact hints (skip_in, emphasis)
- Renders + validates

**Output:** Files in output bundle

### Phase 5 — CONSISTENCY CHECK (auto, 1-2 min)
Cross-artifact validation:
- Block count consistent across artifacts (modulo `skip_in`)?
- Titles identical between deck slide N and workbook block N?
- Brand colors consistent (Brand Kit applied uniformly)?
- Page numbers / slide numbers align?

**Output:** Consistency report (PASS / WARN / FAIL)

### Phase 6 — DELIVERY (5 min)
- Generate README.md for bundle (artifact list, regeneration instructions)
- Validate all files open in target apps
- Generate PDF previews
- Package as ZIP (optional)
- Present to user with download links

**Output:** Final bundle ready to ship

---

## 3. Source → Content Model Conversion

### 3.1 From PPTX (most common)
```python
from pptx import Presentation

def pptx_to_content_model(pptx_path, project_metadata, brand_kit_id):
    prs = Presentation(pptx_path)
    pages = []
    
    # Detect cover slide (typically slide 1)
    if is_cover_slide(prs.slides[0]):
        pages.append({'archetype': 'cover'})
    
    # Detect TOC slide
    toc_idx = find_toc_slide(prs.slides)
    if toc_idx is not None:
        pages.append({'archetype': 'toc', 'toc_data': extract_toc_data(prs.slides[toc_idx])})
    
    # Process remaining slides → blocks
    blocks = []
    for i, slide in enumerate(prs.slides, 1):
        if i in [1, toc_idx]: continue  # Skip cover/TOC
        if is_note_slide(slide): continue  # Note slides handled separately
        
        block = {
            'id': f'blk_{i}',
            'variant': detect_variant(slide),  # Heuristic-based
            'banner': {
                'section_label': extract_section_label(slide),
                'slide_number': i
            },
            'title': extract_action_title(slide),
            'subtitle': extract_subtitle(slide),
            'body': extract_body(slide),
            'hints': {
                'source_slide_ref': i,
                'height_score': estimate_height_score(slide)
            }
        }
        blocks.append(block)
    
    # Group blocks into pages (per density rule)
    block_pages = group_blocks_into_pages(blocks)
    pages.extend(block_pages)
    
    # Note page (gathered from note slides)
    note_clusters = extract_note_clusters(prs.slides)
    if note_clusters:
        pages.append({'archetype': 'note', 'note_clusters': note_clusters})
    
    return {
        'project': {
            'metadata': project_metadata,
            'brand_kit': brand_kit_id,
            'pages': pages
        }
    }
```

### 3.2 Variant Detection Heuristics
```python
def detect_variant(slide):
    """Map slide content type → block variant."""
    if has_long_code_block(slide):    return 'prompt'
    if has_table(slide) and is_comparison_table(slide):  return 'comparison'
    if has_table(slide):              return 'process'
    if has_callout_box(slide) and has_short_paragraph(slide):  return 'concept_callout'
    if is_divider_slide(slide):       return 'divider'
    return 'simple'
```

### 3.3 Action Title Extraction
```python
def extract_action_title(slide):
    """Extract slide title, verify verb-first action statement."""
    raw_title = slide.shapes.title.text if slide.shapes.title else ''
    
    if not raw_title:
        return '[NEEDS_TITLE]'  # User must fill in Phase 3
    
    if starts_with_topic_noun(raw_title):
        return f'[REVIEW_TITLE: {raw_title}]'  # Flag for user review
    
    return raw_title
```

### 3.4 Manual Source Path
If source is freeform or non-structured:
- Skill ask user via interactive Q&A:
  - "List your main topics/sections..."
  - "For each section, what's the key takeaway?"
  - "Any specific examples or tools to highlight?"
- Build Content Model iteratively
- User confirms each block before moving on

---

## 4. Multi-Artifact Rendering

### 4.1 Render Order
```
1. Workbook (longest, most complex)
2. Deck (mid complexity)
3. Handout (derived from deck)
4. Facilitator notes (derived from all above)
```

Reason: rendering workbook first surfaces content issues. Other artifacts inherit fixes.

### 4.2 Parallel Rendering (optimization)
Adapters can run in parallel (no shared state). For MVP: serial OK. Future: parallel via job queue.

### 4.3 Adapter Selection Matrix
```
                  | Training | Presentation | Reporting | Proposal |
------------------|----------|--------------|-----------|----------|
Deck              | ✅       | ✅           | ✅         | ✅       |
Workbook          | ✅ DFLT  | ❌           | ❌         | ❌       |
Handout (1-page)  | optional | ✅ DFLT      | ✅ DFLT    | ❌       |
Report (exec)     | ❌       | ❌           | ✅ DFLT    | ❌       |
Facilitator notes | optional | ❌           | ❌         | ❌       |
Speaker notes     | optional | ✅           | optional  | ✅       |
```

For Training workflow specifically: deck + workbook default; handout/facilitator optional.

---

## 5. Cross-Artifact Consistency Rules

### 5.1 Title Consistency
```
Block.title MUST be identical in:
  - Deck slide title
  - Workbook block title
  - Handout entry title (if included)

Validator FAIL on mismatch.
```

### 5.2 Block Order Consistency
```
Block order in Content Model = order in all artifacts (after skip_in filtering).

If block X comes before block Y in Content Model:
  - Deck: slide for X precedes slide for Y
  - Workbook: block X comes before block Y in page order
  - Handout: X listed before Y

Validator FAIL on out-of-order rendering.
```

### 5.3 Brand Consistency
```
Same brand_kit_id resolves to same color/font/voice across artifacts.

Validator: load each artifact, check:
  - Primary color appears in expected positions (banner, accent)
  - Font family consistent (sample text)
  - Voice consistent (page labels, etc.)
```

### 5.4 Banner / Slide # Reference
```
Workbook block banner: "DAY 2 · SECTION 0.2 · SLIDE 5"
Deck slide footer: "Slide 5 / 60"

These numbering MUST align. Validator check.

Special case: hints.deck_emphasis = 'hero' → may take extra slide (multi-slide expansion). 
Adapter must update reference: SLIDE 5 in workbook → SLIDES 5-6 in deck. Validator aware.
```

### 5.5 Update Propagation
```
If user edits Content Model after initial build:
  1. Re-validate Content Model
  2. Identify changed pages/blocks (diff)
  3. Re-render only affected artifacts (incremental, if supported)
  4. Re-run consistency check

For MVP: full re-render (simpler). Incremental in v2.
```

---

## 6. Decision Tree: Artifact Selection

```
START
  │
  ▼
Is this for TRAINING (people learn + practice)?
  │
  ├── YES
  │     │
  │     ▼
  │     Deck = trainer presents? → YES → include deck
  │     Learners take notes / reference later? → YES → include workbook
  │     Need facilitator brief (multi-trainer or new trainer)? → optional → include facilitator_notes
  │     Need 1-page summary for attendees post-training? → optional → include handout
  │
  └── NO (presentation/report instead)
        │
        ▼
        Route to different workflow (workflow-presentation.md, workflow-reporting.md)
```

### 6.1 Common Training Bundle Patterns

**Pattern A — Standard Training (default)**
```
Artifacts: deck + workbook
Use case: Internal training, workshop with 8-30 attendees
Time to build: ~30-60 min after source ready
```

**Pattern B — Train-the-Trainer**
```
Artifacts: deck + workbook + facilitator_notes
Use case: Training material for multiple trainers to deliver
Time to build: ~45-90 min
```

**Pattern C — Quick Workshop**
```
Artifacts: deck + handout (no workbook)
Use case: Short workshop (1-2 hours), no take-home content needed
Time to build: ~20-40 min
```

**Pattern D — Full Kit**
```
Artifacts: deck + workbook + facilitator_notes + handout
Use case: Flagship training, multi-day program
Time to build: ~60-120 min
```

---

## 7. Output Bundle Structure

### 7.1 Standard Bundle
```
{project_id}_bundle/
├── README.md                      ← Bundle overview, regeneration instructions
├── content_model.yaml             ← Source of truth (edit here to update)
├── 01_deck/
│   ├── {project_id}_deck.pptx
│   ├── {project_id}_deck.pdf
│   └── {project_id}_deck.md       ← Marp source
├── 02_workbook/
│   ├── {project_id}_workbook.docx
│   └── {project_id}_workbook.pdf
├── 03_handout/                    ← if included
│   └── {project_id}_handout.pdf
├── 04_facilitator/                ← if included
│   ├── {project_id}_facilitator.md
│   └── {project_id}_facilitator.pdf
├── _validation/
│   ├── validation_report.md       ← All warnings/errors
│   └── consistency_check.md       ← Cross-artifact alignment
└── _brand_kit/
    └── brand-kit-{client_id}.yaml ← Snapshot of brand kit used (for reproducibility)
```

### 7.2 README.md Template
```markdown
# {project_title} — Material Bundle

**Client:** {brand_kit.client_display_name}
**Generated:** {timestamp}
**Material Studio version:** v1.0

## Artifacts Included
- ✅ Deck (PPTX + PDF preview)
- ✅ Workbook (DOCX + PDF preview)
- ⚠️ Handout — not included this build
- ⚠️ Facilitator notes — not included this build

## How to Update

1. Edit `content_model.yaml` (single source of truth)
2. Re-run: `material-studio render --project {project_id}`
3. New artifacts will replace existing in this folder

## Brand Kit Snapshot
The brand kit used for this build is captured in `_brand_kit/`. If brand updates after this build, update the kit file in skill folder, then re-render.

## Validation Notes
See `_validation/validation_report.md` for any warnings/errors during build.
```

---

## 8. Iteration + Revision Flow

### 8.1 Common Revision Scenarios

**Scenario A: Single block edit**
```
1. User: "Update block blk_5 — change title to '...'"
2. Skill: edit content_model.yaml at block id=blk_5
3. Skill: re-render only artifacts containing blk_5 (deck + workbook)
4. Validate cross-artifact consistency
5. Replace files in bundle
```

**Scenario B: Brand change (color update)**
```
1. User: "Update brand kit MindX — primary color change to '#XXXXXX'"
2. Skill: edit brand-kit-mindx.yaml
3. Skill: re-render ALL artifacts for ALL projects using this brand
4. (Or: incremental — only projects user specifies)
```

**Scenario C: Add new block**
```
1. User: "Insert new block after blk_5: variant comparison, title '...'"
2. Skill: edit content_model.yaml, add block + recompute density
3. Skill: re-render
4. Validate updated banner.slide_number references
```

**Scenario D: New client onboarding**
```
1. Brand Intake workflow (per brand-kit-schema.md § 4)
2. Save new brand-kit-{client_id}.yaml
3. Project: same Content Model, swap brand_kit reference
4. Re-render → new branded bundle
```

### 8.2 Versioning
```
content_model.yaml versioning (Git or skill-internal):
  v1.0 — initial build
  v1.1 — added 3 blocks based on Day 1 feedback
  v1.2 — updated tools list per Q2 changes
  ...
```

Each build = snapshot of content model + brand kit at build time. Past bundles reproducible.

---

## 🔗 Dependencies

**Upstream (depends on):**
- `skeleton-patterns.md` (universal patterns)
- `brand-kit-schema.md` (per-client styling)
- `content-model.md` (project schema)
- `adapter-workbook.md` (workbook adapter)
- `adapter-deck.md` (deck adapter)

**Downstream (used by):**
- `SKILL.md` (Tầng 5 orchestrator entry)

---

## 📋 Change Log

| Version | Date | Changes | By |
|---|---|---|---|
| v1.0 | 2026-05-17 | Initial training workflow spec — 6-phase pipeline | MAESTRO + Trainer |

---

*Material Studio · Tầng 4 Training Workflow · v1.0 · 2026-05-17*
