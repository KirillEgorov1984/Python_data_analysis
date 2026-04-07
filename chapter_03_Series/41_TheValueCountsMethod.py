import pandas as pd

pokemon = pd.read_csv("C:\\datasets\\pokemon.csv"
                      , index_col=["Name"]).squeeze("columns")
# print(pokemon.head())
print(pokemon.value_counts(ascending=True))
print(pokemon.value_counts(normalize=True) * 100)