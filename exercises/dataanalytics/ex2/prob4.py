import pandas as pd
from getpass import getuser

# user = getuser()
# csv_location = f'/home/varpha/dan/private/{user}' + \
#                 f'/exrc_02/data/{user}_prob04_weather.csv'
csv_location = "ah4323_prob04_weather.csv"

# Load input CSV data related to old weather data from Jyväskylä 1959-2021
df = pd.read_csv(csv_location)

# # Get basic information about data
# print(df.info()) # prints concise summary about DataFrame's structure
# print(df.head()) # prints first five rows - default

# Create new 'Date' column by combinining 'Year, 'Month' and 'Day' columns
# Used Pandas DataFrame method ´to_datetime()´ to create valid calendar date as CCYY-MM-DD
df["Date"] = pd.to_datetime(df[["Year", "Month", "Day"]])

# Extract only 'Date' and 'Snow depth (cm)' columns
df = df[["Date", "Snow depth (cm)"]].copy()

# # Print sample data and information about dataframe for debugging
# print(df.head())
# print(df.info())  # There are Null entries in 'Snow depth (cm)' column


# Replace -1 with 0 on 'Snow depth (cm)' column
# Used Pandas DataFrame method ´replace()´ to replace value of -1 to 0
df["Snow depth (cm)"] = df["Snow depth (cm)"].replace(-1, 0)

# Fill missing values in 'Snow depth (cm)' column with previous day's snow depth
# Used Pandas DataFrame method ´ffill()´
# Used .ffill() instead of .fillna(method="ffill") since later one is depricated
df["Snow depth (cm)"] = df["Snow depth (cm)"].ffill()

# # Confirm no Null / NaN entries
# print(df.info()) # No Null entries anymore


# Define function to assign winter season as follow
# Sept–Dec -> winter belongs to (year)–(year+1)
# Jan–Aug -> winter belongs to (year-1)–year
def assign_winter(date):
    if date.month >= 9:
        return f"{date.year}-{date.year+1}"
    else:
        return f"{date.year-1}-{date.year}"


# Create new column 'Winter' in the form of (year)-(year+1)
# Used Pandas DataFrame method ´apply()´ to call custom function ´assign_winter()´ get the required value
df["Winter"] = df["Date"].apply(assign_winter)

# # Print sample data for debugging
# print(df.head())

# Keep only data where winters 1959 through 2020 as per requirement
# Used Pandas DataFrame method ´isin()´ to filter the data
valid_winters = [f"{y}-{y+1}" for y in range(1959, 2020)]
# print("valid winters", valid_winters)
df = df[df["Winter"].isin(valid_winters)]

# # Print sample data for debugging
# print(df.head())  # print first 5 rows
# print(df.tail())  # print last 5 rows

# Group the match information at each winter range level
# Used Pandas DataFrame method ´groupby()´ to groupby at ´Winter´ column
snow_stats = df.groupby("Winter").agg(
    # Create a new column ´Snow_sum´ with sum of snow depth
    Snow_sum=("Snow depth (cm)", "sum"),
    # Create column ´count´ count of days where snow depth has been positive
    count=("Snow depth (cm)", lambda x: (x > 0).sum()),
    # Create column ´max´ with max snow depth of the winter
    max=("Snow depth (cm)", "max")
)

# # Print sampe data for debugging
# print(snow_stats.head())

# Create new column ´rank´ to store rank for all the Winter
# Used Pandas DataFrame method ´rank()´ on ´Snow_sum´ coloumn
# ´ascending=False´ used so largest Snow sum get 1st rank
# ´method="min"´ used if there’s a tie, give all tied values the smallest rank number they could take
# ´astype(int)´ used to covert the float into int since ´rank()´ output is float by default
snow_stats["rank"] = snow_stats["Snow_sum"].rank(
    ascending=False, method="min")

# Reorder columns as the per the requirement
snow_stats = snow_stats[["Snow_sum", "rank", "count", "max"]]

# # Print sample data for debugging
# print(snow_stats.head()) # Found float value for ´Snow_sum´, 'rank' and 'max' columns

# Convert the values to int for ´Snow_sum´, 'rank' and 'max' columns
# Used Pandas DataFrame method ´astype()´ method to convert floats to integers
snow_stats[["Snow_sum", "rank", "max"]] = snow_stats[[
    "Snow_sum", "rank", "max"]].astype(int)

# # Print sampe data for debugging
# print(snow_stats.head())

# print(snow_stats.to_string())  # to print the full data as ouput

# Print first and last 3 winters as shown in the Problem 5
print(snow_stats.head(3))
print("...")
print(snow_stats.tail(3))
