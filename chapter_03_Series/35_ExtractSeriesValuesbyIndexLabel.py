import pandas as pd
pokemon = pd.read_csv("C:\\datasets\\pokemon.csv"
                      , index_col="Name").squeeze("columns")
print(pokemon.loc["Bulbasaur"])
print(pokemon.loc[["Charizard", "Jolteon", "Meowth"]])
