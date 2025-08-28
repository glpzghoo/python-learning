capitals = {
    "Mongolia": "Ulaanbaatar",
    "Japan": "Tokyo",
    "France": "Paris",
    "Germany": "Berlin",
    "USA": "Washington"
}

for country in capitals.keys():
    print(country)

for capital in capitals.values():
    print(capital)

for country, capital in capitals.items():
    print(f"{country}, {capital}")