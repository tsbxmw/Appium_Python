#coding=utf-8
from selenium import webdriver

class Caps(object):
	def __init__(self,platformName,platformVersion,deviceName,appPackage,appActivity):
		self.desired_caps = {}
		self.desired_caps['platformName'] = platformName
		self.desired_caps['platformVersion'] = platformVersion
		self.desired_caps['deviceName'] = deviceName
		self.desired_caps['appPackage'] = appPackage
		self.desired_caps['appActivity'] = appActivity
	def connect(self):
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
		return self.driver

	def disconnect(self):
		self.driver.quit()
if __name__ == '__main__':
	caps = Caps('Android','6.0','e26bc444','com.android.calculator2','.Calculator')
	android = caps.connect()

	android.find_element_by_name("1").click()
	caps.disconnect()