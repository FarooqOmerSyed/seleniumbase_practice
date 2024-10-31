from seleniumbase import BaseCase

class CheckboxTests(BaseCase):
  def test_checkboxes(self):
    self.open("https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
    checkboxes = [ 'Option 1', 'Option 2', 'Option 3', 'Option 4' ]

    for checkbox in checkboxes:
      get_text