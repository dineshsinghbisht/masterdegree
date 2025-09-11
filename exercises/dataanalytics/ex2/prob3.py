import pandas as pd
from getpass import getuser
import ast

# user = getuser()
# csv_location = f'/home/varpha/dan/private/{user}' + \
#                 f'/exrc_02/data/{user}_prob03_epl.csv'
csv_location = "ah4323_prob03_epl.csv"

# Load input CSV data into dataframes
df = pd.read_csv(csv_location)

# # Get basic information about data
# print(df.info()) # display concise summary about dataframe
# print(df.head()) # display first five rows - default

# Parse score dict -> goals
def parse_fulltime(x):
    if isinstance(x, dict):
        d = x
    elif isinstance(x, str):
        d = ast.literal_eval(x)
    else:
        d = {}
    return pd.Series([d.get("homeTeam"), d.get("awayTeam")], index=["home_goals", "away_goals"])

df[["home_goals", "away_goals"]] = df["fullTime"].apply(parse_fulltime)

# 3) Long format (home & away rows)
home = pd.DataFrame({"team": df["homeTeam"], "gf": df["home_goals"], "ga": df["away_goals"]})
away = pd.DataFrame({"team": df["awayTeam"], "gf": df["away_goals"], "ga": df["home_goals"]})

def add_result_flags(frame: pd.DataFrame) -> pd.DataFrame:
    f = frame.copy()
    f["games"]   = 1
    f["wins"]    = (f["gf"] > f["ga"]).astype(int)
    f["draws"]   = (f["gf"] == f["ga"]).astype(int)
    f["defeats"] = (f["gf"] < f["ga"]).astype(int)
    return f

home = add_result_flags(home)
away = add_result_flags(away)
long = pd.concat([home, away], ignore_index=True)

# 4) Aggregate per team
agg = (
    long.groupby("team", as_index=True)
        .agg(
            games   = ("games", "sum"),
            wins    = ("wins", "sum"),
            draws   = ("draws", "sum"),
            defeats = ("defeats", "sum"),
            gf      = ("gf", "sum"),
            ga      = ("ga", "sum"),
        )
)

# 5) Points, GD, goals string
agg["points"] = 3*agg["wins"] + agg["draws"]
agg["gd"]     = agg["gf"] - agg["ga"]
agg["goals"]  = agg["gf"].astype(int).astype(str) + "-" + agg["ga"].astype(int).astype(str)

# 6) Sort and select display columns
league_table = (
    agg.sort_values(by=["points", "gd", "gf"], ascending=[False, False, False])
       .loc[:, ["games", "wins", "draws", "defeats", "goals", "points"]]
)

# 7) Remove the index name so no "team" label appears
league_table.index.name = None        # or: league_table = league_table.rename_axis(None)

# 8) Print neatly
print(league_table.to_string())
