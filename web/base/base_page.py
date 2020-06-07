import selenium.common.exceptions
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from web.base.web_driver_factory import WebDriverFactory
import os
import time
from PIL import Image


class BasePage(object):
    """Base class to initialize the base web_pages that will be called from all pages"""
    _driver = None

    @classmethod
    def get_driver(cls) -> webdriver:
        cls.driver = WebDriverFactory.generate_driver()
        return cls.driver

    def __init__(self):
        self._driver: WebDriver = WebDriverFactory.generate_driver()

    def open_page(self, url: str):
        self._driver.get(url)

    # @staticmethod
    def _wait_for_element(self, locator) -> WebElement:
        """locate the element to be visible"""

        try:
            return WebDriverWait(self._driver, 50).until(EC.visibility_of_element_located(locator))
        except selenium.common.exceptions.NoSuchElementException:
            print("定位控件失败by:", locator)

    def maximize_window(self):
        self._driver.maximize_window()

    def minimize_window(self):
        self._driver.fullscreen_window()

    def execute_script(self, js: str):
        """execute javascript
            for example: self._driver.execute_script("return JSON.stringify(window.performance.timing)")
        """

        return self._driver.execute_script(js)

    def execute_command(self, driver_command, **kwargs):
        self._driver.execute(driver_command, params=kwargs)

    def add_cookie(self, cookies: list):
        """
        注意，cookie要以字典形式传入
        :param cookies:
        :return:
        """
        # print(self.driver.get_cookies())
        for cookie in cookies:
            self._driver.add_cookie(cookie)

        # print(self.driver.get_cookies())

    def full_screen_shot(self, driver, file):
        print("Starting chrome full page screenshot workaround ...")

        total_width = self._driver.execute_script("return document.body.offsetWidth")
        total_height = self._driver.execute_script("return document.body.parentNode.scrollHeight")
        viewport_width = self._driver.execute_script("return document.body.clientWidth")
        viewport_height = self._driver.execute_script("return window.innerHeight")
        print(
            "Total: ({0}, {1}), Viewport: ({2},{3})".format(total_width, total_height, viewport_width, viewport_height))
        rectangles = []

        i = 0
        while i < total_height:
            ii = 0
            top_height = i + viewport_height

            if top_height > total_height:
                top_height = total_height

            while ii < total_width:
                top_width = ii + viewport_width

                if top_width > total_width:
                    top_width = total_width

                print("Appending rectangle ({0},{1},{2},{3})".format(ii, i, top_width, top_height))
                rectangles.append((ii, i, top_width, top_height))

                ii = ii + viewport_width

            i = i + viewport_height

        stitched_image = Image.new('RGB', (total_width, total_height))
        previous = None
        part = 0

        for rectangle in rectangles:
            if not previous is None:
                self._driver.execute_script("window.scrollTo({0}, {1})".format(rectangle[0], rectangle[1]))
                print("Scrolled To ({0},{1})".format(rectangle[0], rectangle[1]))
                time.sleep(0.2)

            file_name = "part_{0}.png".format(part)
            print("Capturing {0} ...".format(file_name))

            self._driver.get_screenshot_as_file(file_name)
            screenshot = Image.open(file_name)

            if rectangle[1] + viewport_height > total_height:
                offset = (rectangle[0], total_height - viewport_height)
            else:
                offset = (rectangle[0], rectangle[1])

            print("Adding to stitched image with offset ({0}, {1})".format(offset[0], offset[1]))
            stitched_image.paste(screenshot, offset)

            del screenshot
            os.remove(file_name)
            part = part + 1
            previous = rectangle

        stitched_image.save(file)
        print("Finishing chrome full page screenshot workaround...")
        return True
