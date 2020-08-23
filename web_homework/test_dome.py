from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# 使用强制等待的方式获取cookie，
class Testcookies():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def test_cookie(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        # 先打开企业微信登录页面，停留10s，用手机扫码登录，然后再去get_cookies
        sleep(10)
        cookies = self.driver.get_cookies()
        print(cookies)
