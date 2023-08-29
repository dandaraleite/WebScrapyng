import requests
from bs4 import BeautifulSoup
import pandas as pd

class Book:
    def __init__(self, title, review, price, image_url):
        self.title = title
        self.review = review
        self.price = price
        self.image_url = image_url

    def __repr__(self):
        return f"<Book {self.title}>"

class BookScraper:
    BASE_URL = "https://books.toscrape.com"

    def __init__(self):
        self.books = []
    
    def scraper_category(self, category, page=1):
        r = requests.get(
            f"{self.BASE_URL}/catalogue/category/books/{category}/page-{page}.html"
            )

        if r.status_code == 200:
            page_content = r.text
            html = BeautifulSoup(page_content, "html.parser")

            # Inspecionando a tag que contém os livros e suas propriedades do livro #section
            book_section = html.find("section")

            for book in book_section.find("ol").select("li"):
                image_url = book.find("div", class_="image_container").find("img").get("src")
                
                review = book.find("p").get("class")[1] #Pegando a primeira posição da tag <p>, atributo 'class'
                
                title = book.find("h3").find("a").get("title")
                
                #Pegando o preço e tratando o modo como ele vai ser exibido
                price = (
                book.find("div", class_="product_price")
                .find("p", class_="price_color")
                .text.replace("Â", "")
                )

                self.books.append(
                    Book(title=title, review=review, price=price, image_url=image_url)
                )
            
            if self.__has_next(page_content):
                self.scraper_category(category, page + 1)
    
    def __has_next(self, html):
        soup = BeautifulSoup(html, "html.parser")

        next_button = soup.find_all("li.next a")

        return not next_button is None
    
    def save(self, name):
        data = []

        for book in self.books:
            data.append([book.title, book.review, book.price, book.image_url])

        df = pd.DataFrame(data=data, columns=["Title", "Review", "Price", "Image"])

        df.to_csv(name)