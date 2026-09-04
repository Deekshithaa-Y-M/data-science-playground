"""
Handling Missing Values in a Dataset
------------------------------------
Techniques: Drop, Fill (mean), Interpolation
"""

import pandas as pd
from pathlib import Path

# Load dataset
base_dir = Path(__file__).resolve().parent
input_path = base_dir / "data" / "data1.csv"
df = pd.read_csv(input_path)

# Show original missing values
print("Original Missing Values:\n", df.isnull().sum())

# --- Method 1: Drop rows with missing values ---
drop_df = df.dropna()

# --- Method 2: Fill numeric columns with mean ---
fill_df = df.copy()

# Ensure numeric conversion for numeric columns
numeric_columns = fill_df.select_dtypes(include="number").columns
for col in numeric_columns:
    fill_df[col] = pd.to_numeric(fill_df[col], errors='coerce')

# Fill NaN with column mean
for col in fill_df.select_dtypes(include="number").columns:
    fill_df[col] = fill_df[col].fillna(fill_df[col].mean())

# --- Method 3: Linear Interpolation ---
interp_df = df.copy()
interp_df[numeric_columns] = interp_df[numeric_columns].interpolate(method="linear")

# Save outputs beside the input dataset
drop_df.to_csv(base_dir / "drop_output.csv", index=False)
fill_df.to_csv(base_dir / "fill_output.csv", index=False)
interp_df.to_csv(base_dir / "interpolated_output.csv", index=False)

print("Files created: drop_output.csv, fill_output.csv, interpolated_output.csv")
