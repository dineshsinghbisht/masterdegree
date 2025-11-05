import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# from getpass import getuser

# user = getuser()
# csv_location_windmill = f'/home/{user}/dan/public/exrc_04/data/windmill_temperature.csv'
# csv_location_fmi = f'/home/{user}/dan/public/exrc_04/data/fmi_temperature.csv'
csv_location_windmill = "windmill_temperature.csv"
csv_location_fmi = "fmi_temperature.csv"

# load the input data into pandas dataframe
df_windmill = pd.read_csv(csv_location_windmill)
df_fmi = pd.read_csv(csv_location_fmi)

# Parse windmill timestamps
df_windmill['t'] = pd.to_datetime(df_windmill['t'], format="%Y %m %d %H:%M:%S")
df_windmill = df_windmill.set_index('t')
print(df_windmill.head())


# Build and parse FMI timestamps with the same format as windmill 
df_fmi['datetime_str'] = (
    df_fmi['Year'].astype(str) + ' ' +
    df_fmi['Month'].astype(str).str.zfill(2) + ' ' +
    df_fmi['Day'].astype(str).str.zfill(2) + ' ' +
    df_fmi['Time'].astype(str) + ':00' # add seconds to match format
)
df_fmi['datetime'] = pd.to_datetime(df_fmi['datetime_str'], format="%Y %m %d %H:%M:%S")
df_fmi = df_fmi.set_index('datetime')
print(df_fmi.head())

# Drop not required cloumns from df_fmi
df_fmi.drop(columns=["Year", "Month", "Day", "Time", "Timezone", "datetime_str"],inplace=True)
print(df_fmi.head())

# Check data types for both dataframes before doing resampling with mean()
print(df_windmill.dtypes)
print(df_fmi.dtypes)

# Convert Temperature(degC) to numeric
df_fmi['Temperature(degC)'] = pd.to_numeric(df_fmi['Temperature(degC)'], errors='coerce')
print(df_windmill.dtypes)
print(df_fmi.dtypes)


# --- 4. Resample both to hourly means ---
df_windmill_hourly = df_windmill.resample('1h').mean()
df_fmi_hourly = df_fmi.resample('1h').mean()

print(df_windmill_hourly.head())
print(df_fmi_hourly.head())


df_combined = pd.DataFrame({
    'windmill': df_windmill_hourly['T_NacOutAir.actual'],
    'fmi': df_fmi_hourly['Temperature(degC)']
}).dropna()

print(df_combined.head())

results = []

# Loop over possible timezone shifts (±5 hours)
for shift in range(-5, 6):
    corr = df_combined['windmill'].shift(shift).corr(df_combined['fmi'])
    results.append((shift, corr))

# Put results into a DataFrame for easy analysis
df_corr = pd.DataFrame(results, columns=['shift_hours', 'correlation'])

# Find best
best_shift = df_corr.loc[df_corr['correlation'].idxmax(), 'shift_hours']
best_corr = df_corr['correlation'].max()

print(f"✅ Best timezone offset: {best_shift:+} hours (correlation={best_corr:.3f})")