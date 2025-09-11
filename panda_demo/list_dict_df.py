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



