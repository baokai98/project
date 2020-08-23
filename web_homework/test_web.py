import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestWeb():
    def setup_method(self):
        # option = Options()
        # option.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=option)
        # 实例化driver
        self.driver = webdriver.Chrome()
        # 使用隐式等待
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def test_cookie(self):
        # 打开企业微信
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        # cookies = self.driver.get_cookies()
        # print(cookies)
        # 使用复用浏览器获取带有登录信息的cookie，但这个值有时效性
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851918879575'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'fBNUuJNaA-9fVWl38sltKjrwoy1Wba3g1ga0bnEtmLVhyvjOVRgsrfK6k-6LuHaBMCvmtYr87YW1cZUVR1YQPTBEeIzhfbidoTykwbl_n0Civi_pgfitHGlGgOn8Res9pn0VmILLrWMuv5Den5X55pNTyxieUGmy8AZ8wo6ygT2vZB7O04iIoLeCODgaVjyEOyP3NGSHsU9_Rz6-_JZoncMbWPlBJBnLjzgFseyb5_lysXIDomCJJnNnZtXmjhTd51EVTHUF0zivx-hTktOBGQ'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851918879575'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325005155704'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '5374823484'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a9165074'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'rogAy0x-xl_n4XJtdo1h2o0-j5CDfoiqPh2AxlE_0rZ5Py7kddKe760l76N9NpA_'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '16312238471593594'},
            {'domain': '.qq.com', 'expiry': 1598264807, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.472148947.1598155912'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1598187446.730042, 'httpOnly': True, 'name': 'ww_rtkey',
             'path': '/', 'secure': False, 'value': '3gmgrja'},
            {'domain': '.qq.com', 'expiry': 1661250407, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1161903829.1598155912'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1629691910.729965, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1600770409.766372, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh-cn'}]

        for cookie in cookies:
            # cookie不支持浮点数，删了不影响
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
                # 获取当前页面的cookies
            self.driver.add_cookie(cookie)
            # 重新打开 已带有cookie 信息的index 页面，完成自动登录
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        sleep(5)

    def test_importcontact(self):
        # 打开页面
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851918879575'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'fBNUuJNaA-9fVWl38sltKjrwoy1Wba3g1ga0bnEtmLVhyvjOVRgsrfK6k-6LuHaBMCvmtYr87YW1cZUVR1YQPTBEeIzhfbidoTykwbl_n0Civi_pgfitHGlGgOn8Res9pn0VmILLrWMuv5Den5X55pNTyxieUGmy8AZ8wo6ygT2vZB7O04iIoLeCODgaVjyEOyP3NGSHsU9_Rz6-_JZoncMbWPlBJBnLjzgFseyb5_lysXIDomCJJnNnZtXmjhTd51EVTHUF0zivx-hTktOBGQ'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851918879575'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325005155704'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '5374823484'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a9165074'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'rogAy0x-xl_n4XJtdo1h2o0-j5CDfoiqPh2AxlE_0rZ5Py7kddKe760l76N9NpA_'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '16312238471593594'},
            {'domain': '.qq.com', 'expiry': 1598264807, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.472148947.1598155912'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1598187446.730042, 'httpOnly': True, 'name': 'ww_rtkey',
             'path': '/', 'secure': False, 'value': '3gmgrja'},
            {'domain': '.qq.com', 'expiry': 1661250407, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1161903829.1598155912'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1629691910.729965, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1600770409.766372, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh-cn'}]

        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        sleep(3)
        # 点击导入通讯录
        self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]/div/span[2]').click()
        # 自动上传指定文件
        self.driver.find_element_by_xpath('//*[@id="js_upload_file_input"]').send_keys(
            r'C:\Users\Administrator\Desktop\mydata.xls')
        sleep(3)
        # 断言
        assert 'mydata.xls' == self.driver.find_element_by_xpath('//*[@id="upload_file_name"]').text
        sleep(3)

    def test_shelve(self):
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

        # cookies = [
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #      'value': '1688851918879575'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #      'value': 'fBNUuJNaA-9fVWl38sltKjrwoy1Wba3g1ga0bnEtmLVhyvjOVRgsrfK6k-6LuHaBMCvmtYr87YW1cZUVR1YQPTBEeIzhfbidoTykwbl_n0Civi_pgfitHGlGgOn8Res9pn0VmILLrWMuv5Den5X55pNTyxieUGmy8AZ8wo6ygT2vZB7O04iIoLeCODgaVjyEOyP3NGSHsU9_Rz6-_JZoncMbWPlBJBnLjzgFseyb5_lysXIDomCJJnNnZtXmjhTd51EVTHUF0zivx-hTktOBGQ'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #      'value': '1688851918879575'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        #      'value': '1970325005155704'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
        #      'secure': False, 'value': '5374823484'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        #      'value': 'direct'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        #      'value': 'a9165074'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
        #      'value': 'rogAy0x-xl_n4XJtdo1h2o0-j5CDfoiqPh2AxlE_0rZ5Py7kddKe760l76N9NpA_'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        #      'value': '16312238471593594'},
        #     {'domain': '.qq.com', 'expiry': 1598264807, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.472148947.1598155912'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1598187446.730042, 'httpOnly': True, 'name': 'ww_rtkey',
        #      'path': '/', 'secure': False, 'value': '3gmgrja'},
        #     {'domain': '.qq.com', 'expiry': 1661250407, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.1161903829.1598155912'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1629691910.729965, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
        #      'path': '/', 'secure': False, 'value': '0'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1600770409.766372, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #      'path': '/', 'secure': False, 'value': 'zh-cn'}]
        # db = shelve.open('./mydbs/cookies')
        # db['cookie'] = cookies
        # db.close()
        db = shelve.open('./mydbs/cookies')
        cookies = db['cookie']
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]/div/span[2]').click()
        self.driver.find_element_by_xpath('//*[@id="js_upload_file_input"]').send_keys(
            'Users\Administrator\Desktop\mydata.xls')
        sleep(3)

        assert 'mydata.xls' == self.driver.find_element_by_xpath('//*[@id="upload_file_name"]').text
        sleep(3)
