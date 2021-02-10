#-*- coding: utf-8 -*-
# @Time    : 2018/6/21 11:21
# @Author  : TangYong
# @File    : execute_case.py
# @Software: PyCharm
import os
import  sys

import requests

cur_path = os.path.abspath(os.path.dirname(__file__))
project_path = os.path.split(cur_path)[0]
sys.path.append(project_path)

from fun import public
from settings import config
from cases.system import conf
from main.runner import ExecuteCase

if __name__ == '__main__':

    pc_id = sys.argv[1]
    child_path = sys.argv[2]

    sys_name = child_path.split('\\')[0]

    case_build_path = os.path.join(config.case_root_path, child_path).replace('\\','/')
    if not os.path.exists(case_build_path):
        raise OSError('用例路径【%s】不存在' % case_build_path)

    report_info = public.generate_test_report(pc_id,child_path)

    runner = ExecuteCase(report_info)
    runner.execute_discover_case(case_build_path)
    response = requests.post(
        url='http://127.0.0.1:8000/saveTestInfo/',
        json=conf.test_case_suite,
        headers={
            'Content-Type': 'application/json',
            'charset': 'utf-8'
        }
    )

    print('回传用例:', response.text)

    response = requests.post(
        url='http://127.0.0.1:8000/caseExeStatus/',
        json={'pc_id':pc_id},
        headers={
            'Content-Type': 'application/json',
            'charset': 'utf-8'
        }
    )
    print('回传状态:', response.text)



    response = requests.post(
        url='http://127.0.0.1:8000/getTestReport/',
        files= {'test_report':open(report_info['report_dir'],'rb') },
        # headers={
        #     'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
        # }
    )

    print('上传测试报告结果')


