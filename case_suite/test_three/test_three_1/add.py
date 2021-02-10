#!/anaconda3/envs/FEALPy/bin 
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: add.py
# @Author: TangYong
# @Time: 三月 21, 2020

import unittest
class TestAdd(unittest.TestCase):
    ''' test_three_1 TestAdd'''

    def test_add1(self):
        s = 3 + 6
        self.assertEqual(9,s)

    def test_sdd2(self):
        s = 3 + 5
        self.assertEqual(7, s)
