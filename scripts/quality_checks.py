import pandas as pd
import os

# ── Config ───────────────────────────────────────────────
BRONZE_FILE = "data/bronze/bronze_superstore.csv"
SILVER_FILE = "data/silver/silver_superstore.csv"
GOLD_DIR    = "data/gold"

print("=" * 50)
print("DATA QUALITY CHECKS")
print("=" * 50)

results = []

# ── Load all layers ──────────────────────────────────────
bronze = pd.read_csv(BRONZE_FILE, encoding="latin-1")
silver = pd.read_csv(SILVER_FILE, encoding="latin-1")

# ── Check 1: Null check ──────────────────────────────────
bronze_nulls = bronze.isnull().sum().sum()
silver_nulls = silver.isnull().sum().sum()
status = "✔ PASS" if silver_nulls == 0 else "✘ FAIL"
results.append(("Null Check (Silver)", status, f"{silver_nulls} nulls found"))
print(f"{status} — Null Check     : {silver_nulls} nulls in Silver layer")

# ── Check 2: Duplicate check ─────────────────────────────
bronze_dups = bronze.duplicated().sum()
silver_dups = silver.duplicated().sum()
status = "✔ PASS" if silver_dups == 0 else "✘ FAIL"
results.append(("Duplicate Check (Silver)", status, f"{silver_dups} duplicates found"))
print(f"{status} — Duplicate Check: {silver_dups} duplicates in Silver layer")

# ── Check 3: Row count validation ────────────────────────
status = "✔ PASS" if len(silver) <= len(bronze) else "✘ FAIL"
results.append(("Row Count Validation", status, f"Bronze={len(bronze)}, Silver={len(silver)}"))
print(f"{status} — Row Count       : Bronze={len(bronze)}, Silver={len(silver)}")

# ── Check 4: Schema validation ───────────────────────────
expected_cols = ["Sales", "Quantity", "Category", "Order Date", "Region",
                 "Year", "Month", "Month_Name", "Day_of_Week", "Revenue"]

missing_cols  = [c for c in expected_cols if c not in silver.columns]
status = "✔ PASS" if not missing_cols else "✘ FAIL"
results.append(("Schema Validation", status, f"Missing: {missing_cols}"))
print(f"{status} — Schema Check    : {len(missing_cols)} missing columns {missing_cols}")

# ── Check 5: Data type validation ────────────────────────
status = "✔ PASS" if silver["Sales"].dtype in ["float64", "int64"] else "✘ FAIL"
results.append(("Data Type Check (Sales)", status, str(silver["Sales"].dtype)))
print(f"{status} — Data Type Check : Sales column dtype = {silver['Sales'].dtype}")

# ── Check 6: Range check — no negative revenue ───────────
negative_rev = (silver["Revenue"] < 0).sum()
status = "✔ PASS" if negative_rev == 0 else "✘ FAIL"
results.append(("Range Check (Revenue)", status, f"{negative_rev} negative values"))
print(f"{status} — Range Check     : {negative_rev} negative Revenue values")

# ── Check 7: Gold files exist ────────────────────────────
gold_files = [
    "gold_revenue_by_category.csv",
    "gold_revenue_by_region.csv",
    "gold_monthly_trend.csv",
    "gold_avg_transaction.csv",
    "gold_top_category.csv",
    "gold_revenue_by_shipmode.csv"
]
missing_gold = [f for f in gold_files if not os.path.exists(os.path.join(GOLD_DIR, f))]
status = "✔ PASS" if not missing_gold else "✘ FAIL"
results.append(("Gold Files Exist", status, f"Missing: {missing_gold}"))
print(f"{status} — Gold Files Check: {len(missing_gold)} missing files {missing_gold}")

# ── Summary ──────────────────────────────────────────────
print("=" * 50)
passed = sum(1 for r in results if "PASS" in r[1])
failed = sum(1 for r in results if "FAIL" in r[1])
print(f"SUMMARY: {passed} passed / {failed} failed out of {len(results)} checks")
print("=" * 50)