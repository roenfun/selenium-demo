import time

from selenium import webdriver


class WebDriverFactory(object):
    """Base class to initialize the base web_pages that will be called from all pages"""
    __driver: webdriver = None
    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    @classmethod
    def generate_driver(cls) -> webdriver:
        # self.driver = webdriver.Firefox()

        # options = webdriver.ChromeOptions()
        # options.binary_location="chrome path"
        # self.driver = webdriver.Chrome(options=options)
        # self.driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)

        if cls.__driver is None:
            abs_file = __file__
            print("abs path is %s" % (__file__))
            abs_dir = abs_file[:abs_file.rfind("/")]  # "./../seleium_drivers/chromedriver"

            cls.__driver = webdriver.Chrome(
                executable_path="/Users/chad.long/project/study-material/huogewozi/8-14.ui-automation/appium_online_9-master/web/seleium_drivers/chromedriver")
            cls.__driver.implicitly_wait(20)

        return cls.__driver

    @classmethod
    def quit_driver(cls):
        print("quit web driver...")
        time.sleep(3)
        cls.__driver.quit()
