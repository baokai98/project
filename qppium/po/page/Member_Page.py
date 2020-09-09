from appium.webdriver.common.mobileby import MobileBy

from qppium.po.page.Edimemberl_Page import Editmemberpage
from qppium.po.page.base_page import BasePage
# 个人信息页面

class Memberpage(BasePage):

    memberselect = (MobileBy.ID, 'com.tencent.wework:id/hvd')
    # 打来联系人编辑页面
    def open_memeber(self):
        self.find_and_click(self.memberselect)
        return Editmemberpage(self.driver)
