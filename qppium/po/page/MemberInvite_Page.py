"""
添加成员界面

"""
# from qppium.po.page.ContactEdit_Page import ContactEditPage
from appium.webdriver.common.mobileby import MobileBy

from qppium.po.page.base_page import BasePage


class MemberInvitePage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    # 手动添加联系人
    addmember_element = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    def addcontact_menual(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.find_and_click(self.addmember_element)
        from qppium.po.page.ContactEdit_Page import ContactEditPage
        return ContactEditPage(self.driver)
    # 获取toast
    def get_toast(self):
        # mytoast = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        mytoast = self.gettoast_text()

        return mytoast




