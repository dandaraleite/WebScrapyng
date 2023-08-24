import requests
from bs4 import BeautifulSoup

r = requests.get("https://books.toscrape.com")

if r.status_code == 200:
    page_content = r.text
    soup = BeautifulSoup(page_content, 'html.parser')

    print(soup.prettify())

# SELECT 
import requests
from bs4 import BeautifulSoup

r = requests.get("https://books.toscrape.com")

if r.status_code == 200:
    page_content = r.text
    soup = BeautifulSoup(page_content, 'html.parser')

    categories_div = soup.select(".side_categories")[0]
    categories_li = categories_div.select("ul li ul li")
    print(categories_li)


# SELECT + ARMAZENAMENTO + REPLACE NOS \N E NOS ESPAÇOS

import requests
from bs4 import BeautifulSoup

r = requests.get("https://books.toscrape.com")

categories = []

if r.status_code == 200:
    page_content = r.text
    soup = BeautifulSoup(page_content, "html.parser")

    categories_li = soup.select(".side_categories ul li ul li")

    for li in categories_li:
        categories.append(li.text.replace("\n", "").rstrip().lstrip())

    print(categories)
