import pandas as pd

pokemon = pd.read_csv("C:\\datasets\\pokemon.csv"
                      ,index_col=["Name"]).squeeze("columns")
print(pokemon.head())

attack_powers = pd.Series({
    "Grass": 10,
    "Fire":15,
    "Water":15,
    "Fairy, Fighting":20,
    "Grass, Psychic":50
})

print(pokemon.map(attack_powers))