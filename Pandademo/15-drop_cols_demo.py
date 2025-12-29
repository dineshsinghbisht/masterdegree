# import pandas as pd

# df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# # Drop a single column by name
# df = df.drop('B', axis=1)
# print(df)

# # Drop multiple columns by name
# df = df.drop(['A', 'C'], axis=1) # no need to mention axis=1 its implied
# print(df)

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, 3], 
    'B': [4, np.nan, 6], 
    'C': [7, 8, 9],
    'D': [10, np.nan, 12]
})

print(df.columns)
# Find columns with at least one NaN
print(df)
print(df.isnull().any()) # this columnwise operations
print(df.isnull()) # this checks null for each entry

cols_with_nan = df.columns[df.isnull().any()]

print("cols with nan")
print(cols_with_nan)

# # Drop those columns
# df = df.drop(cols_with_nan, axis=1)

# print(df)