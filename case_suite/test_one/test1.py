# import  unittest
# import HTMLTestRunner
# dir_rep = open('D:\\result.html','wb')
# class TestOne(unittest.TestCase):
#
#     def test_one(self):
#         ''' test_one'''
#         print('test_one')
#
#
#
#
#
#
#
# if __name__ == '__main__':
#
#     test = TestOne()
#     suite = unittest.TestSuite()
#     # suite.addTest(test.test_one())
#     #runner = unittest.TextTestRunner()
#     suite.addTest(TestOne('test_one'))
#
#     runner = HTMLTestRunner.HTMLTestRunner(stream=dir_rep,title='标题',description='详情')
#
#     res = runner.run(suite)
#     print(res.success_count,res.testsRun)
#
#     dir_rep.close()