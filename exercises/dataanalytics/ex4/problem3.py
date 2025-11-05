import csv
import pandas as pd
from getpass import getuser

# user = getuser()
# csv_location = f'/home/{user}/dan/private/exrc_04/data/{user}_prob3_sales.csv'
csv_location = "ah4323_prob3_sales.csv"

# Load input CSV data contains some (fake) daily sales data
df = pd.read_csv(csv_location)
print(df.head())
print(df.info())
print(df.columns)

# Drop not required cloumns from dataframe ie extract sales and date columns
df = df[["date", "sales"]] 
print(df.head())
print(df.info())
print(df.columns)

# Convert data type of date column
df['date'] = pd.to_datetime(df['date'])
print(df.info())