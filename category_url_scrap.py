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
	#category_urls = []
	soup = get_Parse_Url(url)
	ul = soup.find('ul', class_="nav nav-list").findChildren("ul")
	#print (ul)
	for li in ul :
		# soup2 = BeautifulSoup(str(ul), 'html.parser')
		hrefs = li.find_all('a', href=True)
		print(hrefs)	
		#category_urls = (hrefs.get_all("href").replace("catalogue/","http://books.toscrape.com/catalogue/"))
	#print (category_urls)