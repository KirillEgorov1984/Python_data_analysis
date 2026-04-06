import pandas as pd
pokemon = pd.read_csv("C:\\datasets\\pokemon.csv"
                      , usecols=["Name"]).squeeze("columns")
google_stock_price = pd.read_csv("C:\\datasets\\google_stock_price.csv"
                      , usecols=["Price"]).squeeze("columns")


print(pokemon.head(n=10))
print(google_stock_price.tail(n=15))

# print(google_stock_price)