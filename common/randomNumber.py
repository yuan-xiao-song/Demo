"""
======================
-*- coding :utf-8 -*-
File Name:randomNumber
Create Date:2020/02/26
Change Activity:16:57
Email:18523607242@163.com
Author: 袁晓松
======================
"""
""" 
封装一个随机数类，自动生成随机电话号码,随机密码

"""
from random import choice, random
from common.config import conf


class RandomNumeber(object):

    def random_phone(self):
        """
        生成随机的电话号码
        :return:random_phone
        """
        pefixlist = eval(conf.get("rand_number", "random_tp"))
        le = str(random())[2:10:]
        random_phone = "".join((choice(pefixlist), le))
        return random_phone

    def random_pwd(self, length):
        random_passwd = conf.get("rand_number", "random_pwd")
        pwd = str()
        for i in range(length):
            pwd += choice(random_passwd)
        return pwd


if __name__ == '__main__':
    res = RandomNumeber()
    password = res.random_pwd(9)
    print(password)
