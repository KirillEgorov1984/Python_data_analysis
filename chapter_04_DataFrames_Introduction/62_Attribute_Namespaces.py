import pandas as pd

nba = pd.read_csv("C:\\datasets\\nba.csv").dropna(how="all")
nba["Position"] = nba["Position"].astype("category")
nba["Team"] = nba["Team"].astype("category")
nba.head()

print(nba["Team"].str.upper())
print(nba["Position"].cat.categories)