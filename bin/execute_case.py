#-*- coding: utf-8 -*-
# @Time    : 2018/6/21 11:21
# @Author  : TangYong
# @File    : execute_case.py
# @Software: PyCharm


import os
import sys
import requests

from cases.system.NAC import nac_config
sys.path.append(nac_config.base_dir)

from cases.system import conf
from main.runner import ExecuteCase



if __name__  == '__main__':

      runner = ExecuteCase(nac_config.report_info)

      runner.execute_discover_case(nac_config.case_root_path)



      response = requests.post(
           url='http://127.0.0.1:8000/saveTestInfo/',
           json=conf.test_case_suite,
           headers = {
                 'Content-Type': 'application/json',
                 'charset':'utf-8'
           }
      )

      print('测试完成:',response.text)




