
"""
存放app一些特有的操作
比如：启动应用，关闭应用。重启应用，进到首页等等

"""
from appium import webdriver

from qppium.po.page.Main_Page import MainPage
from qppium.po.page.base_page import BasePage


class App(BasePage):
    # 启动应用
    def start(self):
        if self.driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.WwMainActivity"
            caps["noReset"] = "true"
            # caps["dontStopAppOnReset"] = "true"
            # 等待动态页面空闲时间（预防动态页面拖时间）--打卡页面时间一直在刷新
            caps['settings[waitForIdleTimeout]'] = 1

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            # 隐式等待
            self.driver.implicitly_wait(5)
        else:
            # launch_app()--能直接调用上面代码配置的启动参数，并且不用做任何的初始化操作
            self.driver.launch_app()
        return self

    # 重新开始
    def restart(self):
        self.driver.launch_app()
    # 停止
    def stop(self):
        self.driver.quit()



    # 跳转到首页
    def goto_mainpag(self) -> MainPage:
        return MainPage(self.driver )