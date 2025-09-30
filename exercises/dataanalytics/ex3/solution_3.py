import csv
import pandas as pd

# Load input CSV data related to public city bicycles into pandas DataFrame
df_bicycles = pd.read_csv("exrc03p01_bicycles.csv")

# # Get basic information about data
df_bicycles.info() # prints concise summary about DataFrame's structure
print(df_bicycles.head()) # prints first five rows - default

# '''
# Bicycle data observations
# total 1442 rows 
# No Null values for Month, Day and Hour columns, all are types on integer
# No Null value for Sammonpuistikko city data
# '''

# Load input CSV data related to hourly weather observations into pandas DataFrame
df_weather = pd.read_csv("exrc03p01_weather.csv")
# # Get basic information about data
df_weather.info() # prints concise summary about DataFrame's structure
print(df_weather.head()) # prints first five rows - default

'''
Bicycle data observations
total 1464 rows 
No Null values for month, day, time
month and day coloumns values are integer
Time column values are object type
'''

# Convert the 'Time' column value to int format
df_weather["time"] = df_weather["time"].str.split(":").str[0].astype(int)

# Print sample weather data for debugging
df_weather.info() # prints concise summary about DataFrame's structure
print(df_weather.head()) # prints first five rows - default

# Print Column names of both dataframe to find merging columns
print("Columns in df_bicycles DataFrame:", df_bicycles.columns)
print("Columns in df_weather DataFrame:", df_weather.columns)

# Rename coloumn names for df_weather with df_bicyles for merge operation
df_weather = df_weather.rename(columns={"month":"Month", "day":"Day", "time":"Hour"})

# Print column names for debugging
print("Columns in df_bicycles DataFrame:", df_bicycles.columns)
print("Columns in df_weather DataFrame:", df_weather.columns)


# Merge dataframes df_bicyles and df_weather
# Used merge function with with how=outer option to combine the data
df_merged = pd.merge(df_bicycles, df_weather, on=["Month", "Day", "Hour"], how="outer", indicator = True )
print(df_merged.head())
print(df_merged.tail())
print(df_merged.columns)
df_merged.info()

