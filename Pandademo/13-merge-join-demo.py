import pandas as pd

df1 = pd.DataFrame({"id": [10, 20],
                    "name": ["Raju", "Hero"]})
print(df1)

df2 = pd.DataFrame({"id": [10, 40],
                    "age": [100, 40]})

print(df2)

# df_merge = pd.merge(df1, df2, on = ["id"], how = "inner")
# df_merge = pd.merge(df1, df2, on = ["id"], how = "outer")
# df_merge = pd.merge(df1, df2, on = ["id"], how = "left")
# df_merge = pd.merge(df1, df2, on = ["id"], how = "right")
df_merge = pd.merge(df1, df2, how = "cross")

print("Merge OutPut")
print(df_merge)