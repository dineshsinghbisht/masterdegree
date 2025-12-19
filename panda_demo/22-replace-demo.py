'''
df["age"] = df["age"].replace(-1, None)

df["status"] = df["status"].replace(
    ["new", "in_progress", "done"],
    [0, 1, 2]
)

df = df.replace({
    "gender": {"M": "Male", "F": "Female"},
    "active": {"yes": True, "no": False}
})

df.loc[df["salary"] < 30000, "salary"] = 30000

'''