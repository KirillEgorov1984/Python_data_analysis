import pandas as pd
pokemon = pd.read_csv("C:\\datasets\\pokemon.csv"
                      , usecols=["Name"]).squeeze("columns")
print(pokemon)

google_stock_price = pd.read_csv("C:\\datasets\\google_stock_price.csv"
                      , usecols=["Price"]).squeeze("columns")
print(google_stock_price)
