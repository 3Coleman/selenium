
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class RahulTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_shop(self):
        driver = self.driver
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        
        # Enter name
        name = driver.find_element(By.NAME, "name")
        name.send_keys("abel")
        
        # Enter email
        email = driver.find_element(By.NAME, "email")
        email.send_keys("abelsibi05@gmail.com")
        
        # Enter password
        password = driver.find_element(By.ID, "exampleInputPassword1")
        password.send_keys("abel@2000")
        
        # Take a screenshot
        driver.get_screenshot_as_file("pic.png")
        
        # Assert that the title contains "ProtoCommerce"
        self.assertIn("ProtoCommerce", driver.title)
        
        # Click the button
        button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-success")
        button.send_keys(Keys.RETURN)
        
        # Wait for 5 seconds
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
