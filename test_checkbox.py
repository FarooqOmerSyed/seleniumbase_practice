from seleniumbase import BaseCase
import time 

class MyTestClass(BaseCase):
    def test_checkbox(self):
        self.open("https://demoqa.com/checkbox")
        self.maximize_window()
        self.click('span[class="rct-checkbox"]')
        self.click('//*[@id="tree-node"]/div/button[1]')
        self.click('//*[@id="tree-node"]/div/button[2]')
        time.sleep(2)