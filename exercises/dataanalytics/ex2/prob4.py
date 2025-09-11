import pandas as pd
from getpass import getuser

# user = getuser()
# csv_location = f'/home/varpha/dan/private/{user}' + \
#                 f'/exrc_02/data/{user}_prob04_weather.csv'
csv_location = "ah4323_prob04_weather.csv"

# Load input CSV data into dataframes
df = pd.read_csv(csv_location)

# # Get basic information about data
# print(df.info()) # display concise summary about dataframe
# print(df.head()) # display first five rows - default

# Create 'Date' column by combinining 'Year, 'Month', 'Day' cloumns
df["Date"] = pd.to_datetime(df[["Year", "Month", "Day"]])

# Extract only 'Date' and 'Snow depth (cm)' columns
df = df[["Date", "Snow depth (cm)"]].copy()

# # Print sample data and information about dataframe
# print(df.head())
# print(df.info()) ## There are Null entries in 'Snow depth (cm)' column

# Replace -1 with 0 on 'Snow depth (cm)' column
df["Snow depth (cm)"] = df["Snow depth (cm)"].replace(-1, 0)

# Fill missing values in 'Snow depth (cm)' column with previous day's snow depth
df["Snow depth (cm)"] = df["Snow depth (cm)"].ffill()

# Confirm no Null / NaN entries
print(df.info())


# Function to assign winter season
def assign_winter(date):
    if date.month >= 9:  # Sept–Dec -> winter belongs to year–year+1
        return f"{date.year}-{date.year+1}"
    else:  # Jan–Aug -> winter belongs to year-1–year
        return f"{date.year-1}-{date.year}"

df["Winter"] = df["Date"].apply(assign_winter)

# Keep winters 1959–1960 through 2019–2020
valid_winters = [f"{y}-{y+1}" for y in range(1959, 2020)]
df = df[df["Winter"].isin(valid_winters)]

# Group and calculate statistics
snow_stats = df.groupby("Winter").agg(
    Snow_sum=("Snow depth (cm)", "sum"),
    Count=("Snow depth (cm)", lambda x: (x > 0).sum()),
    Max=("Snow depth (cm)", "max")
)

# Add ranking (largest snow sum = rank 1)
snow_stats["Rank"] = snow_stats["Snow_sum"].rank(ascending=False, method="min").astype(int)

# Reorder columns
snow_stats = snow_stats[["Snow_sum", "Rank", "Count", "Max"]]

# Show first and last 3 winters
print(snow_stats.head(3))
print("...")
print(snow_stats.tail(3))
