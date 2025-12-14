import numpy as np

array_2d = np.array([[10,8],[4,3],[15,100],])
print(array_2d)
print(np.sort(array_2d))
print(np.sort(array_2d,axis=0)) # down the rows columnwise
print(np.sort(array_2d,axis=1)) # across colum rowwise and its default too
