# File: libraries/core/browser_manager.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from robot.api.deco import keyword
from webdriver_manager.chrome import ChromeDriverManager

class BrowserManager:
    _instance = None  # Singleton instance

    def __init__(self):
        self.driver = None
        BrowserManager._instance = self

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = BrowserManager()
        return cls._instance

    @keyword("Open Application")
    def open_application(self, url="https://www.saucedemo.com"):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        self.driver.get(url)

    @keyword("Close Application")
    def close_application(self):
        if self.driver:
            self.driver.quit()

    @keyword("Get Driver")
    def get_driver(self):
        return self.driver
