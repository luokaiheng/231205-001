#!/usr/bin/env python3
# encoding: utf-8
'''
@author: Loeb{luokaiheng}
@file: test_DDT.py
@time: 2024/6/8  14:49
@software: PyCharm
@desc:基于ddt实现Unittest测试用例与数据分离的形态
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

li = ['li01', 'li02', 'li03']


@ddt()
class Demo(unittest.TestCase):
    @data('li01', 'li02', 'li03')
    def test_01(self, name):
        print(name)

    @data(['li01', '这是一个list'], {'name': 'li02'}, 'li03')
    def test_02(self, name):
        print(name)

    @data(['申远', '陈树波'], ['林钊颖', '李华丽'], ['王华其', '莫朝辉'])
    @unpack
    def test_03(self, name, type_):
        print(name)
        print('*' * 20)
        print(type_)

    # 传参报错
    @data(['申远', '陈树波', '罗凯恒'], ['林钊颖', '李华丽'], ['王华其', '莫朝辉'])
    @unpack
    def test_04(self, name, type_, type_0):
        print(name)
        print('*' * 20)
        print(type_)
        print('*' * 20)
        print(type_0)


if __name__ == '__main__':
    unittest.main()
