from time import sleep

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from web.web_pages.home_page import HomePage
from web.web_pages.profile_page import ProfilePage
from web.testcase.base_test_case import BaseTestCase


class TestXueQiu(BaseTestCase):

    def setup(self):
        # remote driver, 需要下载，后续再作
        self.driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.implicitly_wait(30)
        self.driver.get("https://xueqiu.com/")
        self.main = HomePage()

    def test_search(self):
        self.main.search("alibaba").follow("1688")
        # todo: add assertion

    def test_profile(self):
        profile = ProfilePage(self.driver)
        profile.login()
        selected = profile.gotoSelected()
        selected.select("alibaba", "1688")

    def test_log(self):
        self.log.warning("warning demo")
        self.log.debug("debug demo")

    def teardown(self):
        sleep(30)
        self.driver.quit()
