from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _base_url = ""
    def __init__(self, driver: WebDriver = None):
        # 避免driver重复实例化
        if driver is None:
            # 复用浏览器
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=option)
            # self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        else:
            self.driver = driver
        if self._base_url != "":
            self.driver.get(self._base_url)
        self.driver.implicitly_wait(5)
    # 封装查找元素的方法
    def find(self, by, value):
        return self.driver.find_element(by, value)
    # 封装查找元素列表的方法
    def finds(self, by, value):
        return self.driver.find_elements(by, value)
    #
    # 显示等待元素可被点击
    def wait_for_clickable(self, element):

        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))

    # 显示等待
    def wait(self, element):
        return WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(element))
    '''
    
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

    '''
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

