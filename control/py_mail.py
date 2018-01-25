#!/usr/bin/env python
#encoding: utf-8
#Author: guoxudong
import smtplib
from email.mime.text import MIMEText


def send_html(title,name):
    # 第三方 SMTP 服务
    mail_host = "smtp.xxx.com"  # SMTP服务器
    mail_user = "xxxxxxx"  # 用户名
    mail_pass = "xxxxxxx"  # 密码

    sender = 'xxxxx@xxx.com'  # 发件人邮箱(最好写全, 不然会失败)
    receivers = ['xxxx@xxx.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    f = open('../htmlTemplate/'+name+'.html', 'r',encoding='utf8')
    content = f.read()
    # title = 'PyFun have a good time!'  # 邮件主题
    message = MIMEText(content, 'html', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)

if __name__ == '__main__':
    send_html('测试压缩','hua')