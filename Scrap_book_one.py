# -*- coding: utf8 -*-
import requests
from bs4 import BeautifulSoup
import re
from gazpacho import Soup

url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

response = requests.get(url)

#print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')

#print(soup.prettify())

def getParseUrl(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	return(soup)

title = []
universal_product_coc = []
price_including_tax = []
price_excluding_tax = []
number_available = []
product_description = []
category = []
review_rating =[]
image_url = []

table = soup.find("table", {"class": "table table-striped"}, mode="first")
trs = table.find_all("tr")

if response.ok:
  soup = getParseUrl(url)
  #title :
  title.append(soup.find("div", class_ = re.compile("col-sm-6 product_main")).h1.text)
  # upc :
  # universal_product_coc.append(soup.find("tr", {'id': 'UPC'}).find("t"))

  def parse_tr(tr):
    return {
        "universal_product_coc": tr.find("td")[0].text,
        "price_excluding_tax": tr.find("td")[2].text,
        "price_including_tax": tr.find("td")[3].text,
        "number_available": tr.find("td")[5].text,
        "review_rating": tr.find("td")[-1].text, }
  # number available :
  # how to remove some characters ?
  number_available.append(soup.find("p", class_= re.compile("instock availability")).text)
  # description
  # how to select description <p>
  #product_description.append(soup.find("p", class_=re.compile("product_description")).text)
  # category :
  category.append(soup.find("a", href = re.compile("../category/books/")).text)
  # review rating :

  # image url :
  # how to have all url ?
  image_url.append(soup.find("img").get("src"))
# test github

print(table)
