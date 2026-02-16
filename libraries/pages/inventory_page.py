# File: libraries/pages/inventory_page.py
from robot.api.deco import keyword
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from libraries.core.browser_manager import BrowserManager

class InventoryPage:

    @keyword
    def add_product_to_cart(self, product_name):
        driver = BrowserManager.get_instance().get_driver()
        button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((
                By.XPATH,
                f"//div[@class='inventory_item' and .//div[text()='{product_name}']]//button"
            ))
        )
        button.click()

    @keyword
    def go_to_cart(self):
        driver = BrowserManager.get_instance().get_driver()
        cart_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "shopping_cart_container"))
        )
        cart_button.click()

    @keyword
    def should_see_product_in_cart(self, product_name):
        driver = BrowserManager.get_instance().get_driver()
        cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        item_names = [i.text for i in cart_items]
        if product_name not in item_names:
            raise AssertionError(f"Product '{product_name}' not found in cart")

    @keyword
    def remove_product_from_cart(self, product_name):
        driver = BrowserManager.get_instance().get_driver()
        # Updated XPath for cart page
        remove_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((
            By.XPATH,
            f"//div[@class='cart_item' and .//div[text()='{product_name}']]//button[text()='Remove']"
        ))
    )
        remove_button.click()

    @keyword
    def should_not_see_product_in_cart(self, product_name):
        driver = BrowserManager.get_instance().get_driver()
        cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        item_names = [i.text for i in cart_items]
        if product_name in item_names:
            raise AssertionError(f"Product '{product_name}' still in cart")

    @keyword
    def cart_should_be_empty(self):
       driver = BrowserManager.get_instance().get_driver()
       cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
       if cart_items:
           raise AssertionError("Cart is not empty")
