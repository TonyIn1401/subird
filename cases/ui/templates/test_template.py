# _*_ coding: utf-8 _*_
'''
    @Author: zhaoxiang.zheng
    @Date: 2018-12-18 12:24:43
    @Last Modified by:   zhaoxiang.zheng
    @Last Modified time: 2018-12-18 12:24:43
'''
import unittest
import time
import logging

class TestTemplate(unittest.TestCase):    
    @classmethod
    def setUpClass(cls):
        logging.info("SetUp Class for testcase")

    @classmethod
    def tearDownClass(cls):
        logging.info("tearDown Class for testcase")

    def tearDown(self):
        logging.info("tearDown for testcase")
        super(TestTemplate, self).tearDown()
        #用例间隔时间5s
        time.sleep(5)
        