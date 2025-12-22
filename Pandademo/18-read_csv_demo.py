import pandas as pd

df = pd.read_csv("sample_students.csv")  # assumes you have a CSV file
#print(df.head())  # show first 5 rows
#print(df.tail())  # show last 5 rows
#print(df) # smart/truncated view (depends on DataFrame size & pandas settings)
#print(df.to_string()) # forces all rows and all columns

#print(df["Name"])       # Select a single column and return Series
#print(df[["Name", "Age"]])  # Select multiple columns and returns DataFrame
#print(df.iloc[0])       # First row by position
#print(df.loc[1, "City"]) # Row 1, column "City"

young_people = df[df["Age"] < 30]
print(young_people)

young_people.to_csv("update_students.csv", index=False)


