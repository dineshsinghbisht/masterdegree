## np.split, np.hsplit, np.vsplit

import numpy as np

arr_1 = np.array([1,2,3,4,5,6,])
arr_2, arr_3 = np.split(arr_1,2)
print(arr_2)
print(arr_3)

print(np.hsplit(arr_1,2))
## print(np.vsplit(arr_1,2)) # ValueError: vsplit only works on arrays of 2 or more dimensions