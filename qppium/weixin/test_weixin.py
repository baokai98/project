# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
class Testweixin:
    def setup(self):
        # 初始化
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.WwMainActivity"
        caps["noReset"] = "true"
        # 等待动态页面空闲时间（预防动态页面拖时间）--打卡页面时间一直在刷新
        caps['settings[waitForIdleTimeout]'] = 1

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 退出

        self.driver.quit()


    def test_faxinxi(self):
        # 定义输入的信息
        sendtext = "关二爷在此，尔等报上名来！"
        el5 = self.driver.find_element_by_id("hvn")
        el5.click()
        el6 = self.driver.find_element_by_id("gfs")
        # 搜索蛮王

        el6.send_keys("蛮王")

        el7 = self.driver.find_element_by_id("e12")
        el7.click()
        el8 = self.driver.find_element_by_id("ei_")
        el8.click()
        # 点击输入框
        el8.send_keys(sendtext)
        el9 = self.driver.find_element_by_id("ei6")
        el9.click()
        # 取出对话框的值
        elements = self.driver.find_elements_by_id("ehv")
        print(elements)
        # 断言

        assert sendtext == elements[-1].text
    def test_daka(self):
        # 点击工作台
        self.driver.find_element_by_xpath("//*[@text='工作台']").click()
        # 滚动查找
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("打卡").instance(0));').click()
        # 点击外出打卡
        self.driver.find_element_by_id("hgs").click()
        # 点击打卡按钮
        # 打卡页面是动态元素，使用模糊匹配
        self.driver.find_element_by_xpath('//*[contains(@text, "次外出")]').click()
        # 获取打卡成功text
        result = self.driver.find_element_by_id("oh").text
        # 断言
        assert "外出打卡成功" == result









