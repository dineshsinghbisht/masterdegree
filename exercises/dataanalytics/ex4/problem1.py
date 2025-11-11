import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# from getpass import getuser

# user = getuser()
# csv_location_windmill = f'/home/{user}/dan/public/exrc_04/data/windmill_temperature.csv'
# csv_location_fmi = f'/home/{user}/dan/public/exrc_04/data/fmi_temperature.csv'
csv_location_windmill = "windmill_temperature.csv"
csv_location_fmi = "fmi_temperature.csv"

# load the input csv files into pandas dataframe
df_windmill = pd.read_csv(csv_location_windmill)
df_fmi = pd.read_csv(csv_location_fmi)

# # Lets describe and check the data and properties of both the dataframes
# print(df_windmill.info())  # prints concise summary about DataFrame's structure
# print(df_windmill.head())  # prints first five rows - default

# print(df_fmi.info())  # prints concise summary about DataFrame's structure
# print(df_fmi.head())  # prints first five rows - default

# In df_windmill: Reformat the column ´t´ to proper date format for comparison and then set it as a index
df_windmill['t'] = pd.to_datetime(df_windmill['t'], format="%Y %m %d %H:%M:%S")
df_windmill = df_windmill.set_index('t')

# print(df_windmill.head()) # print sample data

# In df_fmi: Create new column ´datetime_str´ by using existing date and time related columns and set it as a index
df_fmi['datetime_str'] = (
    df_fmi['Year'].astype(str) + ' ' +
    df_fmi['Month'].astype(str).str.zfill(2) + ' ' +
    df_fmi['Day'].astype(str).str.zfill(2) + ' ' +
    df_fmi['Time'].astype(str) + ':00' # add seconds to match format with df_windmill['t']
)
df_fmi['datetime'] = pd.to_datetime(df_fmi['datetime_str'], format="%Y %m %d %H:%M:%S")
df_fmi = df_fmi.set_index('datetime')
# print(df_fmi.head()) # print sample data

# Drop not required cloumns from df_fmi dataframe
df_fmi.drop(columns=["Year", "Month", "Day", "Time", "Timezone", "datetime_str"],inplace=True)
# print(df_fmi.head()) # print sample data

# # Check data types for both dataframes before doing resampling with mean() function
# print(df_windmill.dtypes)
# print(df_fmi.dtypes)

# Convert Temperature(degC) to numeric on df_fmi
df_fmi['Temperature(degC)'] = pd.to_numeric(df_fmi['Temperature(degC)'], errors='coerce')
# print(df_windmill.dtypes) # for verification
# print(df_fmi.dtypes) # for verification

# Resample both dataframes with 1h interval to easier comparison
df_windmill_hourly = df_windmill.resample('1h').mean()
df_fmi_hourly = df_fmi.resample('1h').mean()

# print(df_windmill_hourly.head()) # print sample data
# print(df_fmi_hourly.head()) # print sample data

# Cobine the two hours dataseries df_windmill_hourly and df_fmi_hourly
df_combined = pd.DataFrame({
    'windmill': df_windmill_hourly['T_NacOutAir.actual'],
    'fmi': df_fmi_hourly['Temperature(degC)']
}).dropna() # remove the rows where any of the column has NaN

# print(df_combined.head()) # print sample data

results = []

# Loop over possible timezone shifts (±5 hours)
for shift in range(-5, 6):
    corr = df_combined['windmill'].shift(shift).corr(df_combined['fmi'])
    results.append((shift, corr))

# Put results into a DataFrame for easy analysis
df_corr = pd.DataFrame(results, columns=['shift_hours', 'correlation'])
print(df_corr.head())

# Analyse the correlations and find the highest correlation
best_shift = df_corr.loc[df_corr['correlation'].idxmax(), 'shift_hours']
best_corr = df_corr['correlation'].max()

if best_shift > 0:
    relation = f"Windmill data is {abs(best_shift)} hours behind FMI"
elif best_shift < 0:
    relation = f"Windmill data is {abs(best_shift)} hours ahead of FMI"
else:
    relation = "Windmill and FMI timestamps are already aligned (no timezone difference)."

print(f"Best timezone offset: {best_shift:+} hours (correlation={best_corr:.3f}) — {relation}")
