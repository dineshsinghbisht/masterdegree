import csv
import pandas as pd
from getpass import getuser

# user = getuser()
# csv_location = f'/home/varpha/dan/private/{user}' + \
#                 f'/exrc_02/data/{user}_prob01_profiles.csv'


# Read input CSV data in dataframe
# df = pd.read_csv(csv_location, dtype=str)
df = pd.read_csv("ah4323_prob02_weather.csv")
print(df.head())

# Remove the first unnamed column
df_cleaned = df[ ["Time", "ParameterName", "ParameterValue" ] ]
print(df_cleaned)
df_cleaned.to_csv("clean.csv",index=False, na_rep="NaN")


# Remove the rows contain NaN
df_filtered = df_cleaned.dropna()
print(df_filtered)
df_filtered.to_csv("filtered.csv",index=False, na_rep="NaN")

wide = df_filtered.pivot_table(
    index="Time",
    columns="ParameterName",
    values="ParameterValue",
    aggfunc="first"   # use first if there are duplicates
).reset_index()

# Save to a new CSV
wide.to_csv("filtered_wide.csv", index=False)

# Drop rows where tmax or tmin is missing
valid = wide.dropna(subset=["tmax", "tmin"]).copy()

# Save to a new CSV
valid.to_csv("filtered_valid.csv", index=False)

# Compute (tmax + tmin)/2
valid["t_avg"] = (valid["tmax"] + valid["tmin"]) / 2

# Calculate mean, std, and percentage within ±1 std
mean = valid["t_avg"].mean()
std = valid["t_avg"].std(ddof=1)
percent_within = 100 * valid["t_avg"].between(mean - std, mean + std).mean()

print(f"Percentage within ±1 std: {percent_within:.2f}%")
print(f"Mean: {mean:.2f}, Std: {std:.2f}, Count used: {len(valid)}")