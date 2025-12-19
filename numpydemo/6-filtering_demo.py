import numpy as np

# array_1d = np.array([1,10,45,30,2,100])
# print(array_1d > 20) # [False False  True  True False  True]
# print(~(array_1d > 20)) # [ True  True False False  True False]
# print(array_1d[array_1d > 20]) # [ 45  30 100]
# print(array_1d[~(array_1d > 20)]) # [ 1 10  2]

# mask = (array_1d > 10) & (array_1d < 50) # combine conditions using bitwise operators (&, |, ~)
# print(array_1d[mask])

array_2d = np.random.randint(10,100,(2,4))
print(array_2d)
# print(array_2d %2 == 0)
# print(array_2d[array_2d %2 == 0])

# print(array_2d[:, 0] % 2 == 0)
# print(array_2d[array_2d[:, 0] % 2 == 0])

print(array_2d[0, :] % 2 == 0)
print(array_2d[:,array_2d[0, :] % 2 == 0])


# print(np.where(array_2d %2 == 0))
# print(array_2d[np.where(array_2d %2 == 0)])



