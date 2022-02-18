from selenium import webdriver

driver = webdriver.Chrome()

url = 'C:///Users/basmi/demoProject1/python_selenium_course_material/python_selenium_course_material/SELENIUM_SECTION/iFrames/iFrames_example.html'

driver.get(url)

# driver.find_element('id','btnOutFrame').click()
# my_alert = driver.switch_to.alert
# my_alert_text = my_alert.text
# assert my_alert_text == 'Just clicked Outside iFrame', "Should've gotten outside message"
# my_alert.dismiss()

my_frame = driver.find_element('id','myFrame1')
driver.switch_to.frame(my_frame)
driver.find_element('id', 'btnInFrame').click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.dismiss()

driver.switch_to.default_content()
driver.find_element('id','btnOutFrame').click()