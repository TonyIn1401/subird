# _*_ coding: utf-8 _*_
'''
    @Author: zhaoxiang.zheng
    @Date: 2019-01-17 15:36:09
    @Last Modified by:   zhaoxiang.zheng
    @Last Modified time: 2019-01-17 15:36:09
'''
import os, sys, time
import unittest
import xmlrunner
from config.config import Config
from common.constant import GenerateType
from common.HTMLTestRunnerCn import HTMLTestRunner
from common.result import Result
import logging

class Cases():
    def __init__(self):
        conf = Config()
        self.suites_conf = conf.suits
        self.conf = conf.constant

    def load(self):
        '''
        加载配置中的所有测试用例
        '''
        suites_all = unittest.TestSuite()
        for folder in self.suites_conf:
            file_path = folder["file_path"]
            sys.path.append(os.path.dirname(file_path))
            suites = unittest.TestSuite()
            for case_file in folder["file"]:
                runable = case_file["runable"]
                file_name = case_file["name"]
                class_name = case_file["class"]
                if not runable:
                    print("cases in {0}/{1}.py is skiped cause runable status is {2}".format(file_path, file_name, runable))
                    continue
                cases = unittest.TestSuite()
                cases_conf = case_file["cases"]
                module = __import__(file_name)
                module_obj = getattr(module, class_name)
                for case in cases_conf:
                    cases.addTest(module_obj(case))
                suites.addTests(cases)
            suites_all.addTests(suites)
        return suites_all

    def run(self, runner_type):
        result = Result()
        try:
            file_name = 'TEST-REPORT-{0}.{1}'.format(time.strftime("%Y%m%d%H%M%S"), runner_type)
            suites = self.load()
            if runner_type == GenerateType().XML:
                result.msg = self.__run_xml(suites, file_name)
            else:
                result.msg = self.__run_html(suites, file_name)
            result.ok = True
        except Exception as e:
            result.ok = False
            result.msg = "error durring run suits {}".format(e)
        finally:
            return result
        

    def __run_xml(self, suites, file_name):
        report_path = os.path.join(self.conf["RESULT_PATH_XML"], file_name)
        with open(report_path, 'w', encoding='UTF-8') as fp:
            xml_runner = xmlrunner.XMLTestRunner(output=fp)
            xml_runner.run(suites)
        return report_path

    def __run_html(self, suites, file_name):
        report_path = os.path.join(self.conf["RESULT_PATH_HTML"], file_name)
        with open(report_path, 'wb') as fp:
            runner = HTMLTestRunner(
                stream=fp,
                title='自动化测试报告',
                tester='Zhaoxiang'
                )
            runner.run(suites)
        return report_path

if __name__ == "__main__":
    cons = Config().constant
    Cases().run(cons["GENERATE_TYPE"])