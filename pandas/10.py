import pandas as pd

df = pd.read_csv('books.csv', names=['Name', 'Genre', "Rating"])

scifi_books = df[df['Genre'] == 'Sci-Fi'].copy()
scifi_books['Status'] = "Recommended"
scifi_books.loc[scifi_books['Rating'] >= 4.5, 'Status'] = "Masterpiece"

scifi_books.to_csv('Sci-Fi Books.csv', index=False)

print(scifi_books)