# Machine Learning Lab

## Practical 01: Data Preprocessing

This practical is now notebook-based and GitHub-friendly.

- Notebook: `notebooks/01_data_preprocessing.ipynb`
- Input data: `data/sample_input.csv`

The notebook performs:

- missing value handling for numerical columns using mean imputation,
- missing value handling for categorical columns using mode imputation,
- duplicate row removal, and
- output checks for features, target, null counts, and duplicates.

## How to run

1. Clone the repository.
2. Open the project in VS Code (or Jupyter environment).
3. Install dependency:

```bash
pip install pandas
```

4. Open `Machine-Learning-Lab/notebooks/01_data_preprocessing.ipynb`.
5. Run all cells.

The notebook uses relative path detection so it can find `data/sample_input.csv`
when run from either the repository root or the `notebooks` folder.