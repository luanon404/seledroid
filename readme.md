Seledroid WebDriver
======================

Important
---------

Termux support only.

I use java and javascript to do the task so sometime it won't really work.

So if you get any errors just free open issue.

Introduction
------------

Instead of needing pc to use selenium you just need a smart phone to use seledroid.

Everything is simple, no need for any dependencies.

Supported Python Versions
-------------------------

* Python 3.7+

Installing
----------

#### Step 1

``` git clone https://github.com/luanon404/seledroid ```

#### Step 2

``` cd seledroid ```

#### Step 3

``` python setup.py install ```

#### Or just use this short command

``` git clone https://github.com/luanon404/seledroid && cd seledroid && python setup.py install ```

Drivers
-------

You can download driver at [here](https://github.com/luanon404/seledroid-drivers).

Example 0
---------

```
from seledroid import webdriver
driver = webdriver.Chrome()
driver.get("http://demo.t3-framework.org/joomla30/index.php/en/joomla-pages/sample-page-2/login-page")
elem = driver.find_element_by_id("remember")
elem.click()
driver.implicitly_wait(5)
driver.close()
```


