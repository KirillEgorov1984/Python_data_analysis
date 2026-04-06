import pandas as pd
pokemon = pd.read_csv("C:\\datasets\\pokemon.csv"
                      , index_col="Name").squeeze("columns")
print(pokemon.iloc[[100, 200, 300]])
print(pokemon.iloc[27:36])
print(pokemon.iloc[700:1010])
print(pokemon.iloc[700:])
print(pokemon.iloc[700:50000])
print(pokemon.iloc[-10:-5])
print(pokemon.iloc[-8:])