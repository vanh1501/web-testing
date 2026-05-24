#!/usr/bin/env python3
"""
scaffold_pmbok.py — Project scaffolder cho skill quan-ly-du-an.

Clone 5 PMBOK templates, hydrate placeholder, tạo folder structure, register vào DANH-SACH-DU-AN.md.

Usage:
    python scaffold_pmbok.py --name "Dự án ABC" --code "ABC-2026-001" --folder "DA-ABC-2026" \\
        --pm "Sếp Hậu" [--sponsor "CEO"] [--coordinator "Trợ lý AI"] \\
        [--template-dir .agents/templates/pmbok] [--workspace-root .]

Output: JSON status of scaffold operation
"""

import argparse
import json
import re
import shutil
import sys
import unicodedata
from datetime import date
from pathlib import Path


PMBOK_TEMPLATES = [
    "00_Project_Charter.md",
    "00_Project_Master_Index.md",
    "00_RACI_Matrix.md",
    "00_Risk_Issue_Log.md",
    "00_Change_Log.md",
]


def slugify(text):
    """Convert 'Vận hành E-commerce 2026' → 'Van-hanh-E-commerce-2026'"""
    nfkd = unicodedata.normalize("NFKD", text)
    no_diacritic = "".join(c for c in nfkd if not unicodedata.combining(c))
    sanitized = re.sub(r"[^\w\s-]", "", no_diacritic).strip()
    return re.sub(r"[-\s]+", "-", sanitized)


def auto_code(project_name):
    """Auto-gen project code from name: take 3-letter prefix + year"""
    slug = slugify(project_name).upper()
    words = slug.split("-")
    prefix = "".join(w[0] for w in words[:3] if w)[:4] or "PRJ"
    return f"{prefix}-{date.today().year}-001"


def hydrate_template(template_content, replacements):
    """Replace all {{KEY}} with values"""
    result = template_content
    for key, value in replacements.items():
        result = result.replace(f"{{{{{key}}}}}", str(value))
    return result


def create_default_template(template_name):
    """If template not found in template-dir, create minimal default"""
    defaults = {
        "00_Project_Charter.md": """# Project Charter — {{PROJECT_NAME}}

**Mã dự án:** {{PROJECT_CODE}}
**Ngày khởi tạo:** {{DATE}}
**PM:** {{PM_NAME}}
**Sponsor:** {{SPONSOR}}
**Coordinator:** {{COORDINATOR}}

## 1. Business Case
(Mô tả lý do dự án — Operator điền)

## 2. Scope
(Mô tả phạm vi — Operator điền)

## 3. Deliverables
(Liệt kê các deliverable chính — Operator điền)

## 4. Timeline & Milestones
(Milestone chính — Operator điền)

## 5. Success Criteria
(Tiêu chí thành công — Operator điền)
""",
        "00_Project_Master_Index.md": """# Master Index — {{PROJECT_NAME}}

**Mã:** {{PROJECT_CODE}} | **PM:** {{PM_NAME}} | **Date:** {{DATE}}

## File Registry
| # | File | Vị trí | Owner | Status |
|---|------|--------|-------|--------|
| 1 | 00_Project_Charter.md | Du-An/{{PROJECT_FOLDER}}/ | {{PM_NAME}} | Active |
| 2 | 00_Project_Master_Index.md | Du-An/{{PROJECT_FOLDER}}/ | {{PM_NAME}} | Active |
| 3 | 00_RACI_Matrix.md | Du-An/{{PROJECT_FOLDER}}/ | {{PM_NAME}} | Active |
| 4 | 00_Risk_Issue_Log.md | Du-An/{{PROJECT_FOLDER}}/ | {{PM_NAME}} | Active |
| 5 | 00_Change_Log.md | Du-An/{{PROJECT_FOLDER}}/ | {{PM_NAME}} | Active |
""",
        "00_RACI_Matrix.md": """# RACI Matrix — {{PROJECT_NAME}}

R = Responsible | A = Accountable | C = Consulted | I = Informed

| Deliverable / Activity | {{PM_NAME}} | {{SPONSOR}} | {{COORDINATOR}} |
|------------------------|-------------|-------------|------------------|
| Project Charter | A,R | C | I |
| (Operator điền các deliverable khác) | | | |
""",
        "00_Risk_Issue_Log.md": """# Risk & Issue Log — {{PROJECT_NAME}}

**PM:** {{PM_NAME}} | **Date:** {{DATE}}

## Risks (rủi ro có thể xảy ra)
| ID | Risk | Severity (L/M/H) | Probability (L/M/H) | Mitigation | Owner | Status |
|----|------|------------------|---------------------|-----------|-------|--------|
| R1 | (Mô tả risk — Operator điền) | | | | | Open |

## Issues (vấn đề đã xảy ra)
| ID | Issue | Severity | Impact | Resolution | Owner | Status |
|----|-------|----------|--------|-----------|-------|--------|
| I1 | (Mô tả issue — Operator điền) | | | | | Open |
""",
        "00_Change_Log.md": """# Change Log — {{PROJECT_NAME}}

**PM:** {{PM_NAME}} | **Date:** {{DATE}}

| Date | Change Description | Requested by | Impact | Approved by | Status |
|------|--------------------|--------------|--------|-------------|--------|
| {{DATE}} | Project initiated | {{PM_NAME}} | N/A | {{SPONSOR}} | Approved |
""",
    }
    return defaults.get(template_name, f"# {template_name}\n\n(Template default — Operator điền)")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True, help="Project full name")
    parser.add_argument("--code", default=None, help="Project code (auto-gen if missing)")
    parser.add_argument("--folder", default=None, help="Folder name (auto-gen if missing)")
    parser.add_argument("--pm", required=True, help="Project Manager name")
    parser.add_argument("--sponsor", default=None, help="Sponsor (default = PM)")
    parser.add_argument("--coordinator", default="Trợ lý AI", help="Coordinator")
    parser.add_argument("--template-dir", default=".agents/templates/pmbok", help="PMBOK templates dir")
    parser.add_argument("--workspace-root", default=".", help="Workspace root dir")
    parser.add_argument("--allow-overwrite", action="store_true", help="Overwrite existing folder (DANGEROUS)")
    args = parser.parse_args()

    # Auto-fill defaults
    auto_filled = []
    if not args.code:
        args.code = auto_code(args.name)
        auto_filled.append(f"code (auto-gen: {args.code})")
    if not args.folder:
        args.folder = slugify(args.name)
        auto_filled.append(f"folder (auto-gen: {args.folder})")
    if not args.sponsor:
        args.sponsor = args.pm
        auto_filled.append("sponsor (default=PM_NAME)")
    if args.coordinator == "Trợ lý AI":
        auto_filled.append("coordinator (default='Trợ lý AI')")

    workspace = Path(args.workspace_root).resolve()
    project_dir = workspace / "Du-An" / args.folder
    input_dir = workspace / "Kho-Du-Lieu" / "Du-Lieu-Vao" / args.folder
    output_dir = workspace / "Kho-Du-Lieu" / "Ket-Qua" / args.folder
    registry_path = workspace / "Bang-Dieu-Khien" / "DANH-SACH-DU-AN.md"
    template_dir = workspace / args.template_dir

    # Pre-check folder existence
    if project_dir.exists() and not args.allow_overwrite:
        result = {
            "scaffold_result": "folder_exists",
            "project_folder": str(project_dir),
            "ship_decision": "halt",
            "confidence_level": "high",
            "escalation_needed": True,
            "message": f"Folder {project_dir} đã tồn tại. Dùng --allow-overwrite để force, hoặc đổi --folder.",
        }
        print(json.dumps(result, indent=2, ensure_ascii=False))
        sys.exit(1)

    # Build replacements
    replacements = {
        "PROJECT_NAME": args.name,
        "PROJECT_CODE": args.code,
        "PROJECT_FOLDER": args.folder,
        "DATE": date.today().isoformat(),
        "PM_NAME": args.pm,
        "SPONSOR": args.sponsor,
        "COORDINATOR": args.coordinator,
    }

    # Create folders
    folders_created = []
    for folder in [project_dir, input_dir, output_dir]:
        folder.mkdir(parents=True, exist_ok=True)
        folders_created.append(str(folder.relative_to(workspace)))

    # Clone + hydrate templates
    files_created = []
    template_missing = []
    for template_name in PMBOK_TEMPLATES:
        template_path = template_dir / template_name
        if template_path.exists():
            content = template_path.read_text(encoding="utf-8")
        else:
            content = create_default_template(template_name)
            template_missing.append(template_name)

        hydrated = hydrate_template(content, replacements)
        output_path = project_dir / template_name
        output_path.write_text(hydrated, encoding="utf-8")
        files_created.append({
            "path": str(output_path.relative_to(workspace)),
            "status": "ok",
        })

    # Register in DANH-SACH-DU-AN.md
    registry_updated = False
    try:
        registry_path.parent.mkdir(parents=True, exist_ok=True)
        if not registry_path.exists():
            registry_path.write_text(
                "# DANH SÁCH DỰ ÁN\n\n| Mã | Tên dự án | PM | Sponsor | Ngày khởi tạo | Folder | Status |\n"
                "|----|-----------|-----|---------|---------------|--------|--------|\n",
                encoding="utf-8",
            )
        with registry_path.open("a", encoding="utf-8") as f:
            f.write(
                f"| {args.code} | {args.name} | {args.pm} | {args.sponsor} | {replacements['DATE']} | "
                f"{args.folder} | Active |\n"
            )
        registry_updated = True
    except Exception as e:
        print(f"Warning: registry update failed — {e}", file=sys.stderr)

    # Determine confidence
    if template_missing:
        confidence = "medium"
        message = f"Scaffold OK nhưng {len(template_missing)} template default được dùng (templates dir thiếu): {template_missing}. Operator nên setup `.agents/templates/pmbok/` để có template chính thức."
    else:
        confidence = "high"
        message = "Scaffold success — Operator điền chi tiết business logic vào Charter."

    result = {
        "scaffold_result": "success",
        "project_metadata": {
            "project_name": args.name,
            "project_code": args.code,
            "project_folder": args.folder,
            "pm": args.pm,
            "sponsor": args.sponsor,
            "coordinator": args.coordinator,
            "date_created": replacements["DATE"],
        },
        "files_created": files_created,
        "folders_created": folders_created,
        "registry_updated": registry_updated,
        "templates_used_default": template_missing,
        "auto_filled_fields": auto_filled,
        "ship_decision": "ship",
        "confidence_level": confidence,
        "escalation_needed": False,
        "message": message,
        "next_steps": [
            f"Operator điền chi tiết Business Case vào Du-An/{args.folder}/00_Project_Charter.md",
            f"Khi project running → cần skill quan-ly-du-an-running (chưa build) cho tracking/escalation",
        ],
    }

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
