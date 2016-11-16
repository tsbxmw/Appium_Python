#coding=utf-8
from appium import webdriver

class Caps(object):

	def __init__(self,platformName,platformVersion,deviceName,appPackage,appActivity):
		self.desired_caps = {}
		self.desired_caps['platformName'] = platformName
		self.desired_caps['platformVersion'] = platformVersion
		self.desired_caps['deviceName'] = deviceName
		self.desired_caps['appPackage'] = appPackage
		self.desired_caps['appActivity'] = appActivity

	def connect(self):
		try:
			self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
			print("connect successful!")
			return self.driver
		except Exception ,e:
			print("connect failed!")
			raise(e)

	def disconnect(self):
		try:
			self.driver.quit()
			print("disconnect successful!")
		except Exception ,e:
			print("disconnect failed!")
			raise(e)