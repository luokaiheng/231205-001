'''
    通过selenium底层来实现同样的浏览器操作效果
'''
from selenium.webdriver.chrome.webdriver import WebDriver

# driver = webdriver.Chrome()
driver = WebDriver(executable_path="chromedriver")
# driver.get('http://39.98.138.157/shopxo/index.php')
driver.execute("get", {'url': 'http://39.98.138.157/shopxo/index.php'})
# el = driver.find_element("name", 'kw')
# # 对元素进行输入文本的操作
# el.send_keys('F12开启开发者工具')
a = driver.execute("findElement", {
    'using': "xpath",
    'value': '//input[@id="search-input"]'})
print(a)
el = driver.execute("findElement", {
    'using': "xpath",
    'value': '//input[@id="search-input"]'})['value']
# el._execute("sendKeysToElement", {'text': "selenium逻辑代码", 'value': ""})
# # driver.find_element_by_id('ai-topsearch').click()
# el1 = driver.execute("findElement", {
#     'using': "xpath",
#     'value': '//input[@id="ai-topsearch"]'})['value']
# el1._execute("clickElement")
