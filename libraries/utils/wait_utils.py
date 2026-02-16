from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


@keyword("Wait For Element")
def wait_for_element(locator, timeout=10):
    selib = BuiltIn().get_library_instance("SeleniumLibrary")
    selib.wait_until_element_is_visible(locator, timeout)
