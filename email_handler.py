# _*_ coding: utf-8 _*_
'''
    @Author: zhaoxiang.zheng
    @Date: 2019-01-16 16:34:43
    @Last Modified by:   zhaoxiang.zheng
    @Last Modified time: 2019-01-16 16:34:43
'''

from email.mime.text import MIMEText
import smtplib
from config.config import Config

class Email():
    '''
    邮件处理类
    '''
    def __init__(self):
        self.email_conf = Config().email

    def __init_msg(self, body, body_type, subject):
        msg = MIMEText(body, body_type, 'utf-8')
        msg['From'] = '{} {}'.format(self.email_conf["nick_name"], self.email_conf["from"])
        msg['To'] = str(self.email_conf["to"])
        msg['Subject'] = subject
        return msg

    def __init_server(self):
        server = smtplib.SMTP(self.email_conf["smtp_server"], int(self.email_conf["smtp_port"]))
        server.set_debuglevel(1)
        return server

    def send(self, body, body_type, subject):
        '''
        发送邮件
        body: 邮件内容
        body_type: 邮件内容的格式，可选plain, html
        subject: 邮件主题
        '''
        msg = self.__init_msg(body, body_type, subject)
        server = self.__init_server()
        server.login(self.email_conf["username"], self.email_conf["password"])
        server.sendmail(self.email_conf["from"], self.email_conf["to"], msg.as_string())
        server.quit()
    
if __name__ == '__main__':
    Email().send('Test email body', 'plain', 'Test subject')