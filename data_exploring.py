# FIND

import requests
from bs4 import BeautifulSoup

r = requests.get("https://books.toscrape.com")
soup = BeautifulSoup(r.text, "html.parser")

# ACESSANDO PRIMEIRO ELEMENTO 'A' DE CADA 'LI' E O ATRIBUTO DA URL PARA A QUAL O LINK APONTA 'HREF'
for li in soup.find("div", class_="side_categories").find_all("ul")[-1].find_all("li"):
    link = li.find("a").get("href")
    print(link)

# PASSANDO O LINK (SEM O HREF) PARA A REQUESTS E PROCURANDO PELA CATEGORIA 'FANTASY'

    if "Fantasy" in link.text:
        r = requests.get(f"https://books.toscrape.com/{link.get('href')}")
        
        
        fantasy_soup = BeautifulSoup(r.text, "html.parser")
        print(
            fantasy_soup.prettify()
        )  # Agora nós estamos em uma nova página: https://books.toscrape.com/catalogue/category/books/fantasy_19/index.htm
