import numpy as np
import pandas as pd

## read csv
df = pd.read_csv("sample_students.csv")
# print("Shape is", df.shape)
# print("Columns are:", df.columns)
# print(df.head())
grouped = df.groupby("City")["Age"].sum()
# print(grouped)


df = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR", "Finance"],
    "Salary": [60000, 65000, 50000, 52000, 70000],
    "EmployeeID": [123, 456, 467, 23423, 9999]
})

print((df["Department"].value_counts()))
dep_counts = df["Department"].value_counts()
print(dep_counts.info())
print(dep_counts.index)
print(dep_counts.values)

# print(df.groupby("Department")["Salary"].mean())
# print(df.groupby("Department", as_index=False)["Salary"].mean())
# print(df.groupby("Department")["Salary"].agg(["mean", "min", "max"]))

df.groupby("Department").agg({
    "Salary": ["mean", "sum"],
    "EmployeeID": "count"
})