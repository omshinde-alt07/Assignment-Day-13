Part D 
1. Exact Prompt Used
Write a Python function that takes a Pandas DataFrame and generates an automated data quality report including:
shape, dtypes, missing values percentage, duplicate rows, unique value counts per column, and basic stats.
Return the report as a dictionary and also print a formatted summary.
Handle possible edge cases such as empty DataFrames or columns with all null values.
2. AI-Generated Code
import pandas as pd

def data_quality_report(df):

    report = {}

    if df.empty:
        print("DataFrame is empty.")
        return {"message": "Empty DataFrame"}

    report["shape"] = df.shape

    report["dtypes"] = df.dtypes.astype(str).to_dict()

    report["missing_percent"] = (
        (df.isnull().sum() / len(df)) * 100
    ).to_dict()

    report["duplicate_rows"] = int(df.duplicated().sum())

    report["unique_counts"] = df.nunique().to_dict()

    numeric_cols = df.select_dtypes(include="number")

    if not numeric_cols.empty:
        report["basic_stats"] = numeric_cols.describe().to_dict()
    else:
        report["basic_stats"] = {}

    report["memory_usage_mb"] = (
        df.memory_usage(deep=True).sum() / (1024 * 1024)
    )

    print("\nDATA QUALITY REPORT")
    print("----------------------")
    print(f"Shape: {report['shape']}")
    print(f"Duplicate Rows: {report['duplicate_rows']}")
    print(f"Memory Usage: {report['memory_usage_mb']:.2f} MB")

    print("\nColumn Types")
    for col, dtype in report["dtypes"].items():
        print(f"{col}: {dtype}")

    print("\nMissing Values (%)")
    for col, val in report["missing_percent"].items():
        print(f"{col}: {val:.2f}%")

    print("\nUnique Values per Column")
    for col, val in report["unique_counts"].items():
        print(f"{col}: {val}")

    return report
3. Testing the Function
Test 1 — Clean DataFrame
import pandas as pd

df_clean = pd.DataFrame({
    "name": ["A", "B", "C", "D"],
    "age": [23, 25, 27, 29],
    "salary": [40000, 45000, 50000, 52000]
})

report1 = data_quality_report(df_clean)
Expected Output
Shape: (4,3)
Duplicate Rows: 0

Missing Values:
name: 0%
age: 0%
salary: 0%

Unique values:
name: 4
age: 4
salary: 4
Test 2 — Messy DataFrame
df_messy = pd.DataFrame({
    "name": ["Alice", "Bob", None, "Bob"],
    "age": [25, None, 25, 25],
    "salary": [50000, 60000, None, 60000],
    "constant_col": [1,1,1,1]
})

report2 = data_quality_report(df_messy)
Expected Output
Shape: (4,4)

Duplicate Rows: 1

Missing Values:
name: 25%
age: 25%
salary: 25%

Unique Values:
constant_col: 1

This shows:

Missing values

Duplicate rows

A constant column (constant_col) with only one unique value.

4. Critical Evaluation (≈200 Words)

The generated function provides a useful automated data quality report that summarizes important dataset characteristics such as shape, data types, missing value percentages, duplicate rows, and unique value counts. It also calculates descriptive statistics for numeric columns and reports memory usage using the df.memory_usage() function. This makes it helpful for quickly understanding the structure and potential issues in a dataset before deeper analysis.

The function handles some edge cases effectively. For example, it checks if the DataFrame is empty and returns a message instead of raising an error. However, while it calculates missing value percentages, it does not explicitly flag columns that contain only null values. These columns could be automatically detected and marked as unusable features.

Another limitation is that although unique value counts are provided, the function does not automatically identify columns with only a single unique value. Such constant columns are often useless for modeling and should ideally be highlighted in the report.