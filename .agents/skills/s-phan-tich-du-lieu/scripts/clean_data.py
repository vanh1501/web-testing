#!/usr/bin/env python3
"""
clean_data.py — Data cleaning pipeline cho skill phan-tich-du-lieu.

Apply 6 cleaning rules per HOOK_INPUT_SCHEMA của phòng ban MindX.

Usage:
    python clean_data.py --input <file.xlsx> --schema <domain> [--output <file>]

Schema options: kd_mkt | back_hr | tech | back_ketoan | default

Output: cleaned CSV + cleaning_log.json
"""

import argparse
import json
import re
import sys
from pathlib import Path

try:
    import pandas as pd
    import numpy as np
except ImportError:
    print("Installing pandas + numpy...", file=sys.stderr)
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas", "openpyxl", "numpy"])
    import pandas as pd
    import numpy as np


SCHEMAS = {
    "kd_mkt": ["date", "campaign_id", "channel", "impressions", "clicks", "conversions", "spend"],
    "back_hr": ["candidate_id", "source", "stage", "application_date", "status_date"],
    "tech": ["ticket_id", "severity", "opened_at", "resolved_at", "category"],
    "back_ketoan": ["transaction_date", "type", "amount", "counterparty", "reference"],
    "default": ["date", "dimension_1", "metric_value"],
}


def normalize_headers(df):
    """Rule 1: lowercase, remove special chars, trim whitespace"""
    df.columns = [
        re.sub(r"[^a-z0-9_]", "_", str(c).lower().strip()).strip("_")
        for c in df.columns
    ]
    return df


def parse_dates(df, date_cols):
    """Rule 2: detect date format → normalize ISO 8601"""
    parsed_log = []
    for col in date_cols:
        if col not in df.columns:
            continue
        before = df[col].iloc[0] if len(df) > 0 else None
        df[col] = pd.to_datetime(df[col], errors="coerce", dayfirst=True)
        parsed_log.append(f"{col}: sample before={before} → after={df[col].iloc[0] if len(df) > 0 else None}")
    return df, parsed_log


def parse_numbers(df, num_cols):
    """Rule 3: strip currency, comma→dot, thousand separator"""
    for col in num_cols:
        if col not in df.columns:
            continue
        if df[col].dtype == object:
            df[col] = df[col].astype(str).str.replace(r"[đ₫$\s]", "", regex=True)
            df[col] = df[col].str.replace(",", "", regex=False)
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def detect_missing(df, key_cols, threshold=0.20):
    """Rule 4: mark NA; >20% missing in key col → warn"""
    warnings = []
    for col in key_cols:
        if col not in df.columns:
            continue
        missing_pct = df[col].isna().sum() / len(df) if len(df) > 0 else 0
        if missing_pct > threshold:
            warnings.append(f"{col}: {missing_pct:.1%} missing (>20%) — recommend supplement data")
    return warnings


def detect_outliers(df, num_cols, sigma=3):
    """Rule 5: values >3σ → flag (NOT remove)"""
    outlier_log = []
    for col in num_cols:
        if col not in df.columns or df[col].dtype == object:
            continue
        mean = df[col].mean()
        std = df[col].std()
        if std == 0 or pd.isna(std):
            continue
        outliers = df[(df[col] - mean).abs() > sigma * std]
        if len(outliers) > 0:
            outlier_log.append({
                "column": col,
                "count": len(outliers),
                "sigma": sigma,
                "values": outliers[col].head(5).tolist(),
            })
    return outlier_log


def dedupe(df, key_cols):
    """Rule 6: dedupe identical key columns, keep latest"""
    if not key_cols:
        return df, 0
    existing_keys = [c for c in key_cols if c in df.columns]
    if not existing_keys:
        return df, 0
    before = len(df)
    df = df.drop_duplicates(subset=existing_keys, keep="last")
    return df, before - len(df)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to .xlsx, .csv, or .tsv")
    parser.add_argument("--schema", default="default", choices=list(SCHEMAS.keys()))
    parser.add_argument("--output", default=None, help="Output cleaned CSV path")
    parser.add_argument("--log", default=None, help="Output cleaning log JSON path")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(json.dumps({"error": f"File not found: {args.input}"}), file=sys.stderr)
        sys.exit(1)

    # Read
    if input_path.suffix.lower() in [".xlsx", ".xls"]:
        df = pd.read_excel(input_path)
    elif input_path.suffix.lower() == ".tsv":
        df = pd.read_csv(input_path, sep="\t")
    else:
        df = pd.read_csv(input_path)

    rows_input = len(df)
    expected_cols = SCHEMAS[args.schema]

    # Cleaning pipeline
    df = normalize_headers(df)
    date_cols = [c for c in expected_cols if "date" in c.lower() or "_at" in c.lower()]
    num_cols = [c for c in df.columns if c not in date_cols and c not in ["channel", "source", "stage", "severity", "category", "type", "counterparty", "reference", "campaign_id", "candidate_id", "ticket_id"]]

    df, date_log = parse_dates(df, date_cols)
    df = parse_numbers(df, num_cols)
    missing_warnings = detect_missing(df, expected_cols)
    outlier_log = detect_outliers(df, num_cols)

    # Dedupe by first 2 expected cols
    key_cols = expected_cols[:2]
    df, dupes_removed = dedupe(df, key_cols)

    rows_after = len(df)

    # Output
    output_path = Path(args.output) if args.output else input_path.parent / f"{input_path.stem}_cleaned.csv"
    df.to_csv(output_path, index=False)

    log = {
        "input_file": str(input_path),
        "output_file": str(output_path),
        "schema_applied": args.schema,
        "rows_input": rows_input,
        "rows_after_cleaning": rows_after,
        "dupes_removed": dupes_removed,
        "date_parse_log": date_log,
        "missing_warnings": missing_warnings,
        "outliers_flagged": outlier_log,
        "expected_columns_found": [c for c in expected_cols if c in df.columns],
        "expected_columns_missing": [c for c in expected_cols if c not in df.columns],
    }

    log_path = Path(args.log) if args.log else output_path.parent / "cleaning_log.json"
    log_path.write_text(json.dumps(log, indent=2, ensure_ascii=False, default=str))

    print(json.dumps(log, indent=2, ensure_ascii=False, default=str))


if __name__ == "__main__":
    main()
