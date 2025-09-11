import numpy as np
import pandas as pd


## read csv
df = pd.read_csv("sample_students.csv")
print("Shape is", df.shape)
print("Columns are:", df.columns)
#print("Select Name Col only", df[["Name"]])
#print("Select Name & Age Col only", df[["Name", "Age"]])

df["Student"] = "Yes"
df['is_less_than_25'] = np.where(df['Age'] < 25, 'Yes', 'No')

print(df)
