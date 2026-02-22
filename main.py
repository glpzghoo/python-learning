# refreshing the memory
Groceries = []

while True:
    UserInput = input("add grocery (or type 'done'): ").strip()
    
    if UserInput.lower() == "done":
        break
    
    if UserInput.isdigit():
        print("that’s a price, not a product! Try again.")
        continue
        
    Groceries.append(UserInput)

first_three = Groceries[0:3]

print(f"first items: {', '.join(first_three)}")
print(f"total items in list: {len(Groceries)}")