"""
======================
-*- coding :utf-8 -*-
@File:mySql.py
@Create:2020/05/09_14:04
@Email:18523607242@163.com
@Author: 袁晓松
@Software: PyCharm
======================
"""
import pymysql

from common.config import conf


class MySQL:
    # 初始化MySql类
    def __init__(self):
        # 数据库连接对象
        self.conn = pymysql.connect(
            host=conf.get("db", "host"),
            port=conf.getint("db", "port"),
            user=conf.get("db", "user"),
            password=conf.get("db", "pwd"),
            charset=conf.get("db", "charset"),
            cursorclass=pymysql.cursors.DictCursor
        )
        # 创建数据库游标对象
        self.cur = self.conn.cursor()

    def find_one(self, sql):
        """获取查询出来的第一条数据"""
        # 执行查询语句
        self.conn.commit()
        self.cur.execute(sql)
        data = self.cur.fetchone()
        return data

    def find_all(self, sql):
        """获取查询出来的所有数据"""
        self.conn.commit()
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data

    def find_count(self, sql):
        """返回查询数据的条数"""
        self.conn.commit()
        return self.cur.execute(sql)

    def close(self):
        """关闭游标，断开连接"""
        self.cur.close()
        self.conn.close()
