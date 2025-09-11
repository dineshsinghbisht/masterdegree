import numpy as np

arr_float = np.array([1.4, 2.6, 3.2])
arr_int= arr_float.astype(int)
print(arr_int) # [1 2 3]
print(arr_int.dtype)