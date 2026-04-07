import pandas as pd

google = pd.read_csv("C:\\datasets\\google_stock_price.csv"
                      , usecols=["Price"]).squeeze("columns")
google.head()
print(google.head())
print(google.count())
print(google.size)
print(google.sum())
#print(google.product())
print(google.mean())
print(google.std())
print(google.max())
print(google.min())
print(google.median())
print(google.mode())
print(pd.Series([1,2,3,4]).product())
print(pd.Series([1,2,2,2,3]).mode())
print(google.describe())
