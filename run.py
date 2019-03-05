# _*_ coding: utf-8 _*_
'''
    @Author: zhaoxiang.zheng
    @Date: 2019-01-16 15:40:49
    @Last Modified by:   zhaoxiang.zheng
    @Last Modified time: 2019-01-16 15:40:49
'''
import time
from case_handler import Cases
from email_handler import Email
from config.config import Config

def run():
    """
    begin to run the test
    """
    cons = Config().constant
    cases = Cases()
    result = Cases().run(cons["GENERATE_TYPE"])
    email = Email()
    email_body = ""
    email_body_type = ""
    if result.ok:
        with open(result.msg, 'r', encoding='UTF-8') as fp:
            email_body = fp.read()
    else:
        email_body = result.msg
    
    email_body_type = "html" if cons["GENERATE_TYPE"] == "html" else "xml"
    email_subject = 'TEST-REPORT-{0}'.format(time.strftime("%Y-%m-%d"))
    email.send(email_body, email_body_type, email_subject)

if __name__ == '__main__':
    """
    main method
    """
    run()