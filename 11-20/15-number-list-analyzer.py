numbers = [12, 45, 7, 32, 19]

total = 0
largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    total += num
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print(numbers)
print(f"Нийлбэр: {total}, Хамгийн их: {largest}, Хамгийн бага: {smallest}")