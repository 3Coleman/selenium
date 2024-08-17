import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrg(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
    
    def test_python(self):
        driver=self.driver
        driver.get("https://www.python.org/")
        self.assertIn("Python",driver.title)
        search=driver.find_element(By.NAME,"q")
        search.send_keys("pycon")
        but=driver.find_element(By.NAME,"submit")
        but.send_keys(Keys.RETURN)
        screenshot=driver.get_screenshot_as_file("python.png")
        self.assertNotIn("No results found.",driver.page_source)
        time.sleep(1)

        def tearDown(self):
            self.driver.close()
if __name__=="__main__":
    unittest.main()
