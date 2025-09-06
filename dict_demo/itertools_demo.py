# itertools.groupby(iterable, key=None)

from itertools import groupby

data = [1, 1, 2, 2, 2, 3, 1, 1]
print(list(groupby(data)))

for key, group in groupby(data):
    print(key, list(group))


words = ["apple", "ant", "bat", "ball", "cat"]

# Group by first letter
for key, group in groupby(sorted(words), key=lambda x: x[0]):
    print(key, list(group))