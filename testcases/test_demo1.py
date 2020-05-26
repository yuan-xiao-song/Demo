"""
======================
-*- coding :utf-8 -*-
@File:test_demo1.py
@Create:2020/05/12_17:05
@Email:18523607242@163.com
@Author: 袁晓松
@Software: PyCharm
======================
"""
import os
import allure
import pytest
from common.config import conf
from common.data import replace_data
from common.filepath import DATADIR
from common.log import log
from common.request import Request
from common.excel import Excel


@allure.feature("注册功能")  # 测试场景
@allure.suite("注册")  # 添加进测试套件
@allure.severity(allure.severity_level.CRITICAL)  # 用例严重程度
class TestTegister:
    # 读取测试用例
    excel_path = os.path.join(DATADIR, "interfaceCase.xlsx")
    excel1 = Excel(excel_path, "register_success")
    cases1 = excel1.get_data()
    # 发送请求对象
    request = Request()

    @pytest.mark.parametrize("case", cases1)
    @allure.title("{case[title]}")  # 用例名称
    @allure.story("注册正常情况")  # 特性场景
    @allure.description("注册成功")  # 用例描述
    @allure.tag("注册")  # 标签
    def test_register_success(self, case):
        allure.dynamic()
        with allure.step("第一步：准备数据"):
            with allure.step("接口地址"):
                url = conf.get("env", "host") + case["url"]
                allure.attach(body=url, name="接口请求地址")  # , extension=allure.attachment_type.TEXT
            with allure.step("请求方法"):
                method = case["method"]
                allure.attach(body=method, name="接口请求方法", extension=allure.attachment_type.TEXT)
                headers = eval(conf.get("env", "headers"))
            with allure.step("请求数据"):
                case["data"] = replace_data(case["data"])
                json = case["data"]
                allure.attach(body=json, name="用例数据", extension=allure.attachment_type.JSON)
            with allure.step("预期结果"):
                expected = eval(case["expected"])
                allure.attach(body=case["expected"], name="预期结果", extension=allure.attachment_type.TEXT)
            row = case["case_id"] + 1
            # 发送请求

        with allure.step("第二步：获取响应结果"):
            response = self.request.send_request(url=url, method=method, headers=headers, json=eval(json))
            allure.attach(str(response.json()), "响应结果", allure.attachment_type.JSON)
        res = response.json()
        with allure.step("第三步：测试结果"):
            try:
                assert expected["code"] == res["code"]
                assert expected["msg"] == res["msg"]
            except AssertionError as e:
                self.excel1.write_data(row=None, column=8, value="未通过")
                log.error(f"用例{case['title']},测试未通过")
                log.exception(e)
                raise e
            else:
                self.excel1.write_data(row=row, column=8, value="通过")
                log.info(f"用例{case['title']},测试通过")
                allure.attach(f"{case['title']}用例测试通过", "测试结果", allure.attachment_type.TEXT)
