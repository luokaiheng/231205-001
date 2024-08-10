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


