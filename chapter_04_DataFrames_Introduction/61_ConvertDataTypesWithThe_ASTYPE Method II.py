import pandas as pd
nba = pd.read_csv("C:\\datasets\\nba.csv").dropna(how='all')
print(nba.tail())

print(nba["Team"].nunique())
print(nba["Position"].nunique())
print(nba["Name"].nunique())

print(nba.info())

nba["Position"] = nba["Position"].astype("category")
print(nba["Position"])
nba["Team"] = nba["Team"].astype("category")
print(nba["Team"])