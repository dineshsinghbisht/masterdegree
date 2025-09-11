import numpy as np
import pandas as pd

## read csv
df = pd.read_csv("sample_students.csv")
print("Shape is", df.shape)
print("Columns are:", df.columns)
print(df.head())

df.loc[1,"Name"] = "Robin"
print(df.head())

df["Age"] = df["Age"] + 100
print(df.head())