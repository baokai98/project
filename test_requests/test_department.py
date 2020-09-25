# 增加部门-->修改部门-->删除部门
import requests


class TestDepartment:
    def setup_class(self):
        corp_id = "wwf536893ca336a017"
        corp_secret = "fKqa6LDnPScoFWBR9a3KW49lhmAaD8DMH-9AMXcsL6c"
        token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"
        r = requests.get(url=token_url)
        print(r.json()['access_token'])
        self.token = r.json()["access_token"]
        self.ID = 2
    def test_add_department(self):
        add_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"

        data = {
               "name": "霍格沃兹",
               "name_en": "RDGZ",
               "parentid": 1,
               "order": 1,
               "id": self.ID
             }
        # 发送添加部门请求
        r = requests.post(url=add_url,json=data)
        print(r.json())
        # 获取请求结果列表   调用查询部门列表接口，获取部门列表信息
        get_department_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list = requests.get(url=get_department_url)
        print(list.json())

        assert r.json()['errmsg'] == 'created'
        # 判断部门列表信息中有没有添加的部门名称，防止部门信息没刷新而看不到,用上面的短语不稳定
        assert list.json()["department"][1]["name"] == '霍格沃兹'
    def test_update_department(self):
        update = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        get_department_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        data = {
               "id": self.ID,
               "name": "广州研发中心",
               "name_en": "RDGZ",
               "parentid": 1,
               "order": 1
            }
        requests.post(url=update,json=data)
        list = requests.get(url=get_department_url)
        print(list.json())
        print(len(list.json()["department"]))
        # self.ele = len(list.json()["department"])
        assert list.json()["department"][1]["name"] == '广州研发中心'


    def test_del_department(self):
        delet_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={self.ID}"
        get_department_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        requests.get(url=delet_url)
        list = requests.get(url=get_department_url)
        assert len(list.json()["department"]) == 1
