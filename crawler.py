#! /usr/bin/python
import random
import requests
import selenium.webdriver.support.ui as ui

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import auth_settings

class Crawler:

	def __init__(self):
		self._proxies = []
		self._nav = []
		self._elements = []
		self.get_proxies('proxies.txt')
		self._headers = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'


	def get_proxies(self,file_name):
		with open(file_name,'r') as f:
			for line in f:
				self._proxies.append(line.strip())

	def walk(self, target, element, wait):
		try:
			wait.until(
				EC.presence_of_element_located((By.CLASS_NAME, element))
				)
			content = driver.find_element_by_class_name(element)
			print "{} amigos".format(content.text)
		finally:
			driver.get(target)

	def crawl(self, url):

		rand = random.SystemRandom()
		proxy = rand.choice(self._proxies)

		profile = webdriver.FirefoxProfile()
		profile.set_preference("general.useragent.override", self._headers)
		
		driver = webdriver.Firefox(profile)
		driver.implicitly_wait(30)
		driver.set_window_size(1180, 980)


		#LOGIN FACEBOOK
		driver.get(url)

		inputElement = driver.find_element_by_id("email")
		inputElement.send_keys(auth_settings.login['email'])
		inputElement = driver.find_element_by_id("pass")
		inputElement.send_keys(auth_settings.login['password'])
		inputElement.submit()

		wait = ui.WebDriverWait(driver,10)
		wait.until(lambda driver: 'welcome' in driver.current_url)

		target = "https://www.facebook.com/lindaliukas"

		driver.get(target)

		for tab, el in zip(self._nav, self._elements):
			walk(target + tab, el wait)
		




if __name__ == '__main__':
	crawler = Crawler()
	crawler.crawl("https://www.facebook.com/")