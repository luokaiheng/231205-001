# 导包Selenium
from selenium import webdriver

# 创建webdriver，生成浏览器对象
driver = webdriver.Chrome()
# 访问URL
driver.get('http://www.baidu.com')

# 输入内容：找到页面元素，对其进行输入文本的操作
input_ = driver.find_element_by_name('wd')
input_.send_keys('虚竹')

# 点击一个元素：找到页面元素，对其进行点击操作
button = driver.find_element_by_id('su')
button.click()
