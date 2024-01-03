'''
    这是UnitTest的应用：
        1. 通过unittest.TestCase的继承，让UnitTest生效
        2. 测试用例的定义都是基于函数的形态，并且函数命名必须以test开头。推荐以test_开头会更加规范
        3. 测试用例的运行顺序是基于ascll码来执行的，基本顺序是0-9、A-Z，a-z
        4. 在UnitTest中是可以支持普通函数的定义
        5. 前置后置的调用:一般只用于做初始化与资源释放。不接受参数的传递
            因为前置和后置只能够编写一次。写多了就会被新写的覆盖。
            如果每一个测试用例的前置都不一样，那就表明你setup是运行不了的。
            基于cls对象生成的class级别前后置：需要添加@classmethod进行标注
        6. 一个py文件是可以有多套UnitTest对象存在的。
        7. 除非必要，一般一个class管理一套测试用例即可。一个py文件对应一套class


'''
import unittest


# 调用UnitTest
class TestDemo(unittest.TestCase):
    # 定义Class前置
    @classmethod
    def setUpClass(cls) -> None:
        print('这是class setup函数')

    # 定义Class后置
    @classmethod
    def tearDownClass(cls) -> None:
        print('这是class teardown函数')

    # 定义前置:测试用例的前置，每一个用例执行前都会执行该前置
    def setUp(self):
        print('这是setup用例前置函数')

    # 定义后置：测试用例的后置，每一个测试用例执行完毕后都会执行该后置
    def tearDown(self):
        print('这是tearDown用例后置函数')

    # 测试用例1
    def test_02_login(self):
        print('这是test_login测试用例')

    # 测试用例2
    def test_01(self):
        print('这是test_1测试用例')

    # 测试用例3
    def test_03_Login(self):
        print('这是test_Login测试用例')

    # 普通函数
    def temp(self):
        print('这是temp函数')

    # 测试用例4
    def test_04(self):
        print('这是test_04')
        self.temp()





class TestDemo1(unittest.TestCase):
    def test_01(self):
        print('这是testdemo1中的test01函数')


# 执行UnitTest
if __name__ == '__main__':
    unittest.main()
