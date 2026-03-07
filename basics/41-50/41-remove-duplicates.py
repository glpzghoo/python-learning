def remove_duplicates(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
        
    return unique

numbers = [5, 5, 5, 5]

print(remove_duplicates(numbers))