# -*- coding: utf8 -*-
import requests
from bs4 import BeautifulSoup
import re
from gazpacho import Soup
import csv

url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

response = requests.get(url)

#print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')

#print(soup.prettify())

def get_Parse_Url(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	return(soup)

# listes des éléments a récuperer
# title = []
# universal_product_coc = []
# price_including_tax = []
# price_excluding_tax = []
# number_available = []
# product_description = []
# category = []
# review_rating =[]
# image_url = []
# product_url =[]

# liste des "td" 
Tds = []

# liste produit regroupant toutes les infos produits
#produit =[title , universal_product_coc, price_excluding_tax, price_including_tax, number_available, product_description, category, review_rating, image_url]

if response.ok:
  with open('produit.csv', 'w') as outfile :
    write = csv.writer(outfile)
    # creer fichier csv - avec entête.
    # outfile.write('title, universal_product_coc, price_excluding_tax, price_including_tax, number_available, product_description, category, review_rating, image_url\n')

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
        # print("===============================",star)
        rating = star.attrs['class'][-1]
        # print("=====>>>>>>>>",star.attrs['class'])

    # image url :
    image_url = (soup.find("img").get("src").replace("../../","http://books.toscrape.com/"))
    # ajout des infos produit au fichier csv
    write.writerow(['title', 'UPC', 'price_excluding_tax', 'price_including_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url', 'product_url'])
    write.writerow([title, universal_product_coc, price_excluding_tax, price_including_tax,  number_available, product_description, category, rating + ' out of five', image_url, url])

print("fin des programmes", )
