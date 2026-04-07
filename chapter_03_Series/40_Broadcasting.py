import pandas as pd

google = pd.read_csv("C:\\datasets\\google_stock_price.csv"
                      , usecols=["Price"]).squeeze("columns")
google.head()
print(google)
print(google.add(10))# аналог операции + по всем элементам
print(google.sub(30))# аналог операции - по всем элементам
print(google.mul(1.25))# аналог операции * по всем элементам
print(google.div(2))# аналог операции / по всем элементам