"""
======================
-*- coding :utf-8 -*-
@File:email.py
@Create:2020/05/11_09:51
@Email:18523607242@163.com
@Author: 袁晓松
@Software: PyCharm
======================
"""
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from common.config import conf


def send_email(filename, title):
    """
    发送邮件
    :param filename: 附件名称(路径)
    :param title: 邮件主题
    :return:
    """
    """连接smtp服务器,登录邮箱"""
    # 创建smtp服务器连接对象
    smtp = smtplib.SMTP_SSL(host=conf.get_data("email", "host"), port=conf.get_data("email", "port", "int"))
    # 登录邮箱
    smtp.login(user=conf.get_data("email", "user"), password=conf.get_data("email", "pwd"))

    """构建邮件内容"""
    # 创建一封带附件的邮件
    msg = MIMEMultipart()

    with open(filename, "rb") as f:
        content = f.read()
    # 正文内容
    text_msg = MIMEText(_text=content, _subtype="html", _charset="utf8")
    # 讲正文类容添加到正文中
    msg.attach(text_msg)
    # 邮件附件
    report_file = MIMEApplication(content)
    report_file.add_header('content-disposition', 'attachment', filename=filename)
    msg.attach(report_file)
    msg["Subject"] = title
    # 发件人
    msg["From"] = conf.get("email", "from_addr")
    # 收件人
    msg["To"] = conf.get("email", "to_addr")

    """发送邮件"""
    smtp.send_message(msg, from_addr=conf.get("email", "from_addr"), to_addrs=eval(conf.get("email", "to_addr")))



