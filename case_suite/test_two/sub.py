#!/anaconda3/envs/FEALPy/bin 
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: sub.py
# @Author: TangYong
# @Time: 三月 21, 2020

import unittest

class TestAdd(unittest.TestCase):

    def test_sub1(self):
        s = 3 - 2
        self.assertEqual(5, s)

    def test_sub2(self):
        s = 3 - 3
        self.assertEqual(6, s)
