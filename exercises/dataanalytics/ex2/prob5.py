import json
import pandas as pd
import ast

## Data downloaded from sstatfi service => Railway statistics (rtie)
## https://pxdata.stat.fi/PxWeb/pxweb/en/StatFin/StatFin__rtie/statfin_rtie_pxt_12lz.px/ 

json_data_location = "prob05.json"

# Read the data into a python dict
with open(json_data_location) as handle:
    rtie_data = json.load(handle)

# # Get basic information about data
# print(type(rtie_data))
# print(list(rtie_data.keys()))
# print(list(rtie_data.values()))

# Convert the data into a pandas dataframe using normalisation
df = pd.json_normalize(rtie_data, record_path = 'data')

# # Sample data
# print(df.head())
'''
           key          values
0  [SSS, 2005]  [48227, 67559]
1  [SSS, 2006]  [50880, 72020]
2  [SSS, 2007]  [52577, 73336]
3  [SSS, 2008]  [53259, 74901]
4  [SSS, 2009]  [50019, 69244]
'''

# Expand the 'key' column into two columns
df[['type_of_locomotive', 'year']] = pd.DataFrame(df['key'].tolist(), index=df.index)

# Expand the 'values' column into two columns
df[['trainkilometres', 'locomotivekilometres']] = pd.DataFrame(df['values'].tolist(), index=df.index)

# Drop the original list columns if you don’t need them
df = df.drop(columns=['key', 'values'])

# # Get basic information about data post processing it 
# print(df.info()) # display concise summary about dataframe
# print(df.head()) # display first five rows by default

# Convert columns to numeric
df['year']                   = pd.to_numeric(df['year'], errors='coerce')
df['trainkilometres']        = pd.to_numeric(df['trainkilometres'], errors='coerce')
df['locomotivekilometres']   = pd.to_numeric(df['locomotivekilometres'], errors='coerce')

# # Check datatypes for columns now
# print(df.dtypes) # display data types for columnst
# print(df.head()) # display first five rows by default

# # Write to a CSV file for debugging and anlalysis purpose
# df.to_csv("prob05_report.csv", index=False)


# Group by using 'type_of_locomotive' column and compute average per year
df_groupby = (
    df.groupby("type_of_locomotive")[["trainkilometres", "locomotivekilometres"]].mean()
)

# Rename the 'trainkilometres' and 'locomotivekilometres' columns to meaningfule names
df_groupby.rename(columns={
    "trainkilometres": "average_train_km_year",
    "locomotivekilometres": "average_locomotive_km_year"
}, inplace=True)

# # Print to see the affect
# print(df_groupby)

# Sort the data with 'average_train_km_year' column on descending order
df_final_result = df_groupby.sort_values(by = ["average_train_km_year"], ascending=False).copy()

# Print the final outcome which summarise the data
# print(df_final_result)

'''
                    average_train_km_year  average_locomotive_km_year
type_of_locomotive                                                   
SSS                              49667.00                    68715.85
050                              43002.75                    53437.15
060                              26892.60                    31354.00
070                              16110.15                    22083.15
010                               6664.35                    15278.70
020                               5172.65                    13420.70
040                               1491.70                     1858.00

'''
