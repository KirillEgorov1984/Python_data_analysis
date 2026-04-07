import pandas as pd

pokemon_df = pd.read_csv("C:\\datasets\\pokemon.csv", usecols=["Name"])
pokemon_series = pokemon_df.squeeze("columns").copy()
#print(pokemon_df)
pokemon_series[0] = "Whatever"
pokemon_series.head()
print(pokemon_df)