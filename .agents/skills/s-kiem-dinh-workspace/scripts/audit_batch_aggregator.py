#!/usr/bin/env python3
"""
MAS Audit Batch Aggregator
===========================
Aggregates findings from Micro-Audit Batches (A, B, C) into a single
consolidated report for Phase 7 (Scoring & Remediation).

Usage:
    python audit_batch_aggregator.py [workspace_path]

Output:
    tmp/audit_aggregate.json

Input Files (all in workspace tmp/):
    - audit_batch_A.json  (Đợt A: Structural & Value Stream)
    - audit_batch_B.json  (Đợt B: Architecture & Governance)
    - audit_batch_C.json  (Đợt C: Runtime & Memory)
    - structural_scan_report.json  (Phase 0: Deterministic Scanner)
"""

import json
import sys
from datetime import datetime
from pathlib import Path

# Fix Windows console encoding for Vietnamese output
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')


def load_batch_file(filepath):
    """Load a JSON batch file. Return empty structure if not found."""
    if filepath.exists():
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"  ⚠️  Warning: Could not parse {filepath.name}: {e}")
            return {"findings": [], "error": str(e)}
    else:
        print(f"  ⚠️  Warning: {filepath.name} not found. Skipping.")
        return {"findings": [], "missing": True}


def aggregate(workspace_path):
    """Aggregate all batch findings into a single report."""
    ws = Path(workspace_path)
    tmp_dir = ws / 'tmp'

    if not tmp_dir.exists():
        print(f"❌ Error: tmp/ directory not found in {ws}")
        sys.exit(1)

    print(f"=== MAS Audit Batch Aggregator ===")
    print(f"Workspace: {ws}")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Define batch files
    batch_files = {
        "phase_0_scanner": tmp_dir / "structural_scan_report.json",
        "batch_A": tmp_dir / "audit_batch_A.json",
        "batch_B": tmp_dir / "audit_batch_B.json",
        "batch_C": tmp_dir / "audit_batch_C.json",
    }

    # Load all batches
    aggregate_data = {
        "meta": {
            "workspace": str(ws),
            "aggregated_at": datetime.now().isoformat(),
            "scanner_version": "3.0.0",
            "batch_sources": {}
        },
        "summary": {
            "total_findings": 0,
            "systemic_halt": 0,
            "local_fix": 0,
            "warnings": 0,
            "batches_loaded": 0,
            "batches_missing": 0
        },
        "all_findings": [],
        "per_batch": {}
    }

    for batch_name, filepath in batch_files.items():
        print(f"  Loading {batch_name}... ", end="")
        data = load_batch_file(filepath)

        if data.get("missing"):
            aggregate_data["summary"]["batches_missing"] += 1
            aggregate_data["meta"]["batch_sources"][batch_name] = "MISSING"
            print("❌ MISSING")
        else:
            aggregate_data["summary"]["batches_loaded"] += 1
            aggregate_data["meta"]["batch_sources"][batch_name] = "LOADED"
            print("✅ LOADED")

        # Extract findings based on format
        findings = []
        if "findings" in data:
            findings = data["findings"]
        elif "scan_results" in data:
            # Phase 0 scanner format
            for check_name, check_data in data.get("scan_results", {}).items():
                for item in check_data.get("items", []):
                    findings.append({
                        "source": f"phase_0_{check_name}",
                        "severity": item.get("severity", "LOCAL-FIX"),
                        "message": item.get("message", ""),
                        "path": item.get("path", ""),
                        "auto_fixable": item.get("auto_fixable", False)
                    })

        # Count severities
        for f in findings:
            sev = f.get("severity", "LOCAL-FIX").upper()
            if "SYSTEMIC" in sev or "HALT" in sev:
                aggregate_data["summary"]["systemic_halt"] += 1
            elif "WARNING" in sev:
                aggregate_data["summary"]["warnings"] += 1
            else:
                aggregate_data["summary"]["local_fix"] += 1

        aggregate_data["summary"]["total_findings"] += len(findings)
        aggregate_data["all_findings"].extend(findings)
        aggregate_data["per_batch"][batch_name] = {
            "finding_count": len(findings),
            "findings": findings
        }

    # Write aggregate report
    output_path = tmp_dir / "audit_aggregate.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(aggregate_data, f, indent=2, ensure_ascii=False)

    # Print summary
    s = aggregate_data["summary"]
    print()
    print("=" * 50)
    print(f"AGGREGATE SUMMARY:")
    print(f"  Batches loaded:  {s['batches_loaded']}/4")
    print(f"  Batches missing: {s['batches_missing']}/4")
    print(f"  Total findings:  {s['total_findings']}")
    print(f"    🔴 SYSTEMIC-HALT: {s['systemic_halt']}")
    print(f"    🟡 LOCAL-FIX:     {s['local_fix']}")
    print(f"    ⚪ WARNING:       {s['warnings']}")
    print(f"Report: {output_path}")
    print()

    if s["batches_missing"] > 0:
        print("⚠️  Some batches are missing. Run the corresponding Đợt first.")
    elif s["systemic_halt"] > 0:
        print("🔴 SYSTEMIC-HALT findings detected. Remediation required before go-live.")
    elif s["total_findings"] > 0:
        print("🟡 LOCAL-FIX findings detected. Auto-heal recommended.")
    else:
        print("✅ All batches PASS. Workspace is audit-clean.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python audit_batch_aggregator.py [workspace_path]")
        sys.exit(1)

    aggregate(sys.argv[1])
