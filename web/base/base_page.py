import selenium.common.exceptions
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from web.base.web_driver_factory import WebDriverFactory


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
