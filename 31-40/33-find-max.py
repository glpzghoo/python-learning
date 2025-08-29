def find_max(numbers):
    if len(numbers) == 0:
        return 'none'
    
    largest = numbers[0]

    for num in numbers[1:]:
        if num > largest:
            largest = num

    return largest

numbers = [3, 7, 2, 9, 5]

print(f"{find_max(numbers)}")