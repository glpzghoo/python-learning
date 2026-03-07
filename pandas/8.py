import pandas as pd

content = pd.read_csv('transactions.csv', names=['Name', "Price"])

bob_high_price = content[(content['Price'] > 100) & (content['Name'] == 'Bob')]

print(bob_high_price)