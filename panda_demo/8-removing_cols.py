import numpy as np
import pandas as pd

## read csv
df = pd.read_csv("sample_students.csv")
print("Shape is", df.shape)
print("Columns are:", df.columns)

print("before", df.head())

df.drop(columns=["Age"],inplace=True)
print("after") 
print(df.head())