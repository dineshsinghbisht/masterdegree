'''
np.nan, np.isnan, np.nan_to_num
np.inf, np.isinf,
'''

import numpy as np

array_1 = np.array([1,3,4,np.nan,4,np.nan])
print(np.isnan(array_1))
print(np.nan_to_num(array_1))
print(np.nan_to_num(array_1,nan=10))

array_2 = np.array([1,3,4,np.nan,4,np.nan])

arr = np.array([1, np.nan, np.inf, -np.inf])
print(np.isinf(arr))

print(np.nan_to_num(arr, nan=10, posinf=99, neginf=-99))
# [  1.  10.  99. -99.]

array2d = np.random.randint(20,50, (3,4)).astype(float)
array2d[2,3] = np.nan # ValueError: cannot convert float NaN to integer
print(array2d)
print(np.isnan(array2d))
print(array2d[~np.isnan(array2d)])