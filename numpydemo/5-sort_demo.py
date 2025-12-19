import numpy as np

array1d = np.random.randint(10,30,6)
print("Original 1D Array")
print(array1d)
print("Sorted 1D Array")
print(np.sort(array1d))


array_2d = np.array([[10,8],[4,3],[15,100],])
print("Original 2D Array")
print(array_2d)
print("Default Sorting")
print(np.sort(array_2d)) # default axis=1
print("Sorting with axis=0")
print(np.sort(array_2d,axis=0)) # down the rows columnwise
print("Sorting with axis=1")
print(np.sort(array_2d,axis=1)) # across colum rowwise and its default too
print("Sorting with axis=None") # it will flatten the array
print(np.sort(array_2d,axis=None)) # across colum rowwise and its default too
