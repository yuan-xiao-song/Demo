"""
======================
-*- coding :utf-8 -*-
@File:request.py
@Create:2020/05/09_15:09
@Email:18523607242@163.com
@Author: 袁晓松
@Software: PyCharm
======================
"""
import requests

"""
发送Http请求
"""
class Request:
    """初始化Request类"""
    def __init__(self):
        self.session = requests.session()

    def send_request(self, url, method, headers=None, params=None, data=None, json=None, files=None):
        method = method.lower()
        if method == "get":
            response = self.session.get(url=url, params=params, headers=headers)
            return response
        elif method == "post":
            response = self.session.post(url=url, json=json, data=data, files=files, headers=headers)
            return response
        elif method == "patch":
            response = self.session.patch(url=url, json=json, data=data, files=files, headers=headers)
            return response
        elif method == "put":
            response = self.session.put(url=url, json=json, data=data, headers=headers)
            return response
