'''
info()
describe()
shape
columns
head()
tail()
read_csv, read_json, read_excel
to_csv, to_json, to_excel
'''

import pandas as pd

# read_csv, read_json, read_excel

dataframe = pd.read_csv("sample_students.csv") # encoding="utf-8" or "latin1"
# print(dataframe)
# print(dataframe.head())
# print(dataframe.tail())


# how many rows and column type of data in column
## info(), describe(), head(), tail(), columns, shape
# print(dataframe.info())

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20 entries, 0 to 19
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   Name    20 non-null     object
 1   Age     20 non-null     int64 
 2   City    20 non-null     object
dtypes: int64(1), object(2)
memory usage: 612.0+ bytes
None
'''

# print(dataframe.describe()) # describe on numeric columns
'''
             Age
count  20.000000
mean   28.950000
std     7.444355
min    19.000000
25%    22.750000
50%    27.500000
75%    36.250000
max    40.000000
'''

## shape, coloumn
# print(dataframe.shape) # (20, 3) does not include header row
# print(dataframe.columns) # list columns

# for col in dataframe.columns:
#     print(col)

## how to select one or multiple cols
subset1 = dataframe["Name"] # This returns Series
subset2 = dataframe[["Name"]] # This returns DataFrame
subset3 = dataframe[["Name","Age"]]
print(f"Subset 1 \n {subset1.head()} \n Subset 2 \n {subset2.head()} \n Subset 3 \n {subset3.head()} ")


dataframe["newcol1"] = 10 # to add new column
# print(dataframe)
dataframe.insert(0, "newcol2", 10) # to add new column
# print(dataframe)
## filters
# subset = df[["col1"] > 80]
# subset = df[(["col1"] > 80) & (df["col22] > 40]
