from time import sleep

from pagobject.testcases.BasePage import BasePage


class ContactPage(BasePage):
    def go_to_add_member(self):


        # 解决循环导入问题，吧导入放到方法里
        from pagobject.pages.add_member_page import AddMemberpage
        sleep(5)
        self.driver.find_element_by_css_selector('.ww_operationBar .js_add_member').click()
        return AddMemberpage(self.driver)