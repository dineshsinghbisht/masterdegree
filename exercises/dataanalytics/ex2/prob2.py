import csv
import pandas as pd
from getpass import getuser

# user = getuser()
# csv_location = f'/home/varpha/dan/private/{user}' + \
#                 f'/exrc_02/data/{user}_prob02_weather.csv'
csv_location = "ah4323_prob02_weather.csv"

# Load input CSV data into dataframe
df = pd.read_csv(csv_location)

# # Get basic information about data
# print(df.info()) # prints concise summary about DataFrame's structure
# print(df.head()) # prints first five rows - default

##########################################  Data Wrangling  ########################################
# Select only required columns to remove the 'Unnamed' column
df_cleaned = df[["Time", "ParameterName", "ParameterValue"]]

# # Print sample data for debugging
# print(df_cleaned.head())

# Transponse the data from long format to wide format and make 'Time' column to index
# Used Pandas DataFrame method ´pivot()´
df_transposed = df_cleaned.pivot(
    index='Time', columns='ParameterName', values='ParameterValue')

# # Print sample data for debugging
# print(df_transposed.head())

# Reset the index to make 'Time' column back to a regular column instead of the index
df_transposed = df_transposed.reset_index()

# # Print sample data for debugging
# print(df_transposed.head().to_string(index=False)) # To see the transposed data as below
'''
                Time  TG_PT12H_min  rrday  snow  tday  tmax  tmin
2022-02-01T00:00:00Z           NaN   -1.0  25.0  -7.7  -5.3  -8.9
2022-02-01T01:00:00Z           NaN    NaN   NaN   NaN   NaN   NaN
2022-02-01T02:00:00Z           NaN    NaN   NaN   NaN   NaN   NaN
2022-02-01T03:00:00Z           NaN    NaN   NaN   NaN   NaN   NaN
2022-02-01T04:00:00Z           NaN    NaN   NaN   NaN   NaN   NaN
'''

# Drop the columns 'TG_PT12H_min', 'rrday' and 'snow' (Not Needed)
# Used Pandas DataFrame method ´drop()´
df_transposed.drop(columns=["TG_PT12H_min", "rrday",
                   "snow", "tday"], inplace=True)

# # Print sample data for debugging
# print(df_transposed.head())

# Drop rows which contains at least one missing value ie NaN
# Used Pandas DataFrame method `dropna()`
# Used Pandas DataFrame method `copy()` to create true independent copy as a best practice
df_transposed_cleaned = df_transposed.dropna().copy()

# # Print sample data for debugging
# print(df_transposed_cleaned.head())
# print(df_transposed_cleaned.info())

#############################################  Task a)  ###########################################

# Copy the data for "task a" from cleaned data (df_transposed_cleaned)
df_task_a = df_transposed_cleaned.copy()

# Add a new column 'tmax+tmin/2' to store (tmax+tmin)/2 calculation
# Used ´df.loc[:, "col"]' instead of ´df["col"]´ to follow best practices
df_task_a.loc[:, "tmax+tmin/2"] = (df_task_a["tmax"] + df_task_a["tmin"]) / 2

# # Print sample data for debugging
# print(df_task_a.head())

# Calculate the average (mean) and standard deviation for 'tmax+tmin/2' column
# Used Pandas DataFrame methods ´mean()´ to get average and ´std()´ to get standard deviation
tavg_mean = df_task_a["tmax+tmin/2"].mean()
tavg_std = df_task_a["tmax+tmin/2"].std()

# Determine the lower and upper range for one standard deviation away from the mean for 'tmax+tmin/2' column
lower_range = tavg_mean - tavg_std
upper_range = tavg_mean + tavg_std

# Calculate the number of tmax+tmin/2 observations within the range of one standard deviation
# Used boolean masking and `shape` method with slicing to get the required count
observations_within_range = df_task_a[(
    df_task_a["tmax+tmin/2"] >= lower_range) & (df_task_a["tmax+tmin/2"] <= upper_range)].shape[0]

# Get the total number of valid tmax+tmin/2 observations
total_observations = df_task_a.shape[0]

# Calculate the percentage
percentage = (observations_within_range / total_observations) * 100

print(f"{percentage}% of the (tmax+tmin)/2 observations are at most one standard deviation away from the total average of (tmax+tmin)/2")
print()  # print a blank line before next print for better display


############################################  Task b)  ############################################

# Copy the data for "task b" from cleaned data (df_transposed_cleaned)
df_task_b = df_transposed_cleaned.copy()

# Add a new column 'tmax-tmin' to store (tmax - tmin) calculation
# Used ´df.loc[:, "col"]' instead of ´df["col"]´ to follow best practices
df_task_b.loc[:, "tmax-tmin"] = df_task_b["tmax"] - df_task_b["tmin"]

# # Print sample data for debugging
# print(df_task_b.head())

# Find and print top-5 timestamps for the difference between tmax and tmin
# Used Pandas DataFrame method ´sort_values()´ for sorting the data
# Used ´head(5)' to dispay 5 rows
# Used ´to_string(index=False)´ not to display index for better output
print("------------------------------------------------------------------------------")
print("   information of Top-5 timestamps for the difference between tmax and tmin   ")
print("------------------------------------------------------------------------------")
print(df_task_b.sort_values(by=["tmax-tmin"],
      ascending=False).head(5).to_string(index=False))
