students = [
    {"name": "Alice", "age": 25, "score": 85},
    {"name": "Bob", "age": 22, "score": 90},
    {"name": "Charlie", "age": 23, "score": 88}
]

print(students)

import pandas as pd
df = pd.DataFrame(students)
print(df)

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
}

df = pd.DataFrame(data)
print(df) # smart/truncated view (depends on DataFrame size & pandas settings).
print(df.to_string()) # forces all rows and all columns.

df = pd.DataFrame(
    {"Age": [25, 30, 35]},
    index=[10, 20, 30]
)
print(df)
print(type(df))

df = pd.DataFrame(
    {"Age": [25, 30, 35]}
)
print(df)
print(type(df))
