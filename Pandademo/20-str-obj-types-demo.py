import pandas as pd

df = pd.DataFrame({
    "obj_col": ["A", None, "C"],
    "str_col": pd.Series(["A", None, "C"], dtype="string")
})

print(df.dtypes)
print(df.info())

df["obj_col"] = df["obj_col"].astype("string")
print(df.info())