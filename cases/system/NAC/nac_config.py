#!/anaconda3/envs/FEALPy/bin 
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: nac_config.py
# @Author: TangYong
# @Time: 四月 19, 2020
import os
import time

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))).replace('/','\\')

sys_name = 'NAC'

#用例根目录
case_root_path = os.path.join(base_dir,'cases','system',sys_name)

#测试报告根路径
report_save_path = os.path.join(base_dir,'report',sys_name)
if not os.path.exists(report_save_path ):
    os.makedirs(report_save_path)

current_time = time.strftime('%y%m%d%H%M%S')
report_name = ''.join([sys_name,'_TestReport_',current_time,'.html'])
report_dir = os.path.join(report_save_path,report_name)

#测试报告详情信息
report_info = {
    'report_dir':report_dir,
    'report_title':'%s_auto_test_report'%sys_name,
     'report_detail':'请查看附件详情测试报告'
}





