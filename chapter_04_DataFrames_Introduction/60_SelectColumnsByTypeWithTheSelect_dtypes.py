import pandas as pd
import numpy as np
nba = pd.read_csv("C:\\datasets\\nba.csv")
# print(nba.tail())
# print(nba.dtypes)
# print(nba.info())
# выборка только столбцов с числовыми значениями
print(nba.select_dtypes(include="number"))
# выборка столбцов не влючающих числовые значения
print(nba.select_dtypes(exclude="number"))