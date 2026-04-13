import pandas as pd
import numpy as np
nba = pd.read_csv("C:\\datasets\\nba.csv").dropna(how='all').fillna({"Salary":0})
print(nba.tail())
print(nba.dtypes) # просмотр типа данных колонок
nba["Salary"]= nba["Salary"].astype(int)
print(nba.dtypes) # просмотр типа данных колонок
print(nba.memory_usage())
print(nba.info())
nba["Salary"]= nba["Salary"].astype(pd.Int32Dtype())
print(nba.info())
