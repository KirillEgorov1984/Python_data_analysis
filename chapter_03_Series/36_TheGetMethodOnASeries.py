import pandas as pd
pokemon = pd.read_csv("C:\\datasets\\pokemon.csv",index_col="Name").squeeze("columns")
print(pokemon.get("Moltres"))
print(pokemon.get("Digimon"))
print(pokemon.get("Moltres", "Nonexistent"))
print(pokemon.get("Digimon", "Nonexistent"))
print(pokemon.get(["Moltres","Digimon"], "One of the values in the list was not found"))