#!/usr/bin/env python3
# encoding: utf-8
'''
@author: Loeb{luokaiheng}
@file: unittest_shop.py
@time: 2024/4/11  23:12
@software: PyCharm
@desc:
'''
import unittest
from CMVIP05_TEST.KeyTool.keys import Keys


class TestCase_01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 在执行用例前，做初始化准备
        # 这里是类对象,所以是cls
        cls.key = Keys('Chrome')

    @classmethod
    def tearDownClass(cls):
        # 执行用例后，做资源回收
        cls.key.quit()

    def test_00_register(self):
        self.key.open("http://shop-xo.hctestedu.com")
        self.key.click('link text', '注册')
        self.key.input('name', 'accounts', 'xuzhu66666')
        self.key.input('name', 'pwd', '123456')
        self.key.click('xpath', '//button[text()="注册"]')
        self.key.wait(3)
        # self.key.assert_text('link text', '退出','退出')
        self.assertEqual(first='退出',
                         second=self.key.get_text('link text', '退出'),
                         msg='断言失败')
        self.key.click('link text', '退出')

    def test_01_login(self):
        # 实现登录操作，访问地址，定位控件，输入内容，点击登录，最后做断言
        self.key.open("http://shop-xo.hctestedu.com")
        self.key.click('link text', '登录')
        self.key.input('name', 'accounts', 'xuzhu66666')
        self.key.input('name', 'pwd', '123456')
        self.key.click('xpath', '//button[text()="登录"]')
        self.key.wait(3)
        # # 写法1：因为assert_text中把错误异常都处理掉了，所以需要一个status去接收这个用例的状态，在根据status的状态去对应做操作或判断
        # status = self.key.assert_text('link text', '退出', '退出1')
        # self.assertTrue(status, msg='断言失败，{}不为True'.format(status))
        # 写法2:unittest中自带的断言方式,直接进行断言,通过判断两个值是否相等,来进行断言,失败就报错
        self.assertEqual(first='退出',
                         second=self.key.get_text('link text', '退出'),
                         msg='断言失败')

    def test_02_seach(self):
        # 实现查询效果，定位控件，输入内容，点击搜索
        # self.key.wait(10)
        self.key.open('http://shop-xo.hctestedu.com')
        self.key.input('name', 'wd', '手机')
        self.key.click('id', 'ai-topsearch')
        self.key.wait(3)


if __name__ == '__main__':
    unittest.main()
