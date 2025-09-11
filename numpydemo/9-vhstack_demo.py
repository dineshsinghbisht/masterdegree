## vstack (row-wise) Vs hstack (column-wise)

import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])
c = np.array([[5],[6]])
print("shape of a", a.shape)
print("shape of b", b.shape)
print("shape of c", c.shape)
print("add row to a",np.vstack((a,b))) # 
print("add col to a",np.hstack((a,c))) # 
