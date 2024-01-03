'''
    POM下的测试用例
'''
from selenium import webdriver

from class12_pom.page_object.index_page import IndexPage
from class12_pom.page_object.login_page import LoginPage

driver = webdriver.Chrome()
# driver1 = webdriver.Chrome()
lp = LoginPage(driver)
lp.login('xuzhu666', '123456')
ip = IndexPage(driver)
ip.search('手机')
