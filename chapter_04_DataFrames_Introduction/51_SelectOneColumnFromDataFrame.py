import pandas as pd
nba = pd.read_csv("C:\\datasets\\nba.csv")
nbahead = nba.head()
print(nbahead)
name = nba["Name"]
team = nba['Team']
print(name)
print(team)

valueofteam = team.value_counts()
print(valueofteam)
