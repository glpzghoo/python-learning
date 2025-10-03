import re
from collections import Counter 
content = ""
with open("sample-texts/sample-text.txt", "r") as file:
    content = file.read()
    print(content)

words = re.findall(r'\w+', content.lower())

word_counts = Counter(words)

print(word_counts.most_common(5))