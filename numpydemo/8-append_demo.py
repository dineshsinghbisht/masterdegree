## append vs concatenate
## np.append(arr, values, axis=None)

import numpy as np

array_1d = np.array([6,8,9,])
print(np.append(array_1d,10)) # [ 6  8  9 10]
print(np.append(array_1d,[10,56,7,])) # [ 6  8  9 10 56  7]

print(np.concatenate((array_1d,[34,5]))) ## [10 56  7 34  5] we use tuple to pass the arrays

array_2d = np.array([[1,2,3],[4,5,6]])

import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.append(a, [5, 6])  
# Result: array([1, 2, 3, 4, 5, 6])  # flattened

c = np.append(a, [[5, 6]], axis=0) # default is axis=None
print("c is", c)
'''
c is [[1 2]
 [3 4]
 [5 6]] 
'''

d = np.append(a, [[5], [6]], axis=1)
print("d is", d)
