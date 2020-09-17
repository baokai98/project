from time import sleep

from selenium.webdriver.common.by import By

from pagobject.pages.add_member_page import AddMemberpage
from pagobject.pages.contact_page import ContactPage
from pagobject.pages.BasePage import BasePage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    _contant_click = (By.ID,'menu_contacts')
    _add_member = (By.CSS_SELECTOR,"[node-type='addmember']")
    def go_to_contant(self):
        # 点击通讯录
        # self.driver.find_element_by_id('menu_contacts').click()
        self.find(*self._contant_click).click()

        return ContactPage(self.driver)

    def go_to_add_member(self):
        # option = Options()
        # option.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=option)
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        # sleep(2)

        # self.driver.find_element_by_css_selector("[node-type='addmember']").click()
        # 点击添加成员
        self.find(*self._add_member).click()
        sleep(2)

        return AddMemberpage(self.driver)