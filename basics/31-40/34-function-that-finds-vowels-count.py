def count_vowels(text):
    vowels = 'aeiou'
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count


user_input = input('Үг оруулна уу~ ')

count = count_vowels(user_input)

print(f"{count}")
