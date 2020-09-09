from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver_base=None):
        # 避免driver重复实例化
        if driver_base is None:

            option =Options()
            option.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=option)
            self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        else:
            self.driver = driver_base
            self.driver.implicitly_wait(5)
    # def __init__(self , driver_base = None):
    #     # 避免driver 的重复实例化
    #     if driver_base is None:
    #         option = Options()
    #         option.debugger_address = '127.0.0.1:9222'
    #         self.driver = webdriver.Chrome(options=option)
    #         self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    #     else:
    #         self.driver = driver_base
    #
    #     self.driver.implicitly_wait(5)

