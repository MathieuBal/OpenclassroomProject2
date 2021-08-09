"""-*- coding: utf8 -*-"""
import re
import csv
import requests
from bs4 import BeautifulSoup



# 1 : request html and html parser
def get_parse_url(url):
    """ use requests and if response is ok use BeautifulSoup to parse """
    url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return(soup)

# 2 : scrap book information
def get_book_info():
    """ liste des "td" """
    tds_list = []
    url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
    soup = get_parse_url(url)
    # title :
    title  = soup.find("div", class_ = re.compile("col-sm-6 product_main")).h1.text
    # find all td in table
    tds_list.append(soup.findAll("td"))
    for td in tds_list :
        # Upc :
        universal_product_coc = (tds_list[0][0].text)
        # price excluding tax :
        price_excluding_tax = (tds_list[0][2].text)
        # price including tax :
        price_including_tax = (tds_list[0][3].text)
        # number available :
        number_available = (tds_list[0][5].text)
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
    book_data = [title, universal_product_coc, price_excluding_tax,
    price_including_tax,  number_available, product_description,
    category, rating + ' out of five', image_url, url]

"""3 : Open and write cvs file"""
def write_csv_file():
    """ creat produit.csv file / write header and book information """
    headername = ['title', 'UPC', 'price_excluding_tax', 'price_including_tax',
    'number_available', 'product_description', 'category', 'review_rating',
    'image_url', 'product_url']
    with open('produit.csv', 'w') as outfile :
        write = csv.writer(outfile)
        write.writerow([headername,])
        write.writerow([book_data,])
