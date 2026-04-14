import pandas as pd

nba = pd.read_csv("C:\\datasets\\nba.csv").dropna(how="all")
print(nba.tail())

print(nba.sort_values(["Team", "Name"]))
print(nba.sort_values(by=["Team", "Name"]))
print(nba.sort_values(by=["Team", "Name"], ascending=True))
print(nba.sort_values(by=["Team", "Name"], ascending=False))
print(nba.sort_values(by=["Team", "Name"], ascending=[True, False]))
print(nba.sort_values(["Position", "Salary"], ascending=[True, False]))
print(nba.sort_values(["Position", "Salary"], ascending=[False,True ]))