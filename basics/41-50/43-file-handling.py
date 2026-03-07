import re
from collections import Counter 
content = ""
with open("sample-text.txt", "r") as file:
    content = file.read()
    print(content)

words = re.findall(r'\w+', content.lower())

word_counts = Counter(words)

sorted_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

print(word_counts)
print(sorted_counts)