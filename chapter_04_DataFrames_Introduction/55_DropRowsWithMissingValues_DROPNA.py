# import pandas as pd
# nba = pd.read_csv("C:\\datasets\\nba.csv")
# print(nba.tail())

#nbadropna = nba.dropna()
#nbadropna = nba.dropna(how = "all")
#nbadropna = nba.dropna(subset = ["College"])
#nbadropna = nba.dropna(subset = ["College", "Salary"])
# nbadropna = nba.dropna(thresh=5)
# print(nbadropna)


import pandas as pd
import numpy as np

# Создание примера DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9, 10, np.nan, 12],
    'D': [np.nan, np.nan, np.nan, 11]
})

print(df)

# 1. Удалить строки, где есть хотя бы один NaN
df_cleaned = df.dropna()
print(df_cleaned)

# 2. Удалить столбцы, где есть хотя бы один NaN
df_col_cleaned = df.dropna(axis=1)
print(df_col_cleaned)

# 3. Удалить строки, если NaN только в определенных столбцах
df_subset = df.dropna(subset=['D'])
print(df_subset)

# 4. Удалить строки, где все значения - NaN
df_all = df.dropna(how='all')
print(df_all)

# 5. Оставить строки, где есть хотя бы 2 не-NaN значения
df_thresh = df.dropna(thresh=2)
print(df_thresh)