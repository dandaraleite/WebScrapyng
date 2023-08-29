from book_scraper import BookScraper

scraper = BookScraper()
scraper.scraper_category("mystery_3", page=1)
scraper.save("mystery_books")

print(scraper.books)
