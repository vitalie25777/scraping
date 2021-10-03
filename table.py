import requests
from bs4 import BeautifulSoup
# import pandas as pd
import csv

HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}

url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")
# name = soup.find("table", class_="table table-striped").find("tr").find_all("th")
"""content = soup.find("div", class_="col-sm-6 product_main")
titres = []
for product_main in content:
    titres.append({"""

title = soup.find("h1").text,
price = soup.find("p", class_="price_color").text,
stock = soup.find("p", class_="instock availability").text

# })


with open("table.csv", 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=";")
    writer.writerow((title, price, stock))


"""df = pd.DataFrame(title, price, stock)
df.to_csv("titres.csv")
df.to_excel((title, price, stock).xlsx)
print("saved to file")"""
