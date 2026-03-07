def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a

user_input1 = int(input('Тоо оруулна уу~ 1: '))
user_input2 = int(input('Тоо оруулна уу~ 2: '))

print(f"{gcd(user_input1, user_input2)}")