import csv
import pandas as pd
from getpass import getuser
import ast
# user = getuser()
# csv_location = f'/home/varpha/dan/private/{user}' + \
#                 f'/exrc_02/data/{user}_prob03_epl.csv'


# Read input CSV data in dataframe
# df = pd.read_csv(csv_location, dtype=str)
df = pd.read_csv("ah4323_prob03_epl.csv")
print(df)
