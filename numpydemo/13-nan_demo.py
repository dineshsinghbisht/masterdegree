# import numpy as np

# print(np.nan)
# print(type(np.nan)) # <class 'float'>
# print(np.isnan(np.nan))

import numpy as np

a = np.array([[1, 2, np.nan],
              [4, 5, 6],
              [7, np.nan, 9]])
print(~np.isnan(a).any(axis=1)) # its check if there is any nan in a row
print(~np.isnan(a).any(axis=0)) # its check if there is any nan in a column all checks for all all the values in col
print(a[~np.isnan(a).any(axis=1)]) # it drops rows
print(a[:, ~np.isnan(a).any(axis=0)]) # it drops columns

print(a[:,[True, False, True]])
print(np.isnan(a))

'''
import pandas as pd

df = pd.DataFrame([[1, 2, np.nan],
                   [4, 5, 6],
                   [7, np.nan, 9]])

# Drop rows with any NaN
df.dropna(axis=0, how="any")

# Drop columns with any NaN
df.dropna(axis=1, how="any")

# Drop rows with all NaN
df.dropna(axis=0, how="all")

# Drop columns with all NaN
df.dropna(axis=1, how="all")
'''


