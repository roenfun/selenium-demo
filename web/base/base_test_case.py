from web.base.web_driver_factory import WebDriverFactory


class BaseTestCase(object):
    """Base class to initialize the base web_pages that will be called from all pages"""
    #
    # @classmethod
    # def setup(cls):
    #     print("BaseTestCae setup...")
    #
    # @classmethod
    # def teardown(cls):
    #     print("BaseTestCae teardown...")

    def setup(self):
        print("setup: 每个用例开始前执行")

    def teardown(self):
        print("teardown: 每个用例结束后执行")

    def setup_class(self):
        print("setup_class：所有用例执行之前")

    def teardown_class(self):
        print("teardown_class：所有用例执行之前")
        WebDriverFactory.quit_driver()

    def setup_method(self):
        print("setup_method:  每个用例开始前执行")

    def teardown_method(self):
        print("teardown_method:  每个用例结束后执行")
