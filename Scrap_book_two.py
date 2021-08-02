# -*- coding: utf8 -*-
import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/index.html"

response = requests.get(url)

#print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')

#print(soup.prettify())

def get_Parse_Url(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	return(soup)

# scraper les urls des catégories 

if response.ok:
	category_urls = []
	soup = get_Parse_Url(url)
	ul = soup.findAll('ul', class_="nav nav-list")
	for li in ul :
		soup2 = BeautifulSoup(str(ul), 'html.parser')
		hrefs = soup2.find_all('a', href=True)
		#for href in hrefs :
		    #category_urls.append(hrefs['href'])
	print(hrefs)