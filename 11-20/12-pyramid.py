number = int(input("Тоо оруулна уу~ "))

# for i in range(1, number + 1):
#     print("*" * i)
for i in range(0, number):
    print("*" * (number - i))

# exact pyramid
for i in range(1, number + 1):
        print(" " * (number - i) + "*" * (i * 2 -1))