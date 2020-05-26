# -*- coding :utf-8 -*-
# File Name:handlepath
# Create Date:2020/02/14
# Change Activity:下午 9:14
# Email:18523607242@163.com
# Author: 袁晓松

import os

BASDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目的基础目录

DATADIR = os.path.join(BASDIR, "data")  # 测试用例数据文件存放目录

REPORTDIR = os.path.join(BASDIR, "reports")  # 测试报告存放目录

CONFIGDIR = os.path.join(BASDIR, "conf")  # 配置文件存放目录

CASEDIR = os.path.join(BASDIR, "testcases")  # 测试用例类存放目录

LOGDIR = os.path.join(BASDIR, "logs")  # 测试运行程序日志存放目录

