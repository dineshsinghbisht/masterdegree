import numpy as np

a = np.array([[1,2,3,4,5,6,7,8,9,10],[10,20,30,40,50,60,70,80,90,100]])
print(a[1,5])
print(a[1,5:7])
print(a[0, :]) # to get specific row
print(a[:, 2]) # to get specific col
