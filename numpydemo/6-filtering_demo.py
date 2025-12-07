import numpy as np

array_1d = np.array([1,10,45,30,2,100])
print(array_1d > 20) # [False False  True  True False  True]
print(~(array_1d > 20)) # [ True  True False False  True False]
print(array_1d[array_1d > 20]) # [ 45  30 100]
print(array_1d[~(array_1d > 20)]) # [ 1 10  2]
