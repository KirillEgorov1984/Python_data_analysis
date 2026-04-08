import pandas as pd
nba = pd.read_csv("C:\\datasets\\nba.csv")
print(nba.head())
print(nba.head(9))
print(nba.tail(2))
# s = pd.Series([1,2,3,4,5])
print(nba.index)
print(nba.columns)