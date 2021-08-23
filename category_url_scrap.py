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
	category_url = []
	url = "http://books.toscrape.com/index.html"
	soup = get_parse_category_url(url)
	list_li = soup.find('ul', class_="nav nav-list").find_next("ul").findChildren("li")
	lien = 1
	for li in list_li:
		print("***** liens catégories :", lien, " *****")
		list_links = li.find('a', href=True).get("href").replace("catalogue/", "http://books.toscrape.com/catalogue/")
		category_url.append(list_links)
		lien += 1
	return category_url


def write_csv_category_urls_file():
	with open("category_links.csv", "w") as outfile:
		for link in get_category_urls():
			outfile.write(link + '\n')
