import pandas as pd

nba = pd.read_csv("C:\\datasets\\nba.csv").dropna(how="all")
print(nba.tail())

print(nba.sort_values("Name"))
print(nba.sort_values(by="Name"))
print(nba.sort_values(by="Name", ascending=True))
print(nba.sort_values(by="Name", ascending=False))
print(nba.sort_values(by="Salary"))
print(nba.sort_values(by="Salary", ascending=True))
print(nba.sort_values(by="Salary", ascending=False))
print(nba.sort_values(by="Salary", na_position="last"))
print(nba.sort_values(by="Salary", na_position="first", ascending=False))