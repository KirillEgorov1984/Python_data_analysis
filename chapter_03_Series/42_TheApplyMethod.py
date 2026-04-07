import pandas as pd

pokemon = pd.read_csv("C:\\datasets\\pokemon.csv"
                      ,usecols=["Name"]).squeeze("columns")
print(pokemon.head())

print(pokemon.apply(len))

def count_of_a(pokemon):
    return pokemon.count("a")

print(count_of_a("apple"))

print(pokemon.apply(count_of_a))