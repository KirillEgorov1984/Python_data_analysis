import pandas as pd
messy = pd.Series(["10", "20", "thirty", "", "40", "50.5"])
print(messy)


messy2 = pd.to_numeric(messy, errors='coerce').dropna().astype(int)
print(messy2)


