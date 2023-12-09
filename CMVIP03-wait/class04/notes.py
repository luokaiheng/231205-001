'''
    三类等待的场景应用：
        1. 强制等待：需要的时候调用即可
        2. 隐式等待：创建driver的时候调用
        3. 显式等待：除去关键性元素以外，还可以将显示等待的调用方式作为断言的机制
            until:用于在关键性元素进行定位时，调用
                在为了确保整个流程可以正常执行的目的的情况下，可以选择显式等待来进行元素的查找和定位
            until_not:用于在校验流程时，调用
    在系统中，弹窗分为两种：
        1、 需要进行操作之后，才可以消失的弹窗
        2、 一定时间后，自动消失
    当显示与隐示同时存在的情况下：
        1. 如果出现元素找不到，则爆出超时异常
        2. 在等待机制下，默认会遵循时间更长的等待方式

    显示等待机制：作为断言的时候，可以通过显示等待来判定元素的是否显示，从而判定到流程是否执行成功
        如果成功，会返回一个元素对象，如果失败会返回一个异常，基于显示等待返回的结果，可以判定本次流程是否成功

'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
# 隐式等待添加，以便于后续整个driver中，都可以尽量减少强制等待调用
driver.implicitly_wait(5)

driver.get('http://shop-xo.hctestedu.com/')
# 登录
# driver.find_element(by='xpath' , value='/html/body/div[2]/div/ul[1]/div/div/a[1]').click()
driver.find_element(by='link text', value='登录').click()

# 在关键性的元素上，进行显示等待。
link_el = WebDriverWait(driver, 2, 0.5).until(
    lambda el: driver.find_element(by='name', value='accounts'), message='登录失败')
link_el.send_keys('666666')
# driver.find_element(by='name',value='accounts').send_keys('666666')
driver.find_element(by='name', value='pwd').send_keys('111111')
driver.find_element(by='xpath', value='/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button').click()

sleep(3)
driver.quit()
