"""
======================
-*- coding :utf-8 -*-
@File:handle_yaml.py
@Create:2020/04/16_10:29
@Email:18523607242@163.com
@Author: 袁晓松
@Software: PyCharm
======================
"""
import os

import yaml
from common.filepath import DATADIR


class Handelyaml:
    def __init__(self, filemane):
        self.filename = filemane

    def read_data(self):
        """读取数据"""
        with open(file=self.filename, mode='r', encoding='utf-8') as f:
            datas = yaml.load(f, Loader=yaml.Loader)
            return datas


if __name__ == '__main__':
    data_path = os.path.join(DATADIR, "get_token.yml")

    res = Handelyaml(data_path)
    cases = res.read_data()
    print(cases, type(cases))
