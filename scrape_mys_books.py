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
        
        #Pegando o preço e tratando o modo como ele vai ser exibido
        price = (
        book.find("div", class_="product_price")
        .find("p", class_="price_color")
        .text.replace("Â", "")
        )

        #print(image_url, stars, title, price)   
        books.append([title, stars, price, image_url])

        #Tratando os dados com a biblioteca pandas
        df = pd.DataFrame(data=books, columns=["Title", "Stars", "Price", "Image_URL"]) #passando pra dataframe
        df = df.sort_values(by="Title") #ordenando alfabeticamente pelos títulos
        #df = df.drop(column="Image_URL", axis = 1) #excluindo coluna "Image_URL"
        #print(df)

        #Passando o dataframe para o formato .csv
        df.to_csv("scrape_mystery_books.csv")

        df = pd.read_csv("scrape_mystery_books.csv", index_col=0)

        #Iterando somente entre as colunas "Title, Stars e Price"
        for index, book in df.iterrows():
            df = index, book[["Title", "Stars", "Price"]]
            print(df)

       

