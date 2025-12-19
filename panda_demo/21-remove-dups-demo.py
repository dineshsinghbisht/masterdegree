import pandas as pd

df = pd.DataFrame({
    "A": [1, 2, 2, 3],
    "B": ["x", "y", "y", "z"]
})

df_no_dupes = df.drop_duplicates()
print(df)
print(df_no_dupes)

'''
df_no_dupes = df.drop_duplicates(subset=["A"])
df_no_dupes = df.drop_duplicates(subset=["A", "B"])
df.drop_duplicates(keep="first")   # default
df.drop_duplicates(keep="last")
df_no_dupes = df.drop_duplicates(keep=False)
df.drop_duplicates(inplace=True)
df_no_dupes = df.drop_duplicates().reset_index(drop=True)

'''