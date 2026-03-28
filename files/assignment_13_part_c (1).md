

------------------------------------------------------------------------

# Table of Contents

1.  Conceptual Question -- `.loc[]` vs `.iloc[]`
2.  CSV Analysis Function
3.  Debugging Exercise

------------------------------------------------------------------------

# 1. Conceptual Question: `.loc[]` vs `.iloc[]`

## `.loc[]` (Label-Based Indexing)

`.loc[]` selects rows and columns **based on labels**.

Characteristics:

-   Uses **index labels**
-   End index is **inclusive**
-   Accepts **boolean conditions**

### Example

``` python
import pandas as pd

df = pd.DataFrame(
    {"A": [10,20,30,40,50]},
    index=[0,1,2,3,4]
)

df.loc[0:3]
```

### Output

  Index   A
  ------- ----
  0       10
  1       20
  2       30
  3       40

Rows **0,1,2,3** are returned because `.loc` includes the end label.

------------------------------------------------------------------------

## `.iloc[]` (Position-Based Indexing)

`.iloc[]` selects rows and columns based on **integer position**.

Characteristics:

-   Uses **numeric positions**
-   End index is **exclusive**
-   Follows **Python slicing rules**

### Example

``` python
df.iloc[0:3]
```

### Output

  Index   A
  ------- ----
  0       10
  1       20
  2       30

Rows **0,1,2** are returned because the end index is excluded.

------------------------------------------------------------------------

## Comparison

  Feature      `.loc[]`      `.iloc[]`
  ------------ ------------- ------------------
  Type         Label based   Position based
  Index type   Labels        Integer position
  End index    Inclusive     Exclusive

------------------------------------------------------------------------

## Case 1: Index = `[0,1,2,3,4]`

  Code             Result
  ---------------- --------------
  `df.loc[0:3]`    rows 0,1,2,3
  `df.iloc[0:3]`   rows 0,1,2

------------------------------------------------------------------------

## Case 2: Index = `['a','b','c','d','e']`

Example DataFrame:

``` python
df = pd.DataFrame(
    {"A":[10,20,30,40,50]},
    index=['a','b','c','d','e']
)
```

  Code                Result
  ------------------- ------------
  `df.loc['a':'c']`   rows a,b,c
  `df.iloc[0:3]`      rows a,b,c

Important distinction:

-   `.loc` uses **labels**
-   `.iloc` uses **positions**

------------------------------------------------------------------------

# 2. CSV Analysis Function

The function below loads a CSV file, prints a quick dataset overview,
and returns useful dataset metadata.

## Code

``` python
import pandas as pd

def analyze_csv(filepath):

    df = pd.read_csv(filepath)

    print("First 5 rows")
    print(df.head())

    print("\nDataset Info")
    df.info()

    print("\nSummary Statistics")
    print(df.describe())

    print("\nColumns")
    print(df.columns)

    print("\nShape")
    print(df.shape)

    print("\nMissing Values")
    print(df.isnull().sum())

    num_rows = df.shape[0]
    num_cols = df.shape[1]

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    categorical_cols = df.select_dtypes(exclude="number").columns.tolist()

    null_counts = df.isnull().sum().to_dict()

    memory_mb = df.memory_usage(deep=True).sum() / (1024 * 1024)

    return {
        "num_rows": num_rows,
        "num_cols": num_cols,
        "numeric_cols": numeric_cols,
        "categorical_cols": categorical_cols,
        "null_counts": null_counts,
        "memory_mb": memory_mb
    }
```

------------------------------------------------------------------------

## Example Usage

``` python
report = analyze_csv("data.csv")
print(report)
```

### Example Output

    {
      'num_rows': 500,
      'num_cols': 6,
      'numeric_cols': ['price','quantity'],
      'categorical_cols': ['product','category'],
      'null_counts': {'price':0,'category':2},
      'memory_mb': 0.23
    }

------------------------------------------------------------------------

# 3. Debugging Exercise

## Original Code with Bugs

``` python
import pandas as pd
 
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "salary": [50000, 60000, 70000]
})
 
# Bug 1: Wrong operator for compound condition
high_earners = df[df["age"] > 25 and df["salary"] > 55000]
 
# Bug 2: Chained indexing for assignment
df["age"][0] = 26
 
# Bug 3: iloc with inclusive end expectation
first_two = df.iloc[0:2]
print(f"Got {len(first_two)} rows, expected 3")
```

------------------------------------------------------------------------

## Bug 1: Incorrect Logical Operator

Problem:

`and` cannot be used with pandas Series.

Correct approach:

``` python
high_earners = df[(df["age"] > 25) & (df["salary"] > 55000)]
```

Explanation:

`&` performs **element-wise logical AND** for pandas Series.

------------------------------------------------------------------------

## Bug 2: Chained Indexing

Problem:

    df["age"][0] = 26

This can cause a **SettingWithCopyWarning**.

Correct approach:

``` python
df.loc[0, "age"] = 26
```

Reason:

`.loc` safely updates the original DataFrame.

------------------------------------------------------------------------

## Bug 3: Incorrect `.iloc` Expectation

Problem:

    df.iloc[0:2]

Returns only **rows 0 and 1**.

Correct code:

``` python
first_three = df.iloc[0:3]
print(f"Got {len(first_three)} rows, expected 3")
```

Explanation:

`.iloc` slicing excludes the end index.

------------------------------------------------------------------------

# Corrected Final Code

``` python
import pandas as pd
 
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "salary": [50000, 60000, 70000]
})
 
# Fix 1
high_earners = df[(df["age"] > 25) & (df["salary"] > 55000)]
 
# Fix 2
df.loc[0, "age"] = 26
 
# Fix 3
first_three = df.iloc[0:3]

print(f"Got {len(first_three)} rows, expected 3")
```

------------------------------------------------------------------------

# Conclusion

This assignment demonstrates:

-   Understanding of **Pandas indexing (`.loc` vs `.iloc`)**
-   Ability to perform **basic dataset analysis**
-   Knowledge of **data types and missing values**
-   Practical **debugging of common pandas mistakes**
