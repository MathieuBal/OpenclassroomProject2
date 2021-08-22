""" -*- coding: utf8 -*- """
import requests
from bs4 import BeautifulSoup


def get_parse_category_url(url):
	""" use requests and if response is ok use BeautifulSoup to parse """
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	return soup


# scraper les urls des categories
def get_category_urls():
	"""scrap all urls from index page"""
	url = "http://books.toscrape.com/index.html"
	soup = get_parse_category_url(url)
	list_li = soup.find('ul', class_="nav nav-list").find_next("ul").findChildren("li")
	for li in list_li:
		list_links = li.find('a', href=True).get("href").replace("catalogue/", "http://books.toscrape.com/catalogue/")
