import pandas as pd

content = pd.read_csv('transactions.csv', names=['Name', "Price"])

high_value = content[content['Price'] > 100]

unique = high_value['Name'].unique()

avg = high_value['Price'].mean()

alice = content[content['Name'] == 'Alice']
print(alice)