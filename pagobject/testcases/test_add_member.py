from pagobject.pages.main_page import MainPage


class TestAddMember:
    def setup_class(self):
        self.main = MainPage()
    def test_add_member(self):
        # self.main = MainPage()
        # 1.从首页跳转到添加成员页面
        # 2.添加成员
        # 3.保存

        self.main.go_to_add_member().add_member().save_member()

    def test_contact_member(self):
        # self.main = MainPage()
        # 1.从首页跳转到通讯录
        # 2.再跳转到添加成员页面
        # 3.添加成员
        # 4.保存
        self.main.go_to_contant().go_to_add_member().add_member().save_member()