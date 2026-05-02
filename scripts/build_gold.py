import duckdb
import pandas as pd
import os

# ── Config ───────────────────────────────────────────────
SILVER_FILE = "data/silver/silver_superstore.csv"
GOLD_DIR    = "data/gold"

print("=" * 50)
print("GOLD LAYER — KPI Aggregations")
print("=" * 50)

# ── Load Silver into DuckDB ──────────────────────────────
con = duckdb.connect()
con.execute(f"CREATE TABLE silver AS SELECT * FROM read_csv_auto('{SILVER_FILE}')")
print(f"✔ Loaded Silver into DuckDB")

os.makedirs(GOLD_DIR, exist_ok=True)

# ── KPI 1: Revenue by Category ───────────────────────────
kpi1 = con.execute("""
    SELECT Category,
           ROUND(SUM(Sales), 2)        AS total_revenue,
           COUNT(*)                    AS total_orders
    FROM silver
    GROUP BY Category
    ORDER BY total_revenue DESC
""").df()
kpi1.to_csv(f"{GOLD_DIR}/gold_revenue_by_category.csv", index=False)
print(f"✔ KPI 1 saved: gold_revenue_by_category.csv")

# ── KPI 2: Revenue by Region ─────────────────────────────
kpi2 = con.execute("""
    SELECT Region,
           ROUND(SUM(Sales), 2)        AS total_revenue,
           COUNT(*)                    AS total_orders
    FROM silver
    GROUP BY Region
    ORDER BY total_revenue DESC
""").df()
kpi2.to_csv(f"{GOLD_DIR}/gold_revenue_by_region.csv", index=False)
print(f"✔ KPI 2 saved: gold_revenue_by_region.csv")

# ── KPI 3: Monthly Revenue Trend ─────────────────────────
kpi3 = con.execute("""
    SELECT Year, Month, Month_Name,
           ROUND(SUM(Sales), 2)        AS total_revenue
    FROM silver
    GROUP BY Year, Month, Month_Name
    ORDER BY Year, Month
""").df()
kpi3.to_csv(f"{GOLD_DIR}/gold_monthly_trend.csv", index=False)
print(f"✔ KPI 3 saved: gold_monthly_trend.csv")

# ── KPI 4: Average Transaction Value ─────────────────────
kpi4 = con.execute("""
    SELECT ROUND(AVG(Sales), 2) AS avg_transaction_value
    FROM silver
""").df()
kpi4.to_csv(f"{GOLD_DIR}/gold_avg_transaction.csv", index=False)
print(f"✔ KPI 4 saved: gold_avg_transaction.csv")

# ── KPI 5: Top Performing Category ───────────────────────
kpi5 = con.execute("""
    SELECT Category,
           ROUND(SUM(Sales), 2) AS total_revenue
    FROM silver
    GROUP BY Category
    ORDER BY total_revenue DESC
    LIMIT 1
""").df()
kpi5.to_csv(f"{GOLD_DIR}/gold_top_category.csv", index=False)
print(f"✔ KPI 5 saved: gold_top_category.csv")

# ── KPI 6: Revenue by Ship Mode ──────────────────────────
kpi6 = con.execute("""
    SELECT "Ship Mode",
           ROUND(SUM(Sales), 2)        AS total_revenue,
           COUNT(*)                    AS total_orders
    FROM silver
    GROUP BY "Ship Mode"
    ORDER BY total_revenue DESC
""").df()
kpi6.to_csv(f"{GOLD_DIR}/gold_revenue_by_shipmode.csv", index=False)
print(f"✔ KPI 6 saved: gold_revenue_by_shipmode.csv")

print("=" * 50)
print("Gold aggregations complete.")
print("=" * 50)