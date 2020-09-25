import requests

# 获取access_token，获取access_token是调用企业微信API接口的第一步，相当于创建了一个登录凭证，其它的业务API接口，都需要依赖于access_token来鉴权调用者身份。
class WeWork():
    def get_token(self):
        # token的定义
        corp_id = "wwf536893ca336a017"
        corp_secret = "fKqa6LDnPScoFWBR9a3KW49lhmAaD8DMH-9AMXcsL6c"
        token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"
        r = requests.get(url=token_url)
        self.token = r.json()["access_token"]
        return self.token