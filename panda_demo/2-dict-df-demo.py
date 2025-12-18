# a dictionary is column-oriented, while a list is row-oriented
'''
Creating a DataFrame from a dictionary is the most common and intuitive method because it directly maps to the DataFrame's column-based structure.
Structure: The dictionary keys become the column names, and the values, which are lists, become the data for each column.
Best for: When your data is already organized by columns. It's often cleaner and more readable.
'''

import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['London', 'Paris', 'Tokyo']}

df = pd.DataFrame(data)
print(df)

# This will create a CSV with the extra index column
df.to_csv('with_index.csv')

# This is the fix: set index=False to prevent it
df.to_csv('without_index.csv', index=False)