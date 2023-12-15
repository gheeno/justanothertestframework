import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from page.python_page import PythonPage


class SampleTest(unittest.TestCase):

  def setUp(self):
    service = Service()
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    self.driver = webdriver.Chrome(service=service, options=options)
    self.driver.get("https://python.org/")

  def test_sample_test(self):
    pp = PythonPage(self.driver)
    pp.sendtext_search_bar("Selenium")
    pp.click_go_button()
    assert(pp.assert_is_element_present())

  def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
  unittest.main()
