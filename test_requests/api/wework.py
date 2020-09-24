import requests


class WeWork():
    def get_token(self):
        # token的定义
        corp_id = "wwf536893ca336a017"
        corp_secret = "fKqa6LDnPScoFWBR9a3KW49lhmAaD8DMH-9AMXcsL6c"
        token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"
        r = requests.get(url=token_url)
        return r.json()["access_token"]