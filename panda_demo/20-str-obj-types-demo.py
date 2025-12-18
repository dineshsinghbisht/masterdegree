import pandas as pd

df = pd.DataFrame({
    "obj_col": ["A", None, "C"],
    "str_col": pd.Series(["A", None, "C"], dtype="string")
})

print(df.dtypes)
print(df.info())

# df["cat_cols"] = df[cat_cols].astype("string")
