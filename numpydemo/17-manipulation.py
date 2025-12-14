## arrays are fixed size unlike list
## insert, delete 
## append, concantenate
## vstack, hstack
## split, hsplit, vsplit

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


arr = np.arange(6)
print(np.split(arr,2))

arr = np.random.random(5)
print("Randon array is", arr)
print("brodcast is ", arr * 2)
print("After broadcasting array is", arr)

print(np.array([1,2,3] * np.array([4,2])))