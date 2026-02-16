from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger


class ScreenshotListener:

    ROBOT_LISTENER_API_VERSION = 3

    def end_test(self, data, result):
        if result.status == "FAIL":
            browser = BuiltIn().get_library_instance("BrowserManager")
            driver = browser.get_driver()
            if driver:
                driver.save_screenshot(f"{data.name}.png")
                logger.info("Screenshot captured on failure.")
