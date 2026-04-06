import pandas as pd
pokemon = pd.read_csv("C:\\datasets\\pokemon.csv"
                      , usecols=["Name"]).squeeze("columns")
google_stock_price = pd.read_csv("C:\\datasets\\google_stock_price.csv"
                      , usecols=["Price"]).squeeze("columns")
# print(pokemon.head())
# print(len(pokemon))
# print(type(pokemon))
# print(list(pokemon))
# print(sorted(pokemon)) # сортировка
# print(sorted(google_stock_price)) # сортировка
# print(dict(pokemon))
print(max(google_stock_price))
print(min(google_stock_price))
print(max(pokemon))
print(min(pokemon))