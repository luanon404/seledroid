Seledroid WebDriver
======================

###### I dont know how to create document

Important
---------

**All is my own build include driver**

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

#### Pypi Install

```pip install seledroid```

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
driver.wait(10)
driver.close()
```

Example 1
---------

```
from seledroid import webdriver
from seledroid.webdriver.common.by import By
from seledroid.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://google.com")
elem = driver.find_element(By.NAME, "q")
elem.send_text("seledroid")
elem.send_keys(Keys.ENTER)
driver.wait(10)
driver.close()
```

Update
------

[update 1.0.6](https://github.com/luanon404/seledroid/issues/13)

[update 1.0.5](https://github.com/luanon404/seledroid/issues/11)

[update 1.0.4](https://github.com/luanon404/seledroid/issues/9)

[update 1.0.3](https://github.com/luanon404/seledroid/issues/7)

[update 1.0.2](https://github.com/luanon404/seledroid/issues/6)

[update 1.0.1](https://github.com/luanon404/seledroid/issues/3)
