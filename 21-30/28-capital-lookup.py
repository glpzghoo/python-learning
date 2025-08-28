capitals = {
    "Mongolia": "Ulaanbaatar",
    "Japan": "Tokyo",
    "France": "Paris",
    "Germany": "Berlin",
    "USA": "Washington"
}

user_input = input("Улс: ")

capital = capitals.get(user_input, "Улс олдсонгүй!")

print(capital)