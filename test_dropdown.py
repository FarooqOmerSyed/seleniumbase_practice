from seleniumbase import BaseCase

class DropdownTest(BaseCase):
    def test_dropdown(self):
        self.open("https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
        self.maximize_window()
        self.select_option_by_text("select#dropdowm-menu-1", "Python")
        self.select_option_by_text("select#dropdowm-menu-2", "Maven")
        self.select_option_by_text("select#dropdowm-menu-3", "CSS")
