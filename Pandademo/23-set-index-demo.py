import pandas as pd

df = pd.DataFrame({
    "ID": [101, 102, 103],
    "Name": ["Alice", "Bob", "Charlie"],
    "Salary": [3000, 4000, 5000]
})

# df = df.set_index("ID")
# df = df.set_index("ID", drop=False) # Keep the column still default is drop=True
# df.set_index("ID", inplace=True) # inplace

df = df.set_index(["ID", "Name"])
print(df)
 