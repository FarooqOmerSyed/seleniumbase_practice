from seleniumbase import BaseCase

class GoogleSearchTest(BaseCase):
    def test_google_search(self):
        self.open("https://www.google.com/")
        self.type("textarea[name='q']", "SeleniumBase documentation")
        self.click("input[name='btnK']")
        self.assert_text("SeleniumBase documentation", "body")
