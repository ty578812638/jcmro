#-*- coding: utf-8 -*-
# @Time    : 2018/6/20 16:00
# @Author  : TangYong
# @File    : runner.py
# @Software: PyCharm


import unittest
import HTMLTestRunner
# from  settings import config

class ExecuteCase(unittest.TestCase):
    def __init__(self,report_info):

        self.report_info = report_info

        #打开测试报告
        self.report_dir = open(self.report_info['report_dir'], 'wb')


    def execute_discover_case(self,case_path):

            self.discover = unittest.defaultTestLoader.discover(case_path, pattern='*.py')

            self.runner = HTMLTestRunner.HTMLTestRunner(
                stream=self.report_dir,
                title=self.report_info['report_title'],
                description=self.report_info['report_detail'],
                verbosity=2
            )

            runner_result = self.runner.run(self.discover)
            self.report_dir.close()

            success_count = runner_result.success_count
            failure_count = runner_result.failure_count
            error_count = runner_result.error_count

            print('success_count:',success_count)
            print('failure_count:', failure_count)
            print('error_count:', error_count)

            # public.send_email()




