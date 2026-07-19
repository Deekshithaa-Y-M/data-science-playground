"""
CSV Statistics Pipeline
-----------------------
Reads a CSV file, extracts numeric columns,
and computes mean, median, and mode for each.
Results are saved into a CSV file.
"""

import pandas as pd
from pathlib import Path

# -----------------------------
# CONFIGURATION
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "data" / "data1.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_FILE = OUTPUT_DIR / "statistics_output.csv"

# -----------------------------
# ETL PIPELINE
# -----------------------------
def extract_data(file_path: Path) -> pd.DataFrame:
    """Extract tabular data from CSV."""
    return pd.read_csv(file_path)

def transform_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """Compute mean, median, and mode for numeric columns."""
    numeric = df.select_dtypes(include="number")
    summary = {
        col: {
            "mean": numeric[col].mean(),
            "median": numeric[col].median(),
            "mode": numeric[col].mode().iloc[0] if not numeric[col].mode().empty else None
        }
        for col in numeric.columns
    }
    return pd.DataFrame(summary)

def load_statistics(summary_df: pd.DataFrame, output_file: Path) -> None:
    """Save statistics to CSV."""
    output_file.parent.mkdir(parents=True, exist_ok=True)
    summary_df.to_csv(output_file, index=True)

# -----------------------------
# MAIN EXECUTION
# -----------------------------
if __name__ == "__main__":
    df = extract_data(INPUT_FILE)
    stats_df = transform_statistics(df)
    load_statistics(stats_df, OUTPUT_FILE)

    print("✅ Statistics computed successfully!\n")
    print(stats_df)
