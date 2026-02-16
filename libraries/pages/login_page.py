# File: libraries/pages/login_page.py
from robot.api.deco import keyword
from selenium.webdriver.common.by import By
from libraries.core.browser_manager import BrowserManager

class LoginPage:

    @keyword
    def go_to_login_page(self):
        driver = BrowserManager.get_instance().get_driver()
        driver.get("https://www.saucedemo.com/")

    @keyword
    def login_with_credentials(self, username, password):
        driver = BrowserManager.get_instance().get_driver()
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()

    @keyword
    def verify_error_message(self, expected_message):
        driver = BrowserManager.get_instance().get_driver()
        error_elem = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
        actual_message = error_elem.text.strip()
        if expected_message not in actual_message:
            raise AssertionError(f"Expected error '{expected_message}' but got '{actual_message}'")

    @keyword
    def verify_inventory_page(self):
        driver = BrowserManager.get_instance().get_driver()
        inventory_list = driver.find_element(By.CLASS_NAME, "inventory_list")
        if not inventory_list.is_displayed():
            raise AssertionError("Inventory page did not load properly")    
