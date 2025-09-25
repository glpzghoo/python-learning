with open("sample-texts/sample-text.txt", "r") as file:
    content = file.read()

vowels = ("a", "e", "i", "o", "u")

vowels_count = 0
consonants_count = 0

for letter in content:
    if letter.isalpha():  
        if letter.lower() in vowels:
            vowels_count += 1
        else:
            consonants_count += 1

print(f"Vowels: {vowels_count}, Consonants: {consonants_count}")
