# -*- coding: utf-8 -*-
import os
import sys
import requests
import bs4
import webbrowser
import time

base_url = 'http://www.jinyongwang.com'


def timer(func):
	# decorator without parameter
	def _timer():
		start_time = time.time()
		func()
		end_time = time.time()
		print("\nTotal time: " + str(end_time - start_time))
	return _timer


def get_soup(url):
	response = requests.get(url)
	try:
		# Connection check
		response.raise_for_status()
	except Exception as exc:
		print('There is a problem: %s' % exc)
	soup = bs4.BeautifulSoup(response.text, "html.parser")
	return soup


def get_page_url(url):
	index_list = []
	soup = get_soup(url)
	# with open('index.html', 'w') as f:
	# 	f.write(soup.prettify())
	index_tag = soup.select('.mlist a')
	# print(len(index_tag))
	for tag in index_tag:
		index_list.append((tag['href'], tag.text))
	return index_list


def get_chapter(url, title, path):
	# url = 'http://www.jinyongwang.com/tian/644.html'
	response = requests.get(url)
	try:
		# Connection check
		response.raise_for_status()
	except Exception as exc:
		print('There is a problem: %s' % exc)

	soup = bs4.BeautifulSoup(response.text, "html.parser")
	content_tag_list = soup.select('#vcon p')
	# with open('tianlong_643.html', 'w') as f:
	# 	f.write(soup.prettify())
	with open(path, 'a') as f:
		f.write(title + '\r\n' * 2)
		for content_tag in content_tag_list:
			content = content_tag.text
			f.write('    ' + content + '\r\n'*2)


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


@timer
def main():
	store_path = '金庸全集'
	if not os.path.exists(store_path):
		os.mkdir(store_path)
	novel_list = get_novel_list(base_url)
	for novel in novel_list:
		url, title = novel
		get_novel(base_url+url, title, store_path)


if __name__ == '__main__':
	main()
