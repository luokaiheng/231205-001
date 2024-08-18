#!/usr/bin/env python3
# encoding: utf-8
'''
@author: Loeb{luokaiheng}
@file: unit_yaml.py
@time: 2024/8/11  11:41
@software: PyCharm
@desc:基于yaml来是想数据驱动的测试行为
在unitest中操作yaml文件作为数据驱动，需要调用file data的装饰器
'''
import unittest

from CMVIP05_TEST.KeyTool.keys import Keys

from ddt import ddt, file_data


@ddt
class UnitYaml(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.key = Keys('Chrome')
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.key.quit()

    def setUp(self):
        self.key = Keys('Chrome')

    def tearDown(self):
        self.key.quit()

    # 实现登录操作流程：file data中传入yaml文件路径即可
    @file_data('./data/data_login.yaml')
    def test_01_login(self, **kwargs):
        print(kwargs)
        # self.key.open(kwargs['url'])
        # self.key.click(**kwargs['login'])
        # self.key.input(**kwargs['accounts'])
        # self.key.input(**kwargs['password'])
        # self.key.click(**kwargs['button'])
        # self.key.wait(kwargs['time_'])
        # # status = self.key.assert_text('link text', '退出', '退出1')
        # # self.assertTrue(status, msg='断言失败，{}不为True'.format(status))
        # self.assertEqual(first=kwargs['assert_text']['expect'],
        #                  second=self.key.get_text(**kwargs['assert_text']['reality']),
        #                  msg='断言失败')

        '''
            {
                'url': 'http://shop-xo.hctestedu.com', 
                'login': {'name': 'link text', 'value': '登录'}, 
                'accounts': {'name': 'name', 'value': 'accounts', 'txt': 'xuzhu666'}, 
                'password': {'name': 'name', 'value': 'pwd', 'txt': '123456'}, 
                'button': {'name': 'xpath', 'value': '//button[text()="登录"]'}, 
                'time_': 3, 
                'assert_text': {
                    'reality': {
                        'name': 'link text', 
                        'value': '退出'
                        }, 
                    'expect': '退出'
                    }
                }

        '''

    # 实现商品搜索流程
    # def test_02_search(self):
    #     self.key.open('http://shop-xo.hctestedu.com')
    #     self.key.input('name', 'wd', '手机')
    #     self.key.click('id', 'ai-topsearch')
    #     self.key.wait(3)


if __name__ == '__main__':
    unittest.main()
