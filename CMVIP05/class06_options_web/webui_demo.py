'''
    web实操：实现一个从登陆到商品购买的整个流程
'''
from time import sleep

from selenium import webdriver

from chrome_options import ChromeOptions

print('这是启动的自动化测试执行')
driver = webdriver.Chrome(options=ChromeOptions().options())
driver.implicitly_wait(10)
# 访问URL
driver.get('http://39.98.138.157/shopxo/index.php')

# 实现登录
driver.find_element('link text', '登录').click()
driver.find_element('name', 'accounts').send_keys('xuzhu666')
driver.find_element('name', 'pwd').send_keys('123456')
driver.find_element('xpath', '//button[text()="登录"]').click()

# 手机搜索
driver.find_element('id', 'search-input').send_keys('手机')
driver.find_element('id', 'ai-topsearch').click()
driver.find_element('xpath', '//img[contains(@alt,"苹果")]').click()

# 句柄的切换
handles = driver.window_handles
driver.close()
driver.switch_to.window(handles[1])

# 商品属性添加
driver.find_element('xpath', '//*[@data-value="套餐一"]').click()
sleep(1)
driver.find_element('xpath', '//*[@data-value="银色"]').click()
sleep(1)
driver.find_element('xpath', '//*[@data-value="64G"]').click()
el = driver.find_element('id', 'text_box')
el.clear()
el.send_keys('20')
driver.find_element('xpath', '//button[@title="加入购物车"]').click()


# 购物车页选择商品进入结算
driver.find_element('xpath', '//span[text()="购物车"]').click()
driver.find_element('xpath', '//*[@class="am-ucheck-icons"]').click()
driver.find_element('xpath', '//button[text()="结算"]').click()

# 结算
driver.find_element('xpath', '//*[@data-value="1"]').click()
driver.find_element('xpath', '//button[text()="提交订单"]').click()
# driver.find_elements('xpath', '//button[text()="提交订单"]')[0].click()

# 断言校验
text = driver.find_element('xpath', '//span[text()="支付成功"]').text
assert '支付成功' == text, '支付流程失败，实际结果{}'.format(text)
