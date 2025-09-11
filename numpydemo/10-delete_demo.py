import numpy as np
array_1d = np.array([92,3,4,6,])
print(np.delete(array_1d,0))

array_2d = np.array([[1,2],[3,4]])
print(np.delete(array_2d,0)) # it flattens the array
print(np.delete(array_2d,0,axis=0)) # deletes the rows
print(np.delete(array_2d,0,axis=1)) # deletes the cols

import numpy as np

arr = np.arange(1, 13).reshape(4, 3)  # 4 rows, 3 cols
print("Original array:\n", arr)

# Delete rows 1 and 3 (0-based indexing)
new_arr = np.delete(arr, [1, 3], axis=0)
print("After deleting rows 1 and 3:\n", new_arr)

## Both let you delete continuous slices without listing indices manually
np.delete(arr, range(1,4), axis=0)  # same as np.s_[1:4]
np.delete(arr, np.s_[1,4], axis=0)  # same as range(1,4)
