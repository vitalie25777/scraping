
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

url = "http://books.toscrape.com/catalogue/a-summer-in-europe_458/index.html"
r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

book_info = {
    "title": soup.find("h1").text,
    "price": soup.find("p", class_="price_color").text,
    "prod_info": pd.read_html(url),
    "url": url,
    "image": "http://books.toscrape.com/" + soup.find("img").get("src")
}
print(book_info)

df = pd.DataFrame(book_info)
df.to_csv("book_info")
df.to_excel(book_info.xlsx)
print("saved to file")
