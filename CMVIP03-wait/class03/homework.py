from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# driver.get('http://music.163.com')
# # 窗体最大化
# driver.maximize_window()
# # driver.find_element_by_link_text('登录').click()
# driver.find_element_by_xpath('//a[@data-action="login"]').click()
# sleep(1)
# driver.find_element_by_link_text('选择其他登录模式').click()
# sleep(1)
# driver.find_element_by_id('j-official-terms').click()
# # 获取浏览器句柄
# handles = driver.window_handles
# print(handles)
# # 获取当下的标签页的title
# print(driver.title)
# driver.find_element_by_link_text('QQ登录').click()
# sleep(3)
# # driver.find_element_by_id('img_out_508419907').click()
# # 切换一下页面，当一个新的海王
# driver.find_element_by_xpath('//a[@data-action="login"]').click()
# # 获取句柄
# handles = driver.window_handles
# print(handles)
# # 切换句柄到第二个页面
# driver.switch_to.window(handles[1])
#
# print(driver.title)
# # 切换到页面的iframe中：可以直接在frame()中输入iframe元素对象，或者是iframe元素的id值
# iframe = driver.find_element_by_id('ptlogin_iframe')
# driver.switch_to_frame('ptlogin_iframe')
# fff = driver.switch_to.frame('ptlogin_iframe')
# driver.find_element_by_id('img_out_508419907').click()
# 我的函数有横杠，表示你调用的函数已经过时了。
# 元素操作返回的结果为None:因为函数本身没有return
# 操作完iframe，需要再操作iframe以外的元素，需要先出去，再操作，否则无法操作iframe以外的元素
# driver.switch_to.default_content()
# sleep(2)
# driver.switch_to.window(handles[0])
# print(driver.title)
# 在句柄的操作时候：一定记得最多保留不超过3个页面，最好是控制在2个页面，所以在控制标签页的时候，需要关联一个函数
# 在Selenium中有两种关闭手段：1是用quit，可以关闭整个webdriver，释放进程；2是用close，关闭当前句柄页
# driver.close()
# driver.quit()
# send_keys：是用于文本输入的。用于input标签配合使用，上传文件的元素一般都是input标签，也是通过sendkeys来实现
# driver.get('https://image.baidu.com/')
# sleep(2)
# driver.find_element_by_xpath('//*[@id="sttb"]').click()
# sleep(2)
# # 文件上传：首先确定需要上传的元素是input标签，再用sendkeys上传路径+文件名+后缀名进行上传
# # r表示原格式读取内容
# driver.find_element_by_xpath('//*[@id="stfile"]').send_keys(r'D:\头像\1.jpg')
# 下拉列表框：在现在的阶段一般是通过div、span、input标签来实现展示，而以往的老的实现形式是通过select标签来实现的
'''
    select:
        option1
        option2
'''
# el = driver.find_element_by_name('value(nf)')
# select = Select(el)
# 获取select元素中所有的选项
# select.options
# 选择元素
# select.select_by_index/value/visible_text
'''
    如果是input标签这一类型的元素实现的下拉列表框：
        1. 非input标签类型：都是通过click操作来实现
        2. input标签类型：默认是通过sendkeys来实现操作，如果实现不了就通过click实现
            在input标签中，要做任何操作都基本可以通过sendkeys来实现
            在input标签的下拉列表框中，readonly属性是基本上100%会存在的，一般先修改input标签属性，再sendkeys操作
            如果上述方式行不通，就还是通过click操作来实现
'''
driver.get('http://www.baidu.com')
# driver.maximize_window()
# # 隐式等待，可以暂时忽略
# driver.implicitly_wait(10)
# # 这一段也可以忽略，这是悬停
# el = driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
# action = ActionChains(driver)
# action.move_to_element(el).perform()
# # 下拉列表框操作赋值
# driver.find_element_by_xpath('//*[@id="s-user-setting-menu"]/div/a[1]').click()
# driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/div/div/ul/li[2]').click()
# driver.find_element_by_xpath('//*[@id="adv-setting-gpc"]/div/div[1]/span').click()
# sleep(3)
# driver.find_element_by_xpath('//*[@id="adv-setting-gpc"]/div/div[2]/div[2]/p[3]').click()

'''
    真的是最后一个了。
    find_element函数：用于元素定位
'''
# driver.find_element_by_xpath()等同于
# driver.find_element(by=By.XPATH, value=xpath)
# by=定位方法，value=匹配定位方法的值
# driver.find_element(by='id', value='kw').send_keys('虚竹')
'''
    验证码的处理：
        1. 输入型
        2. 短信验证
        3. 滑动条
        4. 看图找图
        5. 看图找字
    虽然有很多验证码的自动化处理形式，但是，不要用。因为在自动化中，验证码不是你们要处理的对象
    如果说你们非要验证，就先了解验证码的机制：
        验证码一般只出现在无缓存的环境执行授权操作时才有
        解决方案：
            1. 让你的浏览器有缓存（通过加载本地缓存数据、通过接口访问，传入token实现验证机制的绕过）
            2. 设置万能验证码
            3. 屏蔽
            4. 通过OpenCV模块实现
        
'''
'''
    课后作业：
        1. 实现商城的注册与登录自动化流程
        请自行添加自己的账号密码
        商城URL：http://39.98.138.157/shopxo/index.php
        作业发我QQ邮箱
'''