import requests
from bs4 import BeautifulSoup
#from openpyxl.workbook import Workbook
import pandas as pd

books = []
pagenation = input("Spécifier le nombre des pages pour parsing: ")
pagenation = int(pagenation.strip())
for i in range(0, pagenation):
    print(f'Page parsing: {i}')

    url = f'http://books.toscrape.com/catalogue/category/books_1/page-{i}.html'
    host = "http://books.toscrape.com/catalogue/category"
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
df.to_excel("books_3.xlsx")
print("saved to file")
