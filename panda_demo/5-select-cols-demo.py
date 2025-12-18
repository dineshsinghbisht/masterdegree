import numpy as np
import pandas as pd

# iloc vs loc

## read csv
df = pd.read_csv("sample_students.csv")
print("Shape is", df.shape)
print("Columns are:", df.columns)
print("Select Name Col only", df[["Name"]]) # Output would be Pandas DataFrame
print("Select Name Col only", df["Name"]) # the output would be Pandas Series
#print("Select Name & Age Col only", df[["Name", "Age"]])

df["Student"] = "Yes"
df['is_less_than_25'] = np.where(df['Age'] < 25, 'Yes', 'No')

print(df)

df_first_col = df.iloc[:, :1]
print("df_first_col is \n", df_first_col)
df_rest_cols = df.iloc[:, 1:]
print(df_rest_cols)

df_last_col = df.iloc[:, -1:]
df_except_last = df.iloc[:, :-1]