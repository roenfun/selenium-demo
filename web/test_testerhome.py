import json
from time import sleep

from web.web_pages.home_page import HomePage
from web.base.base_page import BasePage
from web.base.base_test_case import BaseTestCase


class TestTesterHome(BaseTestCase):
    __home_page = HomePage()

    def setup(self):
        super().setup()
        print("TestTesterHome setup")
        self.__home_page.open_page("https://testerhome.com")

    # def setup_method(self):
    #     pass

    def teardown(self):
        print("TestTesterHome teardown")
        super().teardown()

    def test_mtsc2019(self):
        self.__home_page.navigate_to_community()

    # def test_execute_script(self):
    #     raw = self.__home_page.execute_script("return JSON.stringify(window.performance.timing)")
    #     print(raw)
    #     print(json.dumps(json.loads(raw), indent=4))
    #
    # def test_execute(self):
    #     # self.driver.execute("getXXX", params={"x": 1, "y": 2})
    #     self.__home_page.execute_command("getXXX", params={"x": 1, "y": 2})
    #
    # def test_cookie(self):
    #     print(self.driver.get_cookies())
    #     cookies = [{"name": "a", "value": "b"}, {"name": "name", "value": "name demo"}]
    #     self.__home_page.add_cookie(cookies)
    #     # self.driver.add_cookie({"name": "a", "value": "b"})
    #     # self.driver.add_cookie({"name": "name", "value": "name demo"})
    #     print(self.driver.get_cookies())
