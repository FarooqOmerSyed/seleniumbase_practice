from seleniumbase import BaseCase
import time

class MyTestClass(BaseCase):
    def test_textbox(self):
        self.open("https://demoqa.com/text-box")
        self.maximize_window()
        self.type("input[id='userName']", "SeleniumBase")
        self.type("input[id='userName']", "SeleniumBase")
        self.type("textarea[id='currentAddress']", "SeleniumBase")
        self.type("textarea[id='permanentAddress']", "SeleniumBase")
        self.click("button[id='submit']")
        time.sleep(2)

