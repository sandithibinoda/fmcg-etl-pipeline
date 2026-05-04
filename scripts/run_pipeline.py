import subprocess
import sys
from datetime import datetime

def run_stage(stage_name, script_path):
    print(f"\n{'=' * 50}")
    print(f"RUNNING: {stage_name}")
    print(f"Started : {datetime.now().strftime('%H:%M:%S')}")
    print(f"{'=' * 50}")
    
    result = subprocess.run(
        [sys.executable, script_path],
        capture_output=False
    )
    
    if result.returncode == 0:
        print(f"\n✔ {stage_name} completed successfully")
    else:
        print(f"\n✘ {stage_name} FAILED — stopping pipeline")
        sys.exit(1)

# ── Run Pipeline ─────────────────────────────────────────
print("\n" + "=" * 50)
print("FMCG ETL PIPELINE — Full Run")
print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 50)

run_stage("Bronze Layer — Raw Ingestion",         "scripts/ingest_bronze.py")
run_stage("Silver Layer — Cleaning & Transform",  "scripts/transform_silver.py")
run_stage("Gold Layer — KPI Aggregations",        "scripts/build_gold.py")
run_stage("Data Quality Checks",                  "scripts/quality_checks.py")

print("\n" + "=" * 50)
print("✔ PIPELINE COMPLETE")
print(f"Finished: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 50)