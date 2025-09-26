import json
import pandas as pd

# Data obtained from sstatfi service in Round 1 Problem-5 => Railway statistics (rtie)
# https://pxdata.stat.fi/PxWeb/pxweb/en/StatFin/StatFin__rtie/statfin_rtie_pxt_12lz.px/

json_data_location = "prob05.json"

# Read the data into a python dict
with open(json_data_location) as handle:
    rtie_data = json.load(handle)

# # Get basic information about data
# print(type(rtie_data))
# print(list(rtie_data.keys()))
# print(list(rtie_data.values()))

# Convert the data into a pandas dataframe using normalisation
# Used Pandas DataFrame method ´json_normalize()´ to flatten JSON data into tabular DataFrame
df = pd.json_normalize(rtie_data, record_path='data')

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

# Explode the 'key' column into two columns
# Used Pandas DataFrame method ´apply()´ as apply(pd.Series) to convert list into separate columns
df[["type_of_locomotive", "year"]] = df["key"].apply(pd.Series)

# Explode the 'values' column into two columns
df[["trainkilometres", "locomotivekilometres"]] = df["values"].apply(pd.Series)

# Drop the cloumns 'key' and 'values' not needed
# Used Pandas DataFrame method ´drop()´ to drop the required columns
df = df.drop(columns=["key", "values"])

# # Get basic information about data post processing it
# print(df.info()) # display concise summary about dataframe
# print(df.head()) # display first five rows by default

# Convert columns 'year', 'trainkilometres' & 'locomotivekilometres' data into numeric form to perform calculations
# Used Pandas DataFrame method ´to_numeric()´ to convert the values to numeric (int/float)
df["year"] = pd.to_numeric(df["year"], errors='coerce')
df["trainkilometres"] = pd.to_numeric(df["trainkilometres"], errors='coerce')
df["locomotivekilometres"] = pd.to_numeric(
    df["locomotivekilometres"], errors='coerce')

# # Check and confirm the information post converting the data
# print(df.info()) # display concise summary about dataframe
# print(df.head()) # display first five rows - default

# # Write to a CSV file for debugging and anlysis purpose
# df.to_csv("prob05_output_report.csv", index=False)

# Group by using 'type_of_locomotive' column and compute average for 'trainkilometres' and 'locomotivekilometres' columns
# Used Pandas DataFrame method ´groupby()´ to summarise with respect to type_of_locomotive
df_summary = (
    df.groupby("type_of_locomotive")[
        ["trainkilometres", "locomotivekilometres"]].mean()
)

# Rename the 'trainkilometres' and 'locomotivekilometres' columns to meaningfule names
# Used Pandas DataFrame method ´rename()´ to rename the column names
df_summary.rename(columns={
    "trainkilometres": "average_train_km_year",
    "locomotivekilometres": "average_locomotive_km_year"
}, inplace=True)


# Sort the data with 'average_train_km_year' column on descending order
# Used Pandas DataFrame method ´sort_values()´ for sorting the data
# Used Pandas DataFrame method `copy()` to create a true independent copy as a best practice
df_final_result = df_summary.sort_values(
    by=["average_train_km_year"], ascending=False).copy()

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

'''
Usage summary (most to least activity)
    - SSS locomotives have the highest usage, averaging about ~50k train km and ~69k locomotive km per year
    - 050 locomotives are next, with roughly ~43k train km and ~53k locomotive km per year
    - 060 locomotives follow, averaging around ~27k train km and ~31k locomotive km per year
    - 070 locomotives show moderate activity, with about ~16k train km and ~22k locomotive km year
    - 010 locomotives record lower usage, roughly ~7k train km and ~15k locomotive km per year
    - 020 locomotives are similar, at about ~5k train km and ~13k locomotive km year
    - 040 locomotives show the least activity, with only ~1.5k train km and ~2k locomotive km per year
'''
