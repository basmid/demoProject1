## all about driver: https://www.selenium.dev/documentation/en/webdriver/driver_requirements/
# Error: “chromedriver” cannot be opened because the developer cannot be verified.
# Solution: xattr -d com.apple.quarantine /Users/admas/Downloads/chromedriver
# Solution: xattr -d com.apple.quarantine /usr/local/bin/geckodriver


from selenium import webdriver


##### Chrome
driver = webdriver.Chrome(executable_path="C:/Users/basmi/chromedriver.exe")
driver.get('http://demostore.supersqa.com')

#### Firefox
# driver = webdriver.Firefox(executable_path="C:/Users/basmi/geckodriver.exe")
# driver.get('http://www.tvgids.nl')

### Safari
# driver = webdriver.Safari()
# driver.get('http://demostore.supersqa.com')

