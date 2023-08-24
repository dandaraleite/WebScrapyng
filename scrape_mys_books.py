import requests
from bs4 import BeautifulSoup
import pandas as pd

# Buscando a url dos livros de mistério
r = requests.get("https://books.toscrape.com/catalogue/category/books/mystery_3/index.html")

# Criando armazenamento de livros
books = []

# Passando conteúdo da page para HTML com BeautifulSoup
if r.status_code == 200:
    page_content = r.text
    html = BeautifulSoup(page_content, "html.parser")

    # Inspecionando a tag que contém os livros e suas propriedades do livro #section
    book_section = html.find("section")

    for book in book_section.find("ol").select("li"):
        image_url = book.find("div", class_="image_container").find("img").get("src")
        
        stars = book.find("p").get("class")[1] #Pegando a primeira posição da tag <p>, atributo 'class'
        
        title = book.find("h3").find("a").get("title")
        
        price = book.find("div", class_="product_price").find("p", class_="price_color").text

        print(image_url, stars, title, price)   
        books.append([image_url, stars, title, price])