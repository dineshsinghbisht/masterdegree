import numpy as np

# # Read entire CSV as strings to create a 2d array
# data = np.genfromtxt("details.csv", delimiter=",", dtype=str)

# print(data)
# print(type(data))
# np.savetxt("output_data.csv", data, delimiter=",", fmt="%s")


data_fm = np.genfromtxt( "details.csv", delimiter=",", names=True, dtype=None, encoding="utf-8" )
print(data_fm)
print(type(data_fm))
print(data_fm.shape)
print(data_fm.dtype)
print(data_fm['name'])
print(data_fm.dtype.names)