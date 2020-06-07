# @File : demo_test.py 
# @Author : Chad
# @Time : 2020-06-07
# coding:utf-8
import time

from appium import webdriver

'''
adb shell dumpsys window w | grep mCurrentFocus
adb shell dumpsys activity top | grep ACTIVITY
adb shell ps 1624
'''
desired_caps = {
    'platformName': 'Android',
    "noReset": True,
    'fullReset': False,  # fuck demo的代码清了我微信数据！
    'deviceName': 'GSL0217819000200',
    'appPackage': 'com.tencent.mm',
    'appActivity': '.ui.LauncherUI',
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'chromeOptions': {
        'androidProcess': 'com.tencent.mm:appbrand0'  # 参考 https://testerhome.com/topics/12003
    }
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(20)
print(driver.contexts)
print(driver.current_context)
time.sleep(10)
# driver.find_element_by_name("发现").click()
# time.sleep(6)
# driver.find_element_by_name("小程序").click()
# time.sleep(5)
# print(driver.page_source)
# driver.find_element_by_name("唯品会").click()
driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')
# driver.switch_to.context(driver.contexts[1])

time.sleep(20)
print("--" * 20)
print(driver.page_source)
