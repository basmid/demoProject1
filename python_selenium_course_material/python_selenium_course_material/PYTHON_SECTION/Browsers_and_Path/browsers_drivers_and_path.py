from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#option 1 (Selenium 3)
#driver = webdriver.Chrome(executable_path="C:/Users/basmi/chromedriver.exe")
#driver.get("https://www.google.com")

#option 1 (Selenium 4)
# se = Service(executable_path="C:/Users/basmi/chromedriver.exe")
# driver = webdriver.Chrome(serivce=se)

#option 2 is adding the executable to system path
