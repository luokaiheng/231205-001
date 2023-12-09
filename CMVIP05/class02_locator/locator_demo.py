'''
    元素定位示例
'''
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

# id
# driver.find_element_by_id('kw').send_keys('虚竹')
# name
# driver.find_element('name', 'wd').send_keys('name')
# link text
# driver.find_element('link text', '新闻').click()
# partial link text：关键词很重要
# driver.find_element('partial link text', '使用百度').click()
# tag name
# li = driver.find_elements('tag name', 'input')
# for i in li:
#     print(i)
# el = driver.find_element('tag name', 'input')
# print('*' * 20)
# print(el)
# class name：非常不推荐，属性值不太友好
# driver.find_element('class name', 's_ipt').send_keys('class')
# css selector
# driver.find_element('css selector', '#kw').send_keys('css selector')
# xpath
# driver.find_element('xpath', '//input[@id="kw"]').send_keys('xpath')
