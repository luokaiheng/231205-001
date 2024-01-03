'''
    selenium 4.0 相对定位器
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')
# 定位输入框
el = driver.find_element('xpath', '//input[@id="kw"]')
# el.send_keys('虚竹')
# 右侧
# search = driver.find_element(locate_with(By.TAG_NAME, 'input').to_right_of(el))
# search.click()
# 左侧
# search = driver.find_element(locate_with(By.TAG_NAME, 'input').to_left_of(el))
# search.click()
# 上方
# img = driver.find_element(locate_with(By.TAG_NAME, 'img').above(el))
# print(img)
# 下方
# div = driver.find_element(locate_with(By.TAG_NAME, 'div').below(el))
# print(div)
# 靠近
span = driver.find_element(locate_with(By.TAG_NAME, 'span').near(el))
print(span.get_attribute('class'))
