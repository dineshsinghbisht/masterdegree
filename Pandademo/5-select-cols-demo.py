'''
# iloc vs loc
.loc — label-based indexing
df.loc[row_label, column_label]

.iloc — integer position-based indexing

df.iloc[row_position, column_position]
'''

import numpy as np
import pandas as pd


# Read csv file into DataFrame
df = pd.read_csv("sample_students.csv")
# print(df.info())
# print("Shape is", df.shape)
# print("Columns are:", df.columns)
# print("Select Name Col only", df[["Name"]]) # Output would be Pandas DataFrame
# print("Select Name Col only", df["Name"]) # the output would be Pandas Series
# print("Select Name & Age Col only", df[["Name", "Age"]])

df["Student"] = "Yes"
df['is_less_than_25'] = np.where(df['Age'] < 25, 'Yes', 'No')

# print(df.head())
# print(df.iloc[0])
# print(df.iloc[0,1]) # 21

df.iloc[0,2] = np.nan
df.loc[1,"Age"] = np.nan
# print(df.head())
# print(df.info())

df_first_col = df.iloc[:, :1]
# print("df_first_col is \n", df_first_col)
df_rest_cols = df.iloc[:, 1:]
# print(df_rest_cols.head())

df_last_col = df.iloc[:, -1:]
df_except_last = df.iloc[:, :-1]

df = pd.DataFrame({
    "Age": [25, 30],
    "Salary": [50000, 60000],
    "Name": ["Alice", "Bob"],
    "City": ["NY", "LA"],
    "Active": [True, False]
})

numeric_df = df.select_dtypes(include="number")
non_numeric_df = df.select_dtypes(exclude="number")

print(numeric_df)
print(non_numeric_df)

num_cols = df.select_dtypes(include="number").columns
cat_cols = df.select_dtypes(exclude="number").columns
# # print(num_cols,cat_cols)
# print(df[num_cols])
# print(df[cat_cols])
