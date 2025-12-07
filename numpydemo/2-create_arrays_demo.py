import numpy as np
'''
.zeros()
.ones()
.full()
.arange()
.eye()
'''

print(np.zeros(5)) # [0. 0. 0. 0. 0.]
array1_2d = np.zeros([2,3])
print(array1_2d)

array2 = np.ones([2,3],dtype='int8')
print(array2)

array3 = np.full([2,3],8)
print(array3)

array4 = np.random.randint(1,3,(3,8))
print(array4)

array5 = np.random.random(5)
print(array5) # [0.30200863 0.83504348 0.95578712 0.30809614 0.94655111]

array6 = np.array([1,2,3,np.nan])
print(array6) # [ 1.  2.  3. nan]

array7 = np.arange(1,11) # arange(start,stop,step)
print(array7) # [ 1  2  3  4  5  6  7  8  9 10]

array8 = np.eye(4) # identity matrix
print(array8)

