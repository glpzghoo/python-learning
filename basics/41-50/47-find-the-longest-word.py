import re

with open("sample-texts/sample-text.txt", 'r') as file:
    content = file.read()

words = re.findall(r'\w+', content.lower())

longest = words[0]

for word in words:
   if len(word) > len(longest):
       longest = word

print(longest)