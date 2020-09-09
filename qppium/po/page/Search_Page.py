from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from qppium.po.page.Edimemberl_Page import Editmemberpage
from qppium.po.page.Member_Page import  Memberpage
from qppium.po.page.base_page import BasePage
# 搜索页面

class Searchpag(BasePage):
    dellmember = (MobileBy.ID, 'com.tencent.wework:id/gfs')

    membernamelist = (MobileBy.ID, 'com.tencent.wework:id/hvd')
    backsearck = (MobileBy.ID, 'com.tencent.wework:id/gfs')

    # 查找联系人
    def click_searchname(self, name):
        # 点击搜索，输入成员
        membername = (MobileBy.XPATH, f"//*[@text='{name}']")
        self.find_and_sendkeys(self.dellmember, name)
        sleep(3)

        # ele = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        ele = self.finds(membername)
        # 找到搜索到的成员

        # 统计成员个数
        beforenum = len(ele)

        print(f'查到联系人数{beforenum}')
        # 判断成员个数
        if beforenum < 2:

            print("没有可删除的人员")
            # 把成员的个数返回到test，用来判断是否继续执行删除操作
            return beforenum
        else:

            ele[1].click()

            return Memberpage(self.driver)
    # 获取执行结果
    def get_result(self,name):
        membernames = (MobileBy.XPATH, f"//*[@text='{name}']")
        # self.driver.find_element_by_id('com.tencent.wework:id/gfs').click()

        self.find_and_click(self.backsearck)

        self.driver.find_element_by_id('com.tencent.wework:id/gfs').send_keys(name)
        # eles1 = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        eles1 = self.finds(membernames)
        # afternum = len(eles1)
        # print(f'剩余联系人数{afternum}')
        return len(eles1)
