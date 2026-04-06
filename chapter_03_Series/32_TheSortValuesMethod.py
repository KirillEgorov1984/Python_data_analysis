import pandas as pd
pokemon = pd.read_csv("C:\\datasets\\pokemon.csv"
                      , usecols=["Name"]).squeeze("columns")
google_stock_price = pd.read_csv("C:\\datasets\\google_stock_price.csv"
                      , usecols=["Price"]).squeeze("columns")
print(google_stock_price.head())
print(google_stock_price.sort_values(ascending=False))
print(google_stock_price.sort_values(ascending=False).head())
print(pokemon.sort_values(ascending=False).tail())