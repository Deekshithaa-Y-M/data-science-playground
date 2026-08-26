# Data Preprocessing

This practical demonstrates the basic cleaning steps used before training a
machine learning model:

- remove duplicate observations;
- fill missing numeric values with the column mean;
- fill missing categorical values with the most frequent value; and
- convert categorical features to numeric one-hot encoded columns.

## Run the program

From the repository root:

```bash
pip install pandas
python Machine-Learning-Lab/data-preprocessing/03_data_preprocessing.py
```

The program reads `Machine-Learning-Lab/data/student.csv`, uses `Marks` as the
target column, and prints the cleaned features and target. Paths are built from
the script location, so the command also works after cloning the repository.

To use another dataset, update `DATA_FILE` and `TARGET_COLUMN` near the top of
`03_data_preprocessing.py`.