import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from page.python_page import PythonPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from allure_commons.types import AttachmentType
import unittest
import allure


@allure.feature("Python Page Tests")
class PythonPageTest(unittest.TestCase):


  def setUp(self):
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    self.driver = webdriver.Chrome(service=service, options=options)
    self.driver.get("https://python.org/")


  @allure.title("Sample Test")
  def test_sample_test(self):
    '''
    Simple python page test.
    '''
    #NOTE : Test method needs to have `test_` as a prefix, for pytest to search for the method accurately.
    pp = PythonPage(self.driver)
    pp.sendtext_search_bar("Selenium")
    pp.click_go_button()
    assert(pp.assert_is_element_present())
    allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


  def tearDown(self):
    self.driver.close()


### ROBOT FRAMEWORK KEYWORD ###
def robot_sampletest():
  rst = PythonPageTest()
  rst.setUp()
  rst.test_sample_test()
  rst.tearDown()


### PYTHON COMMAND RUNNER ###
if __name__ == "__main__":
  unittest.main()