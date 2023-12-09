'''
    八大元素定位
'''

from selenium import webdriver
from time import sleep

'''
    1. id：类似于身份证的身份证号码，但为了避免出现重复，最好定位之前校验一下
    2. name：类似于身份证的名字，容易重名
    3. link text：一般用于定位a标签这一类超链接，通过text进行定位
    4. partial link text：和link text是一样的。不同在于这是模糊查询，类似于sql中的like关键字
    5. classname：通过class属性进行查找元素，除非无奈，不要使用它（元素定位一定不会到无奈的地步）
    6. tagname：通过标签名来进行元素查找，一般用于定位下拉列表框的值，或者用于多个元素定位
        像后台系统新增后，下拉列表值变动了
    7. cssselector：基于Class样式进行查找，有自己的固定表达式，类似于xpath，作为应用广度仅次于xpath的定位方法
        一般直接使用xpath即可，只有在出现伪元素的时候，会应用这个定位方法
    8. xpath：定位界的万金油
        xpath定位形式类似于文件系统，根据路径来查找元素
        相对路径： //*[@id="kw"]
            // 根路径
            * 所有的元素
            [] 筛选条件
            @ 通过属性来筛选
            text() 通过text文本筛选
            "" 查找的值
        绝对路径: /html/body/div/div[2]/div[5]/div[1]/div/form/span[1]/input 不可取，一般不用这种方式进行定位
        xpath的定位不推荐使用class属性进行定位
        xpath的函数：
            contains：通过模糊查找的行为查找元素的属性或者文本，继而查找到这个元素
            //*[contains(@id,'search')]
            //*[contains(text(),'search')]
        
'''

driver = webdriver.Chrome()
# driver.get('http://39.98.138.157/shopxo/index.php')
driver.get('http://www.baidu.com')
# 通过id查找元素
# input_ = driver.find_element_by_id('search-input')
# 通过Name查找元素
# el = driver.find_element_by_name('wd')
# 通过link text查找元素
# el = driver.find_element_by_link_text('登录')
# partial link text
# el = driver.find_element_by_partial_link_text('登')
# classname定位
# el = driver.find_element_by_class_name('submit')
# tagname定位
# els = driver.find_elements_by_tag_name('a')  # elements用于查找多个元素，结果会返回一个list
# el = driver.find_element_by_tag_name('a')
# cssselector定位
# el = driver.find_element_by_css_selector('#kw')
# xpath元素定位
el = driver.find_element_by_xpath('//*[@id="kw"]')
el.send_keys()
