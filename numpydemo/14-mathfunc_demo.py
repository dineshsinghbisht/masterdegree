import numpy as np

array_1 = np.array([1,2,3])
array_2 = np.array([1,2,3])
print(array_1 + array_2) # [2 4 6]
print(array_1 + 10) # [11 12 13]

## aggregation

print("sum of array_1 is", np.sum(array_1))
print("mean of array_1 is", np.mean(array_1))
print("median of array_1 is", np.median(array_1))
print("min of array_1 is", np.min(array_1))
print("max of array_1 is", np.max(array_1))
print("Standard deviation is", np.std(array_1)) # Standard deviation is 0.816496580927726
print("Variance is", np.var(array_1)) # Variance is 0.6666666666666666
