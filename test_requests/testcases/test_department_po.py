
import yaml
from jsonpath import jsonpath

from test_requests.api.department import Department
from test_requests.api.wework import WeWork


class TestDepartment():
    def setup_class(self):

        self.department = Department()
        config_infor = yaml.safe_load(open("config.yaml"))
        # 通过传递不同的secret获取不同的token权限，给不同的业务测试用例使用
        # 当secret和业务加密相关，应该抽离出来维护
        self.department.get_token(config_infor["token"]["department_secret"])

    def test_add_department(self):
        self.department.add_department(3)
        list = self.department.get_department_list()
        # 使用jsonpath
        name = jsonpath(list,"$..name")
        # assert list["department"][1]["name"] == '霍格沃兹'
        assert '霍格沃兹' in name

    def test_update_department(self):
        self.department.update_department(3)
        list = self.department.get_department_list()
        name = jsonpath(list,"$..name")
        # assert list["department"][1]["name"] == '广州研发中心'
        assert '广州研发中心' in name

    def test_del_department(self):
        self.department.delete_department(3)
        list = self.department.get_department_list()
        name = jsonpath(list, "$..name")
        # assert len(list["department"]) == 1
        assert '广州研发中心'not in name

    def get_department_list(self):
        self.department.get_department_list()
        list = self.department.get_department_list()
        print(list)