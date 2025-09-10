def is_armstrong(n):
    stringsN = str(n)
    
    total = 0
    for number in stringsN:
        total += int(number) ** len(stringsN)
    return n == total


user_input = int(input(f"Тоо оруулна уу~ "))

print(is_armstrong(user_input))