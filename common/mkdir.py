"""
======================
-*- coding :utf-8 -*-
@File:mkdir.py
@Create:2020/05/09_15:59
@Email:18523607242@163.com
@Author: 袁晓松
@Software: PyCharm
======================
"""
import os

def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    is_exists = os.path.exists(path)
    if not is_exists:
        os.mkdir(path)
        return True
    else:
        return False
