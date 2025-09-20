import random, os

with open("sample-text.txt", "r") as content:
    data = content.read()
    
os.makedirs("sample-outputs", exist_ok=True)

with open(f"sample-outputs/copied-{random.random()}.txt", 'w') as destination:
    destination.write(data)

print(f"file copied")