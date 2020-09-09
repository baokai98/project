"""
通讯录页面
"""
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from qppium.po.page.MemberInvite_Page import MemberInvitePage
# from qppium.po.page.Member_Page import Memberpage
# from qppium.po.page.Search_Page import Searchpag
from qppium.po.page.base_page import BasePage


class AddressListpage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    addmember_text = "添加成员"

    search_click = (MobileBy.ID, 'com.tencent.wework:id/hvn')


    def add_memeber(self):
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("添加成员").instance(0));').click()
        self.scroll_find_and_click(self.addmember_text)
        return MemberInvitePage(self.driver)
    def click_search(self):
        # 点击搜索
        self.find_and_click(self.search_click)

        from qppium.po.page.Search_Page import Searchpag
        return Searchpag(self.driver)
