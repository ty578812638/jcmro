#!/anaconda3/envs/FEALPy/bin 
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_time_share.py
# @Author: TangYong
# @Time: 三月 29, 2020

import unittest
# import  time_test_data

class TimeShare(unittest.TestCase):
    def test_time_share1(self):
        '''测试分时1'''
        # self.assertEqual(time_test_data.string,'time_share')
        self.assertEqual('time_share', 'time_share')
        print('我的分时')

    def test_time_share2(self):
        '''测试分时2'''
        # self.assertEqual(time_test_data.string,'time_share')
        self.assertEqual('time', 'time_share')
        print('我的分时')