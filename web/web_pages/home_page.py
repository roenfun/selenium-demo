import time

from web.base.base_page import BasePage
from web.web_pages.search_page import SearchPage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    __COMMUNITY_NAME = "社区"
    __PUBLISH_TOPIC_CSS = ".new-topic"  # .btn btn-primary btn-block new-topic
    __LOGIN_CSS = ".form-actions .btn-primary"  # 两层class
    __TIPS_PART = "注册或者登录" #继续操作前请注册或者登录

    def search(self, keyword):
        self.driver.find_element_by_name("q").send_keys(keyword)
        self.driver.find_element_by_css_selector(".nav__search button").click()
        return SearchPage(self.driver)

    def navigate_to_community(self):
        """跳到社区首页"""
        comm = self._wait_for_element((By.LINK_TEXT, self.__COMMUNITY_NAME))
        if comm:
            comm.click()

        publish_topic = self._wait_for_element((By.CSS_SELECTOR, self.__PUBLISH_TOPIC_CSS))

        if publish_topic:
            publish_topic.click()

        # self.driver.find_element_by_xpath('//*[@data-toggle="dropdown" and @class="btn btn-default"]').click()
        self._driver.find_element_by_css_selector(self.__LOGIN_CSS).click()
        time.sleep(5)
        self._driver.find_element_by_partial_link_text(self.__TIPS_PART).is_displayed()
        # import time
        # time.sleep(2)
        # self.driver.find_element_by_partial_link_text("金数据").click()
        # self.driver.find_element_by_partial_link_text("http://2019.test-china.org/").click()
