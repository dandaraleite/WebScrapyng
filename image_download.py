import requests
import pandas as pd
import os

df = pd.read_csv("mystery_books", index_col=0)
path = "mystery_books_image"
os.mkdir(path)

for index, book in df.iterrows():
    with open(f"mystery_books_image/{book['Title']}.jpeg", "wb") as f:
        response = requests.get(
            f"https://books.toscrape.com/{book['Image'].replace('../../../../', '')}"
        )
        f.write(response.content)
