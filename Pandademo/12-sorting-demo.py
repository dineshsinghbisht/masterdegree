import numpy as np
import pandas as pd

## read csv
df = pd.read_csv("sample_students.csv")
print("Shape is", df.shape)
print("Columns are:", df.columns)
print(df.head())

df.sort_values(by=["Name", "Age"], inplace=True) # ascending=True|False
print(df.head())