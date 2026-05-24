# File Forensics Checklist — MECE 4 Dimensions

**Mục đích**: Bóc tách file Excel hỗn loạn của non-tech user theo MECE — không bỏ sót, không trùng lặp. Output là AS-IS Audit Report với severity flags.

**Cách dùng**: Step 1 của pipeline. Đọc file qua python (openpyxl/pandas), apply checklist 4 dimensions dưới.

---

## TABLE OF CONTENTS

- [Dimension 1: Sheet Anatomy](#dimension-1-sheet-anatomy)
- [Dimension 2: Data Structure Quality](#dimension-2-data-structure-quality)
- [Dimension 3: Workflow Archaeology](#dimension-3-workflow-archaeology)
- [Dimension 4: Output Ecosystem](#dimension-4-output-ecosystem)
- [Severity scoring](#severity-scoring)
- [Quick scan script template](#quick-scan-script-template)

---

## Dimension 1: Sheet Anatomy

**Mục tiêu**: Mỗi sheet đóng vai trò gì trong workflow.

### Sheet role classification

| Role type | Signal nhận biết | % frequency (non-tech files) |
|---|---|---|
| **Raw input** | User paste data, ít hoặc không formula | 20% |
| **Lookup/master** | Static reference data (vd: AE list, product catalog) | 10% |
| **Calculation/model** | Heavy formulas, transform raw → metric | 30% |
| **Display** | Charts, formatted view, ít data | 20% |
| **Mixed (anti-pattern)** | ≥2 roles trong 1 sheet (vd: raw + chart trộn) | **60% với non-tech** ⚠️ |
| **Orphan** | Không link tới sheet nào khác | 15% — ELIMINATE candidate |
| **Snapshot** | Lưu 1 kỳ rồi quên (vd: "T01_2023", "Q3_2022") | 25% với file >6 tháng |

### Checklist per sheet

- [ ] Sheet role: [Raw / Lookup / Calc / Display / Mixed / Orphan / Snapshot]
- [ ] Có dependents (sheet khác reference vào)? Yes/No
- [ ] Last meaningful update: [recent / >3 kỳ ago / never updated]
- [ ] Hidden? Yes/No (hidden sheets thường là dead code)
- [ ] Tab color: có semantic không? (red=raw, green=dashboard...)

**Auto-flag**:
- Sheet "Mixed" → MAJOR (vi phạm separation of concerns)
- Sheet "Orphan" + last update >3 kỳ → ELIMINATE candidate
- Sheets named "Sheet1, Sheet2, Sheet3..." → MINOR (no semantic naming)
- Hidden sheets >5 → MAJOR (dead code accumulation)

---

## Dimension 2: Data Structure Quality

**Mục tiêu**: Data trong file có sạch để build BI không.

### Structural checklist

| Check item | Pass criteria | Flag if fail |
|---|---|---|
| Column headers consistent across kỳ? | Same names + order each cycle | **CRITICAL** — schema unstable |
| Data type consistent within column? | All cells in column = same type (date/text/number) | MAJOR |
| Merged cells trong data range? | NO merged cells in tabular data | **CRITICAL** — vỡ Pivot, Filter, Sort |
| Blank rows/columns giữa data? | Continuous data range | MAJOR — Table auto-expand broken |
| Formula vs hardcoded mix? | Same column = same type (all formula or all hardcoded) | MAJOR — audit trail loss |
| Hidden columns trong data range? | If hidden, document reason | MINOR if <5, MAJOR if ≥10 |
| External links còn sống? | All `[file.xlsx]Sheet!Range` resolvable | **CRITICAL** if `#REF!` |
| Named ranges còn reference đúng? | All named ranges point to valid range | MAJOR if broken |
| Date format consistent? | Same date column = same format (ngày/tháng/năm) | MAJOR |
| Numeric format consistent? | Same numeric column = same precision + decimal | MINOR |
| Trailing whitespace trong text columns? | Trim test passes | MINOR but affects lookup matching |
| Encoding issues (Vietnamese diacritics broken)? | All chars readable | MINOR but affects display |

### Quick data structure scan

```python
import openpyxl
wb = openpyxl.load_workbook(path, data_only=False)
for sheet in wb.sheetnames:
    ws = wb[sheet]
    # Check merged cells
    if ws.merged_cells.ranges:
        flag(f"Sheet '{sheet}' has {len(ws.merged_cells.ranges)} merged ranges")
    # Check blank rows
    # Check column type consistency
    # Check external link references
```

---

## Dimension 3: Workflow Archaeology

**Mục tiêu**: User vận hành file thế nào mỗi kỳ?

### Workflow signals

Đọc từ file pattern + ask user nếu cần xác nhận:

| Aspect | Signals to detect | Inference |
|---|---|---|
| **Refresh trigger** | Power Query connection? Manual paste signs? VBA macro? | Auto / Semi / Manual |
| **Input pattern** | User paste raw vào sheet "Raw"? Type-in manually? Import button? | Paste / Type / Import |
| **Distribution** | Multiple file copies? Email signature in cell? Print page setup configured? | Email / Print / Screenshot / Link |
| **Version control** | "v1, v2, v3" file names? "TEMP", "OLD" sheets? Single template file? | Save-As / Overwrite / Template |
| **Time burden** | Ask user OR estimate from anti-pattern count | X phút/giờ per cycle |

### Time burden estimation rule

Estimate based on observed anti-patterns:

| Anti-pattern | Time cost/kỳ |
|---|---|
| VLOOKUP chain ≥3 cấp (recalc lag) | 2-5 phút lag + 5 phút maintain |
| Manual copy-paste raw mỗi kỳ | 10-20 phút |
| Manual chart range update | 5-10 phút per chart |
| Save-As file mỗi kỳ + rebuild Power Query | 20-30 phút |
| 3+ sheets to sync manually | 15-30 phút |
| Conditional formatting >5 rules/range lag | 3-5 phút wait time |

Sum total → "Maintenance burden hiện tại ~X giờ/kỳ"

---

## Dimension 4: Output Ecosystem

**Mục tiêu**: File này tương tác với system nào khác?

### Ecosystem map

| Aspect | Detect from | Action |
|---|---|---|
| **Inputs FROM** | External links, Power Query connections, paste source comments | Map upstream data sources |
| **Outputs TO** | Sheet "For [recipient]"? Export to PDF setup? Email template integration? | Map downstream consumers |
| **Downstream dependencies** | Ask user: "Output file/sheet này ai dùng?" | List downstream files/people |
| **Upstream sources** | "Data nhận từ ai? Format gì? Stable không?" | List upstream sources + stability |

### Critical ecosystem questions to ask (if not inferrable)

1. "Ai gửi data cho bạn? Format gì? Stable không?" — upstream source stability
2. "Báo cáo này gửi cho ai? Format gì?" — downstream consumers
3. "Nếu file này không có nữa, downstream impact gì?" — criticality

**Auto-flag**:
- External link broken (#REF!) → **CRITICAL**
- Source data manual email attachment (not systematic) → MAJOR (refresh fragility)
- Downstream has dependencies (other files reference this file) → consider before major refactor

---

## Severity scoring

Aggregate flags from 4 dimensions:

| Severity | Definition | Examples |
|---|---|---|
| **CRITICAL** | Vi phạm foundation → file không vận hành đúng | Merged cells trong data range, external #REF!, schema unstable mỗi kỳ |
| **MAJOR** | Anti-pattern rõ ràng → cần fix ngay | VLOOKUP chain ≥4, ≥5 hidden sheets, ≥10 conditional formatting rules, blank rows trong data |
| **MINOR** | Cosmetic/efficiency → fix nếu có thời gian | Generic sheet names, inconsistent colors, trailing whitespace |

### Decision based on severity count

| CRITICAL count | MAJOR count | Recommendation |
|---|---|---|
| 0-1 | 0-2 | **Acceptable** — minor cleanup |
| 0-2 | 3-5 | **Refactor** — build TO-BE on cleaned AS-IS |
| ≥3 hoặc 1+ với ≥5 MAJOR | ≥5 | **Rebuild from scratch** — confirm với user |

---

## Quick scan script template

```python
"""
Quick file forensics — run on uploaded Excel
"""
import openpyxl
from pathlib import Path

def scan_file(path):
    wb = openpyxl.load_workbook(path, data_only=False)
    report = {
        'file_size_mb': Path(path).stat().st_size / 1024 / 1024,
        'sheet_count': len(wb.sheetnames),
        'critical': [],
        'major': [],
        'minor': [],
        'sheet_roles': {},
    }
    
    # File size check
    if report['file_size_mb'] > 50:
        report['major'].append(f"File size {report['file_size_mb']:.1f}MB — performance risk")
    
    # Sheet count check
    if report['sheet_count'] > 20:
        report['major'].append(f"{report['sheet_count']} sheets — focus top 3 by recent modified")
    
    # Per-sheet checks
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        
        # Merged cells in data range
        if ws.merged_cells.ranges:
            report['critical'].append(f"Sheet '{sheet_name}': {len(ws.merged_cells.ranges)} merged ranges")
        
        # Hidden sheet
        if ws.sheet_state == 'hidden':
            report['minor'].append(f"Sheet '{sheet_name}': hidden")
        
        # Generic naming
        if sheet_name.lower().startswith('sheet') and sheet_name[5:].isdigit():
            report['minor'].append(f"Sheet '{sheet_name}': generic name")
        
        # Snapshot pattern
        if any(snap in sheet_name.lower() for snap in ['_2022', '_2023', 'old', 'backup', 'temp']):
            report['major'].append(f"Sheet '{sheet_name}': possible snapshot/dead code")
    
    # Hidden sheets count
    hidden_count = sum(1 for s in wb.sheetnames if wb[s].sheet_state == 'hidden')
    if hidden_count >= 5:
        report['major'].append(f"{hidden_count} hidden sheets — possible dead code accumulation")
    
    return report

# Usage
report = scan_file('user_file.xlsx')
print(f"CRITICAL: {len(report['critical'])}")
print(f"MAJOR: {len(report['major'])}")
print(f"MINOR: {len(report['minor'])}")
# Then build user-facing summary
```

**Output template** (sau khi run scan):

```markdown
## AS-IS File Audit: [filename]

**Inventory**: [N] sheets | [X] MB | last modified [date]

**Sheet roles**:
| Sheet | Inferred role | Notes |
|---|---|---|
| ... | ... | ... |

**Anti-pattern flags**:
- 🔴 CRITICAL ([N]): [list]
- 🟠 MAJOR ([N]): [list]
- 🟡 MINOR ([N]): [list]

**Workflow archaeology**:
- Refresh: [trigger / frequency / owner]
- Distribution: [method]
- Time burden estimate: ~[X] giờ/kỳ

**Overall verdict**: [Acceptable / Refactor / Rebuild]
**Recommendation**: [next step]
```
