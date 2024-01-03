'''
    unittest中的skip装饰器使用：
        skip:无条件跳过   *有点用
        杂技套装：
            skipIf:有条件跳过，当条件为真时跳过
            skipUnless:与if相反，当条件为假时跳过
            expectedFailure:用例报错则忽略，用例成功则报错

'''
import unittest


class Demo(unittest.TestCase):

    def setUp(self) -> None:
        print('setup')

    # @unittest.skip('无条件跳过该条用例')
    def test_01(self):
        print('test01')

    # @unittest.skipIf(1 == 1, '这是reason')
    def test_02(self):
        print('test02')

    # @unittest.skipUnless(1 != 1, '这是reason111')
    def test_03(self):
        print('test03')

    # @unittest.expectedFailure
    def test_04(self):
        print('test04')
        self.assertEqual(1, 2, msg='断言失败')


class Demo01(unittest.TestCase):
    def test_01(self):
        print('asdasda')


# if __name__ == '__main__':
#     unittest.main()
