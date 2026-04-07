import pandas as pd
# pokemon = pd.read_csv("C:\\datasets\\pokemon.csv",usecols="Name").squeeze("columns")
# # print(pokemon.head())
# pokemon.iloc[0]="Borisaur"
# print(pokemon.head())
# pokemon.iloc[[1,2,4]] = ["Firemon", "Flamemon", "Blazemon"]
# print(pokemon.head())
pokemon = pd.read_csv("C:\\datasets\\pokemon.csv",index_col="Name").squeeze("columns")
# print(pokemon.head())
pokemon.loc["Bulbasaur"] = "Awesomeness"
print(pokemon.head())
pokemon.loc["Bulbasaur"] = "Silly"
print(pokemon.head())