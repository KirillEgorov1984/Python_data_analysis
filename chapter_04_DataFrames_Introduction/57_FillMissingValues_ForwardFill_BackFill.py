import pandas as pd
import numpy as np

temperatures = pd.read_csv("C:\\datasets\\temperatures.csv")
setchunks = temperatures[["Year", "AvgTemperature"]].head()

setchunks.loc[temperatures["AvgTemperature"] == 46.4, "AvgTemperature"] = np.nan
print(setchunks)

print(setchunks["AvgTemperature"].ffill())

print(setchunks["AvgTemperature"].bfill())

print(setchunks["AvgTemperature"].ffill(limit=2))