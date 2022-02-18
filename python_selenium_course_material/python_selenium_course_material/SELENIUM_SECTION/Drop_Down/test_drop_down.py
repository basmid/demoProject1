
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()

url = 'C:///Users/basmi/demoProject1/python_selenium_course_material/python_selenium_course_material/SELENIUM_SECTION/drop_down/drop_down_example.html'

driver.get(url)

my_dropdown = driver.find_element('id','age-range-select')
dropdown_object = Select(my_dropdown)
dropdown_object.select_by_value("41-60")

all_options = dropdown_object.options
for option in all_options:
    print(option.text)

import pdb; pdb.set_trace()


