numbers =[]

for i in range(0, 5):
    user_input = int(input(f"Тоо оруулна уу~ {i+1}: "))
    numbers.append(user_input)

print(f"{numbers}")

total = 0
for i in range(0, len(numbers)):
    total += numbers[i]

print(f"total: {total}")