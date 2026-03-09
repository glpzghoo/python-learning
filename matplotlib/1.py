import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("books.csv", names=["Name", "Genre", "Rating"])
scifi_books = df[df["Genre"] == "Sci-Fi"].copy()
plt.bar(scifi_books["Name"], scifi_books["Rating"], color="skyblue")
plt.xlabel("Book Title")
plt.ylabel("Rating")
plt.title("Book Graph")
plt.show()
print(scifi_books)
