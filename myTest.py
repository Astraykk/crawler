# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('https://www.baidu.com')

elem = browser.find_element_by_name('wd')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)