import numpy as np

array_1d = np.array([1,2,3,4,5,6,7,9,10])

print("even array using where", array_1d[np.where(array_1d % 2 == 0)]) # this is similar to fancy indexing
print("calculated array using where", np.where(array_1d % 2 == 0, array_1d*2, array_1d))
print(np.where(array_1d % 2 == 0))

## fancy indexing
indexes = [0,4,5]
print("Fancy indexing", array_1d[indexes])


array2d = np.random.randint(20,50, (3,4))
print(array2d)
print(array2d[array2d % 2 == 0])
print(array2d[np.where(array2d % 2 == 0)])

print(np.where(array2d % 2 == 0, "Even", "Odd"))
