"""
======================
-*- coding :utf-8 -*-
@File:confftest.py
@Create:2020/05/12_16:20
@Email:18523607242@163.com
@Author: 袁晓松
@Software: PyCharm
======================
"""
import pytest

from common.config import conf
from common.data import CaseData
from common.randomNumber import RandomNumeber


@pytest.fixture(autouse=True)
def rand_number(): # 生成随机电话号码
    random_number = RandomNumeber()
    # 生成随机注册号码
    CaseData.phone = random_number.random_phone()
    # 随机密码
    CaseData.pwd = random_number.random_pwd(int(conf.get("rand_number", "length")))