import requests
from bs4 import BeautifulSoup
import csv

# Target website
url = "https://books.toscrape.com/"

# Send request
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Prepare data storage
books = []

# Extract product info
for book in soup.select('article.product_pod'):
    title = book.h3.a['title']
    price = book.select_one('.price_color').text
    rating = book.p['class'][1]  # Example: 'One', 'Two', 'Three', etc.

    books.append({
        'Title': title,
        'Price': price,
        'Rating': rating
    })

# Save to CSV
with open('books.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Title', 'Price', 'Rating'])
    writer.writeheader()
    writer.writerows(books)

print("Data scraped and saved to books.csv")
