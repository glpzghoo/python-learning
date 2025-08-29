def calculate_average(numbers):
    if not numbers:
        return 0
    avg = sum(numbers) / len(numbers)
    return round(avg, 2)

numbers = []

for i in range(3):
    n_input = int(input(f"{i + 1}: "))
    numbers.append(n_input)

print(f"{calculate_average(numbers)}")