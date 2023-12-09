'''
    三类等待:
        1. 强制等待：
            就是time库下的sleep()
            不考虑代码整体的逻辑性和连贯性，运行到sleep这一行的时候，电脑就无条件执行等待的操作。
            等待时间由sleep的参数决定，等待结束后，继续运行后续的代码。
            sleep参数是以秒为单位的。
            优点：容易上手。在有需要的时候，直接调用即可。
            缺点：很蠢。造成大量的代码冗余，造成大量时间的浪费
            在日常测试中，一般情况下不会使用sleep，只有在特定场景下，或者临时性的调试下会使用sleep
            强制等待一定是time模块下的sleep，记住，是time模块
        2. 隐式等待：
            本质意义上而言是driver对象的一个设置项。
            只需要设置一次即可生效，在整个driver生命周期中都有效
            implicitly_wait()参数是以秒为单位
            在页面加载完成之后，调用后续的代码，如果说没有找到对应的元素，进入隐式等待的时间周期。
            在时间周期内会一直等待该元素显示出来，如果获取成功，则继续后续的操作，如果超过最大时间周期
            仍未获取，则抛出异常。
            隐式等待不会阻碍程序的正常运行，如果最后没有找到对应的目标，则依据实际情况报出正常exception信息
            优点：在整个webdriver生命周期中，只需要设置一次，即可一直生效。
            缺点：如果在最大时间周期内无法找到元素，则不管了。
        3. 显式等待：
            专门针对于元素来进行等待的操作行为
            和强制等待是相同的用法，需要等待的时候，就定义，不需要的时候就不定义。
            显示等待有两种不同的等待方法：until与until_not，两种方法的结果相反。
                until()表示如果元素存在则返回
                until_not()表示如果元素不存在则返回
            until的显式等待可以返回被等待的元素
            优势： 直接对单个元素进行等待，效率最高的等待行为
            劣势： 用起来很麻烦
        多种等待是可以同时使用的。selenium官网定义说显示等待与隐式等待不要共用，可能会造成实际等待时间超出设定时间。
    页面加载策略：
        selenium默认的加载策略是normal：所有内容全部加载完成，包含文件、css、js等
                第二种加载策略是eager：放弃加载css、图片等静态资源，提升加载速度
                第三种加载策略是none：只等初始页面加载即可直接操作
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

# chrome浏览器的配置项
options = webdriver.ChromeOptions()
# 配置页面加载策略
options.page_load_strategy = 'none'
driver = webdriver.Chrome(options=options)
# 隐式等待：设置为具体的秒数即可
driver.implicitly_wait(10)
driver.get('http://39.98.138.157/shopxo/index.php')
driver.find_element('name', 'wd').send_keys('123')
driver.find_element('id', 'ai-topsearch').click()

# driver.get('http://www.baidu.com')
# # 百度搜索并点击第一条搜索结果
# driver.find_element('xpath', '//input[@id="kw"]').send_keys('虚竹')
# driver.find_element('id', 'su').click()
# # 强制等待
# # sleep(1)
# # 显式等待，获取连接的元素，元素等待成功则返回该元素对象。
# link_el = WebDriverWait(driver, 5, 0.5).until(
#     lambda el: driver.find_element('xpath', '//*[@id="1"]/h3/a'), message='显式等待查找失败'
# )
# link_el.click()
# # print(link_el)
# # driver.find_element('xpath', '//*[@id="1"]/h3/a').click()
# sleep(3)
# 表示driver的生命周期结束的最后一步
# driver.quit()
