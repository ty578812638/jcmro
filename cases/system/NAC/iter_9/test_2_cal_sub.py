#!/anaconda3/envs/FEALPy/bin 
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_2_计算减法.py
# @Author: TangYong
# @Time: 四月 05, 2020

import unittest
from fun import public
from ddt import ddt,data,unpack
from cases.system.NAC.iter_8 import iter_8_tdt



@ddt
class CalculateAdd(unittest.TestCase):
    '''计算减法'''
    @data((10,1))
    @unpack
    def test_1_sub(self,add1,add2):

        exp_res =  9
        act_res = add1 - add2
        try:
            self.assertEqual(exp_res, act_res, '计算加法结果')


        except Exception as e:
            assert_res = e
            raise AssertionError

        finally:
            iter_8_tdt.start_row_no += 1

    @data((10, 2))
    @unpack
    def test_2_sub(self, add1, add2):

        act_res = add1 - add2
        try:
            self.assertEqual(8, act_res, '计算加法结果')


        except Exception as e:
            raise AssertionError

        finally:
            iter_8_tdt.start_row_no += 1


    @data((10, 3))
    @unpack
    def test_3_sub(self, add1, add2):

        act_res = add1 - add2
        try:
            self.assertEqual(7, act_res, '计算加法结果')

        except Exception as e:

            raise AssertionError

        finally:
            iter_8_tdt.start_row_no += 1

    @data((10, 5))
    @unpack
    def test_4_sub(self, add1, add2):

        act_res = add1 - add2
        try:
            self.assertEqual(5, act_res, '计算加法结果')

        except Exception as e:

            raise AssertionError

        finally:
            iter_8_tdt.start_row_no += 1


    @data((10,6))
    @unpack
    def test_5_sub(self, add1, add2):

        act_res = add1 - add2
        try:
            self.assertEqual(4, act_res, '计算加法结果')


        except Exception as e:
            assert_res = e
            raise AssertionError

        finally:
            iter_8_tdt.start_row_no += 1

if __name__ == '__main__':
    unittest.main()