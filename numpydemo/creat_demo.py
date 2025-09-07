import numpy as np

array1 = np.zeros([2,3])
print(array1)

array2 = np.ones([2,3],dtype='int8')
print(array2)

array3 = np.full([2,3],8)
print(array3)


array4 = np.random.randint(1,3,(3,8))
print(array4)

array5 = np.array([1,2,3,np.nan])
print(array5)