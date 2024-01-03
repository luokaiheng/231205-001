'''
    基于ddt实现UnitTest测试用例与数据分离的形态：
        1. data实现数据分离
        2. unpack 解包data中的数据包
'''
import unittest
from ddt import ddt, data, unpack


# txt文件读取
def read_file():
    li = []
    file = open('./data/demo.txt', 'r', encoding='utf-8')
    for line in file.readlines():
        li.append(line)
    return li


# 表示现在开始，这个测试用例类要调用ddt模块实现数据驱动
@ddt
class Demo(unittest.TestCase):
    # def test_01(self):
    #     li = ['xuzhu', 'fortune', '王飞']
    #     for s in li:
    #         print(s)

    # 声明调用data装饰器:将多组数据存放在data装饰器中，便于用例的多次调用
    '''
        data的实现：
            1. 声明data装饰器，生成对应的测试数据。每一组数据都基于,进行区分
                ‘xuzhu’    ‘fortune’    '王飞'
            2. 基于data分离了多少组数据，则该条用例执行多少次
            3. 基于测试函数中定义的形参，将data分离的每一组数据依次传入
        unpack的使用：
            1. 基于data生成的数据组，进行二次解包
            2. 解包的规则与data本身是一样的。
        基于data和UNpack装饰器解包的数据组，个数上要与形参完全一致
    '''

    # @data('xuzhu', 'fortune', '王飞')
    # @data(['xuzhu'])
    # @unpack
    # def test_02(self, name, type_=None):
    #     print(name)
    #     print('*' * 20)
    #     print(type_)

    # 在数据库数据驱动时，可以通过调用函数来获取数据库中的数据，基于data进行参数化。
    # @data(*read_file())
    # def test_03(self, name):
    #     print(name)
    #     print('*' * 20)
        # print(name1)
    # def test_04(self):
    #     print('xuzhu贼帅')


if __name__ == '__main__':
    unittest.main()
