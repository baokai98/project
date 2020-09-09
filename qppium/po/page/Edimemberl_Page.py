from appium.webdriver.common.mobileby import MobileBy

from qppium.po.page.Dellmembe_Pager import Dellmembepager
from qppium.po.page.base_page import BasePage

# 个人信息编辑成员页面
class Editmemberpage(BasePage):

    editmember = (MobileBy.XPATH, "//*[@text='编辑成员']")


    def dell_memeber(self):
        # self.driver.find_element_by_xpath("//*[@text='编辑成员']").click()
        self.find_and_click(self.editmember)

        return Dellmembepager(self.driver)


