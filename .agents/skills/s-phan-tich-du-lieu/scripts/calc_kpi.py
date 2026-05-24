#!/usr/bin/env python3
"""
calc_kpi.py — KPI calculator cho skill phan-tich-du-lieu.

Apply KPI catalog của phòng ban MindX, compute primary metrics + trend vs prev period,
highlight 3-5 metric đạt warning threshold.

Usage:
    python calc_kpi.py --data <cleaned.csv> --catalog <domain> [--prev-period <file>]

Catalog options: kd_mkt | back_hr | tech | back_ketoan | default

Output: kpi_results.json
"""

import argparse
import json
import sys
from pathlib import Path

try:
    import pandas as pd
    import numpy as np
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas", "numpy"])
    import pandas as pd
    import numpy as np


KPI_CATALOG = {
    "kd_mkt": {
        "ROAS": {
            "formula": lambda df: df["revenue"].sum() / df["spend"].sum() if "revenue" in df.columns and df["spend"].sum() > 0 else None,
            "target": 4.0,
            "warn_threshold": 2.5,
            "direction": "higher_better",
        },
        "CAC": {
            "formula": lambda df: df["spend"].sum() / df["conversions"].sum() if "conversions" in df.columns and df["conversions"].sum() > 0 else None,
            "target": 500000,
            "warn_threshold": 800000,
            "direction": "lower_better",
        },
        "CTR": {
            "formula": lambda df: df["clicks"].sum() / df["impressions"].sum() if "impressions" in df.columns and df["impressions"].sum() > 0 else None,
            "target": 0.02,
            "warn_threshold": 0.01,
            "direction": "higher_better",
        },
        "conversion_rate": {
            "formula": lambda df: df["conversions"].sum() / df["clicks"].sum() if "clicks" in df.columns and df["clicks"].sum() > 0 else None,
            "target": 0.05,
            "warn_threshold": 0.02,
            "direction": "higher_better",
        },
    },
    "back_hr": {
        "time_to_hire_days": {
            "formula": lambda df: (pd.to_datetime(df["status_date"]) - pd.to_datetime(df["application_date"])).dt.days.mean() if "application_date" in df.columns else None,
            "target": 30,
            "warn_threshold": 45,
            "direction": "lower_better",
        },
        "total_applications": {
            "formula": lambda df: df["candidate_id"].nunique() if "candidate_id" in df.columns else None,
            "target": None,
            "warn_threshold": None,
            "direction": "info",
        },
    },
    "tech": {
        "MTTR_hours": {
            "formula": lambda df: (pd.to_datetime(df["resolved_at"]) - pd.to_datetime(df["opened_at"])).dt.total_seconds().mean() / 3600 if "opened_at" in df.columns else None,
            "target": 24,
            "warn_threshold": 72,
            "direction": "lower_better",
        },
        "total_tickets": {
            "formula": lambda df: df["ticket_id"].nunique() if "ticket_id" in df.columns else None,
            "target": None,
            "warn_threshold": None,
            "direction": "info",
        },
    },
    "back_ketoan": {
        "total_amount": {
            "formula": lambda df: df["amount"].sum() if "amount" in df.columns else None,
            "target": None,
            "warn_threshold": None,
            "direction": "info",
        },
        "transaction_count": {
            "formula": lambda df: df["reference"].nunique() if "reference" in df.columns else None,
            "target": None,
            "warn_threshold": None,
            "direction": "info",
        },
    },
}


def evaluate_status(value, target, warn_threshold, direction):
    """Return: 'ok' | 'warn' | 'critical' | 'info'"""
    if value is None or target is None:
        return "info"
    if direction == "higher_better":
        if value >= target:
            return "ok"
        if value >= warn_threshold:
            return "warn"
        return "critical"
    elif direction == "lower_better":
        if value <= target:
            return "ok"
        if value <= warn_threshold:
            return "warn"
        return "critical"
    return "info"


def compute_kpis(df, catalog_key):
    catalog = KPI_CATALOG.get(catalog_key, {})
    results = []
    for name, spec in catalog.items():
        try:
            value = spec["formula"](df)
            if value is None or (isinstance(value, float) and np.isnan(value)):
                results.append({"name": name, "value": None, "status": "unavailable", "reason": "missing required column"})
                continue
            status = evaluate_status(value, spec.get("target"), spec.get("warn_threshold"), spec.get("direction", "info"))
            results.append({
                "name": name,
                "value": round(float(value), 4) if isinstance(value, (int, float, np.floating)) else value,
                "target": spec.get("target"),
                "warn_threshold": spec.get("warn_threshold"),
                "direction": spec.get("direction"),
                "status": status,
            })
        except Exception as e:
            results.append({"name": name, "value": None, "status": "error", "reason": str(e)})
    return results


def compute_trend(curr_results, prev_results):
    """Match by KPI name, compute % change"""
    prev_map = {r["name"]: r.get("value") for r in prev_results}
    for r in curr_results:
        prev = prev_map.get(r["name"])
        curr = r.get("value")
        if prev is None or curr is None or prev == 0:
            r["trend_pct"] = None
            continue
        r["trend_pct"] = round((curr - prev) / prev * 100, 2)
    return curr_results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="Path to cleaned CSV")
    parser.add_argument("--catalog", default="default", choices=list(KPI_CATALOG.keys()) + ["default"])
    parser.add_argument("--prev-period", default=None, help="Optional path to previous period CSV for trend")
    parser.add_argument("--output", default=None, help="Output JSON path")
    args = parser.parse_args()

    df = pd.read_csv(args.data)

    if args.catalog == "default":
        result = {"warning": "default catalog has no KPI definitions, please specify domain"}
        print(json.dumps(result))
        return

    curr_results = compute_kpis(df, args.catalog)

    if args.prev_period:
        prev_df = pd.read_csv(args.prev_period)
        prev_results = compute_kpis(prev_df, args.catalog)
        curr_results = compute_trend(curr_results, prev_results)

    # Highlight 3-5 metrics with warn/critical status
    highlights = [r for r in curr_results if r["status"] in ("warn", "critical")][:5]

    output = {
        "catalog_applied": args.catalog,
        "rows_analyzed": len(df),
        "kpis": curr_results,
        "highlights": highlights,
        "highlight_count": len(highlights),
    }

    if args.output:
        Path(args.output).write_text(json.dumps(output, indent=2, ensure_ascii=False, default=str))

    print(json.dumps(output, indent=2, ensure_ascii=False, default=str))


if __name__ == "__main__":
    main()
