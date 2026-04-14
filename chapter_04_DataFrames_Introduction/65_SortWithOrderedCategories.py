import pandas as pd

nba = pd.read_csv("C:\\datasets\\nba.csv").dropna(how="all")
# print(nba.head())
# print(nba["Team"].nunique())
# print(nba["Team"].unique())

room_type = pd.CategoricalDtype(categories=["Standard", "Deluxe", "Suite", "Presidential"], ordered=True)
print(room_type)