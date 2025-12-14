import numpy as np

arr = np.array(["john", "doe"])

vec_upper = np.vectorize(str.upper)

arr_up = vec_upper(arr)
print(arr_up)