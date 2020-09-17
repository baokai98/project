from time import sleep

from selenium.webdriver.common.by import By

from pagobject.pages.add_partment_page import AddDepartmentPage
from pagobject.pages.BasePage import BasePage


class ContactPage(BasePage):
    _addmember1 = (By.CSS_SELECTOR, '.ww_operationBar .js_add_member')
    _memberlist = (By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
    _addparment = (By.CSS_SELECTOR, '.js_add_sub_party')
    _addparment_list = (By.CSS_SELECTOR, ".jstree-anchor")

    def go_to_add_member(self):

        # 解决循环导入问题，吧导入放到方法里
        from pagobject.pages.add_member_page import AddMemberpage
        # 加强制等待，虽然有点捞，但是不加定位不到元素
        sleep(3)
        # 点击添加成员
        self.find(*self._addmember1).click()
        return AddMemberpage(self.driver)
    # 获取成员列表方法
    def get_member_list(self):
        # self.wait_for_clickable(2)
        # ele = self.driver.find_elements_by_css_selector('.member_colRight_memberTable_td:nth-child(2)')
        # return [name.text for name in ele]
        sleep(2)
        ele = self.finds(*self._memberlist)
        # print(ele)
        list1 = []
        for name in ele:
            list1.append(name.text)
            print(list1)
        return list1
    def add_partment(self):
        # 点击添加子部门
        sleep(2)
        self.find(*self._addparment).click()
        return AddDepartmentPage(self.driver)
    # 获取部门列表方法
    def get_partment_list(self):
        sleep(2)
        # 获得成员列表
        ele1 = self.finds(*self._addparment_list)
        # print(ele1)
        # list2 = []
        # for patrment_name in ele1:
        #     list2.append(patrment_name.text)
        #     print(list2)
        # return list2
        # 使用列表表达式减少代码冗余
        return [patrment_name.text for patrment_name in ele1]


