import requests
from bs4 import BeautifulSoup
import pandas as pd

books = []
for page in range(10):
    print(f'Page parsing: {page}')
    url = f"http://books.toscrape.com/catalogue/category/books/historical-fiction_4/page-/"
    host = "http://books.toscrape.com/catalogue/category/books/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    content = soup.find_all("article", class_="product_pod")

for product_pod in content:
    books.append({

        "titres": product_pod.find("h3").text,
        "prix": product_pod.find("p", class_="price_color").text,
        "links": host + product_pod.find("a").get("href"),
        "images": host + product_pod.find("img", class_="thumbnail").get("src"),

    })

print(books)

df = pd.DataFrame(books)
df.to_csv("books")
df.to_excel("books_2.xlsx")
print("saved to file")
