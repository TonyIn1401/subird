# _*_ coding: utf-8 _*_
'''
    @Author: zhaoxiang.zheng
    @Date: 2019-01-16 16:36:36
    @Last Modified by:   zhaoxiang.zheng
    @Last Modified time: 2019-01-16 16:36:36
'''

import os
import json

class Config():
    """
    return the config info    
    """
    def __init__(self):
        settings = self._get_config()
        self.email = settings["email"]
        self.suits = settings["suits"]
        self.host = settings["host"]
        self.constant = settings["constant"]

    def _get_config(self):
        """
        get the config info from json file
        
        Returns:
            str -- config info
        """
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)) + '/settings.json')
        with open(path, 'r', encoding='UTF-8') as f:
            conf_str = json.load(f)
        return conf_str.decode() if isinstance(conf_str, bytes) else conf_str

if __name__ == '__main__':
    """
    for test
    """
    suits = Config().suits
    for case in suits:
        print(case[0][1])
