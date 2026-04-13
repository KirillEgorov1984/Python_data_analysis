import pandas as pd
import numpy as np
nba = pd.read_csv("C:\\datasets\\nba.csv").dropna(how='all')
# print(nba.tail())
# print(nba.fillna(0))

nbaone = nba.fillna({"Salary": 0, "College": "Unknown", "Position":"N/A"})
nba["Salary"] = nba["Salary"].fillna(0)
print(nba["Salary"])

nba["College"] = nba["College"].fillna(value="Unknown")

print(nba["College"])

# Создание примера данных
df = pd.DataFrame({'A': [1, np.nan, 3], 'B': [np.nan, 5, np.nan]})

# 1. Замена всех NaN на 0
df_filled = df.fillna(0)

# 2. Замена NaN в столбце 'A' средним значением
df['A'] = df['A'].fillna(df['A'].mean())

print(nba["College"].tail(60))