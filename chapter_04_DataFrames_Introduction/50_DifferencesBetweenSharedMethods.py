import pandas as pd
s = pd.Series([1,2,3,4,5])
print(s)
revenue = pd.read_csv("C:\\datasets\\revenue.csv", index_col="Date")
print(revenue)
print(revenue.sum()) # сумма по колонкам
print(revenue.sum(axis="index")) # сумма по колонкам
print(revenue.sum(axis=0))# сумма по колонкам

print(revenue.sum(axis="columns"))#сумма по строке
print(revenue.sum(axis=1))#сумма по строке

print(revenue.axes) # параметры строк(что входит в суммированные строки)

print(revenue.sum(axis=1).sum())#сумма по всему датасету Total
print(revenue.sum(axis=0).sum())#сумма по всему датасету Total