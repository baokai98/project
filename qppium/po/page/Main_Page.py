"""
主页:
    -通讯录
    -工作台
"""
from appium.webdriver.common.mobileby import MobileBy

from qppium.po.page.AddressList_page import AddressListpage
from qppium.po.page.Search_Page import Searchpag
from qppium.po.page.base_page import BasePage


class MainPage(BasePage):
    # 构造特殊方法去接收上一页传过来的self.driver
    # def __init__(self,driver):
    #     self.driver = driver
    # 进入通讯录
    addressslist_element = (MobileBy.XPATH, "//*[@text='通讯录']")
    def goto_addresslist(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.find_and_click(self.addressslist_element)
        return AddressListpage(self.driver)

    def gaoto_delresslist(self):
        self.find_and_click(self.addressslist_element)

        return AddressListpage(self.driver)

    # 封装工作台
    def goto_workbench(self):
        pass