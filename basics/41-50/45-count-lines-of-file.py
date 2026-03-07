lines = 0
words = 0
characters = 0

with open('sample-texts/sample-text.txt', 'r') as file:
    for line in file:
        lines += 1
        words += len(line.split())
        characters += len(line)


print(lines, words, characters)