# -*- coding: utf-8 -*-

"""
Learning web crawler! Based on the book.
"""

import requests
from bs4 import BeautifulSoup
import pdfkit

url1 = "http://www.gutenberg.org/ebooks/1777.txt.utf-8"


def my_crawler_1(url):
	"""
	Test basic utilization of requests module.
	:param url:
	:return:
	"""
	response = requests.get(url)
	try:
		response.raise_for_status()
	except Exception as exc:
		print('There is a problem: %s' % exc)

	file = open('Romeo and Juliet by William Shakespeare.txt', 'wb')
	for chunk in response.iter_content(100000):
		file.write(chunk)
	file.close()


url2 = 'http://www.gutenberg.org/ebooks/1777'


def bs_test_1(url):
	response = requests.get(url)
	try:
		response.raise_for_status()
	except Exception as exc:
		print('There is a problem: %s' % exc)

	soup = BeautifulSoup(response.text)
	element = []
	element.append(soup.select('div'))
	element.append(soup.select('#download'))
	element.append(soup.select('.files'))
	element.append(soup.select('div ul'))
	element.append(soup.select('td > a'))
	element.append(soup.select('table[summary]'))
	element.append(soup.select('a[class="link"]'))

	'''
	for item in element:
		if item:
			print('Element %s\'s content:' % element.index(item))
			print(len(item), type(item), type(item[0]))
			# print(item)
		else:
			print('Element %s not found.' % element.index(item))
	'''
	print(len(element[6]))
	for item in element[6]:
		print(item)


""" Practicing area """

# my_crawler_1(url1)
# bs_test_1(url2)
