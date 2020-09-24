import pytest
import requests


class TestToken:
    # 前面为定义的参数名称，后面是参数具体的值，以[(),()]传值
    @pytest.mark.parametrize(
        "corp_id,corp_secret,errmsg",
         [( "wwf536893ca336a017","fKqa6LDnPScoFWBR9a3KW7AT9tcEMf56HKI1ZdI0C0I","ok"),
          ("","fKqa6LDnPScoFWBR9a3KW7AT9tcEMf56HKI1ZdI0C0I",'corpid missing'),
          ("wwf536893ca336a017","",'corpsecret missing',)])
    def test_token(self,corp_id,corp_secret,errmsg):
        # corp_id = "wwf536893ca336a017"
        # corp_secret = "fKqa6LDnPScoFWBR9a3KW7AT9tcEMf56HKI1ZdI0C0I"
        token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"
        r = requests.get(url=token_url)
        print(r.json())
        # assert r.json()['errcode'] == 0
        # assert r.json()['errmsg'] == 'corpid missing'
        # assert  r.json()['errmsg'] == 'corpsecret missing'
        assert r.json()['errmsg'] == errmsg