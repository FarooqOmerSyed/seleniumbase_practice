from seleniumbase import BaseCase

BASE_URL = "https://practice.expandtesting.com/radio-buttons"

class MyTestClass(BaseCase):
    def test_radiobtnclr(self):
        self.maximize_window()
        self.open(BASE_URL)
        elements = ["//input[@id='yellow']", "//input[@id='blue']", "//input[@id='green']", "//input[@id='red']", "//input[@id='black']"]
        for element in elements:
            self.click(element)
            self.sleep(1)
    
    def test_radiobtnsprt(self):
        self.maximize_window()
        self.open(BASE_URL)
        elements = ["//input[@id='football']", "//input[@id='basketball']", "//input[@id='tennis']"]
        for element in elements:
            self.click(element)
            self.sleep(1)