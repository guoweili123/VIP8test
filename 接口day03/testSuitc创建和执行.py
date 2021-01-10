'''
功能描述：
编写人：
编写日期：

步骤分析：
    1-
    2-
    3-
'''
import  unittest
from myfun import *

from 接口day03.myfun import multi, add


class myTest(unittest.TestCase):
    def setUp(self):
        print('执行setup方法')
    def tearDown(self):
        print('执行tearDown方法')
    def test_add(self):
        print('执行test_add')
        self.assertEqual(add(1,2),3)
    def test_mul(self):
        print('执行test_mul')
        self.assertEqual(multi(1,2),2)

if __name__ == '__main__':
    suite=unittest.TestSuite()
    # suite.addTest((myTest('test_add'),myTest('test_mul')))
    suite.addTest((myTest('test_add'))
    print(suite)


    runner=unittest.TextTestRuner()
    runner.run(suite)
