# -*- coding: utf-8 -*-
"""
Download manga 5060.
"""
import os,sys,requests,webbrowser
from bs4 import BeautifulSoup
from PIL import Image # Use pillow to handle image files
from selenium import webdriver

main_url = "http://www.manhuagui.com/comic/5060/"
test_url_1 = "http://www.manhuagui.com/comic/5060/249045.html"
downloadNum = 5


def get_soup(url):
	response = requests.get(url)
	try:
		# Connection check
		response.raise_for_status()
		r.encoding = r.apparent_encoding
	except Exception as exc:
		print('There is a problem: %s' % exc)
	print('Downloading page %s ...' % url)
	return BeautifulSoup(response.text, "html.parser")


def download_image(soup):
	"""
	Get url of the comic image.
	Download image.
	:param soup:
	:return:
	"""
	img_elem = soup.select('#comic img')
	if img_elem:
		img_url = 'http:'+img_elem[0].get('src')
		path = os.path.join('xkcd', os.path.basename(img_url))
		if os.path.exists(path):
			print("File %s already exists" % path)
		else:
			print('Downloading image %s ...' % img_url)
			response = requests.get(img_url)
			response.raise_for_status()
			image_file = open(os.path.join('xkcd', os.path.basename(img_url)), 'wb')
			write_file(response, image_file)
			image_file.close()
	else:
		print("Could not find comic image!")


def write_file(response, file):
	"""
	Write response to file.
	:param response:
	:param file:
	:return:
	"""
	for chunk in response.iter_content(10000):
		file.write(chunk)


def prev_url(soup):
	"""
	Return url of Prev button.
	:param soup:
	:return:
	"""
	return main_url + soup.select('.comicNav a[rel="prev"]')[0].get('href')


def img2pdf():
	"""
	Merge all images to pdf.
	:return:
	"""
	pass


def start():
	os.makedirs('xkcd', exist_ok=True)
	url = main_url
	for i in range(downloadNum):
		soup = get_soup(url)
		download_image(soup)
		url = prev_url(soup)
	img2pdf()


'''
soup = get_soup(test_url_1)
img_elem = soup.select('img')
print(img_elem)
'''

browser = webdriver.Firefox()
browser.get(test_url_1)
html = browser.find_element_by_tag_name('img')
print(html)
print(html.get_attribute('src'))

