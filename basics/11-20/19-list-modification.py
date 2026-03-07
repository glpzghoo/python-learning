fruits = ["apple", "banana", "cherry"]

fruits.append("orange")
fruits.insert(1, "mango")
fruits.remove("banana")
index = fruits.index("cherry")
fruits[index] = "grape"

fruits.sort()

print(f"{fruits}")