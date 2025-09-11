import csv
import pandas as pd
from getpass import getuser

# user = getuser()
# csv_location = f'/home/varpha/dan/private/{user}' + \
#                 f'/exrc_02/data/{user}_prob01_profiles.csv'


# Read input CSV data in dataframe
# df = pd.read_csv(csv_location, dtype=str)
df = pd.read_csv("ah4323_prob01_profiles.csv", dtype=str)


# Split name column into first name and last name columns
name_cols = df["name"].str.split(pat=" ", n=1, expand=True)
df["first name"] = name_cols[0]
df["last name"]  = name_cols[1]

# Split address coloumn into street address and rest address data
addr_cols = df["address"].str.split(pat=r"\s*\n\s*", n=1, expand=True)
df["street address"] = addr_cols[0]

# Split rest adress data into state and postal code columns

# state_zip = addr_cols[1].str.extract(r"([A-Z]{2})\s+(\d{5})")
# df["state"] = state_zip[0]
# df["postal code"] = state_zip[1]

state_postalcode = addr_cols[1].str.split(",", n=1, expand=True)[1]
df["state"] = state_postalcode.str.split().str[0]
df["postal code"] = state_postalcode.str.split().str[1]


# Create dataframe with required coloumns and data
cleaned_df = df[[
    "ssn", "username", "first name", "last name",
    "sex", "street address", "state", "postal code",
    "mail", "birthdate"
]]

# Write to a CSV
cleaned_df.to_csv("cleaned_output.csv", index=False) ## For Debugging Purpose

# Extract the entries where last name begins with the letter A
filtered_df = cleaned_df[cleaned_df['last name'].str.startswith('A')].copy()

# Sort by sex (ladies first) - Print here
print(filtered_df.sort_values(by='sex'))

# Sort by state (alphabetically) - Print here
#print(filtered_df.sort_values(by='state'))

# Sort by age / birthdate (youngest first)
#print(filtered_df.sort_values(by='birthdate', ascending=False))