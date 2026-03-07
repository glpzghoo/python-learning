import os, random
with open("sample-texts/sample-text.txt", "r") as file:
    content = file.read()

word_reverse = content[::-1]

os.makedirs("sample-outputs", exist_ok=True)

with open(f"sample-outputs/reversed-{random.random()}.txt", "w") as dest:
    dest.write(word_reverse)

print('success')