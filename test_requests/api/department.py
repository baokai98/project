import requests


class Department:
    def add_department(self,token,department_id):
        add_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={token}"

        data = {"name": "霍格沃兹","name_en": "RDGZ", "parentid": 1, "order": 1,"id": department_id}
        # 发送添加部门请求
        r = requests.post(url=add_url, json=data)
        return r.json()

    def update_department(self,token,department_id):
        update = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={token}"

        data = {"id": department_id,"name": "广州研发中心","name_en": "RDGZ","parentid": 1,"order": 1 }
        r = requests.post(url=update, json=data)
        return r.json()

    def delete_department(self,token,department_id):
        delet_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={token}&id={department_id}"
        r = requests.get(url=delet_url)
        return r.json()

    def get_department_list(self,token):
        get_department_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={token}"
        r = requests.get(url=get_department_url)
        return r.json()
