import pandas as pd
adjectives = pd.Series(["Smart","Handsome","Charming","Brilliant","Humble","Smart"])
print(adjectives)
print(adjectives.size)
print(adjectives.is_unique)
print(adjectives.values)
print(adjectives.index)
print(type(adjectives.values))
print(type(adjectives.index))


