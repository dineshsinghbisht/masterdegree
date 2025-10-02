import csv
import pandas as pd
from getpass import getuser

# user = getuser()
# csv_location = f'/home/varpha/dan/private/{user}' + \
#                 f'/exrc_02/data/{user}_prob01_profiles.csv'
csv_location = "ah4323_prob01_profiles.csv"

# Load input CSV data related to user profiles into pandas DataFrame
df = pd.read_csv(csv_location)

# Load input CSV data related to hourl weather observations into pandas DataFrame
df_weather = pd.read_csv(csv_location)

# # Get basic information about data
# print(df.info()) # prints concise summary about DataFrame's structure
# print(df.head()) # prints first five rows - default

################################### Task a) Data Wrangling  ########################################

# # Print sample data for 'name' and 'address' columns
# print(df[["name", "address"]].head())

# Split 'name' column into 'first_name' and 'last_name' columns
# Used string's ´split()´ method
split_name_col = df["name"].str.split(pat=" ", n=1, expand=True)
df["first_name"] = split_name_col[0]
df["last_name"] = split_name_col[1]

# # Print sample data for debugging post splitting the 'name' column
# print(df[["name", "first_name", "last_name"]].head())

# Split 'address' column into 'street_address' and rest of the address data.
split_addr_cols = df["address"].str.split(pat=r"\s*\n\s*", n=1, expand=True)
df["street_address"] = split_addr_cols[0]

# Split rest adress data into 'state' and 'postal code' columns
state_and_postal_code = split_addr_cols[1].str.split(",", n=1, expand=True)[1]
df["state"] = state_and_postal_code.str.split().str[0]
df["postal_code"] = state_and_postal_code.str.split().str[1]

# # Print sample data for debugging post splitting the 'address' column
# print(df[['address','street_address', 'state', 'postal_code']].head())

# Create cleaned dataframe with required columns
cleaned_df = df[[
    "ssn", "username", "first_name", "last_name",
    "sex", "street_address", "state", "postal_code",
    "mail", "birthdate"
]]

# # Print sample cleaned data for debugging post extracting the required columns
# print(cleaned_df.head())

############################################## Task b) #############################################

# Extract the entries where 'last name' begins with the letter A
# Used strings' ´startswith()´ method
filtered_df = cleaned_df[cleaned_df["last_name"].str.startswith('A')].copy()

# # Print sample data for debugging
# print(filtered_df.head())

# Sort by 'sex' column (ladies first) where name begins with the letter A and print result
# Used Pandas DataFrame method ´sort_values()´ for sorting the data
sorted_by_sex = filtered_df.sort_values(by='sex')

print("--------------------------------------------------------------------------------------------")
print("   All entries where the last name begins with the letter A, sorted by sex (ladies first)   ")
print("--------------------------------------------------------------------------------------------")
# set Index to False not display 'index' column
print(sorted_by_sex.to_string(index=False))

print()  # print a blank line for better display


# Sort by 'state' column (alphabetically) where name begins with the letter A and print result
sorted_by_state = filtered_df.sort_values(by='state')

print("------------------------------------------------------------------------------------------------")
print("   All entries where the last name begins with the letter A, sorted by state (alphabetically)   ")
print("------------------------------------------------------------------------------------------------")
print(sorted_by_state.to_string(index=False))
print()  # insert a blank line for better display

# Sort by 'birthdate' ie age (youngest first) where name begins with the letter A and print result
sorted_by_age = filtered_df.sort_values(by='birthdate', ascending=False)
sorted_by_age.info()
# sorted_by_age["birthdate"] = pd.to_datetime(sorted_by_age["birthdate"])
# sorted_by_age.info()

print("------------------------------------------------------------------------------------------------")
print("    All entries where the last name begins with the letter A, sorted by age (youngest first)    ")
print("------------------------------------------------------------------------------------------------")
print(sorted_by_age.to_string(index=False))
