from seleniumbase import BaseCase

BASE_URL = "https://practice.expandtesting.com/"

class LoginTest(BaseCase):

    def test_login(self):
        self.open(f"{BASE_URL}login")
        self.maximize_window()
        self.type("input[id='username']", "practice")
        self.type("input[id='password']", "SuperSecretPassword!")
        self.click("button[type='submit']")

        # Use BaseCase's wait_for_element_visible method
        self.wait_for_element_visible("div[id='flash']")

        flash_message = self.get_text("div[id='flash']")
        self.assert_equal(flash_message, "You logged into a secure area!")
        print("Login test passed!")

    def test_fail_login(self):
        self.open(f"{BASE_URL}login")
        self.maximize_window()
        self.type("input[id='username']", "practice")
        self.type("input[id='password']", "SuperSecretPassword!!")
        self.click("button[type='submit']")

        # Use BaseCase's wait_for_element_visible method
        self.wait_for_element_visible("div[id='flash']")

        flash_message = self.get_text("div[id='flash']")
        self.assert_equal(flash_message, "Your password is invalid!")
        print("Login test for fail case passed!")

