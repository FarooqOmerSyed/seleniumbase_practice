from seleniumbase import BaseCase

class MyTestClass(BaseCase):
    def test_login_msg(self):
        self.open("https://practice.expandtesting.com/notification-message-rendered")
        self.maximize_window()
        self.click("//a[contains(text(),'Click here')]")
        self.wait_for_element_visible("//div[@id='flash']")
        success_msg = self.get_text("//div[@id='flash']")
        self.assert_equal(success_msg, "Action successful")

