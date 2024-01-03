'''
    测试代码的内容编写与类的管理。
    调用关键字驱动类实现自动化效果
    一个py文件，管理一个测试用例。
'''
from MyDemo.web_keys.keys import Keys

# 百度搜索业务流程
key = Keys('Chrome')
key.open('http://www.baidu.com')
key.input('id', 'kw', '虚竹')

key.click('id', 'su')
# 相对定位器定位搜索按钮
# el = key.locator_with('css selector', '#su', 'id', 'kw', 'right')
# print(el)
# el.click()
print('点击成功')
key.wait(5)
key.quit()
