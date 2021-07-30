# -*- coding: utf8 -*-
import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/index.html"

def get_Parse_Url(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	return(soup)

	soup = get_Parse_Url(url)
	print(response.text)