from qppium.po.page.app import App
from qppium.po.page.base_page import BasePage


class TestConnact:

    def setup(self):

        # 应用的启动
        self.app = App()
        # 开启应用，去到首页
        self.main = self.app.start().goto_mainpag()


    def teardown(self):
        # 关闭应用
        self.app.stop()

    # 添加联系人
    def test_addcontact(self):

        name = "卡牌大师"
        gender = "男"
        phonenum = "15912600008"
        mypage = self.main.goto_addresslist().add_memeber().addcontact_menual().edit_name(name).edit_gender(gender).edit_phonenum(phonenum).click_save()
        # 获取toast的text属性
        mytoast = mypage.get_toast()
        assert mytoast == "添加成功"

    # 删除联系人
    def test_delcontact(self):
        name = "卡牌大师"
        # ******先进入搜索页面，判断被删联系人有没有，如果没有，则停止操作，如果有，则继续执行删除操作*****
        befnum = self.main.gaoto_delresslist().click_search().click_searchname(name)
        # 如果返回值只有一个，代表只有输入搜索的text属性，成员列表没有，则直接跳出
        if befnum == 1:

            assert befnum == 1
        else:
            # 如果返回值大于1，则表示成员列表中有需要删除的联系人，继续执行后面的删除步骤
            mydelpag = befnum.open_memeber().dell_memeber().clicl_dell()

            afternum = mydelpag.get_result(name)

            assert afternum == 1

        # mydelpag = self.main.gaoto_delresslist().click_search().click_searchname(name).open_memeber().dell_memeber().clicl_dell()
        #
        # afternum = mydelpag.get_result(name)
        #
        # assert afternum == 1

