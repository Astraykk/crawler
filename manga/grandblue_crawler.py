# -*- coding: utf-8 -*-
import os
import requests
import bs4
import time
from PIL import Image
from io import BytesIO
from selenium import webdriver
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,landscape
import random


base_url = 'https://www.manhuagui.com/comic/12887/244203.html'
image_base_url = 'https://i.hamreus.com/ps1/g/GrandBlue/{}/{}.jpg.webp?cid=244203&md5=T-VJxMiAZJJNfFLN4hWFlQ'
headers = {
		'Referer': 'https://www.manhuagui.com/comic/12887/244203.html',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
	}


def timer(func):
	# decorator without parameter
	def _timer():
		start_time = time.time()
		func()
		end_time = time.time()
		print("\nTotal time: " + str(end_time - start_time))
	return _timer


def get_soup(url):
	response = requests.get(url, headers=headers)
	try:
		# Connection check
		response.raise_for_status()
	except Exception as exc:
		print('There is a problem: %s' % exc)
	soup = bs4.BeautifulSoup(response.text, "html.parser")
	return soup


def get_chapter_info(url):
	"""
	Get url, cid for each chapter
	:param url:
	:return:
	"""
	browser = webdriver.Firefox()
	browser.get(base_url)
	html = browser.page_source
	soup = bs4.BeautifulSoup(html, 'html.parser')
	print(type(soup))
	with open('juan_1_selenium.html', 'w') as f:
		f.write(soup.prettify())


def get_pic(path, format_url, chapter, page):
	cnt = 0
	# suc_list = []
	page_list = [
		'{}-{:03}'.format(chapter, page),
		'{}-{:03}_1'.format(chapter, page),
		'{}-{:03}_2'.format(chapter, page)
	]
	for i, page in enumerate(page_list):
		url = format_url.format(chapter, page)
		r = requests.get(url, headers=headers)
		print('Downloading chapter {}, page {} ...'.format(chapter, page))
		try:
			# Connection check
			r.raise_for_status()
			# suc_list.append(page)
			pic_path = os.path.join(path, chapter, page+'.jpg')
			save_pic(pic_path, r.content)
			time.sleep(0.2)
			cnt += 1
			# if not i:
			# 	break
		except Exception as exc:
			print('There is a problem: %s' % exc)
	# suc_list.sort()
	# print(suc_list)
	# print(len(suc_list))
	# for i in range(1, len(suc_list)-1):
	# 	if suc_list[i][:3] == suc_list[i+1][:3] and suc_list[i][:3] == suc_list[i-1][:3]:
	# 		print(suc_list[i])
	return cnt


def get_novel(url, title, path):
	path = os.path.join(path, title+'.txt')
	if os.path.isfile(path):
		print(title, 'already exists.')
		return
	index_list = get_page_url(url)
	if title == '雪山飞狐' or title == '射雕英雄传':
		index_list.reverse()
		print(index_list)
	for index in index_list:
		page_url, chapter_title = index
		get_chapter(base_url + page_url, chapter_title, path)
		time.sleep(.200)
	print(title, 'finished!')


def get_novel_list(url):
	novel_list = []
	soup = get_soup(url)
	# with open('main.html', 'w') as f:
	# 	f.write(soup.prettify())
	novel_tag = soup.select('#book_ul li .book_li_title a')
	# print(novel_tag)
	# print(len(novel_tag))
	for tag in novel_tag:
		novel_url = tag['href']
		title = tag.text.rsplit('小说')[0]
		novel_list.append((novel_url, title))
		# print(novel_url, title)
	return novel_list


def save_pic(path, content):
	img = Image.open(BytesIO(content))
	dir_name = os.path.dirname(path)
	if not os.path.exists(dir_name):
		os.makedirs(dir_name)
	if os.path.isfile(path):
		return
	else:
		img.save(path)


def gen_pdf(pdf_path, img_path):
	image_list = os.listdir(img_path)
	image_list.sort()
	print(len(image_list))
	c = canvas.Canvas(pdf_path)
	for image in image_list:
		path = os.path.join(img_path, image)
		img = Image.open(path)
		w, h = img.size
		c.setPageSize((w,h))
		c.drawImage(path, 0, 0, w, h)
		c.showPage()
	c.save()


def test():
	url = image_base_url.format('01', '01-084_1')
	# r = requests.get(url, headers=headers)
	# try:
	# 	# Connection check
	# 	r.raise_for_status()
	# except Exception as exc:
	# 	print('There is a problem: %s' % exc)
	# print(r.content)
	# save_pic('data/01/084_1.jpg', r.content)

	cnt = 0
	chap = '01'
	short_list = []
	for page in range(101):
		num = get_pic('data', image_base_url, chap, page)
		if num == 3:
			short_list.append(page)
		cnt += num
	print(cnt)
	print(short_list)

	# gen_pdf('data/GRANDBLUE-01.pdf', 'data/01')


def main():
	pass


if __name__ == '__main__':
	test()
