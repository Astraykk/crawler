import requests, sys
from bs4 import BeautifulSoup

url = "http://m.ip138.com/"  # Some ip search website
local_ip = "202.120.224.91"  # Get local ip

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

def ip_valid(ip):
	pass

def search_ip(ip=local_ip):
	if ip_valid(ip):
		pass


if __name__ = '__main__':
	if sys.argv < 2:
		search_ip()
	else:
		search_ip(sys.argv[1])