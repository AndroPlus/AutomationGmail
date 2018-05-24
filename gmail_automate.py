from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class MyTest(object):
	
	def __init__(self):
		options = Options()
		self.driver = webdriver.Firefox(firefox_options=options, executable_path='D:\Ram\geckodriver.exe')

	def loginGmail(self):			
		self.driver.get("https://mail.google.com/")
		self.driver.implicitly_wait(10)
		self.driver.maximize_window()

		lists = self.driver.find_elements_by_class_name("bog")
		# get the number of elements found
		print ("Found " + str(len(lists)))

	def browserQuit(self):		
		# close the browser window
		self.driver.quit()

myTest = MyTest()
myTest.loginGmail()   
myTest.browserQuit()      