import html
import base64

from seledroid.webdriver.remote.web_element import WebElement

#----------global const----------#
no_encode_again = False
#----------global const----------#

def exception(type_, msg="", shut_up=False):
	if not shut_up:
		print("< %s :: %s >" %(type_.__name__, msg))
	exit()

def decode_data(data):
	try:
		return html.unescape(data.decode("unicode-escape").encode("latin1").decode("utf8"))
	except Exception:
		try:
			return data.decode("unicode-escape").encode("latin1").decode("utf8")
		except Exception:
			return data

def b64encode(value):
	value = value.encode() if type(value) == str else ("%s" %value).encode()
	return decode_data(base64.b64encode(value))

def b64decode(value):
	value = value.encode() if type(value) == str else ("%s" %value).encode()
	result = decode_data(base64.b64decode(value))
	try:
		if result in ["null", "undefined"]:
			result = None
		if result in ["true", "false"]:
			result = result.capitalize()
		return eval(result)
	except Exception:
		return result

class DictMap(dict):
	
	def __init__(self, *args, **kwargs):
		global no_encode_again
		if "no_encode_again" in args:
			no_encode_again = True
			args = [arg for arg in args if "no_encode_again" != arg]
		args = [arg for arg in args if arg]
		super(DictMap, self).__init__(*args, **kwargs)

		if args:
			for arg in args:
				if isinstance(arg, dict):
					for key, value in arg.items():
						self[key] = DictMap(value) if isinstance(value, dict) else value
						
		if kwargs:
			for key, value in kwargs.items():
				self[key] = DictMap(value) if isinstance(value, dict) else value
		no_encode_again = False
	
	def __getattr__(self, attr):
		return b64decode(self.get(attr))
	
	def __getitem__(self, key):
		super(DictMap, self).__getitem__(key)
		return b64decode(self.__dict__.get(key))
	
	def __getattribute__(self, attr):
		if attr in self:
			return b64decode(self.__dict__[attr])
		return super(DictMap, self).__getattribute__(attr)
	
	def __setattr__(self, key, value):
		self.__setitem__(key, value)
	
	def __setitem__(self, key, value):
		if not no_encode_again:
			value = b64encode(value)
		super(DictMap, self).__setitem__(key, value)
		self.__dict__.update({key: value})
	
	def __delattr__(self, item):
		self.__delitem__(item)
	
	def __delitem__(self, key):
		super(DictMap, self).__delitem__(key)
		del self.__dict__[key]

def presence_of_element_located(locator):
	def _predicate(driver, locator):
		try:
			driver.shut_up = True
			locator = driver.find_element(*locator)
			driver.shut_up = False
			return locator
		except SystemExit:
			return False # no element in page
	return lambda driver: _predicate(driver, locator)

def visibility_of_element_located(locator):
	def _predicate(driver, locator):
		try:
			driver.shut_up = True
			locator = driver.find_element(*locator)
			driver.shut_up = False
		except SystemExit:
			return False # no element in page
		if locator.is_displayed == True:
			return locator
		else:
			return False
	return lambda driver: _predicate(driver, locator)
	
def element_to_be_clickable(locator):
	def _predicate(driver, locator):
		if not isinstance(locator, WebElement):
			try:
				driver.shut_up = True
				locator = driver.find_element(*locator)
				driver.shut_up = False
			except SystemExit:
				return False # no element in page
		if locator.is_displayed == True and locator.is_disabled == False:
			return locator
		else:
			return False
	return lambda driver: _predicate(driver, locator) # dont ask why