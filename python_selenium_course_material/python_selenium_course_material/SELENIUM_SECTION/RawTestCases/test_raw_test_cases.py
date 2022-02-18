from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)

url = 'http://demostore.supersqa.com/my-account/'
driver.get(url)