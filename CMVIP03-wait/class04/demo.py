# 强制等待
from time import sleep
from selenium import webdriver
# 显示等待
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
'''
    隐式等待：偷偷摸摸的等待，是由WebDriver提供的一种等待模式，是以类似于全局变量的形式存在，对当下
        整个driver的生命周期都有效果，说白了就是对driver的一个等待设置
        当元素未找到时，达到最大等待时间后，程序继续运行
        好处：只需要设置一次，全局皆可生效
        缺陷：比较浪费资源，没有办法对精准度的元素进行定位，会影响到实际的运行效率
'''
# 在整个driver周期中，默认最大等待10秒时间
# driver.implicitly_wait(10)
driver.get('http://www.baidu.com')
driver.find_element(by='id',value='kw').send_keys('罗凯恒')
driver.find_element(by='id',value='su').click()
# driver.find_element_by_id('kw').send_keys('虚竹')
# driver.find_element_by_id('su').click()
'''
    强制等待：无所谓任何的情况，只要运行到强制等待这一行，就一定要等待指定的时间
    实现的形式是通过：time.sleep(秒)
        好处：简单上手，直接粗暴，一般都是在新手阶段和学习阶段以及特定的场景下来使用，平时不推荐使用
        劣势：因为太粗暴了，所以对于实际的执行会带来很费时间的影响
            经常写等待，代码中有非常多的sleep，显得冗余度会非常高
'''
sleep(5)
'''
    显式等待：是唯一的一种专门针对特定的元素（条件）而设置的等待，基本上都是应用在对指定元素来执行的
    until函数，用于判断，当条件为真的时候，返回结果。等待为真时，返回被等待的元素对象，为假时抛出超时异常
    untl_not函数，与until函数相反
'''
# element = WebDriverWait(driver, 10, 0.5).until(
#     lambda el: driver.find_element_by_xpath('//*[@id="1"]/h3/a1'), message='查找元素失败')
element = WebDriverWait(driver, 5, 0.5).until_not(
    lambda el: driver.find_element(by='xpath',value='//*[@id="1"]/h3/a1'), message='查找元素失败')
# driver.find_element_by_xpath('//*[@id="1"]/h3/a').click() .find_element_by_xpath('//*[@id="1"]/h3/a1'), message='查找元素失败')
print(element)
# driver.quit()
