# _*_ coding: utf-8 _*_
'''
    @Author: zhaoxiang.zheng
    @Date: 2018-12-18 12:19:53
    @Last Modified by:   zhaoxiang.zheng
    @Last Modified time: 2018-12-18 12:19:53
'''
import time
from templates.template_baidu import BaiduTemplate

class TestDemo1(BaiduTemplate):

    def test_001(self):
        driver = self.driver
        input_box = driver.find_element_by_id("kw")
        input_box.click()
        time.sleep(1)
        input_box.send_keys("廖雪峰")
        time.sleep(1)
        driver.find_element_by_id("su").click()
        

    def test_002(self):
        a = self.driver.find_element_by_xpath("div[@id='1']/h3/a")
        print(a.text())