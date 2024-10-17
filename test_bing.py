from seleniumbase import BaseCase
from selenium.webdriver.common.keys import Keys
import time

class MyTestClass(BaseCase):
    def test_keyboard_events(self):
        # Open a website
        self.open("https://www.bing.com")

        # Find an input element
        self.type("textarea[id='sb_form_q']", "Hello World!")  # Simulate typing "Hello World!"

        # Use keyboard events like pressing ENTER
        self.send_keys("textarea[id='sb_form_q']", Keys.ENTER)
        time.sleep(4)

       
