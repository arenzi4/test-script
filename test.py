from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Initialize the Chrome driver (you should have chromedriver installed)
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.example.com")

# Find an element by its name and type something
element = driver.find_element_by_name("q")
element.send_keys("Hello, Selenium!")

# Simulate hitting the 'Enter' key
element.send_keys(Keys.RETURN)

# Wait for a few seconds to see the results
driver.implicitly_wait(5)

# Close the browser
driver.close()

