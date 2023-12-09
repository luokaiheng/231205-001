'''
    断言机制：断言就是要让代码报错
    断言是断言的表达式，表达式的内容可以是多样性的。
        1. assert
        2. 显式等待
        3. if...else
'''
from selenium import webdriver

# 登录流程
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html')
driver.find_element('name', 'accounts').send_keys('xuzhu666')
driver.find_element('name', 'pwd').send_keys('123456')
driver.find_element('xpath', '//button[text()="登录"]').click()

# 断言：assert a = b
# text = '退出1'
# text1 = driver.find_element('link text', '退出').text
# assert text == text1, '{0}不等于{1}'.format(text, text1)
# try:
#     assert 1 == 2, '断言失败'
# except Exception as e:
#     print(e)
# print('这里是断言后的代码')
# 显式等待
# WebDriverWait(driver, 5, 0.5).until(lambda el: driver.find_element('link text', '退出1'),
#                                     message='流程运行失败，登录失败')
# if...else
# text = '退出1'
# text1 = driver.find_element('link text', '退出').text
# if text == text1:
#     print(True)
# else:
#     print(False)

# assert el is True, '断言失败'
