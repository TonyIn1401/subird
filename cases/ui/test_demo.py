# _*_ coding: utf-8 _*_
'''
    @Author: zhaoxiang.zheng
    @Date: 2018-12-18 12:19:53
    @Last Modified by:   zhaoxiang.zheng
    @Last Modified time: 2018-12-18 12:19:53
'''
from templates.test_template import TestTemplate

class TestDemo1(TestTemplate):
    def test_001(self):
        self.assertEqual(1, 2, "error")
    def test_002(self):
        self.assertEqual(1, 1, "error")