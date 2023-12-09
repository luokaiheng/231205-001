'''
    这是selenium的第一个demo：“helloword”
'''
from time import sleep

from selenium import webdriver

# 创建webdriver对象
driver = webdriver.Chrome()
# 访问指定url
driver.get('http://39.98.138.157/shopxo/index.php')
# 找到搜索输入框
el = driver.find_element("name", 'kw')
# 对元素进行输入文本的操作
el.send_keys('F12开启开发者工具')
# 找到搜索按钮，并点击一次
driver.find_element_by_id('ai-topsearch').click()
# 等待
sleep(5)
# 关闭浏览器并释放后台进程
driver.quit()



