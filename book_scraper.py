import requests
from bs4 import BeautifulSoup
import pandas as pd

class Book:
    def __init__(self, title, review, price, image_url):
        self.title = title
        self.review = review
        self.price = price
        self.image_url = image_url

class BookScraper:
    BASE_URL = "https://books.toscrape.com"

    def __init__(self):
        self.books = []
    
    def scraper_category(self, category):
        r = requests.get(f"{self.BASE_URL}/catalogue/category/books/{category}/index.html")
        