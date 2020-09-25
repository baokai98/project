import requests

from test_requests.api.Base_api import BaseApi


class WeWork(BaseApi):
    def get_token(self,corp_secret):
        # token的定义
        corp_id = "wwf536893ca336a017"
        # corp_secret = "fKqa6LDnPScoFWBR9a3KW49lhmAaD8DMH-9AMXcsL6c"
        # token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"
        req = {"method":"get",
               "url":f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"

        }
        # r = requests.get(url=token_url)
        r = self.send_requests(req)
        self.token = r.json()["access_token"]
        return self.token
