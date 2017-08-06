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
		self._driver = None
		self._wait = None
		self._headers = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'

	def initialize_webdriver(self):
		profile = webdriver.FirefoxProfile()
		profile.set_preference("general.useragent.override", self._headers)
		
		self._driver = webdriver.Firefox(profile)
		self._driver.implicitly_wait(30)
		self._driver.set_window_size(1180, 980)

		self._wait = ui.WebDriverWait(self._driver,10)

	def login(self):
		inputElement = self._driver.find_element_by_id("email")
		inputElement.send_keys(auth_settings.auth['email'])
		inputElement = self._driver.find_element_by_id("pass")
		inputElement.send_keys(auth_settings.auth['password'])
		inputElement.submit()

		self._wait.until(lambda driver: 'welcome' in driver.current_url)

	def get_friends(self, url):
		try:
			self._wait.until(
				EC.presence_of_element_located((By.CLASS_NAME, "_39g5"))
				)
			content = self._driver.find_element_by_class_name("_39g5")
			print "{} amigos".format(content.text)
		finally:
			self._driver.get(url)



	def crawl(self, url):

		self.initialize_webdriver()

		#LOGIN FACEBOOK
		self._driver.get(url)

		self.login()

		target = "https://www.facebook.com/lindaliukas"

		self._driver.get(target)

		self.get_friends(target + "/photos_albums")



if __name__ == '__main__':
	crawler = Crawler()
	crawler.crawl("https://www.facebook.com/")