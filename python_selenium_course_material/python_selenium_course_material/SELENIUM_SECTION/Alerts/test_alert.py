
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
url = 'C:///Users/basmi/demoProject1/python_selenium_course_material/python_selenium_course_material/SELENIUM_SECTION/Alerts/alerts_example.html'
driver.get(url)

# alert_1_btn = driver.find_element('css selector','div#jsAlertExample button')
# alert_1_btn.click()
# my_alert = driver.switch_to.alert
# import pdb; pdb.set_trace()

#Ex 2

my_js_confirm_btn = driver.find_element('css selector', 'div#jsPromptExample button').send_keys("Selenium")
time.sleep(5)
my_js_confirm_btn = driver.switch_to.alert
my_js_confirm_btn.click()
#my_js_confirm_btn.send_keys(Keys.RETURN)
#my_js_confirm_btn.clear()

# my_js_confirm_btn.send_keys("Bas akkoord")
# my_js_confirm_btn.send_keys(Keys.RETURN)
#my_js_confirm_btn = driver.switch_to.alert

#my_js_confirm_btn.send_keys('Bas akkoord')




# my_confirm_alert.accept()


























