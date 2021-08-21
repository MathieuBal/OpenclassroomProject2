import requests
from bs4 import BeautifulSoup

list_page_url = []
page = 1
while page != 5:
      url = f"http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-{page}.html"
      list_page_url.append(url)
      page = page + 1


url = "http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


def get_parse_books_url(url):
    """ use requests and if response is ok use BeautifulSoup to parse """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


for url in list_page_url:
    soup = get_parse_books_url(url)
    list_li_in_ol = soup.find('ol').findAll('li')
    for li in list_li_in_ol:
        books_urls = li.find('a', href=True).get("href").replace("../../../", "http://books.toscrape.com/catalogue/")
        print(books_urls)
    """
    for li in list_li:
        list_links = li.find('a', href=True).get("href").replace("catalogue/", "http://books.toscrape.com/catalogue/")
        print(list_links)
"""