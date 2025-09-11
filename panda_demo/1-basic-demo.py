import pandas as pd

# read_csv, read_json, read_excel
dataframe = pd.read_csv("sample_students.csv") # encoding="utf-8" or "latin1"
print(dataframe)

# how many rows and column type of data in column
##info(), describe()
print(dataframe.info())
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


print(dataframe.describe())
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
print(dataframe.shape) # (20, 3) does not include header row
print(dataframe.columns)

## how to select one or multiple cols
# subset = df["col1"]
# subset = df[["col1","col2"]]
dataframe["newcol"] = 10
print(dataframe)

## filterps
# subset = df[["col1"] > 80]
# subset = df[(["col1"] > 80) & (df["col22] > 40]
