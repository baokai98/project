from pagobject.pages.main_page import MainPage

"""
po 原则解读
方法意义
用公共方法代表UI所提供的功能
方法应该返回其他的PageObject或者返回用于断言的数据
同样的行为不同的结果可以建模为不同的方法
不要在方法内加断言
字段意义
不要暴露页面内部的元素给外部
不需要建模UI内的所有元素
******
cmd命令打开浏览器：chrome --remote-debugging-port=9222
"""


class TestAddMember:
    def setup_class(self):
        self.main = MainPage()

    def test_add_member(self):
        # self.main = MainPage()
        # 1.从首页跳转到添加成员页面
        # 2.添加成员
        # 3.保存
        name = "蛮王"
        acctid = "55565"
        phone = "13888812346"
        namelist1 = self.main.go_to_add_member().add_member(name, acctid, phone).save_member().get_member_list()
        assert name in namelist1

    def test_contact_member(self):
        # self.main = MainPage()
        # 1.从首页跳转到通讯录
        # 2.再跳转到添加成员页面
        # 3.添加成员
        # 4.保存
        name = "蛮王"
        acctid = "55565"
        phone = "13888812346"
        namelist2 = self.main.go_to_contant().go_to_add_member().add_member(name, acctid,
                                                                            phone).save_member().get_member_list()
        assert name in namelist2

    def test_addmember_fail(self):
        # 添加联系人失败
        name = "蛮子"
        acctid = "55565"
        phone = "13888812346"
        namekist3 = self.main.go_to_add_member().add_member(name, acctid, phone).cancel_member().get_member_list()
        assert name not in namekist3

    def test_addpartment_save(self):
        patrment_name = "黑色玫瑰"
        patrment_namelist1 = self.main.go_to_contant().add_partment().add_new_department(
            patrment_name).save_department().get_partment_list()

        assert patrment_name in patrment_namelist1

    #
    def test_addpartment_cancel(self):
        patrment_name2 = "影流之主"
        patrment_namelist2 = self.main.go_to_contant().add_partment().add_new_department(
            patrment_name2).cancel_department().get_partment_list()
        assert patrment_name2 not in patrment_namelist2
