import requests

from test_requests.api.wework import WeWork


class Department(WeWork):
    def add_department(self,department_id):
        # add_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
        data = {"name": "霍格沃兹","name_en": "RDGZ", "parentid": 1, "order": 1,"id": department_id}
        req = {
            "method":"post",
            "url":f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}",
            "json": data
        }
        r= self.send_requests(req)
        # 发送添加部门请求
        # r = requests.post(url=add_url, json=data)
        return r.json()

    def update_department(self,department_id):
        # update = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"

        data = {"id": department_id,"name": "广州研发中心","name_en": "RDGZ","parentid": 1,"order": 1 }
        # r = requests.post(url=update, json=data)
        req = {
            "method": "post",
            "url":f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}" ,
            "json": data
        }
        r = self.send_requests(req)
        return r.json()

    def delete_department(self,department_id):
        # delet_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={department_id}"
        # r = requests.get(url=delet_url)
        req = {
            "method": "get",
            "url":f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={department_id}" ,
        }
        r = self.send_requests(req)
        return r.json()

    def get_department_list(self):
        # get_department_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        # r = requests.get(url=get_department_url)
        req = {
            "method": "get",
            "url":f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}",
        }
        r = self.send_requests(req)
        print(list)
        return r.json()


