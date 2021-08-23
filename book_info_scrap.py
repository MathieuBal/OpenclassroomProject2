"""-*- coding: utf8 -*-"""
import re
import csv
import requests
from bs4 import BeautifulSoup


def get_parse_url(url):
    """ use requests and if response is ok use BeautifulSoup to parse """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def get_book_info():
    """ scrap all books information """
    with open("books_links.csv", "r") as file:
        all_book_data = []
        livre = 1
        for row in file:
            url = row.strip()
            soup = get_parse_url(url)
            print("***** livres scrapés :", livre, " *****")
            # title :
            title = soup.find("div", class_=re.compile("col-sm-6 product_main")).h1.text
            # find all td in table
            data = soup.findAll("td")
            universal_product_coc = data[0].text
            price_excluding_tax = data[2].text
            price_including_tax = data[3].text
            number_available = data[5].text
            # description
            product_description = soup.find("p", attrs={'class': None}).text.strip()
            # category :
            category = soup.find("a", href=re.compile("../category/books/")).text
            # review rating :
            image_div2 = soup.find('div', attrs={'class': 'col-sm-6 product_main'})
            rating = image_div2.select('p.star-rating')
            for star in rating:
                rating = star.attrs['class'][-1]
            # image url :
            image_url = (soup.find("img").get("src").replace("../../", "http://books.toscrape.com/"))
            # stock all book info into list :

            book_data = (title, universal_product_coc, price_excluding_tax,
                         price_including_tax, number_available, product_description,
                         category, rating + ' out of five', image_url, url)
            all_book_data.append(book_data)
    return all_book_data


def write_csv_books_infos_file():
    """ touch produit.csv file / write header and book information """
    header_name = ['title', 'UPC', 'price_excluding_tax', 'price_including_tax',
                   'number_available', 'product_description', 'category', 'review_rating',
                   'image_url', 'product_url']
    with open('products_infos.csv', 'w') as outfile:
        write = csv.writer(outfile)
        write.writerow([header_name, ])
        write.writerow(get_book_info())
