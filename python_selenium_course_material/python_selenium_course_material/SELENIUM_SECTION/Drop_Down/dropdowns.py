

from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()

url = 'C:///Users/basmi/demoProject1/python_selenium_course_material/python_selenium_course_material/SELENIUM_SECTION/drop_down/drop_down_example.html'

driver.get(url)

# # Option 1 is using the Select class
my_dropdown = driver.find_element('id', 'age-range-select')
# dropdown_object = Select(my_dropdown)
# dropdown_object.select_by_index(3)
# dropdown_object.select_by_value('21-40')
# all_options = dropdown_object.options
# for option in all_options:
#     print(option.text)

# Option 2
dropdown_btn = driver.find_element('id', 'dropdownMenuButton')
dropdown_btn.click()
my_option = driver.find_element('xpath', '//*[@id="dropdowns"]/div[2]/div/ul/li[1]/a')
my_option.click()

import pdb; pdb.set_trace()