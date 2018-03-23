import requests

url = "https://item.jd.com/2967929.html"
r = requests.get(url)
try:
	# Connection check
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[:1000])
except Exception as exc:
	print('There is a problem: %s' % exc)
