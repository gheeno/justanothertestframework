from seleniumpagefactory.Pagefactory import PageFactory


class PythonPage(PageFactory):
  """Base class to initialize the base page that will be called from all
    pages"""

  def __init__(self, driver):
    self.driver = driver

  locators = {
      'search_bar_textbox': ('ID', "id-search-field"),
      'go_button': ('ID', "submit")
  }

  def sendtext_search_bar(self, arg):
    self.search_bar_textbox.set_text(arg)

  def click_go_button(self):
    self.go_button.click()

  def assert_is_element_present(self):
    return self.go_button.visibility_of_element_located()
