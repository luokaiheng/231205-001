#!/usr/bin/env python3
# encoding: utf-8
'''
@author: Loeb{luokaiheng}
@file: test_yaml.py
@time: 2024/6/8  15:59
@software: PyCharm
@desc:读取yaml文件的内容，open读取任何文件都可以，但是yaml格式，在open之后还需要额外的操作
1.data 实现数据分离，data 的实现：
    a.声明data 装饰器，生成对应的测试数据，每一组数据都基于","进行区分
    b.基于data 分离了多少组数据，则该条用例执行多少次
    c.基于测试函数中定义的形参，将data分离的每一组数据依次传入
2.unpack 解包data中的数据包
    a.基于data生成的数据组，进行二次解包
    b.解包的规则和data是一样的
    c.基于data和unpack装饰器解包的数据组，个数上要与形参完全一致
'''
import unittest

from ddt import ddt, data, unpack


def read_file():


# ddt后面不要接括号
@ddt
class Demo(unittest.TestCase):
    def test_01(self):
        li = ['凯恒', '小凯', '恒儿', '小罗']
        for n in li:
            print(n + '，你好，欢迎来到这个世界')
        # print('这是用例001')

    # 声明调用data装饰器：将多组数据存放在data装饰器中，便于用例的多次调用
    '''
        1.data 实现数据分离，data 的实现：
            a.声明data 装饰器，生成对应的测试数据，每一组数据都基于","进行区分
            b.基于data 分离了多少组数据，则该条用例执行多少次
            c.基于测试函数中定义的形参，将data分离的每一组数据依次传入
    '''

    @data('凯恒', '小凯', '恒儿', '小罗')
    def test_02(self, name):
        print(name + '，你好，欢迎来到这个中国')
        # print('这是用例002')

    @data('string', ['list00', 'list01'], {'dict': 'value'})
    def test_03(self, name):
        if type(name) is list:
            print(name, end="")
            print('，列表可以作为参数传进来')
        elif type(name) is dict:
            print(name, end="")
            print('，字典也ok')
        else:
            print(name + '，字符串也可')

    @data(['list00', 'list01'], ['list02', 'list03'], ['list04', 'list05'], ['list06', 'list07', 'list08'])
    @unpack
    def test_04(self, name, type_, type_001='None'):
        print('如果当测试用例中，需要传入多组形参数据，可以通过声明unpack装饰器来对数据组进行拆包')
        print(name + ' ' + type_ + ' ' + type_001)





if __name__ == '__main__':
    unittest.main()
