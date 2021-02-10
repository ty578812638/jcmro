#!/anaconda3/envs/FEALPy/bin 
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_1_计算加法.py
# @Author: TangYong
# @Time: 四月 05, 2020


import sys
import unittest
from fun import public
from cases.system import conf
from ddt import ddt,data,unpack


print('iter_8  test1')

@ddt
class CalculateAdd(unittest.TestCase):
    '''加法运算'''
    @data((5,2))
    @unpack
    def test_1_add(self,add1,add2):
        '''计算加法1'''

        case_no = 'Add0006'
        case_name = '计算加法1'
        test_result = ''



        act_res = add1 + add2

        public.log_record('计算加法:', sys._getframe().f_lineno, '计算加法')



        try:
            test_result = 'passed'
            self.assertEqual(4, act_res, '计算加法结果')


        except Exception as e:
            test_result = 'failed'

            raise AssertionError

        finally:

            conf.case_test_record_list.append(
                {'case_no': case_no, 'case_name': case_name, 'test_result': test_result, 'url_addr':'timeshare'})



    @data((5, 2))
    @unpack
    def test_2_add(self, add1, add2):

        # '''计算加法2'''

        case_no = 'Add0002'
        case_name = '计算加法7'
        test_result = ''


        act_res = add1 + add2

        public.log_record('计算加法:', sys._getframe().f_lineno, '计算加法')
        try:
            test_result = 'passed'
            self.assertEqual(4, act_res, '计算加法结果')

        except Exception as e:
            test_result = 'failed'

            raise AssertionError

        finally:

            conf.case_test_record_list.append(
                {'case_no': case_no, 'case_name': case_name, 'test_result': test_result, 'url_addr': 'timeshare'})


    @data((5, 2))
    @unpack
    def test_3_add(self, add1, add2):
        '''计算加法3'''

        case_no = 'Add0003'
        case_name = '计算加法8'
        test_result = ''


        act_res = add1 + add2

        public.log_record('计算加法:', sys._getframe().f_lineno, '计算加法')
        try:
            test_result = 'passed'
            self.assertEqual(4, act_res, '计算加法结果')

        except Exception as e:
            test_result = 'failed'

            raise AssertionError

        finally:

            conf.case_test_record_list.append(
                {'case_no': case_no, 'case_name': case_name, 'test_result': test_result, 'url_addr': 'timeshare'})


    @data((5, 2))
    @unpack
    def test_4_add(self, add1, add2):

        """  计算加法4  """


        case_no = 'Add0009'
        case_name = '计算加法4'
        test_result = ''


        act_res = add1 + add2

        public.log_record('计算加法:', sys._getframe().f_lineno, '计算加法')
        try:
            test_result = 'passed'
            self.assertEqual(5, act_res, '计算加法结果')

        except Exception as e:
            test_result = 'failed'

            raise AssertionError

        finally:

            conf.case_test_record_list.append(
                {'case_no': case_no, 'case_name': case_name, 'test_result': test_result, 'url_addr': 'timeshare'})



    @data((5, 2))
    @unpack
    def test_5_add(self, add1, add2):
        '''计算加法5'''
        case_no = 'Add00010'
        case_name = '计算加法5'
        test_result = ''


        act_res = add1 + add2

        public.log_record('计算加法:', sys._getframe().f_lineno, '计算加法')
        try:
            test_result = 'passed'
            self.assertEqual(7, act_res, '计算加法结果')

        except Exception as e:
            test_result = 'failed'

            raise AssertionError

        finally:

            conf.case_test_record_list.append(
                {'case_no': case_no, 'case_name': case_name, 'test_result': test_result, 'url_addr': 'timeshare'})


if __name__ == '__main__':
    unittest.main()