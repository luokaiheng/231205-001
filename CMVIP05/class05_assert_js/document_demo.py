'''
    Document对象是前端中非常非常核心的内容。UI自动化就是操作UI界面，也就是所谓的前端对象。
    在特殊的对象处理中，很可能在定位，操作上会因为selenium的限制，导致很难处理。就可以通过document对象
    来进行操作。
    用途：
        1. 定位元素
        2. 通过document修改元素的属性，或者添加删除属性
            innerHTML 设置text
            setAttribute 设置元素属性、添加元素属性
            removeAttribute 移除指定属性
    在Selenium中提供有JS执行器的函数，专门用于执行JS脚本
        当js执行需要获取结果以便后续调用，一定要在js中加上return
'''
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.set_window_size(200, 400)
driver.get('http://www.baidu.com')
sleep(3)
# 滚动条
js = 'window.scrollTo(200,500)'

# 定位元素：加了s的查找元素，返回是list结果
js1 = 'return document.getElementsByName("wd")'

# 设置并获取元素文本
js2 = 'return document.getElementById("kw").innerHTML="虚竹123123123"'

# Selenium+Document实现元素操作
el = driver.find_element('link text', '登录')
# return document.getElementBy*().innerHTML
# arguments[0] 可以直接理解为是占位符
js3 = 'return arguments[0].innerHTML'

# 元素聚焦在页面
js4 = 'arguments[0].scrollIntoView()'
# js语句都是通过js执行器来进行注入
driver.execute_script(js4, el)
