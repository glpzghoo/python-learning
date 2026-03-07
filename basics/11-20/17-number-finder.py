numbers = [3, 7, 12, 18, 25, 30]

number = int(input("Тоо оруулна уу~ ")) 

if number in numbers:
    index = numbers.index(number)
    print(f"{number} жагсаалтанд байна! Индекс: {index}")
else:
    print(f"{number} жагсаалтанд алга!")

