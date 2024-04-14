#!/usr/bin/env python3
# encoding: utf-8
'''
@author: Loeb{luokaiheng}
@file: test_01.py
@time: 2024/4/14  13:53
@software: PyCharm
@desc:
    skip装饰器：@unittest.skip('无条件跳过该测试用例')
    skipif装饰器：@unittest.skipIf(1 == 1, reason='该条件为真则执行，为假不执行')
    skipUnless装饰器：@unittest.skipUnless(1 != 1, reason='该条件为假则执行，为真不执行')
    expectedFailure装饰器：@unittest.expectedFailure，报错即忽略
'''

import unittest


class Demo(unittest.TestCase):
    # @unittest.skip('无条件跳过该测试用例')
    def test_01(self):
        print('test_01')

    # @unittest.skipIf(1 == 1, reason='该条件为真则执行，为假不执行')
    def test_02(self):
        print('test_02')

    # @unittest.skipUnless(1 != 1, reason='该条件为假则执行，为真不执行')
    def test_03(self):
        print('test_03')

    # @unittest.expectedFailure
    def test_04(self):
        print('test_04')


if __name__ == '__main__':
    unittest.main()