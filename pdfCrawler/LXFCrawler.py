# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pdfkit

url = "https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"


def url2html(url):
	"""
	Transfer the given url to html file.

	:param url:
	:return html file:
	"""
	response = requests.get(url)
	soup = BeautifulSoup(response.content, "html.parser")
	body = soup.find_all(class_="x-wiki-content")
	print(body)
	'''html = str(body)
	with open("a.html", 'wb') as f:
		f.write(html)'''


url2html(url)
