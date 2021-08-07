# -*- coding: utf8 -*-
import requests
from bs4 import BeautifulSoup
import re
from gazpacho import Soup
import csv


# 1 : request html + html parser

def get_Parse_Url(url):
    url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
	  response = requests.get(url)
	  soup = BeautifulSoup(response.text, 'html.parser')
	  return(soup)

# 2 : scrap book information 

def get_book_info():
  # liste des "td" 
  Tds = []
  if response.ok:
    soup = get_Parse_Url(url)
    #title :
    title  = soup.find("div", class_ = re.compile("col-sm-6 product_main")).h1.text
    # find all td in table
    Tds.append(soup.findAll("td"))
    for td in Tds :
      #Upc :
      universal_product_coc = (Tds[0][0].text)
      # price excluding tax :
      price_excluding_tax = (Tds[0][2].text)
      # price including tax :
      price_including_tax = (Tds[0][3].text)
      # number available :
      number_available = (Tds[0][5].text)
    # description
    product_description = soup.find("p", attrs={'class': None}).text.strip()
    # category :
    category = soup.find("a", href = re.compile("../category/books/")).text
    # review rating :
    image_div2 = soup.find('div', attrs={'class': 'col-sm-6 product_main'})
    rating = image_div2.select('p.star-rating')
    for star in rating:
        rating = star.attrs['class'][-1]
    # image url :
    image_url = (soup.find("img").get("src").replace("../../","http://books.toscrape.com/"))

# 3 : Open and write cvs file

def write_csv_file():
  with open('produit.csv', 'w') as outfile :
    write = csv.writer(outfile)
    write.writerow(['title', 'UPC', 'price_excluding_tax', 'price_including_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url', 'product_url'])
    write.writerow([title, universal_product_coc, price_excluding_tax, price_including_tax,  number_available, product_description, category, rating + ' out of five', image_url, url])



