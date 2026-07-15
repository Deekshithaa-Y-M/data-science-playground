"""
Program 2: Extracting Features and Target Variable
--------------------------------------------------
Separates independent features (X) and target variable (y).
"""

import pandas as pd

# Load dataset
data = pd.read_csv("student.csv")

# Features (all columns except last)
X = data.iloc[:, :-1]

# Target (last column)
y = data.iloc[:, -1]

print("Features:")
print(X)

print("\nTarget:")
print(y)
