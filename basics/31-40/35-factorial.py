def factorial(number):
    if number == 0:
        return 1
    f = 1

    for i in range(1, number + 1):
        f *= i
    return f


number = int(input('Тоо оруулна уу~ '))

print(f"{factorial(number)}")