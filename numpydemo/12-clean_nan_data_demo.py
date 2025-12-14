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

