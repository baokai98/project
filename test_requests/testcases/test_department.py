from test_requests.api.department import Department
from test_requests.api.wework import WeWork


class TestDeparment():
    def setup_class(self):
        wework = WeWork()
        self.department = Department()
        self.token = wework.get_token()

    def test_add_department(self):
        self.department.add_department(self.token,3)
        list = self.department.get_department_list(self.token)
        assert list["department"][1]["name"] == '霍格沃兹'
    def test_update_department(self):
        self.department.update_department(self.token,3)
        list = self.department.get_department_list(self.token)
        assert list["department"][1]["name"] == '广州研发中心'

    def test_delete_department(self):
        self.department.delete_department(self.token,3)
        list = self.department.get_department_list(self.token)
        assert len(list["department"]) == 1

    def test_get_department_list(self):
        self.department.get_department_list(self.token)
