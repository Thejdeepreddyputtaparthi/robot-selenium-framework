from robot.libraries.BuiltIn import BuiltIn


class BasePage:

    def __init__(self):
        self.selib = BuiltIn().get_library_instance("SeleniumLibrary")

    def click(self, locator):
        self.selib.click_element(locator)

    def type(self, locator, text):
        self.selib.input_text(locator, text)

    def get_text(self, locator):
        return self.selib.get_text(locator)

    def element_should_be_visible(self, locator):
        self.selib.page_should_contain_element(locator)
