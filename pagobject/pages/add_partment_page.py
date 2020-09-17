from time import sleep
from selenium.webdriver.common.by import By


from pagobject.pages.BasePage import BasePage


class AddDepartmentPage(BasePage):
    """
    1.定位到输入框，输入添加部门名称
    2.点击保存
    3.点击取消

    """
    _department_name = (By.CSS_SELECTOR,".ww_inputText:nth-child(2)")
    _click_confire = (By.XPATH,'//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]')
    _department_name_list = (By.CSS_SELECTOR,".jstree-default")
    _click_cancel =(By.XPATH,'//*[@id="__dialog__MNDialog__"]/div/div[3]/a[2]')
    # 添加新部门方法
    def add_new_department(self,name):
        self.find(*self._department_name).send_keys(name)

        # return self 是为了实现返回当前页面时依然可以实现链式调用
        return self

    # 点击确定按钮方法
    def save_department(self):
        from pagobject.pages.contact_page import ContactPage
        sleep(2)
        self.find(*self._click_confire).click()
        return ContactPage(self.driver)

    # 点击取消按钮方法
    def cancel_department(self):
        from pagobject.pages.contact_page import ContactPage
        self.find(*self._click_cancel).click()
        return ContactPage(self.driver)