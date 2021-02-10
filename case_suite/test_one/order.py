
import  unittest
from fun import public
from settings import config
from  settings.config import *
import HTMLTestRunner
from  selenium.webdriver.common.action_chains import ActionChains


# class OrderManage(unittest.TestCase):
#     def verify_login(self):
#         '''登录验证 HTMLTestRunner'''
#         public.LoginLogout().login()
#         self.driver =config.driver
#         title = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/span[2]/a').text
#         if self.assertEqual(title,'个人中心'): pass
#         else:
#             self.driver.get_screenshot_as_file(public.screenshot('verify_login.png'))
#             public.log_record('verify_login', '与预期结果不符')
#         public.LoginLogout().logout()
#
#     def po_search(self):
#         '''po 查询 HTMLTestRunner'''
#         public.LoginLogout().login()
#
#         self.driver = config.driver
#         #点击PO订单/PO订单/输入PO编号的查询条件/点击查询
#         po_manage_btn = self.driver.find_element_by_class_name('ivu-menu-submenu-title')
#         ActionChains(driver).move_to_element(po_manage_btn).perform()
#         self.driver.find_element_by_partial_link_text('PO管理').click()
#         print('2')
#         self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div[2]/div[1]/input').send_keys('P5057')
#         print('3')
#         self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/section/div[1]/span[2]/button').click()
#         print('4')
#
#         #获取列表中的查询数据
#         search_value = public.get_webtable_celldata('/html/body/div[1]/div/div[2]/div/div/section/div[2]/div/table',1,6)
#         print(search_value)
#
#         # self.assertEqual(search_value,'全流程价格验证','查询成功')
#         # public.log_record('po_search','查询成功')
#         # public.LoginLogout().logout()
#
#
#     def add1(self):
#         if self.assertEqual('2','c'):
#             pass
#         else:
#             return public.log_record('verify_login', '不相等')
#
#     def add2(self):
#
#         if self.assertEqual('2','3'):
#             pass
#         else:
#             return public.log_record('verify_login', '不相等')
#
#     def add3(self):
#
#         if self.assertEqual('2', '8'):
#             pass
#         else:
#             return public.log_record('verify_login', '不相等')


class TestAdd(unittest.TestCase):

    def test_add1(self):
        s = 3 + 2
        self.assertEqual(5,s)

    def test_sdd2(self):
        s = 3 + 3
        self.assertEqual(6, s)
