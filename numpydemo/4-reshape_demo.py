'''
reshape - view
flatten - copy
ravel - view
'''

import numpy as np

array_2d = np.array([[1,2,3],[4,5,6]])
print("shape or array array_2d: ", array_2d.shape) # (2, 3)

arr = np.arange(0,12)
print("Original array arr is", arr)

reshaped = arr.reshape((3,4)) # it returns a view ie if you change the view it will update original array
print("Reshaped array arr", reshaped)
'''
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''

flattened = reshaped.flatten()
print("flattened array", flattened) # [ 0  1  2  3  4  5  6  7  8  9 10 11]

raveled = reshaped.ravel() # its returns view 
print("raveled array", raveled) # [ 0  1  2  3  4  5  6  7  8  9 10 11]

# Transpose
print("Transpose is", reshaped.T)



