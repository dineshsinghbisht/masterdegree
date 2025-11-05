#import csv
import pandas as pd
from getpass import getuser

# user = getuser()
# csv_location = f'/home/{user}/dan/private/exrc_04/data/{user}_prob3_sales.csv'
csv_location = "ah4323_prob3_sales.csv" 

# Load input CSV data which contains some (fake) daily sales data
df = pd.read_csv(csv_location)

# Lets try to describe and check the data
print("Display some useeful information about data")
print("*******************************************")
print(df.info())  # prints concise summary about DataFrame's structure
print("*******************************************")
print(df.columns) # prints information about columns
print("*******************************************")
print(df.head())  # prints first five rows - default
print("*******************************************")
# Extract sales and date columns only which are needed
df = df[["date", "sales"]]

# Cehck the columns again
print("Print the df columns")
print(df.columns)

# Convert data type of date column currently its object
df['date'] = pd.to_datetime(df['date'])
print(df.info())