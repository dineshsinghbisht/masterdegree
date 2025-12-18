'''
axis=0|"index"|"rows"
axis=1|"columns"
how=any|all
'''

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [4, 5, 6],
    'C': [np.nan, np.nan, np.nan]
})
print(df.isnull())
print(df.isnull().any())
print(df.isnull().all())

# #print("Column 'A' has a NaN:", df['A'].isnull().any())
# #print("Column 'C' has all NaNs:", df['C'].isnull().all())

# print(df.isnull().any(axis=1))
# print(df.isnull().all(axis=1))

# df = df.dropna() # Drops a row if at least one column has NaN.
# df = df.dropna(axis=1) # Removes any column that contains at least one NaN.
# df = df.dropna(subset=["Age"]) # Only drops rows where Age is NaN.
# df = df.dropna(subset=["Age", "Salary"]) # 
# df = df.dropna(how="all") # Drop rows where all values are NaN
# df = df.dropna(axis=1, how="all") # Drop cols where all values are NaN

