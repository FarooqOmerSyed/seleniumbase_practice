from seleniumbase import BaseCase
import time

class DragDropTests(BaseCase):
    def test_drag_and_drop(self):
        self.open("https://practice.expandtesting.com/drag-and-drop")
        self.maximize_window()
        
        # Use XPath strings directly
        self.drag_and_drop("//div[@id='column-a']", "//div[@id='column-b']")
        time.sleep(2)
