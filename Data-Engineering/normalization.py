# Import necessary libraries
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pandas as pd

# Load the Iris dataset
iris = datasets.load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)

# Initialize scalers
minmax_scaler = MinMaxScaler()
standard_scaler = StandardScaler()

# Apply Min-Max Scaling
X_min = pd.DataFrame(minmax_scaler.fit_transform(X), columns=X.columns)

# Apply Standard Scaling
X_std = pd.DataFrame(standard_scaler.fit_transform(X), columns=X.columns)

# Display first 5 rows of scaled data
print("Min-Max Scaled:\n", X_min.head())
print("\nStandard Scaled:\n", X_std.head())

# Save scaled datasets to CSV files
X_min.to_csv("iris_minmax.csv", index=False)
X_std.to_csv("iris_standard.csv", index=False)
