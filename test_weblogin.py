from seleniumbase import BaseCase

class WebLoginTest(BaseCase):
    def test_web_login(self):
        self.open("https://webdriveruniversity.com/Login-Portal/index.html?")
        self.type("input[id='text']", "testuser")
        self.type("input[id='password']", "testpass")
        self.click("button[id='login-button']")
