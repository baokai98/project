from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pagobject.pages.add_member_page import AddMemberpage
from pagobject.pages.contact_page import ContactPage
from pagobject.testcases.BasePage import BasePage


class MainPage(BasePage):
    def go_to_contant(self):
        self.driver.find_element_by_id('menu_contacts').click()

        return ContactPage(self.driver)

    def go_to_add_member(self):
        # option = Options()
        # option.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=option)
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        # sleep(2)

        self.driver.find_element_by_css_selector("[node-type='addmember']").click()
        sleep(2)

        return AddMemberpage(self.driver)