import pandas as pd
nba = pd.read_csv("C:\\datasets\\nba.csv")
print(nba.head())
nbaassign = nba.assign(Salary_Doubled=nba["Salary"] * 2,
                       Weight_Minus_10=nba["Weight"] - 10.5)
print(nbaassign.head())