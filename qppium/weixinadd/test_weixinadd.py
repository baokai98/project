from time import sleep

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

def get_datas():
    with open("./datas/add_lxr.yml", encoding='utf-8') as f:
        contact_datas = yaml.safe_load(f)
        addcontact = contact_datas['add']
        delcontact = contact_datas['del']
    return [addcontact, delcontact]

class Testweixin:
    def setup(self):
        # 初始化
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.WwMainActivity"
        # appium启动app时会自动清除app里面的数据，怎么做到启动app不清除数据呢？使用
        # 'noReset': "True" # 解决
        caps["noReset"] = "true"
        # caps["dontStopAppOnReset"] = "true"
        # 等待动态页面空闲时间（预防动态页面拖时间）--打卡页面时间一直在刷新
        caps['settings[waitForIdleTimeout]'] = 1

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 隐式等待
        self.driver.implicitly_wait(5)


    def teardown(self):
        # 退出

        self.driver.quit()
    @pytest.mark.parametrize("name,gender,phonenum",get_datas()[0])
    def test_addconnect(self,name,gender,phonenum):
        # name = "盖伦"
        # gender = "男"
        # phonenum = "18288988888"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 滚动查找
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 使用模糊匹配定位
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../*[@text='必填']").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        if gender == "女":
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        else:
            # 直接点击有时可以有时不行
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
            # 显示等待
            # element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='男']"))
            # element.click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '手机') and @class='android.widget.TextView']/..//*[@class='android.widget.EditText']").send_keys(phonenum)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hvk").click()
        # sleep(2)
        # self.driver.find_element_by_id('com.tencent.wework:id/hv3').click()
        # self.driver.find_element_by_id('com.tencent.wework:id/hvn').click()
        # self.driver.find_element_by_id('com.tencent.wework:id/gf').send_keys(name)
        # sleep(3)
        # ell = self.driver.find_element_by_xpath(f"//*[@text='{name}']")
        # addnum = len(ell)
        # assert addnum > 1

        mytoast = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert "添加成功" == mytoast
    @pytest.mark.parametrize("name",get_datas()[1])
    def test_delconnect(self,name):
        # name ="盖伦"
        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        self.driver.find_element_by_id('com.tencent.wework:id/hvn').click()
        self.driver.find_element_by_id('com.tencent.wework:id/gfs').send_keys(name)
        sleep(3)
        ele = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        # ele = self.driver.find_elements(MobileBy.XPATH,"//*[@text='盖伦'and @class='android.widget.TextView']")

        beforenum = len(ele)
        print(f'查到联系人数{beforenum}')
        if beforenum < 2:

            print("没有可删除的人员")
            return
        ele[1].click()
        sleep(2)
        # self.driver.find_element_by_id('com.tencent.wework:id/djf').click()
        self.driver.find_element_by_id('com.tencent.wework:id/hvd').click()

        self.driver.find_element_by_xpath("//*[@text='编辑成员']").click()
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("删除成员").instance(0));').click()
        self.driver.find_element_by_id('com.tencent.wework:id/efq').click()
        # 点击确定
        self.driver.find_element_by_id('com.tencent.wework:id/bit').click()
        # sleep(3)
        self.driver.find_element_by_id('com.tencent.wework:id/gfs').click()
        self.driver.find_element_by_id('com.tencent.wework:id/gfs').send_keys(name)
        eles1 = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        afternum = len(eles1)
        print(f'剩余联系人数{afternum}')
        # assert afternum == 1
        # 未来防止名字有相同字符，用这样的方式断言更好
        assert afternum == beforenum - 1


