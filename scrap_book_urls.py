import requests
import csv
from bs4 import BeautifulSoup


def get_parse_books_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def get_books_links():
    with open("category_links.csv", "r") as file:
        books_links = []
        category = 1
        # print(books_links)
        for row in file:
            print("*****    category:", category, "    *****")
            category += 1
            all_category_books = work_with_one_categorie(row)
            for url in all_category_books:
                books_links.append(url)

    return books_links

def work_with_one_categorie(row):
    one_category_links=[]
    url_base = row.strip().replace("index.html", "")
    url = f"{url_base}index.html"
    while url:
        soup = get_parse_books_url(url)
        pages_books_links = scrap_book(url)
        for links in pages_books_links:
            one_category_links.append(links)
        next_number = soup.find('li', {'class': 'next'})
        if next_number:
            next_link = next_number.find("a", href=True).get("href")
            url = f"{url_base}{next_link}"
        else:
            url = None
    return one_category_links


def scrap_book(url):
    page_links = []
    soup = get_parse_books_url(url)
    list_li_in_ol = soup.find('ol').findAll('li')
    for li in list_li_in_ol:
        books_urls = li.find('a', href=True).get("href").replace("../../../",
                                                                 "http://books.toscrape.com/catalogue/")
        page_links.append(books_urls)
    return page_links


def write_csv_books_urls_file():
    with open("books_links.csv", "w") as outfile:
        for link in get_books_links():
            outfile.write(link + '\n')

