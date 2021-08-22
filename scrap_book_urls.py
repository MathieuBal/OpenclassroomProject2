import requests
import csv
from bs4 import BeautifulSoup

"""list_page_url = []
page = 1
while page != 5:
      url = f"http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-{page}.html"
      list_page_url.append(url)
      page = page + 1"""


def get_parse_books_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def get_books_links():
    books_links = []
    page = 1
    while True:
        url = f"http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-{page}.html"
        # print('---', "page ", page, '---')
        soup = get_parse_books_url(url)
        list_li_in_ol = soup.find('ol').findAll('li')
        for li in list_li_in_ol:
            books_urls = li.find('a', href=True).get("href").replace("../../../",
                                                                     "http://books.toscrape.com/catalogue/")
            books_links.append(books_urls + '\n')
            # print(books_urls)
            # link to next page
        next_page = soup.find('li', {'class': 'next'})
        if next_page:
            href_next_page = next_page.find('a', href=True).get("href")
            url = url + href_next_page
            page += 1
        else:
            break  # exit `while True`

    return books_links


def write_csv_books_urls_file():
    with open("books_links.csv", "w") as outfile:
        write = csv.writer(outfile)
        write.writerow(get_books_links())
