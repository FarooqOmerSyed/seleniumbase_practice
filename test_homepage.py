from seleniumbase import BaseCase

class Homepagetest(BaseCase):
    def test_homepage(self):
        self.open("https://sdetunicorns.com/")
        self.assert_url_contains("sdetunicorns.com")
        self.assert_title_contains("SDET Unicorns")
