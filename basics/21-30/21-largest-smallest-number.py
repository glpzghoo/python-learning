numbers = []

for i in range(0,5):
    user_input = int(input(f"Тоо оруулна уу~ {i+1}: "))
    numbers.append(user_input)

largest = max(numbers)
smallest = min(numbers)

print(f"1. Хамгийн том: {largest}, Хамгийн бага: {smallest}")


largest = numbers[0]
smallest = numbers[0]

for i in range(1, len(numbers)):
    if largest < numbers[i]:
        largest = numbers[i]
    if smallest > numbers[i]:
        smallest = numbers[i]

print(f"2. Хамгийн том: {largest}, Хамгийн бага: {smallest}")