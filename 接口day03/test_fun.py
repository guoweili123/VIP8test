from 接口day03.myfun import add
import unittest

class TestMyFun(unittest.TestCase):
    # testcase 积累方法，所有case执行之前自动执行
    @classmethod
    def setUpClass(cls):
        print('这里是所有的测试用例前的准备工作')
    # testcase基类方法
    @classmethod
    def tearDownClass(cls):
        print('这里是所有测试用例后的清理工作')

    def setUp(self):
        print('这里是一个测试用例前的准备工作')

    def tearDown(self):
        print('这里是一个测试用例后的清理工作')

    def test_add(self):
        print('这里是运行的test开头的用例')
        self.assertEqual(3,add(1,2))

if __name__ == '__main__':
    unittest.main()