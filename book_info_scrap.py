"""-*- coding: utf8 -*-"""
import re
import os
import csv
import requests
import urllib.request
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
        image_folder()
        for row in file:
            #url = row.strip()
            url = "http://books.toscrape.com/catalogue/at-the-existentialist-cafe-freedom-being-and-apricot-cocktails-with-jean-paul-sartre-simone-de-beauvoir-albert-camus-martin-heidegger-edmund-husserl-karl-jaspers-maurice-merleau-ponty-and-others_459/index.html"

            soup = get_parse_url(url)
            print("***** livres scrapés :", livre, " *****")
            livre += 1
            # title :
            title = soup.find("div", class_=re.compile("col-sm-6 product_main")).h1.text
            # find all td in table
            data = soup.findAll("td")
            universal_product_coc = data[0].text
            price_excluding_tax = data[2].text
            price_including_tax = data[3].text
            number_available = data[5].text
            # description
            product_description_link = soup.find("p", attrs={'class': None})
            if product_description_link:
                product_description = product_description_link.text.strip()
            else:
                product_description = "None"
            # category :
            category = soup.find("a", href=re.compile("../category/books/")).text
            # review rating :
            image_div2 = soup.find('div', attrs={'class': 'col-sm-6 product_main'})
            rating = image_div2.select('p.star-rating')
            for star in rating:
                rating = star.attrs['class'][-1]
            # image url :
            image_url = (soup.find("img").get("src").replace("../../", "http://books.toscrape.com/"))
            download_image(row)
            # stock all book info into list :

            book_data = (title, universal_product_coc, price_excluding_tax,
                         price_including_tax, number_available, product_description,
                         category, rating + ' out of five', image_url, url)
            all_book_data.append(book_data)
    return all_book_data

""" image traitement """


def download_image(row):
    # url = row.strip()
    url = "http://books.toscrape.com/catalogue/at-the-existentialist-cafe-freedom-being-and-apricot-cocktails-with-jean-paul-sartre-simone-de-beauvoir-albert-camus-martin-heidegger-edmund-husserl-karl-jaspers-maurice-merleau-ponty-and-others_459/index.html"
    soup = get_parse_url(url)
    image_url = (soup.find("img").get("src").replace("../../", "http://books.toscrape.com/"))
    filename = url.split("/")[4]
    open_image = urllib.request.urlretrieve(image_url, f"{filename}.jpg")
    #read_image = open_image.read()
   # with open(f"books_images/{filename}.jpg", "wb") as img_file:
       # img_file.write(read_image)

def image_folder():
    path = "books_images"
    os.mkdir(path)



""" csv creation """


def write_csv_books_infos_file():
    """ touch produit.csv file / write header and book information """
    header_name = ['title', 'UPC', 'price_excluding_tax', 'price_including_tax',
                   'number_available', 'product_description', 'category', 'review_rating',
                   'image_url', 'product_url']
    with open('products_infos.csv', 'w', encoding='utf-8') as outfile:
        write = csv.writer(outfile)
        write.writerow([header_name, ])
        for book in get_book_info():
            write.writerow(book)

get_book_info()