numbers = [5,10,15,20,25]

total = 0
count = len(numbers)

for i in range(0, count):
    total += numbers[i]

avg = total / count

print(f"{avg:.2f}")