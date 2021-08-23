import requests
import re
import csv
from bs4 import BeautifulSoup


def get_parse_books_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def find_page_number(url):
    soup = get_parse_books_url(url)
    page_number = soup.find('li', {'class': 'current'}).text
    number = page_number.split()[3]
    return number

def get_books_links():
    with open("category_links.csv", "r") as file:
        books_links = []
        category = 1
        print(books_links)
        for row in file:
            print("***** catégories scrapés :", category, " *****")
            category += 1
            page = 1
            url = row.strip()
            while True:
                soup = get_parse_books_url(url)
                print("***** pages livres :", page, " *****")
                check_next_link = soup.find('li', {'class': 'next'})
                if check_next_link:
                    url = url.replace("index", "page-1")
                    pages_books_links = scrap_book(url)
                    for links in pages_books_links:
                        books_links.append(links)
                    check_previous_link = soup.find('li', {'class': 'previous'})
                    if check_previous_link:
                        url = url.replace("page-2", "page-{}").format(page)
                else:
                    page_books_links = scrap_book(url)
                    for links in page_books_links:
                        books_links.append(links)

                    # link to next page
                if check_next_link:
                    number = find_page_number(url)
                    url = url.replace("page-1", "page-2")
                    page += 1

                    #url = url + href_next_page

                else:
                    break  # exit `while True`

    return books_links


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


get_books_links()
