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
