import requests


class BaseApi:
    # 对requests二次封装
    def send_requests(self,req:dict):
        return requests.request(**req)