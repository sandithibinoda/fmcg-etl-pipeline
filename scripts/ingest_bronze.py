import pandas as pd
from datetime import datetime
import os

# ── Config ──────────────────────────────────────────────
RAW_FILE = "data/raw/superstore_sales.csv"
BRONZE_DIR = "data/bronze"
BRONZE_FILE = os.path.join(BRONZE_DIR, "bronze_superstore.csv")

# ── Ingest ──────────────────────────────────────────────
print("=" * 50)
print("BRONZE LAYER — Raw Ingestion")
print("=" * 50)

# Read raw CSV
df = pd.read_csv(RAW_FILE, encoding="latin-1")

print(f"✔ Loaded raw file: {RAW_FILE}")
print(f"✔ Row count      : {len(df)}")
print(f"✔ Columns        : {list(df.columns)}")

# Add metadata columns
df["load_timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
df["source_file"] = os.path.basename(RAW_FILE)

# Save to Bronze layer
os.makedirs(BRONZE_DIR, exist_ok=True)
df.to_csv(BRONZE_FILE, index=False)

print(f"✔ Saved to       : {BRONZE_FILE}")
print("=" * 50)
print("Bronze ingestion complete.")
print("=" * 50)