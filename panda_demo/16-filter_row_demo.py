import pandas as pd
import numpy as np

# Create a sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': ['x', 'y', 'z', 'w'],
    'C': [5, 6, 7, 8]
})

print("Original data")
print(df)
# Filter for rows where column 'A' is NaN
nan_rows_df = df[df['A'].isna()]
non_nan_rows_df = df[~(df['A'].isna())]
not_nan_rows_df = df[df['A'].notna()]

print("Rows where column 'A' is NaN:")
print(nan_rows_df)

print("Rows where column 'A' is non NaN:")
print(non_nan_rows_df)

print("Rows where column 'A' is not NaN:")
print(not_nan_rows_df)


# Create a sample DataFrame with NaNs in different columns
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', np.nan, 'David'],
    'Age': [25, 30, 35, np.nan],
    'City': ['New York', np.nan, 'London', 'Paris']
})

print("Original DataFrame:")
print(df)
print("-" * 30)

# Filter for rows where ANY column has a NaN
rows_with_any_nan = df[df.isnull().any(axis=1)]

print("Rows with at least one NaN value:")
print(rows_with_any_nan)

df_no_nulls = df.dropna()
print("Rows with at where no NaN value:")
print(df_no_nulls)
