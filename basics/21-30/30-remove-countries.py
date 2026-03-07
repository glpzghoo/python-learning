capitals = {
    "Mongolia": "Ulaanbaatar",
    "Japan": "Tokyo",
    "France": "Paris",
    "Germany": "Berlin",
    "USA": "Washington"
}

country = input("Улс: ")

country_exist = capitals.get(country, False)

if country_exist:
    capitals.pop(country)
else:
    print("Тийм улс алга! Шинээр нэмэх үү?")
    answer = input("yes/no: ")
    if answer == "yes":
        capital = input("Нийслэл: ")
        capitals[country] = capital

print(capitals)