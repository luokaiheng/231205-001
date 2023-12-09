'''
    Selenium4.0新增的关于浏览器与标签页的管理
    new_window()函数只支持4.0及以上版本
'''
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
handles = driver.window_handles
print(handles)
sleep(2)
# 新增一个浏览器或者句柄页并且直接进行切换：通过参数来定义（tab,window）
driver.switch_to.new_window('tab')  # tab表示标签页,window表示浏览器
handles = driver.window_handles
print(handles)

driver.get('http://www.baidu.com')
driver.get('http://www.jd.com')
