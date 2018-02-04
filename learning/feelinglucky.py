# -*- coding: utf-8 -*-

import sys,requests,bs4,webbrowser


def feelinglucky(kw):
	print('searching...')
	url = 'https://cn.bing.com/search?q=' + kw
	response = requests.get(url)
	try:
		# Connection check
		response.raise_for_status()
	except Exception as exc:
		print('There is a problem: %s' % exc)

	soup = bs4.BeautifulSoup(response.text, "html.parser")

	link_tab = soup.select('.b_algo h2 a')
	# 'b_ad' is the class of advertisement, which need to be excluded.
	# Normal link is under 'b_algo' class, but there is also results
	# under 'b_ans' that may be useful.
	num_open = min(5, len(link_tab))
	for i in range(num_open):
		# print(linkTab[i].get('href'))
		webbrowser.open(link_tab[i].get('href'))


while 1:
	kw = input("Search something, q to quit: ")
	if kw:
		if kw == 'q':
			break
		else:
			kw = ' '.join(sys.argv[1:])
			feelinglucky(kw)
	else:
		print('Invalid input.')