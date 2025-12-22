'''
List-Based DataFrame
Creating a DataFrame from a list requires a different data structure, usually a list of lists. 
Each inner list represents a row of data.

Structure: The main list contains inner lists, where each inner list represents a single row. 
You must explicitly provide the column names as a separate argument.

Best for: When your data is already structured as rows. 
This is common when iterating over a dataset or reading from a file where each line is a record.
'''
import pandas as pd

# A list where each inner list is a row
data = [['Alice', 25, 'London'],
        ['Bob', 30, 'Paris'],
        ['Charlie', 35, 'Tokyo']]
 
# Provide column names separately
columns = ['Name', 'Age', 'City']

df = pd.DataFrame(data, columns=columns)
print(df)