import pandas as pd

fl = pd.read_csv("sample-texts/sales.csv")

fl['revenue'] = fl['qty'] * fl['price']

total_revenue = fl['revenue'].sum()
total_item_sold = fl['qty'].sum()
unique_items = fl['item'].nunique()
highest_revenue_item = fl.loc[fl['revenue'].idxmax()]
check = fl['revenue'].idxmax()

print("Total Revenue:", total_revenue)
print("Total Items Sold:", total_item_sold)
print("Unique Items:", unique_items)
print("Top Item by Revenue:\n", highest_revenue_item)

print("check:", check)