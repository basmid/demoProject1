from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'C:///Users/basmi/demoProject1/python_selenium_course_material/python_selenium_course_material/SELENIUM_SECTION/radios/radios_example.html'
driver.get(url)

expected_values = ['21-40','41-60','61-80','81+', 'foo']
all_radios = driver.find_elements(By.NAME, 'age-group-radio')
assert len(all_radios) == len(expected_values), "the number of radios does not match the expected"