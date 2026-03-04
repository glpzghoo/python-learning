import pandas as pd

df = pd.read_csv("inventory.txt", names=["Item", "Category", "Quantity"])

print("--- The Table ---")
print(df)

print("\n--- The Summary ---")
summary = df.groupby("Category")["Quantity"].sum()
print(summary)