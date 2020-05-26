"""
======================
-*- coding :utf-8 -*-
@File:data.py
@Create:2020/05/09_16:12
@Email:18523607242@163.com
@Author: 袁晓松
@Software: PyCharm
======================
"""
import re

from common.config import conf


class CaseData:
    """
    用于接收测试过程产生的数据
    """
    member_id = "100"


def replace_data(parameter):
    """
    正则替换
    :param parameter:代替换的数据
    :return:parameter:替换后的数据
    """
    r = r"#(.+?)#"  # 正则匹配表达式
    while re.search(r, parameter):
        res = re.search(r, parameter)
        key = res.group(1)
        # noinspection PyBroadException
        # 没有检查的 PyBroadException
        try:
            # 获取配置文件中的key对应的value
            value = conf.get("test_data", key)
        except Exception:
            # 获取全局变量中的key对应的value
            value = getattr(CaseData, key)
        finally:
            # value 字符串或者是引用可调用的，则将其传递给Match对象，并且必须返回要使用的替换字符串，
            # parameter 待替换的字符串，其中必须包含正则匹配表达式，
            # 1 替换次数，默认全部替换，可用数字控制
            parameter = re.sub(r, value, parameter, 1)
    return parameter


if __name__ == '__main__':
    s = "123#member_id#111111"
    res = replace_data(s)
    print(res)
