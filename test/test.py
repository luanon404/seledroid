import time
from seledroid import webdriver

driver = webdriver.Chrome()

printf = lambda x: print("\033[1;32m=>", x, "\033[1;0m")

print("test .close()")
if input("enter to execute or 'no' => ") == "":
 driver.close()
 print(".close() called")

print("\ntest .get(url)")
if input("enter to execute or 'no' => ") == "":
 driver.get("https://example.com")
 print(".get(url) called")

print("\ntest .title")
if input("enter to execute or 'no' => ") == "":
 printf(driver.title)
 print(".title called")

print("\ntest .current_url")
if input("enter to execute or 'no' => ") == "":
 printf(driver.current_url)
 print(".current called")

print("\ntest .page_source")
if input("enter to execute or 'no' => ") == "":
 printf(driver.page_source)
 print(".page_source called")

print("\ntest .user_agent")
if input("enter to execute or 'no' => ") == "":
 printf(driver.user_agent)
 print(".user_agent called")

print("\ntest set .user_agent")
if input("enter to execute or 'no' => ") == "":
 driver.user_agent = ".user_agent"
 driver.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
 print("set .user_agent called")

print("\ntest .headers")
if input("enter to execute or 'no' => ") == "":
 printf(driver.headers)
 print(".headers called")

print("\ntest set .headers")
if input("enter to execute or 'no' => ") == "":
 driver.headers = {"User-Agent": ".headers", "a": "hello", "Accept-Encoding": "change"}
 driver.get("https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending")
 printf(driver.headers)
 if input("browserleaks or 'no' => ") == "":
  driver.get("https://browserleaks.com/canvas")
 print("set .headers called")

print("\ntest .execute_script(script)")
if input("enter to execute or 'no' => ") == "":
 printf("1 + 1 = %s" %driver.execute_script("1+1"))
 printf("alert(\"1+1\")")
 driver.execute_script("alert(\"1+1\")")
 print(".execute_script(script) called")

print("\ntest .wait(delay)")
if input("enter to execute or 'no' => ") == "":
 printf(driver.wait(3))
 print(".wait(delay) called")

if input("\nopen test paint or 'no' => ") == "":
 driver.get("https://rbyers.github.io/paint.html")

print("\ntest .click_java(x,y)")
if input("enter to execute or 'no' => ") == "":
 printf(driver.click_java(400,400))
 print(".wait(delay) called")

print("\ntest .swipe_down()")
if input("enter to execute or 'no' => ") == "":
 printf(driver.swipe_down())
 print(".swipe_down() called")

print("\ntest .swipe_up()")
if input("enter to execute or 'no' => ") == "":
 printf(driver.swipe_up())
 print(".swipe_up() called")

print("\ntest .swipe(xStart, yStart, xEnd, yEnd, speed)")
if input("enter to execute or 'no' => ") == "":
 printf(driver.swipe(100, 100, 500, 500, 3))
 print(".swipe(xStart, yStart, xEnd, yEnd, speed) called")

print("\ntest .scroll_to(x, y)")
if input("enter to execute or 'no' => ") == "":
 driver.get("http://demo.t3-framework.org/joomla30/index.php/en/joomla-pages/sample-page-2/login-page")
 driver.wait(5)
 printf(driver.scroll_to(0, 500))
 print(".scroll_to(x, y) called")

print("\ntest .set_proxy(host, port)")
if input("enter to execute or 'no' => ") == "":
 printf(driver.set_proxy(*input().split(":")))
 driver.get("https://api.myip.com/")
 print(".set_proxy(host, port) called")

if input("\nopen test cookie or 'no' => ") == "":
 driver.get("http://www.cookiecentral.com/code/eg1.htm")

print("\ntest .set_cookie(cookie_name, value, url=\"\")")
if input("enter to execute or 'no' => ") == "":
 printf(driver.set_cookie("heo", "map"))
 print(".set_cookie(cookie_name, value, url=\"\") called")

print("\ncreate new cookie bro")

print("\ntest .get_cookies(url=\"\")")
if input("enter to execute or 'no' => ") == "":
 printf(driver.get_cookies())
 print(".get_cookies() called")

print("\ntest .get_cookie(cookie_name, url=\"\")")
if input("enter to execute or 'no' => ") == "":
 printf(driver.get_cookie("heo"))
 print(".get_cookie(cookie_name, url=\"\") called")

print("\ntest .clear_cookie(cookie_name, url=\"\")")
if input("enter to execute or 'no' => ") == "":
 printf(driver.clear_cookie("heo"))
 print(".clear_cookie(cookie_name, url=\"\") called")
 printf(driver.get_cookies())

print("\ntest .clear_cookies(url) google.com")
if input("enter to execute or 'no' => ") == "":
 printf(driver.get_cookies("https://google.com"))
 printf(driver.clear_cookies("https://google.com"))
 print(".clear_cookies(url) called")
 printf(driver.get_cookies("https://google.com"))

print("\ntest .clear_cookies(url) current url")
if input("enter to execute or 'no' => ") == "":
 printf(driver.get_cookies())
 printf(driver.clear_cookies())
 print(".clear_cookies(url) called")
 printf(driver.get_cookies())

print("\ntest .delete_all_cookie()")
if input("enter to execute or 'no' => ") == "":
 printf(driver.delete_all_cookie())
 print(".delete_all_cookie() called")
 printf(driver.get_cookies())

print("\ntest .find_elements(by, value)")
if input("enter to execute or 'no' => ") == "":
 printf(driver.find_elements("css selector", "input"))
 print(".find_elements(by, value) called")

print("\ntest .find_element(by, value)")
if input("enter to execute or 'no' => ") == "":
 printf(driver.find_element("css selector", "input"))
 print(".find_element(by, value) called")

if input("\nopen test login form or 'no' => ") == "":
 driver.get("http://demo.t3-framework.org/joomla30/index.php/en/joomla-pages/sample-page-2/login-page")

print("\ntest .click()")
if input("enter to execute or 'no' => ") == "":
 printf(driver.find_element("id", "remember").click())
 print(".click() called")

print("\ntest .click_java()")
if input("enter to execute or 'no' => ") == "":
 driver.wait(5)
 printf(driver.find_element("id", "remember").click_java())
 print(".click_java() called")

print("\ntest .disabled")
if input("enter to execute or 'no' => ") == "":
 printf(driver.find_element("id", "username").disabled)
 print(".disabled called")

print("\ntest set .disabled")
if input("enter to execute or 'no' => ") == "":
 driver.find_element("id", "username").disabled = False
 printf("disabled == " + str(driver.find_element("id", "username").disabled))
 print("set .disabled called")

print("\ntest .position")
if input("enter to execute or 'no' => ") == "":
 printf(driver.find_element("id", "username").position)
 print(".position called")

print("\ntest .is_displayed")
if input("enter to execute or 'no' => ") == "":
 printf(driver.find_element("id", "username").is_displayed)
 print(".is_displayed called")

print("\ntest .read_only")
if input("enter to execute or 'no' => ") == "":
 printf(driver.find_element("id", "username").read_only)
 print(".read_only called")

print("\ntest .value")
if input("enter to execute or 'no' => ") == "":
 printf(driver.find_element("id", "username").value)
 print(".value called")

print("\ntest set .value")
if input("enter to execute or 'no' => ") == "":
 driver.find_element("id", "username").value = "test123"
 printf("value == " + str(driver.find_element("id", "username").value))
 print("set .value called")

print("\ntest .send_text(text)")
if input("enter to execute or 'no' => ") == "":
 driver.wait(5)
 printf(driver.find_element("id", "username").send_text("hello hi"))
 print(".send_text(text) called")

print("\ntest .clear()")
if input("enter to execute or 'no' => ") == "":
 printf(driver.find_element("id", "username").clear())
 print(".clear() called")

print("\ntest .send_key(key)")
if input("enter to execute or 'no' => ") == "":
 driver.wait(5)
 printf(driver.find_element("id", "username").send_key(66))
 print(".send_key(key) called")

print("\ntest .width")
if input("enter to execute or 'no' => ") == "":
 printf(driver.find_element("id", "username").width)
 print(".width called")

print("\ntest .height")
if input("enter to execute or 'no' => ") == "":
 printf(driver.find_element("id", "username").height)
 print(".height called")

print("\ntest .outer_html")
if input("enter to execute or 'no' => ") == "":
 printf(driver.find_element("id", "username").outer_html)
 print(".outer_html called")

print("\ntest .inner_html")
if input("enter to execute or 'no' => ") == "":
 printf(driver.find_element("id", "username").inner_html)
 print(".inner_html called")

print("\ntest set .inner_html")
if input("enter to execute or 'no' => ") == "":
 driver.find_element("id", "username").inner_html = ":))"
 printf(driver.find_element("id", "username").outer_html)
 print("set .inner_html called")
