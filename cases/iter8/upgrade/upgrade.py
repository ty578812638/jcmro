#!/anaconda3/envs/FEALPy/bin 
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: upgrade.py
# @Author: TangYong
# @Time: 四月 05, 2020

import  unittest

class TimeShare(unittest.TestCase):
    def test_time_share1(self):
        '''测试分时%s'''%'1'
        # self.assertEqual(time_test_data.string,'time_share')
        self.assertEqual('upgrade', 'upgrade','升级比较')
        print('升级')

    def test_time_share2(self):
        ''''测试分时%s'''%'2'
        # self.assertEqual(time_test_data.string,'time_share')
        self.assertEqual('time', 'time_share')
        print('我的分时')