import os
import random

with open("sample-texts/text-1.txt", "r") as file1:
    content1 = file1.read()

with open("sample-texts/text-2.txt", "r") as file2:
    content2 = file2.read()

merged = f"{content1}\n{content2}"

os.makedirs("sample-outputs", exist_ok=True)

with open(f"sample-outputs/merged-{random.random()}.txt", "w") as dest:
    dest.write(merged)

print("files merged successfully!")
