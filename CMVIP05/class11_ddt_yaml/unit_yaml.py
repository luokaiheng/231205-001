'''
    基于Yaml来实现数据驱动的测试行为
'''
import unittest

from ddt import ddt, file_data

from class07_web_Keys.web_keys.keys import Keys


@ddt
class TestCase(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.key = Keys('Chrome')
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.key.quit()
    def setUp(self) -> None:
        self.key = Keys('Chrome')

    def tearDown(self) -> None:
        self.key.quit()

    # 实现登录操作流程:file_data中传入yaml的文件路径即可
    @file_data('./data/data_login.yaml')
    def test_01_login(self, common, info):
        self.key.open(common['url'])
        self.key.click(**common['login'])
        self.key.input(**info['accounts'])
        self.key.input(**info['password'])
        self.key.click(**common['button'])
        self.key.wait(common['time_'])
        self.assertEqual(first=info['assert_text']['expect'],
                         second=self.key.get_text(**info['assert_text']['reality']),
                         msg='断言失败')
        '''
        {
            'url': 'http://39.98.138.157/shopxo/index.php', 
            'login': {'name': 'link text', 'value': '登录'}, 
            'accounts': {'name': 'name', 'value': 'accounts', 'txt': 'xuzhu666'}, 
            'password': {'name': 'name', 'value': 'pwd', 'txt': '123456'}, 
            'button': {'name': 'xpath', 'value': '//button[text()="登录"]'}, 
            'time_': 3, 
            'assert_text': 
                {
                    'reality': {'name': 'link text', 'value': '退出'},
                    'expect': '退出'
                }
        }
        '''

    # # 实现商品搜索流程
    # def test_02_search(self):
    #     self.key.open('http://39.98.138.157/shopxo/index.php')
    #     self.key.input('name', 'wd', '手机')
    #     self.key.click('id', 'ai-topsearch')
    #     self.key.wait(3)


if __name__ == '__main__':
    unittest.main()
