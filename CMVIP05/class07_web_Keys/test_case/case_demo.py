'''
    测试代码的内容编写与类的管理。
    调用关键字驱动类实现自动化效果
    一个py文件，管理一个测试用例。
'''
from class07_web_Keys.web_keys.keys import Keys

# 百度搜索业务流程
key = Keys('Firefox')
key.open('http://www.baidu.com')
key.input('id', 'kw', '虚竹')
key.click('id', 'su')
