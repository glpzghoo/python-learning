# Value Mapper

import pandas as pd

content = pd.read_csv('transactions.csv', names=['Name', "Price"])

content['Level'] = 'Standard'

content.loc[content['Price'] >= 200, "Level"] = "Premium"

print(content)