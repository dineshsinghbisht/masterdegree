import csv
from getpass import getuser
import pandas as pd
import matplotlib.pyplot as plt

# user = getuser()
# csv_location = f'/home/{user}/dan/private/exrc_04/data/{user}_prob3_sales.csv'
csv_location = "ah4323_prob3_sales.csv" 

# Load input CSV data which contains some (fake) daily sales data
df = pd.read_csv(csv_location)

# # Lets describe and check the data and properties of dataframe
# print(df.info())  # prints concise summary about DataFrame's structure
# print(df.columns) # prints information about columns
# print(df.head())  # prints first five rows - default

# Extract ´sales´ and ´date´ columns only which are needed
df = df[["date", "sales"]]

# # Check the columns again)
# print(df.columns)

# Convert data type of date column currently its object
df['date'] = pd.to_datetime(df['date'])

print(df.info()) # check the data types for columns again

# index the dataframe by the´date' column
df = df.set_index('date')
print(df.head())

# using **resample** and **sum**, downsample the data from daily to a monthly frequency
df_monthly_sales = df.resample('ME').sum() # Aggregates the sales upto end of each month
print(df_monthly_sales.head())

df_monthly_sales_shifted = df_monthly_sales.shift(1)
print(df_monthly_sales_shifted.head())
print(df_monthly_sales_shifted.to_string())

stats = df_monthly_sales_shifted['sales'].describe()
print("\nDescriptive statistics of shifted monthly sales:")
print(stats)

# # --- 6) Plot a sales curve (shifted monthly totals) ---
# plt.figure(figsize=(10, 5))
# plt.plot(df_monthly_sales_shifted.index, df_monthly_sales_shifted['sales'], marker='+',)
# plt.title("Monthly Sales (Report Month Reflects PREVIOUS Month's Sales)")
# plt.xlabel("Report Month (month-end)")
# plt.ylabel("Sales")
# plt.grid(True)
# plt.tight_layout()
# plt.show()
