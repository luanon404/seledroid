import time
from seledroid.webdriver.common import utils

class WebDriverWait:
	
	def __init__(self, driver, timeout, ping=0.5):
		self.driver = driver
		self.timeout = timeout
		self.ping = ping
	
	def until(self, method):
		end_time = time.time() + self.timeout
		while True:
			try:
				value = method(self.driver)
				if value:
					return value
			except Exception as ex:
				raise ex
			time.sleep(self.ping)
			if time.time() > end_time:
				break
		utils.exception(TimeoutError, "Time out to wait element")
	
	def until_not(self, method):
		end_time = time.time() + self.timeout
		while True:
			try:
				value = method(self.driver)
				if not value:
					return value
			except Exception as ex:
				raise ex
			time.sleep(self.ping)
			if time.time() > end_time:
				break
		utils.exception(TimeoutError, "Time out to wait element")