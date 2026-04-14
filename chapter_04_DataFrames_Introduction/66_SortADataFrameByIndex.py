import pandas as pd

nba = pd.read_csv("C:\\datasets\\nba.csv").dropna(how="all")
print(nba.sort_index())
print(nba.sort_index(ascending=True))
print(nba.sort_index(ascending=False))