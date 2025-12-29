import numpy as np
import pandas as pd

## read csv
df = pd.read_csv("sample_students.csv")
print("Shape is", df.shape)
print("Columns are:", df.columns)
print(df.head())


print("Sum of Age",df["Age"].sum())
print("Max of Age",df["Age"].max())
print("Min of Age",df["Age"].min())
print("Min of Age",df["Age"].std())

print(df["Age"].value_counts())
