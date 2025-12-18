'''
concate
'''


import pandas as pd

df1 = pd.DataFrame({"id": [10, 20],
                    "name": ["Raju", "Hero"]})
print("Value of d1\n",df1)

df2 = pd.DataFrame({"id": [10, 40],
                    "name": ["Hei", "There"]})
print("Value of df2\n", df2)

print(pd.concat([df1, df2], ignore_index=True)) # axis=0|1 (vertical|horizontal)
print(pd.concat([df1, df2], axis = 1, ignore_index=True))