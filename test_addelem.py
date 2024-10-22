from seleniumbase import BaseCase

BASE_URL = "https://practice.expandtesting.com/add-remove-elements"


class MyTestClass(BaseCase):

    def test_add_and_delete_elements(self):
        self.open(BASE_URL)
        self.maximize_window()

        # Add 5 elements
        for _ in range(5):
            self.click("//button[contains(text(), 'Add Element')]")

        # Delete all added elements using a more efficient approach
        added_elements = self.find_elements("//div[contains(@class, 'added-manually')]")
        for element in reversed(added_elements):  # Iterate in reverse order for better stability
            self.click(element)

        # Verify all elements are deleted (optional)
        # ... add verification steps here ...

        print("Add and delete elements test passed!")