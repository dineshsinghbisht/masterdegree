import numpy as np

array_1d = np.array([10,20,40,50,60])
print(array_1d[0])
print(array_1d[::-1])
print(array_1d[[1,4]]) # fancy indexing


# array_2d = np.array([[1,2,3,4,5,6,7,8,9,10],[10,20,30,40,50,60,70,80,90,100]])
# print(array_2d[1,5])

# print(array_2d[1,5:7])
# print(array_2d[1,range(5,7)])
# print(array_2d[1,np.s_[5,7]])

# print(array_2d[0, :]) # to get specific row
# print(array_2d[:, 2]) # to get specific col



