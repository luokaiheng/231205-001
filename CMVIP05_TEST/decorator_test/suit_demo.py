#!/usr/bin/env python3
# encoding: utf-8
'''
@author: Loeb{luokaiheng}
@file: suit_demo.py
@time: 2024/4/14  14:15
@software: PyCharm
@desc:
    测试用例的真正手段，测试套件的应用：
       测试套件：
            相当于一个List的存在，物理形态其实就是文件夹。
            UnitTest.TestSuite中可以自定义添加测试用例执行
            套件运行是依托于运行器runner来运行的
'''
import unittest

from CMVIP05_TEST.decorator_test.test_01 import Demo

# 创建套件
suite = unittest.TestSuite()
# 1.添加单个测试用例,基于测试用例的名称
# suite.addTest(Demo('test_04'))
# suite.addTest(Demo('test_03'))
# suite.addTest(Demo('test_02'))
# 2.添加多个测试用例,通过List实现
# case = [Demo('test_03'), Demo('test_02')]
# suite.addTests(case)
# 3.可以通过添加一整个class进入套件
# suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Demo))
# 4.通过文件名称添加进入套件
# suite.addTest(unittest.TestLoader().loadTestsFromName("test_01.Demo"))
# 5.批量添加,在持续集成中和批量管理中特别好用
path = "./"
discover = unittest.defaultTestLoader.discover(start_dir=path,pattern='test*.py')

# 运行套件内的测试用例,默认运行器,verbosity是日志等级:0-1
runner = unittest.TextTestRunner(verbosity=2)
runner.run(discover)
