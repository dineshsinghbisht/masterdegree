## arrays are fixed size unlike list
import numpy as np

array_1d = np.array([10,23,46]) 
print(np.insert(array_1d,1,100)) # np.insert(array_name,index,value,axis=None|0|1)

array_2d = np.array([[10,23,46],[1,2,3]]) 
print(array_2d)
print(array_2d.shape)


# insert a new row at index 1
print(np.insert(array_2d,1,[1,3,5],axis=0))

# insert a new col at index 1
print(np.insert(array_2d,1,[3,5],axis=1))