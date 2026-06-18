"""
Handling Missing Values in a Dataset
------------------------------------
Techniques: Drop, Fill (mean), Interpolation
"""

import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("student.csv")

# Show original missing values
print("Original Missing Values:\n", df.isnull().sum())

# --- Method 1: Drop rows with missing values ---
drop_df = df.dropna()

# --- Method 2: Fill numeric columns with mean ---
fill_df = df.copy()

# Ensure numeric conversion for relevant columns
for col in ['Age', 'Marks', 'Attendance']:
    fill_df[col] = pd.to_numeric(fill_df[col], errors='coerce')

# Fill NaN with column mean
for col in fill_df.select_dtypes(include="number").columns:
    fill_df[col].fillna(fill_df[col].mean(), inplace=True)

# --- Method 3: Linear Interpolation ---
interp_df = df.copy()
interp_df.interpolate(method="linear", inplace=True)

# Save outputs
drop_df.to_csv("drop_output.csv", index=False)
fill_df.to_csv("fill_output.csv", index=False)
interp_df.to_csv("interpolated_output.csv", index=False)

print("Files created: drop_output.csv, fill_output.csv, interpolated_output.csv")
