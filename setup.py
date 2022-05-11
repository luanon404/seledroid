from setuptools import setup

setup(
	name="seledroid",
	version="1.0.2",
	description="simple python module to control browser but for android",
	author="luanon404",
	author_email="luanon404@gmail.com",
	url="https://github.com/luanon404/seledroid",
	python_requires="~=3.7",
	package_dir={
		"seledroid": "seledroid",
		"seledroid.webdriver": "seledroid/webdriver"
	},
	packages=[
		"seledroid",
		"seledroid.webdriver",
		"seledroid.webdriver.chrome",
		"seledroid.webdriver.remote",
		"seledroid.webdriver.common",
		"seledroid.webdriver.support"
	],
	include_package_data=True,
	install_requires=[""],
	zip_safe=False
)
