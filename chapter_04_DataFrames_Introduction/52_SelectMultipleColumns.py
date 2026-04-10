import pandas as pd
nba = pd.read_csv("C:\\datasets\\nba.csv")
#print(nba.head())
NameTeam = nba[["Name", "Team"]]
print(NameTeam)

#еще один вариант вывода
columns_to_select = ["Name", "Team"]
print(nba[columns_to_select])