#!/usr/bin/env python3
# encoding: utf-8
'''
@author: Loeb{luokaiheng}
@file: unittest_demo.py
@time: 2024/4/11  21:19
@software: PyCharm
@desc:
'''
import unittest


class TestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('====读取账号密码')

    @classmethod
    def tearDownClass(cls):
        print('====封锁账号密码')

    def setUp(self):
        print('----准备操作')

    def tearDown(self):
        print('----查看页面')

    # 作为普通函数，是可以被写入测试用例里面的
    def func_01(self):
        print('把一堆我想要的东西，加入购物车')

    def test_01_Login(self):
        print('点击登录按钮')

    def test_02_Buy(self):
        # 类内自己调用函数，使用 self.方法名 来调用
        self.func_01()
        print('点击购买按钮')

    def test_03_cancel(self):
        print('点击取消按钮')

    def test_04_exit(self):
        print('点击退出按钮')


if __name__ == '__main__':
    unittest.main
