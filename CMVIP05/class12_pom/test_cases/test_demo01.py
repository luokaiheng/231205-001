'''
    第一组测试用例
'''
import unittest

from selenium import webdriver
from ddt import ddt, data, file_data, unpack
from class06_options_web.chrome_options import ChromeOptions
from class12_pom.page_object.index_page import IndexPage
from class12_pom.page_object.login_page import LoginPage


@ddt
class TestDemo01(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(options=ChromeOptions().options())
        cls.lp = LoginPage(cls.driver)
        cls.ip = IndexPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @data(['xuzhu666', '123456', '退出'])
    @unpack
    def test_01_login(self, user, pwd, expect):
        self.lp.login(user, pwd, expect)

    @file_data('../data/info.yaml')
    def test_02_search(self, txt):
        self.ip.search(txt)


if __name__ == '__main__':
    unittest.main()
