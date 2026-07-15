"""
Program 2: Extracting Features and Target Variable
--------------------------------------------------
Separates independent features (X) and target variable (y).
"""

from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR.parent / "data" / "student.csv"

# Load dataset
data = pd.read_csv(DATA_FILE)

# Features (all columns except last)
X = data.iloc[:, :-1]

# Target (last column)
y = data.iloc[:, -1]

print("Features:")
print(X)

print("\nTarget:")
print(y)
