names = ["Adiya", "Saraa", "Boldoo", "Naraa", "Tuvshin"]

search_name = input("Хайх~ ").capitalize()

if search_name in names:
    print(f"{search_name} жагсаалтанд байна!")
else:
    print(f"{search_name} жагсаалтанд алга!")