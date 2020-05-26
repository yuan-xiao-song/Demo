"""
======================
-*- coding :utf-8 -*-
@File:config.py
@Create:2020/05/09_14:04
@Email:18523607242@163.com
@Author: 袁晓松
@Software: PyCharm
======================
"""
import os
from configparser import ConfigParser  # 处理配置文件的python三方库
from common.filepath import CONFIGDIR

"""
处理配置文件
"""


class Config(ConfigParser):
    # 初始化Config类
    def __init__(self, config_name):
        # 调用父类的方法
        super().__init__()
        self.config_name = config_name;
        # 父类调用子类的对象
        self.read(filenames=config_name, encoding="utf-8")

    def get_data(self, section, option, data_type=None):
        """
        读取配置文件的指定部分的选项中
        :param section:部
        :param option:选项
        :param data_type:数据类型
        :return:res:数据
        """

        if data_type == "int":
            res = self.getint(section, option)
            return res
        elif data_type == "float":
            res = self.getfloat(section, option)
            return res
        else:
            res = self.get(section, option)
            return res

    def write_data(self, section, option, value):
        """
        写入数据到配置文件的指定部分的选项中
        :param section:部
        :param option:选项
        :param value:值
        :return:None
        """

        # set 设置指定部分模块的内容
        self.set(section, option, value)
        # write 将数据写入
        self.write(fp=open(self.config_name, "w"))


# 实例化Config对象
conf = Config(os.path.join(CONFIGDIR, "config.ini"))

if __name__ == '__main__':
    res = conf.get_data()
    print(res)
    print(type(res))
