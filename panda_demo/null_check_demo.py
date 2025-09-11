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

#print("Column 'A' has a NaN:", df['A'].isnull().any())
#print("Column 'C' has all NaNs:", df['C'].isnull().all())

print(df.isnull().any(axis=1))
print(df.isnull().all(axis=1))
