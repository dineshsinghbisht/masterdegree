import csv
import pandas as pd
from getpass import getuser

# user = getuser()
# csv_location = f'/home/varpha/dan/private/{user}' + \
#                 f'/exrc_02/data/{user}_prob01_profiles.csv'
csv_location = "ah4323_prob01_profiles.csv"

# Load input CSV data into dataframe
df = pd.read_csv(csv_location)

# # Get basic information about data
# print(df.info()) # display concise summary about dataframe
# print(df.head()) # display first five rows - default


################################### Task a) Data Wrangling  #######################################

# # Print sample data for 'name and 'address' columns
# print(df[["name", "address"]].head())

# Split 'name' column into 'first_name' and 'last_name' columns
split_name_col = df["name"].str.split(pat=" ", n=1, expand=True) # 
df["first_name"] = split_name_col[0]
df["last_name"]  = split_name_col[1]

# # Print sample data for debugging
# print(df[["name","first_name", "last_name"]].head())

# Split 'address' column into 'street_address' and rest of the address data
split_addr_cols = df["address"].str.split(pat=r"\s*\n\s*", n=1, expand=True)
df["street_address"] = split_addr_cols[0]

# Split rest adress data into 'state' and 'postal code' columns
state_and_postal_code = split_addr_cols[1].str.split(",", n=1, expand=True)[1]
df["state"] = state_and_postal_code.str.split().str[0]
df["postal_code"] = state_and_postal_code.str.split().str[1]

# # Print sample data for debugging
# print(df[['address','street_address', 'state', 'postal_code']].head())

# Create dataframe with required columns
cleaned_df = df[[
    "ssn", "username", "first_name", "last_name",
    "sex", "street_address", "state", "postal_code",
    "mail", "birthdate"
]]

# # Print sample data for debugging
# print(cleaned_df.head())

# # Write to a CSV file for Debugging Purpose
# cleaned_df.to_csv("cleaned_df_prob01_profiles.csv", index=False)


############################################## Task b) ############################################

# Extract the entries where 'last name' begins with the letter A
filtered_df = cleaned_df[cleaned_df['last_name'].str.startswith('A')].copy()

# # Print sample data for debugging
# print(filtered_df.head())

# Sort by 'sex' column (ladies first) where name begins with the letter A and print result
sorted_by_sex = filtered_df.sort_values(by='sex')
print("--------------------------------------------------------------------------------------------")
print("   All entries where the last name begins with the letter A, sorted by sex (ladies first)   ")
print("--------------------------------------------------------------------------------------------")
print(sorted_by_sex.to_string(index=False)) # `to_string(index=False)` used to print entire dataframe without index column
print() # insert a blank line for better display

# Sort by 'state' column (alphabetically) where name begins with the letter A and print result
sorted_by_state = filtered_df.sort_values(by='state')
print("------------------------------------------------------------------------------------------------")
print("   All entries where the last name begins with the letter A, sorted by state (alphabetically)   ")
print("------------------------------------------------------------------------------------------------")
print(sorted_by_state.to_string(index=False))
print() # insert a blank line for better display

# Sort by 'birthdate' ie age (youngest first) where name begins with the letter A and print result
sorted_by_age = filtered_df.sort_values(by='birthdate', ascending=False)
print("------------------------------------------------------------------------------------------------")
print("    All entries where the last name begins with the letter A, sorted by age (youngest first)    ")
print("------------------------------------------------------------------------------------------------")
print(sorted_by_age.to_string(index=False))
