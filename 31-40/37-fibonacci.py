def fibonacci(n):
    if n == 0:
        return []
    if(n == 1):
        return [0]
    sq = [0, 1]

    while n > len(sq):
        sum = sq[-1] + sq[-2]
        sq.append(sum)
    return sq

user_input = int(input('Тоо оруулна уу~ '))

print(f"{fibonacci(user_input)}")