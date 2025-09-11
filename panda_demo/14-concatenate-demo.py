import pandas as pd

df1 = pd.DataFrame({"id": [10, 20],
                    "name": ["Raju", "Hero"]})
print(df1)

df2 = pd.DataFrame({"id": [10, 40],
                    "name": ["Hei", "There"]})
print(df2)

print(pd.concat([df1, df2], ignore_index=True))