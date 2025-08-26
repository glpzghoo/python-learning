numbers =[]

for i in range(0, 5):
    user_input = int(input(f"Тоо оруулна уу~ {i + 1}: "))
    numbers.append(user_input)

# ogogdmol functions
sortedAsc = sorted(numbers)
sortedDesc = sorted(numbers, reverse=True)
total = sum(numbers)
average = total / len(numbers)
smallest = min(numbers)
largest = max(numbers)

print(f"1. Asc: {sortedAsc}")
print(f"1. Desc: {sortedDesc}")
print(f"1. Sum: {total}")
print(f"1. Avg: {average}")
print(f"1. largest: {largest}")
print(f"1. smallest: {smallest}")

# manual
smallest = numbers[0]
largest = numbers[0]

for i in range(0, len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        

total = numbers[0]

for i in range(1, len(numbers)):
    total += numbers[i]

    if numbers[i] > largest:
        largest = numbers[i]
    if numbers[i] < smallest:
        smallest = numbers[i]

average = total / len(numbers)


print(f"2. Asc: {numbers}")
print(f"2. Desc: {numbers[::-1]}")
print(f"2. Sum: {total}")
print(f"2. Avg: {average}")
print(f"2. largest: {largest}")
print(f"2. smallest: {smallest}")