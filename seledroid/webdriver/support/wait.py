import os
import time
import threading
from seledroid.webdriver.common import utils

class WebDriverWait:
	
	def __init__(self, driver, timeout):
		self.driver = driver
		self.timeout = timeout
		self.kill = True
	
	def time(self):
		end_time = time.time() + self.timeout
		while True:
			if time.time() > end_time:
				utils.exception(TimeoutError, "Time out to wait element", no_exit=True)
				if self.kill:
					os._exit(2)
		
	def until(self, method):
		threading.Thread(target=self.time, daemon=True).start()
		while True:
			try:
				value = method(self.driver)
				if value:
					self.kill = False
					return value
			except Exception as ex:
				raise ex
	
	def until_not(self, method):
		threading.Thread(target=self.time, daemon=True).start()
		while True:
			try:
				value = method(self.driver)
				if not value:
					self.kill = False
					return value
			except Exception as ex:
				raise ex