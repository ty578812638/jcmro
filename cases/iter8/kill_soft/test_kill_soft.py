#!/anaconda3/envs/FEALPy/bin 
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: kill_test_kill_soft.py
# @Author: TangYong
# @Time: 三月 29, 2020

import unittest
from cases.iter8.kill_soft import kill_test_data

class KillSoft(unittest.TestCase):

    def test_show(self):
        self.assertEqual(kill_test_data.string,'Hello')





if __name__ == '__main__':
    unittest.main()