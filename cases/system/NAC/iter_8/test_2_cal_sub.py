#!/anaconda3/envs/FEALPy/bin 
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_2_计算减法.py
# @Author: TangYong
# @Time: 四月 05, 2020

import unittest
from fun import public
from ddt import ddt,data,unpack
from cases.system import conf

print('iter_8  test2')

@ddt
class CalculateAdd(unittest.TestCase):
    '''计算减法'''
    @data((10,1))
    @unpack
    def test_1_sub(self,add1,add2):

        act_res = add1 - add2
        try:
            self.assertEqual(6, act_res, '计算加法结果')


        except Exception as e:
            assert_res = e

            raise AssertionError

        finally:
            conf.case_test_record_list.append(
                {'case_no': '0004', 'case_name': '测试分时', 'test_result': 'passed', 'url_addr': 'timeshare'})

    @data((10, 2))
    @unpack
    def test_2_sub(self, add1, add2):

        act_res = add1 - add2
        try:
            self.assertEqual(3, act_res, '计算加法结果')


        except Exception as e:
            assert_res = e

            raise AssertionError

        finally:
            conf.case_test_record_list.append(
                {'case_no': 'p0006', 'case_name': '测试分时', 'test_result': 'passed', 'url_addr': 'timeshare'})

    @data((10, 3))
    @unpack
    def test_3_sub(self, add1, add2):

        act_res = add1 - add2
        try:
            self.assertEqual(2, act_res, '计算加法结果')

        except Exception as e:
            assert_res = e

            raise AssertionError

        finally:
            conf.case_test_record_list.append(
                {'case_no': 't0007', 'case_name': '测试分时', 'test_result': 'passed', 'url_addr': 'timeshare'})

    @data((10, 5))
    @unpack
    def test_4_sub(self, add1, add2):

        act_res = add1 - add2
        try:
            self.assertEqual(3, act_res, '计算加法结果')


        except Exception as e:
            assert_res = e

            raise AssertionError

        finally:
            conf.case_test_record_list.append(
                {'case_no': 't0008', 'case_name': '测试分时', 'test_result': 'passed', 'url_addr': 'timeshare'})


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
            conf.case_test_record_list.append(
                {'case_no': 't0009', 'case_name': '测试分时', 'test_result': 'passed', 'url_addr': 'timeshare'})

if __name__ == '__main__':
    unittest.main()