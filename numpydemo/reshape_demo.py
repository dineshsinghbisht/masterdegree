import numpy as np

array_2d = np.array([[1,2,3],[4,5,6]])
print("shape or array array_2d: ", array_2d.shape)

arr = np.arange(0,12)
print("Original array arr is", arr)

reshaped = arr.reshape((3,4))
print("Reshaped array arr", reshaped)

flattened = reshaped.flatten()
print("flattened array", flattened)

raveled = reshaped.ravel() # returns view instead of copy
print("raveled array", raveled)

# Transpose
print("Transpose is", reshaped.T)



