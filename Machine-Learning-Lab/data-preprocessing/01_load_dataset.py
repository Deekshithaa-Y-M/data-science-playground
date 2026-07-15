"""
Program 1: Loading a Dataset
----------------------------
Reads a CSV file and displays its contents.
"""

from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR.parent / "data" / "student.csv"

# Load dataset
data = pd.read_csv(DATA_FILE)

# Display dataset
print("Dataset:")
print(data)
