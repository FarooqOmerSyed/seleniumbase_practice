from seleniumbase import BaseCase
import time

class MyTestClass(BaseCase):
    def test_pwd(self):
        self.maximize_window()
        self.open("https://practice.expandtesting.com/forgot-password")
        self.type("input[id='email']", "examplemail.@gmail.com")
        time.sleep(2)
        self.click("button[type='submit']")
        time.sleep(2)
        self.wait_for_element_visible("div[id='confirmation-alert']")
        success_msg = self.get_text("div[id='confirmation-alert']")
        self.assert_equal(success_msg, "An e-mail has been sent to you which explains how to reset your password.")
