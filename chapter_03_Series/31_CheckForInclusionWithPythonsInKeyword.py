import pandas as pd
pokemon = pd.read_csv("C:\\datasets\\pokemon.csv"
                      , usecols=["Name"]).squeeze("columns")
google_stock_price = pd.read_csv("C:\\datasets\\google_stock_price.csv"
                      , usecols=["Price"]).squeeze("columns")
print(pokemon.head())
print("car" in "racecar")
print( 2 in [3, 2, 1])

print("Bulbasaur" in pokemon)
print(0 in pokemon)
print(pokemon.index)
print(pokemon.values)
print("Bulbasaur" in pokemon.values)