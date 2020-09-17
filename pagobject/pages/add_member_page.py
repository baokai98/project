from selenium.webdriver.common.by import By

from pagobject.pages.contact_page import ContactPage
from pagobject.pages.BasePage import BasePage


class AddMemberpage(BasePage):
    # 加_防止变量暴露在其他方法中，做私有操作****(po第五原则，不要暴露内部元素给外部)
    _username = (By.ID, "username")
    _useracctid = (By.ID, "memberAdd_acctid")
    _userphone = (By.ID, "memberAdd_phone")
    _cancel = (By.CSS_SELECTOR, "[node-type='cancel']")
    _li_kai = (By.CSS_SELECTOR, ".js_btn_cancel")
    # 添加成员
    def add_member(self,name,acctid,phone):
        """
         self.driver.find_element_by_id('username').send_keys(name)
        self.driver.find_element_by_id('memberAdd_acctid').send_keys(acctid)
        self.driver.find_element_by_id('memberAdd_phone').send_keys(phone)
       # 为了实现返回当前页面时依然可以实现链式调用
        """

        #            find_element(By.ID, "username")
        self.find(*self._username).send_keys(name)
        self.find(*self._useracctid).send_keys(acctid)
        self.find(*self._userphone).send_keys(phone)


        return self

    # 定义一个函数保存
    def save_member(self):
        self.driver.find_element_by_css_selector('.js_btn_save').click()
        return ContactPage(self.driver)
    # 定义一个函数取消保存
    def cancel_member(self):
        # self.driver.find_element(By.CSS_SELECTOR, ".js_btn_cancel").click()
        # self.driver.find_element(By.CSS_SELECTOR,"[node-type='cancel']").click()
        # self.wait_for_clickable(self._cancel)
        # 点击取消
        # sleep(4)
        self.driver.find_element(*self._li_kai).click()
        # 点击离开
        self.find(*self._cancel).click()
        return ContactPage(self.driver)