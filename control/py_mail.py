#!/usr/bin/env python
#encoding: utf-8
#Author: guoxudong
import logging
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from logging.config import fileConfig

'''配置日志'''
fileConfig('./log/logging.conf')
logger=logging.getLogger('infoLogger')

def send_html(title,name,msg):
    # 第三方 SMTP 服务
    # mail_host = "smtp.163.com"  # SMTP服务器
    mail_host = "x"  # SMTP服务器
    mail_user = "x"  # 用户名
    mail_pass = "x"  # 密码

    sender = 'x'  # 发件人邮箱(最好写全, 不然会失败)
    receivers = ['x']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # f = open('./htmlTemplate/'+name+'.html', 'r',encoding='utf8')
    # content = f.read()
    # title = 'PyFun have a good time!'  # 邮件主题
    # message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message = MIMEMultipart()
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    with open('./resource/img/'+name+'.jpg', 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('image', 'jpg', filename=name+'.jpg')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename=name+'.jpg')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        message.attach(mime)
        message.attach(MIMEText('<!DOCTYPE html><html><body><h1 align="center">'+msg+'</h1>' +
                        '<p align="center"><img src="cid:0" style="border: medium double #614B40;border-width: 15px"></p>' +
                        '</body><h4 align="right">@sunny0826</h4></html>', 'html', 'utf-8'))
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        logging.debug("event:"+title+",mail has been send successfully.")
    except smtplib.SMTPException as e:
        logging.error(e)

# if __name__ == '__main__':
#     send_html('测试压缩','dengta','come from test')