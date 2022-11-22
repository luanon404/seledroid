Seledroid WebDriver
======================

Stop update
-----------
You can join my [telegram group](https://t.me/RHToolCommunity) to follow me making a webdriver uwu.
I really want to upgrade it but my current knowledge doesn't allow it, this is 100% my self build, I hope you guys like it, just use this code to continue, its free, thanks :)

Welcome
-------

Hi i'm luanon404, i'm the first one to do this crazy thing :], have you ever thought about running selenium on your phone? I guess I'm the only one who thinks that :D, that's how this library is made, enjoy it.

Support
-------

Telegram: [here](https://t.me/RHToolCommunity)

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

You can download driver at [here](https://github.com/luanon404/android-drivers).

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
elem.send_key(Keys.ENTER)
driver.wait(10)
driver.close()
```
