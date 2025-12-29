import numpy as np
import pandas as pd

## read csv
df = pd.read_csv("sample_students.csv")
print("Shape is", df.shape)
print("Columns are:", df.columns)

df["Student"] = "Yes"
df['is_less_than_25'] = np.where(df['Age'] < 25, 'Yes', 'No')
print(df.head())

df.insert(0,"Id", df["Age"]*20) ## insert(loc, "colname", value)
print(df.head())

df.rename(columns={
    "Id": "IDCol", 
    "Student": "student"
    },
    inplace=True
)
print(df.columns)

'''
df = df.rename(index={
    0: "row_1",
    1: "row_2"
})
'''