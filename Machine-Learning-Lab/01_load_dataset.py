"""
Program 1: Loading a Dataset
----------------------------
Reads a CSV file and displays its contents.
"""

import pandas as pd

# Load dataset
data = pd.read_csv("student.csv")

# Display dataset
print("Dataset:")
print(data)
