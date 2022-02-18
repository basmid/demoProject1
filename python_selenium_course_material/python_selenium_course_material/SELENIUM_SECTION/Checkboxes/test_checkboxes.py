from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By

url = 'C:///Users/basmi/demoProject1/python_selenium_course_material/python_selenium_course_material/SELENIUM_SECTION/checkboxes/checkbox_example.html'

driver = webdriver.Chrome()
time.sleep(2)
driver.get(url)
time.sleep(2)

# # Example 1
# to_select_value = '61-80'
# locator_by_value = f'input[name="age-group-checkbox"][value="{to_select_value}"]'
#
# my_choice = driver.find_element(By.CSS_SELECTOR, locator_by_value)
# my_choice.click()

# import pdb; pdb.set_trace()

# Example 2

expected_number_of_options = 4
all_checkboxes = driver.find_elements(By.NAME, 'age-group-checkbox')
assert len(all_checkboxes) == expected_number_of_options, "Number of checkboxes is not the expected"

for checkbox in all_checkboxes:
    checkbox.click()
    value = checkbox.get_attribute('value')
    if checkbox.is_selected():
        print(f"Checkbox with value '{value}' is selectable")
    else:
        raise Exception(f"Value '{value}' is not selectable")











