from book_scraper import BookScraper

scraper = BookScraper()
scraper.scraper_category("mystery_3")

print(scraper.books)