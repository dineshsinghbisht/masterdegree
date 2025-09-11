import numpy as np

array_1d = np.array([1,10,45,30,2,100])
print(array_1d > 20) # [False False  True  True]
print(~ (array_1d > 20)) # [ True  True False False]
print(array_1d[array_1d > 20]) # [ 45 30 ]
print(array_1d[ ~ (array_1d > 20)]) # [ 1 10]

array_2d = np.array([[10,23,np.nan],100,np.nan,100],[34,56,78])
