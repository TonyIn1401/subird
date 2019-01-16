# _*_ coding: utf-8 _*_
'''
    @Author: zhaoxiang.zheng
    @Date: 2019-01-16 16:36:36
    @Last Modified by:   zhaoxiang.zheng
    @Last Modified time: 2019-01-16 16:36:36
'''

import os
import yaml

class Config():
    """
    解析yaml，获取相应配置信息
    """
    def __init__(self):
        self.settings = self._get_config()

    def _get_config(self):
        """
        解析yaml
        :return: s  字典
        """
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)) + '/settings.yaml')
        with open(path, 'r', encoding='UTF-8') as f:
            conf_str = yaml.load(f)
        return conf_str.decode() if isinstance(conf_str, bytes) else conf_str

    def email(self):
        """
        获取邮件配置信息
        """
        return self.settings["email_conf"]

    def suits(self):
        """
        获取测试用例配置
        """
        return self.settings["suits"]

    def host(self):
        """
        获取host信息
        """
        return self.settings["host"]


if __name__ == '__main__':
    suits = Config().suits()
    for case in suits:
        print(case[0][1])
