from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome driver (you should have chromedriver installed)
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
options=options)

# Open a website
driver.get("http://www.google.com")

# Find an element by its name and type something
element = driver.find_element("name","q")
element.send_keys("Hello, Selenium!")

# Simulate hitting the 'Enter' key
element.send_keys(Keys.RETURN)

# Wait for a few seconds to see the results
time.sleep(5)

# Close the browser
driver.close()
driver.quit()
