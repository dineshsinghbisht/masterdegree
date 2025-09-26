import pandas as pd
from getpass import getuser
from ast import literal_eval

# user = getuser()
# csv_location = f'/home/varpha/dan/private/{user}' + \
#                 f'/exrc_02/data/{user}_prob03_epl.csv'
csv_location = "ah4323_prob03_epl.csv"

# Load input CSV data related to some English Premier League results into pandas DataFrame
df = pd.read_csv(csv_location)

# # Get basic information about data
# print(df.info()) # prints concise summary about DataFrame's structure
# print(df.head()) # prints first five rows - default

# Convert the 'fullTime' column data from string into a python dictionary
# Used Pandas DataFrame method ´apply()´ to convert string into list using ´literal_eval´ method call
df["fullTime"] = df["fullTime"].apply(literal_eval)

# Extract goals fullTime 'fullTime' column to create cloumns 'homeGoals' and 'awayGoals'
df["homeGoals"] = df["fullTime"].apply(lambda x: x["homeTeam"])
df["awayGoals"] = df["fullTime"].apply(lambda x: x["awayTeam"])

# Create two rows per match: one for home team and another for away team
# Used Pandas DataFrame method ´rename()´ to rename the columns and make them unique for both rows
# Used Pandas DataFrame method ´concat()´ to create the final data post concatinating home_team and away_team DataFrames
home_team = df[["homeTeam", "homeGoals", "awayGoals"]].rename(
    columns={"homeTeam": "team", "homeGoals": "gf", "awayGoals": "ga"}
)
away_team = df[["awayTeam", "homeGoals", "awayGoals"]].rename(
    columns={"awayTeam": "team", "awayGoals": "gf", "homeGoals": "ga"}
)
match_data = pd.concat([home_team, away_team], ignore_index=True)

# Print sample data for debugging
# print(matches.head())

# Define function ´result´ to find the output as win, loss or draw using gf (goals for) and ga (goals against) as an input


def result(row):
    if row.gf > row.ga:
        return "win"
    elif row.gf < row.ga:
        return "loss"
    else:
        return "draw"


# Create a new column 'result'
# Used Pandas DataFrame method ´apply()´ to call the custom function ´result´ to determine value as 'win', 'loss' or 'draw'
match_data["result"] = match_data.apply(result, axis=1)

# # Print sample data for debugging
# print(matches.head())
# print(matches.tail())

# Group the match information at each team level
# Used Pandas DataFrame method ´groupby()´
# To get total number of games played (games), sum of goals for (gf) and sum of goals against (ga)
match_summary = match_data.groupby("team").agg(
    games=("team", "count"),
    gf=("gf", "sum"),
    ga=("ga", "sum")
).copy()

# # Print sample data for debugging
# print(match_summary.head())

# Count wins, draws, defeats per team
match_summary["wins"] = match_data.groupby(
    "team")["result"].apply(lambda x: (x == "win").sum())
match_summary["draws"] = match_data.groupby(
    "team")["result"].apply(lambda x: (x == "draw").sum())
match_summary["defeats"] = match_data.groupby(
    "team")["result"].apply(lambda x: (x == "loss").sum())

# # Print sample data for debugging
# print(match_summary.head())

# Add new column 'points' to store the value for - a win gives 3 points, a draw gives 1 point, and a loss gives 0 points
match_summary["points"] = match_summary["wins"] * 3 + \
    match_summary["draws"] + match_summary["defeats"] * 0

# Add new column ´goals' to store value as goals for - goals against ie gf-ga
match_summary["goals"] = match_summary["gf"].astype(
    str) + "-" + match_summary["ga"].astype(str)

# Add new temporary column ´goal-diff' to store value as goals for - goals against - needed for sorting requirement
match_summary["goal-diff"] = match_summary["gf"] - match_summary["ga"]

# Sort the data first with most points, then goals difference and then with goals against (ga)
# Used Pandas DataFrame method sort_values() for sorting
match_summary = match_summary.sort_values(
    by=["points", "goal-diff", "ga"],
    ascending=[False, False, False]
)

# # Print sample data for debugging
# print(match_summary.head())
# print(match_summary.tail())

# Select only required coloumns
match_summary = match_summary[["games", "wins",
                               "draws", "defeats", "goals", "points"]]

# Print the final summary as asked in the task
print(match_summary)
