
"""
编辑添加成员页面
"""
# from qppium.po.page.MemberInvite_Page import MemberInvitePage
from appium.webdriver.common.mobileby import MobileBy

from qppium.po.page.base_page import BasePage


class ContactEditPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    name_element = (MobileBy.XPATH, "//*[contains(@text, '姓名')]/../*[@text='必填']")
    gender_element = (MobileBy.XPATH, "//*[@text='男']")
    nv_element = (MobileBy.XPATH, "//*[@text='女']")
    nan_element = (MobileBy.XPATH, "//*[@text='男']")
    phonenum_element = (MobileBy.XPATH,"//*[contains(@text, '手机') and @class='android.widget.TextView']/..//*[@class='android.widget.EditText']")
    save_element = (MobileBy.ID, "com.tencent.wework:id/hvk")
    def edit_name(self, name):
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../*[@text='必填']").send_keys(name)
        self.find_and_sendkeys(self.name_element, name)
        return self

    def edit_gender(self, gender):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        self.find_and_click(self.gender_element)
        if gender == "女":
            # self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
            self.find_and_click(self.nv_element)
        else:
            # 直接点击有时可以有时不行
            # self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
            self.find_and_click(self.nan_element)
            # 显示等待
            # element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='男']"))
            # element.click()
        return self
    def edit_phonenum(self, phonenum):
        # self.driver.find_element(MobileBy.XPATH,"//*[contains(@text, '手机') and @class='android.widget.TextView']/..//*[@class='android.widget.EditText']").send_keys(phonenum)
        self.find_and_sendkeys(self.phonenum_element, phonenum)
        return self
    def click_save(self):
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hvk").click()
        self.find_and_click(self.save_element)
        from qppium.po.page.MemberInvite_Page import MemberInvitePage
        return MemberInvitePage(self.driver)