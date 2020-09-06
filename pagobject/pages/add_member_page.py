from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pagobject.pages.contact_page import ContactPage
from pagobject.testcases.BasePage import BasePage


class AddMemberpage(BasePage):
    def add_member(self):
        # option = Options()
        # option.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=option)


        self.driver.find_element_by_id('username').send_keys('蛮王')
        self.driver.find_element_by_id('memberAdd_acctid').send_keys('5555')
        self.driver.find_element_by_id('memberAdd_phone').send_keys('13888812345')
       # 为了实现返回当前页面时依然可以实现链式调用

        return self


    def save_member(self):
        self.driver.find_element_by_css_selector('.js_btn_save').click()
        return ContactPage(self.driver)
    def cancel_member(self):
        pass