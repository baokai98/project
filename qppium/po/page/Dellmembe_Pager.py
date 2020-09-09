
from appium.webdriver.common.mobileby import MobileBy

# from qppium.po.page.Search_Page import Searchpag
# from qppium.po.page.Search_Page import Searchpag
from qppium.po.page.base_page import BasePage

# 删除成员页面
class Dellmembepager(BasePage):
    dellmember = (MobileBy.ID, 'com.tencent.wework:id/efq')
    affirmdell = (MobileBy.ID, 'com.tencent.wework:id/bit')
    def clicl_dell(self):
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("删除成员").instance(0));').click()
        # self.driver.find_element_by_id('com.tencent.wework:id/efq').click()
        self.find_and_click(self.dellmember)
    # def click_affirm(self):
        # self.driver.find_element_by_id('com.tencent.wework:id/bit').click()
        # 点击确定
        self.find_and_click(self.affirmdell)

        from qppium.po.page.Edimemberl_Page import Editmemberpage
        from qppium.po.page.Search_Page import Searchpag
        return Searchpag(self.driver)