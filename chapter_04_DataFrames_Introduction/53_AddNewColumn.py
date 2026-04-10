import pandas as pd
nba = pd.read_csv("C:\\datasets\\nba.csv")
#print(nba.head())
nba["Sport"] = "Basketball"

print(nba)

nba.insert(loc=3,column="League",value="NBA")

print(nba)