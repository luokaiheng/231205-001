from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# 浏览器窗体的最大化
# driver.maximize_window()
# 设置窗体大小尺寸
# driver.set_window_size(1000, 200)

# 访问指定url和文件
# driver.get(r'D:\测码\头像\index.html')
driver.get('http://www.baidu.com')
sleep(2)

# 浏览器窗体的最小化
# driver.minimize_window()
# 浏览器的前进和后退，以及刷新
# driver.forward()
# driver.back()
# driver.refresh()
# 获取title
# print(driver.title)
# 元素定位
# driver.find_element(定位方法,定位值)
# 页面中的元素操作都是基于元素获取之后才能够进行的。
# 输入和点击
# driver.find_element('xpath', '//*[@id="form"]/span[1]/span[1]').click()
# 文件上传：send_keys只限于input标签的文件上传和string的输入。非input标签使用AutoIT或者AutoTI，具体记不清了。
# driver.find_element('xpath', '//*[@id="form"]/div/div[2]/div[2]/input').send_keys(r'D:\测码\头像\1.jpg')
'''
    下拉列表框：现如今市场上基本都是基于input和div来实现的下拉列表框
        div，通过click来进行操作
        input下拉列表框：
            1. 通过click来进行操作（是推荐行为）
            2. 如果有readonly，就先remove掉，再通过send_keys输入（容易出现问题）
        select标签下拉列表框：是最为传统的形式，相对有年代感的系统才会存在。
'''
# select标签下拉列表框
select = Select(driver.find_element('id', 'deviceType'))
# 获取指定的值，进行选择
select.select_by_index(1)
select.select_by_value('11')
select.select_by_visible_text('自动驾驶')
# div下拉列表框与鼠标悬停
el = driver.find_element('xpath', '//span[text()="设置"]')
# 导入actionchains类进行悬停操作
ActionChains(driver).move_to_element(el).perform()
# 高级搜索
driver.find_element('link text', '高级搜索').click()
sleep(2)
driver.find_element('xpath', '//*[@id="adv-setting-gpc"]/div/div[1]').click()
sleep(1)
driver.find_element('xpath', '//p[text()="最近一月"]').click()
# 退出浏览器与进程，释放资源
driver.quit()
