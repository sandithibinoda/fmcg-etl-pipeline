import pandas as pd
from datetime import datetime
import os

# ── Config ───────────────────────────────────────────────
BRONZE_FILE = "data/bronze/bronze_superstore.csv"
SILVER_DIR  = "data/silver"
SILVER_FILE = os.path.join(SILVER_DIR, "silver_superstore.csv")

# ── Load Bronze ──────────────────────────────────────────
print("=" * 50)
print("SILVER LAYER — Cleaning & Transformation")
print("=" * 50)

df = pd.read_csv(BRONZE_FILE, encoding="latin-1")
print(f"✔ Loaded Bronze file : {len(df)} rows")

# ── Step 1: Drop nulls in critical columns ───────────────
critical_cols = ["Sales", "Quantity", "Category", "Order Date"]
before = len(df)
df.dropna(subset=critical_cols, inplace=True)
print(f"✔ Dropped nulls      : {before - len(df)} rows removed")

# ── Step 2: Remove duplicate rows ────────────────────────
before = len(df)
df.drop_duplicates(inplace=True)
print(f"✔ Dropped duplicates : {before - len(df)} rows removed")

# ── Step 3: Standardise Category column ──────────────────
df["Category"] = df["Category"].str.strip().str.title()
print(f"✔ Standardised Category column")

# ── Step 4: Parse Order Date to datetime ─────────────────
df["Order Date"] = pd.to_datetime(df["Order Date"])
print(f"✔ Parsed Order Date to datetime")

# ── Step 5: Derive Year, Month, Day of Week ──────────────
df["Year"]        = df["Order Date"].dt.year
df["Month"]       = df["Order Date"].dt.month
df["Month_Name"]  = df["Order Date"].dt.strftime("%B")
df["Day_of_Week"] = df["Order Date"].dt.strftime("%A")
print(f"✔ Derived Year, Month, Month_Name, Day_of_Week")

# ── Step 6: Derive Revenue column ────────────────────────
df["Revenue"] = df["Quantity"] * df["Unit Price"] if "Unit Price" in df.columns else df["Sales"]
print(f"✔ Derived Revenue column")

# ── Step 7: Filter voided transactions ───────────────────
before = len(df)
df = df[(df["Sales"] > 0) & (df["Quantity"] > 0)]
print(f"✔ Filtered voided rows: {before - len(df)} rows removed")

# ── Save to Silver ───────────────────────────────────────
os.makedirs(SILVER_DIR, exist_ok=True)
df.to_csv(SILVER_FILE, index=False)

print(f"✔ Saved to           : {SILVER_FILE}")
print(f"✔ Final row count    : {len(df)}")
print("=" * 50)
print("Silver transformation complete.")
print("=" * 50)