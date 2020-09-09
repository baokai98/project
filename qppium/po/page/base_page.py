"""
---基类：封装最基本的方法。初始化，find，显示等待...（常用的方法）
-----让需要的class去继承basepage
"""
# 导入WebDriver附一个初始值，未后面复用应用做准备
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver:WebDriver = None):
        self.driver = driver

    # 封装一个find方法，通过self.driver.find_element方式传入一个locator（默认是元祖类型），并且给它解包
    def find(self, locator):
        return self.driver.find_element(*locator)

    def finds(self, locator):
        # 封装一个find方法，通过self.driver.find_elements方式传入一个locator（默认是元祖类型），并且给它解包
        return self.driver.find_elements(*locator)
        # 封装查找元素和点击操作
    def find_and_click(self, locator):
        self.find(locator).click()
        # 封装查找元素和输入
    def find_and_sendkeys(self, locator, value):
        self.find(locator).send_keys(value)
    # 封装滚动查找
    def scroll_find_and_click(self, text):
        ele = (MobileBy.ANDROID_UIAUTOMATOR,
               'new UiScrollable(new UiSelector()'
               '.scrollable(true).instance(0))'
               '.scrollIntoView(new UiSelector()'
               f'.text("{text}").instance(0));')
        self.find_and_click(ele)
    # 封装查找元素和获取text属性
    def find_and_get_text(self,locator):
        return self.find(locator).text

    def gettoast_text(self):
        element = ((MobileBy.XPATH, "//*[@class='android.widget.Toast']"))
        # mytoast = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return self.find_and_get_text(element)
