import pandas as pd

df = pd.DataFrame({
    "order_date": ["2024-01-10", "2024-02-15", "2024-03-20"]
})

print(df.dtypes)
print(df)
df["order_date"] = pd.to_datetime(df["order_date"])
print("post conversion")
print(df.dtypes)
print(df)

df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month
df["day"] = df["order_date"].dt.day
df["weekday"] = df["order_date"].dt.day_name()
print(df)