# interpolate

import pandas as pd

mydict = {
    "Name": ["John", "David", "Rock"],
    "Age": [10, 20, None]
}

df = pd.DataFrame(mydict)
print(df)

print(df['Age'].interpolate(method="linear",inplace=True))
print(df)