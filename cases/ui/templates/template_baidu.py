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
from selenium import webdriver
from config.config import Config

class BaiduTemplate(unittest.TestCase):
    def tearDown(self):
        """
        # 每个测试用例执行之后做操作
        """
        logging.info("tearDown for each testcase")
        super(BaiduTemplate, self).tearDown()

    def setUp(self):
        """
        # 每个测试用例执行之前做操作
        """
        # 每个测试用例执行之前做操作
        logging.info("setUp for each testcase")

    @classmethod
    def tearDownClass(cls):
        """
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        """
        logging.info("tearDown Class for testcase")
        cls.driver.quit()
        
    @classmethod
    def setUpClass(cls):
        """
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        """
        logging.info("SetUp Class for testcase")
        cls.__lgoin()
        cls.driver = cls.__lgoin()

    @classmethod
    def __lgoin(cls):
        host = Config().host
        url = host["url"]
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        time.sleep(2)
        return driver