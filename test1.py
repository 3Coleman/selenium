from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get("https://www.python.org/")

element=driver.find_element(By.NAME,"q")
element.send_keys("selenium")

button=driver.find_element(By.NAME,"submit")
button.send_keys(Keys.RETURN)

screenshot=driver.get_screenshot_as_file("page.png")

driver.close


hfhf