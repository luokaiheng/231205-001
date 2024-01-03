'''
    基于UnitTest实现关键字驱动的测试操作:
        实现登录
        断言：
            UnitTest中所有的断言函数都是self.assert*
            测试用例标注为失败：
                1. 断言失败则测试用例失败
                2. 用例内容运行时报错了，用例失败。
        测试用例中不要添加try except来处理异常
        基于不同的场景来定义选择对应的前后置方式：
            如果需要用例之间管理缓存信息，则用class级别
            如果需要独立各个用例，就是用case级别
        UnitTest支持在多用例的情况下单独运行指定测试用例，但是不推荐，因为可能会报错。
'''
import unittest

from class07_web_Keys.web_keys.keys import Keys


class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.key = Keys('Chrome')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.key.quit()

    # def setUp(self) -> None:
    #     self.key = Keys('Chrome')
    #
    # def tearDown(self) -> None:
    #     self.key.quit()

    # 实现登录操作流程
    def test_01_login(self):
        self.key.open('http://39.98.138.157/shopxo/index.php')
        self.key.click('link text', '登录')
        self.key.input('name', 'accounts', 'xuzhu666')
        self.key.input('name', 'pwd', '123456')
        self.key.click('xpath', '//button[text()="登录"]')
        self.key.wait(3)
        # status = self.key.assert_text('link text', '退出', '退出1')
        # self.assertTrue(status, msg='断言失败，{}不为True'.format(status))
        self.assertEqual(first='退出',
                         second=self.key.get_text('link text', '退出'),
                         msg='断言失败')

    # 实现商品搜索流程
    def test_02_search(self):
        # self.key.wait(10)
        self.key.open('http://39.98.138.157/shopxo/index.php')
        self.key.input('name', 'wd', '手机')
        self.key.click('id', 'ai-topsearch')
        self.key.wait(3)


if __name__ == '__main__':
    unittest.main()
