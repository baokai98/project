import requests

from api_tag_requests.api_tag.wework import WeWork


class Tag(WeWork):
    def add_tag(self, tagid):
        add_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}"

        data = {
            "tagname": "UI", "tagid": tagid
        }
        r = requests.post(url=add_url, json=data)
        return r.json()

    def update_tag(self, tagid):
        update = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}"

        data = {
            "tagid": tagid,
            "tagname": "UI design"
        }
        r = requests.post(url=update, json=data)
        return r.json()

    def delete_tag(self, tagid):
        delet_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tagid}"
        r = requests.get(url=delet_url)
        return r.json()

    def get_tag_list(self):
        get_department_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        r = requests.get(url=get_department_url)
        print(r.json())
        return r.json()
