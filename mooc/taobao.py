import requests, re
from bs4 import Beautifulsoup

url = "https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180328&ie=utf8"

def getHTMLText():
	try:
		r = requests.get(url, timeout=30)
		# Connection check
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except Exception as exc:
		print('There is a problem: %s' % exc)
		return ""


def parsePage(ilt, html):
	try:
		plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
		tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
		for i in range(len(plt)):
			price = eval(plt[i].split(':')[1])
			title = eval(tlt[i].split(':')[1])
			ilt.append([price, title])
	except:
		print("")



def printGoodList():
	pass


def main():
	goods = '书包'
	depth = 2
	start_url = 'https://s.taobao.com/search?q=' + goods
	infoList = []
	for i in range(depth):
		try:
			url = start_url + '&s=' + str(44*i)
			html = getHTMLText(url)
			parsePage(infoList, html)

