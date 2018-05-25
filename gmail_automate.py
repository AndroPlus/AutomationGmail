from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import time

class MyTest(object):
	
	def __init__(self):
		self.driver = webdriver.Chrome(executable_path=r"E:/ML/chromedriver.exe")

	def loginGmail(self):			
		self.driver.get("https://mail.google.com/")
		
		self.driver.implicitly_wait(10)
		self.driver.maximize_window()

		emailField = self.driver.find_element(By.XPATH, '//input[@id="identifierId"]')		
		actions = webdriver.ActionChains(self.driver)
		actions.move_to_element(emailField)
		actions.click()
		actions.send_keys("XXX@gmail.com"+Keys.ENTER)
		actions.perform()
		print("Email entered")
		time.sleep(5)

		pwdField = self.driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')		
		actionsPWD = webdriver.ActionChains(self.driver)
		actionsPWD.move_to_element(pwdField)
		actionsPWD.click()
		actionsPWD.send_keys("PWD"+Keys.ENTER)
		actionsPWD.perform()
		print("PWD entered")
		time.sleep(15)
		
		mailThreads = self.driver.find_elements(By.XPATH, '//span[@class="bog"]')	
		print("----")
		print(len(mailThreads))

		for mailItem in mailThreads:
			if "Invitation to Functional Exploratory" in mailItem.text:
				print (mailItem.text)	
				mailItem.click()	
				print ("mail opened..")		

		

	def browserQuit(self):		
		# close the browser window
		self.driver.quit()

myTest = MyTest()
myTest.loginGmail()   
myTest.browserQuit()      