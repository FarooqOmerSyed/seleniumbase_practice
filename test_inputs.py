from seleniumbase import BaseCase
import time

class MyTestClass(BaseCase):
    def test_inputs(self):
        self.open("https://practice.expandtesting.com/inputs")
        self.maximize_window()
        self.type("input[name='input-number']", "22")
        self.type("input[name='input-text']", "caspian11")
        self.type("input[name='input-password']", "123whoareyou")
        self.type("input[name='input-date']", "12/11/2022")
        self.click("button[id='btn-display-inputs']")
        time.sleep(2)