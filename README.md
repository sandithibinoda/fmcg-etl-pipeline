# FMCG Retail ETL Pipeline — Medallion Architecture

## Overview
End-to-end ETL pipeline simulating a real-world FMCG analytics workflow using a retail superstore dataset of 9,994 transactions. Implements medallion architecture with Bronze, Silver, and Gold layers using Python, Pandas, and DuckDB. Final Gold layer outputs are visualised in a Power BI dashboard.

## Architecture
```
Raw CSV → Bronze Layer → Silver Layer → Gold Layer → Power BI Dashboard
          (Ingestion)    (Cleaning &    (KPI SQL      (Visualisation)
                          Transform)    Aggregations)
```

## Tech Stack
- Python · Pandas · DuckDB · Power BI · SQL

## Project Structure
```
fmcg-etl-pipeline/
├── data/
│   ├── bronze/       # Raw ingested data with metadata
│   ├── silver/       # Cleaned and transformed data
│   └── gold/         # KPI aggregation outputs
├── scripts/
│   ├── ingest_bronze.py       # Bronze layer ingestion
│   ├── transform_silver.py    # Silver layer transformation
│   ├── build_gold.py          # Gold layer KPI aggregations
│   ├── quality_checks.py      # Data quality validation
│   └── run_pipeline.py        # Master pipeline orchestrator
└── docs/
    └── data_dictionary.md     # Gold layer field definitions
```
## KPIs
| # | KPI | Gold File |
|---|---|---|
| 1 | Revenue by Category | gold_revenue_by_category.csv |
| 2 | Revenue by Region | gold_revenue_by_region.csv |
| 3 | Monthly Revenue Trend | gold_monthly_trend.csv |
| 4 | Average Transaction Value | gold_avg_transaction.csv |
| 5 | Top Performing Category | gold_top_category.csv |
| 6 | Revenue by Ship Mode | gold_revenue_by_shipmode.csv |

## Data Quality Checks
7 automated checks across all pipeline layers:
- Null value detection
- Duplicate record detection
- Row count validation (Bronze vs Silver)
- Schema validation
- Data type validation
- Range check (no negative revenue)
- Gold file existence check

## How to Run
1. Clone the repo
2. Install dependencies: `pip install pandas duckdb`
3. Place dataset in `data/raw/superstore_sales.csv`
4. Run the full pipeline: `python scripts/run_pipeline.py`




