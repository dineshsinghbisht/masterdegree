import numpy as np
'''
.dim => dimesion 0, 1 ,2 
.shape => 
.dtype => 
.itemsize 
'''

array_0d = np.array(100)
array_1d = np.array([1,2,3,4,5])
array_1d_type = np.array([1,2,3,4,5],dtype='int8')
array_2d = np.array([[1,2,3],[10,20,30]])
array_3d = np.array([[[1,2,3],[10,20,30]],[[4,5,6],[100,200,300]]])

print(f'value of array_0d: {array_0d}')
print(f'dimension of array_0d: {array_0d.ndim}') # 0
print(f'shape of array_0d: {array_0d.shape}') # ()
print(f'data type of array_0d: {array_0d.dtype}') # int64
print(f'size of array_0d: {array_0d.size}') # 1
print(f'itemsize of array_0d: {array_0d.itemsize}') # 8

print(f'value of array_1d: {array_1d}')
print(f'dimension of array_1d: {array_1d.ndim}')
print(f'shape of array_1d: {array_1d.shape}')
print(f'type of array_1d: {type(array_1d)}') # type of array_1d: <class 'numpy.ndarray'>,
print(f'type of elements array_1d: {array_1d.dtype}')

print(f'value of array_2d: {array_2d}')
print(f'size of array_2d: {array_2d.size}')
print(f'dimension of array_2d: {array_2d.ndim}')
print(f'shape of array_2d: {array_2d.shape}')
print(f'type of array_2d: {array_2d.dtype}')
print(f'size of array_2d: {array_2d.size}') # 6
print(f'itemsize of array_2d: {array_2d.itemsize}') # 8 

print(f'value of array_3d: {array_3d}')
print(f'dimension of array_3d: {array_3d.ndim}')
print(f'shape of array_3d: {array_3d.shape}')
print(f'type of array_3d: {array_3d.dtype}')
