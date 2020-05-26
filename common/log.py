"""
======================
-*- coding :utf-8 -*-
@File:log.py
@Create:2020/05/09_15:24
@Email:18523607242@163.com
@Author: 袁晓松
@Software: PyCharm
======================
"""
import logging
import os

from common.config import conf
from common.filepath import LOGDIR
from common.mkdir import mkdir


class Log:
    @staticmethod
    def creat_logger():
        """
        创建日志收集器
        :return: log (日志收集器)
        """
        """创建日志收集器"""
        # 获取日志
        log = logging.getLogger(conf.get("log", "log_name"))
        # 设置获取日志等级
        log.setLevel(conf.get("log", "level"))
        """设置日志输出渠道"""
        # 输出到控制台
        console = logging.StreamHandler()
        console.setLevel(conf.get("log", "console_level"))
        log.addHandler(console)
        # 输出到日志文件

        fp = logging.FileHandler(filename=os.path.join(LOGDIR, conf.get("log", "log_file_name")), encoding=conf.get("log", "encoding"))
        fp.setLevel(conf.get("log", "fp_level"))
        log.addHandler(fp)
        """设置日志输出格式"""
        # 日志输出格式
        formater = "%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s"
        fm = logging.Formatter(formater)
        # 绑定日志输出格式到日志输出渠道
        console.setFormatter(fm)
        fp.setFormatter(fm)
        return log


log = Log.creat_logger()
