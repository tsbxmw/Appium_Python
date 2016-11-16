#coding=utf-8
from appium import webdriver
from Caps import Caps

if __name__ == '__main__':
	caps = Caps('Android','6.0','e26bc444','com.example.app_test','.StartShow')
	android = caps.connect()
	android.wait_activity(".MainActivity",10,interval=1)
	
	android.find_element_by_name("1").click()
	caps.disconnect()