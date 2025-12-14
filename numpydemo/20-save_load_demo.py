import numpy as np

arr = np.arange(10)
print(arr)
np.save("arr_save.npy",arr)
load_arr = np.load("arr_save.npy")
print("loaded array is", load_arr)