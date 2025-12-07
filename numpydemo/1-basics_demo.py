import numpy as np
'''
.dim => dimesion 0, 1 ,2 
.shape => how many rows and colums in array 0, 5, (2,3), (1,2,3)
.dtype => data type for each element in array
.itemsize => size of each element in array
.size => no of elements in array
.nbytes => total size of array
type() => type of numpy array
'''

array_0d = np.array(100)
print(f'value of array_0d: {array_0d}')                     # 100
print(f'type of array_0d: {type(array_0d)}')                # <class 'numpy.ndarray'>
print(f'dimension of array_0d: {array_0d.ndim}')            # 0
print(f'shape of array_0d: {array_0d.shape}')               # ()
print(f'data type of array_0d: {array_0d.dtype}')           # int64
print(f'total size of array_0d: {array_0d.size}')           # 1
print(f'itemsize in array_0d: {array_0d.itemsize}')         # 8
print(f'total size of array_0d: {array_0d.nbytes}')         # 8 (arr.size * arr.itemsize)

array_1d = np.array([1,2,3,4,5])
print(f'value of array_1d: {array_1d}')                     # [1 2 3 4 5]
print(f'type of array_1d: {type(array_1d)}')                # <class 'numpy.ndarray'>
print(f'dimension of array_1d: {array_1d.ndim}')            # 1
print(f'shape of array_1d: {array_1d.shape}')               # (5,)
print(f'type of elements in array_1d: {array_1d.dtype}')    # int64
print(f'total size of array_1d: {array_1d.size}')           # 5
print(f'itemsize of array_1d: {array_1d.itemsize}')         # 8

# array_1d_type = np.array([1,2,3,4,5],dtype='int8') # dtype=np.int8
# array_2d = np.array([[1,2,3],[10,20,30]])
# array_3d = np.array([[[1,2,3],[10,20,30]],[[4,5,6],[100,200,300]]])




# print(f'value of array_2d: {array_2d}')
# print(f'size of array_2d: {array_2d.size}')
# print(f'dimension of array_2d: {array_2d.ndim}')
# print(f'shape of array_2d: {array_2d.shape}')
# print(f'type of array_2d: {array_2d.dtype}')
# print(f'size of array_2d: {array_2d.size}') # 6
# print(f'itemsize of array_2d: {array_2d.itemsize}') # 8 

# print(f'value of array_3d: {array_3d}')
# print(f'dimension of array_3d: {array_3d.ndim}')
# print(f'shape of array_3d: {array_3d.shape}')
# print(f'type of array_3d: {array_3d.dtype}')
