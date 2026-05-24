#!/usr/bin/env python3
"""
check_project_exists.py — Pre-check helper cho skill quan-ly-du-an.

Kiểm tra folder dự án + registry entry tồn tại trước khi scaffold, return JSON status.

Usage:
    python check_project_exists.py --folder "Ecom-Operation-2026" [--workspace-root .]
    python check_project_exists.py --code "ECOM-2026-001" [--workspace-root .]

Output: JSON {"exists": bool, "conflicts": [...], "recommendation": "..."}
"""

import argparse
import json
import sys
from pathlib import Path


def check_folder_exists(workspace, folder_name):
    """Check if Du-An/{folder_name}/ exists"""
    project_dir = workspace / "Du-An" / folder_name
    input_dir = workspace / "Kho-Du-Lieu" / "Du-Lieu-Vao" / folder_name
    output_dir = workspace / "Kho-Du-Lieu" / "Ket-Qua" / folder_name

    return {
        "project_dir": {"path": str(project_dir.relative_to(workspace)) if project_dir.exists() else str(project_dir), "exists": project_dir.exists()},
        "input_dir": {"path": str(input_dir.relative_to(workspace)) if input_dir.exists() else str(input_dir), "exists": input_dir.exists()},
        "output_dir": {"path": str(output_dir.relative_to(workspace)) if output_dir.exists() else str(output_dir), "exists": output_dir.exists()},
    }


def check_registry_entry(workspace, project_code=None, folder_name=None):
    """Check if project_code or folder_name already registered in DANH-SACH-DU-AN.md"""
    registry_path = workspace / "Bang-Dieu-Khien" / "DANH-SACH-DU-AN.md"
    if not registry_path.exists():
        return {"registry_exists": False, "entry_found": False, "matched_line": None}

    content = registry_path.read_text(encoding="utf-8")
    lines = content.split("\n")
    matched = None
    for line in lines:
        if project_code and project_code in line:
            matched = line.strip()
            break
        if folder_name and folder_name in line:
            matched = line.strip()
            break

    return {
        "registry_exists": True,
        "entry_found": matched is not None,
        "matched_line": matched,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", default=None, help="Project folder name to check")
    parser.add_argument("--code", default=None, help="Project code to check")
    parser.add_argument("--workspace-root", default=".", help="Workspace root dir")
    args = parser.parse_args()

    if not args.folder and not args.code:
        print(json.dumps({
            "error": "Must provide --folder or --code",
            "ship_decision": "halt",
        }, ensure_ascii=False))
        sys.exit(1)

    workspace = Path(args.workspace_root).resolve()
    conflicts = []

    folder_check = None
    if args.folder:
        folder_check = check_folder_exists(workspace, args.folder)
        if folder_check["project_dir"]["exists"]:
            conflicts.append(f"Du-An/{args.folder}/ đã tồn tại")
        if folder_check["input_dir"]["exists"]:
            conflicts.append(f"Kho-Du-Lieu/Du-Lieu-Vao/{args.folder}/ đã tồn tại")
        if folder_check["output_dir"]["exists"]:
            conflicts.append(f"Kho-Du-Lieu/Ket-Qua/{args.folder}/ đã tồn tại")

    registry_check = check_registry_entry(workspace, args.code, args.folder)
    if registry_check["entry_found"]:
        conflicts.append(f"Entry đã có trong DANH-SACH-DU-AN.md: {registry_check['matched_line']}")

    exists = len(conflicts) > 0

    if exists:
        recommendation = (
            "REFUSE scaffold. Options: (a) đổi project_folder hoặc project_code, "
            "(b) explicit confirm với --allow-overwrite trong scaffold_pmbok.py (nguy hiểm, sẽ ghi đè), "
            "(c) cleanup folder cũ trước"
        )
        ship_decision = "halt"
    else:
        recommendation = "Safe to proceed scaffold. Folder + registry entry chưa tồn tại."
        ship_decision = "ship"

    result = {
        "exists": exists,
        "conflicts": conflicts,
        "folder_check": folder_check,
        "registry_check": registry_check,
        "recommendation": recommendation,
        "ship_decision": ship_decision,
        "confidence_level": "high",
        "escalation_needed": exists,
    }

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
