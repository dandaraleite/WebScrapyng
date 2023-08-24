# UTILIZANDO O PANDAS

import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("https://books.toscrape.com")

categories = []
if r.status_code == 200:
    page_content = r.text
    soup = BeautifulSoup(page_content, "html.parser")

    categories_li = soup.select(".side_categories ul li ul li")

    for li in categories_li:
        name = li.text.replace("\n", "").rstrip().lstrip()
        link = li.find("a").get("href")

        categories.append([name, link])

    df = pd.DataFrame(data=categories, columns=["Name", "Link"])
    df = df.sort_values(by="Name")
    print(df[df["Name"] == "Fantasy"])

    # Salvando os dados no arquivo categories.csv
    df.to_csv("categories.csv")

    # Carregando os dados. O parâmetro index_col informa ao pandas que a primeira coluna do csv está guardando o indice, o que evita dele criar outra coluna só para o index.
    df = pd.read_csv("categories.csv", index_col=0)
    print(df)

    # Iterando sobre as linhas do DataFrame para pegar só o index e o link
    for index, book in df.iterrows():
        print(index, book["Link"])
