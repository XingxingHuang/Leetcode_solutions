import pandas as pd

World = pd.DataFrame({
    "name": ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola"],
    "continent": ["Asia", "Europe", "Africa", "Europe", "Africa"],
    "area": [652230, 28748, 2381741, 468, 1246700],
    "population": [25500100, 2831741, 37100000, 78115, 20609294],
    "gdp": [20343000, 12960000, 188681000, 3712000, 100990000]
})

print(World.loc[(World.area >= 3000000) | (World.population >= 25000000)][["name", "population", "area"]])
