'''
.loc / drop is used with row lable / index and not position unlike iloc

'''

import numpy as np
import pandas as pd

## read csv
df = pd.read_csv("sample_students.csv")
# print("Shape is", df.shape)
# print("Columns are:", df.columns)

# print("before", df.head())
# print(df)

df = df.drop(5)
# df.drop([0,1,2])
# print(df)
df = df.reset_index(drop=True) # to reset the index and drop prev index else it would become column

# print(df)

df = df.drop(df[df["Age"] < 35].index) # to delete the rows conditionally
print(df)
df = df[df["Age"] >= 25] # clean way to keep the required rows
print(df)