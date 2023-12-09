# 导入webdriver包
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
wb = WebDriver(executable_path="chromedriver")

# driver.get('http://www.baidu.com')
wb.execute('get', {'url': 'http://www.baidu.com'})

# 元素定位与操作
# input_ = driver.find_element_by_name('wd')
el = wb.execute('findElement', {
    'using': By.XPATH,
    'value': '//input[@id="kw"]'})['value']
print(el)
# input_.send_keys('虚竹')
el._execute('sendKeysToElement', {
    'text': '虚竹',
    'value': ''
})
# button = driver.find_element_by_id('su')
el1 = wb.execute('findElement', {
    'using': By.XPATH,
    'value': '//input[@id="su"]'})['value']
# button.click()
el1._execute('clickElement')
