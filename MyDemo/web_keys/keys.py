'''
    工具类：结构中层级属于底层逻辑代码层级
    Selenium关键字驱动类：常用操作行为给封装为各类关键字。
        所有的函数，如果不添加return，最后会返回None
        将常用的自行封装到自定义类中，在使用时，直接调用自定义封装的类即可。
        1. 创建driver
        2. 访问url
        3. 定位元素
        4. click
        5. sendkeys
        6. webdriverWait
        7. quit
        8. 相对定位器（由你们课后实现）
        ......
'''

# 自定义关键字驱动类
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait

from MyDemo.test_config.chrome_options import ChromeOptions


# 基于type_值决定生成的driver对象是什么类型
def open_browser(type_):
    if type_ == 'Chrome':
        # driver = webdriver.Chrome(options=ChromeOptions().options())
        driver = webdriver.Chrome()
    else:
        try:
            driver = getattr(webdriver, type_)()
        except Exception as e:
            print("Exception Information:" + str(e))
            driver = webdriver.Chrome()
    return driver


'''
    Python反射机制：
        四大内置函数：常用的是其中的getattr函数，就是获取指定类的指定属性
        getattr(类,属性)   相当于 类.属性 的意思
        例如：
            webdriver.Chrome == getattr(webdriver,'Chrome')
        基于反射获取属性是这个反射函数的基本定义。获取函数就需要在末尾加上()
        例如：
            webdriver.Chrome() == getattr(webdriver,'Chrome')()
    例如open_browser()函数：
        不用反射的形态
            if type_ == Chrome:
                driver = webdriver.Chrome()
            elif type_ == Firefox:
                driver = webdriver.Firefox()
            elif type_ == Ie:
                driver = webdriver.Ie()   
            elif safari
            elif edge
        
'''


class Keys:
    '''
    Keys() 调用这个类会进入构造函数，创建driver，以便实例方法使用，并且在构造函数中设置隐式等待整个driver的生命周期均有效
    其中包含的工具方法有：
        open(self, txt)：访问url
        locate(self, name, value)：定位元素
        click(self, name, value)：点击操作
        input(self, name, value, txt)：输入
        quit(self)：退出driver
        web_el_wait(self, name, value)：显示等待（针对元素的等待方法）
        wait(self, txt)：强制等待
        switch_frame(self, value, name=None)：切换frame
        switch_default(self)：切换至默认frame
        locator_with(self, method, value, el_name, el_value, direction)：相对定位器
        switch_handle(self, close=False, index=1)：句柄的切换（考虑不同场景的不同切换）
        assert_text(self, name, value, expect)：断言校验

    '''

    # 构造函数
    def __init__(self, txt):
        self.driver = open_browser(txt)
        # 隐式等待（全局设置
        self.driver.implicitly_wait(10)

    # 访问url
    def open(self, txt):
        self.driver.get(txt)

    # 定位元素
    def locate(self, name, value):
        return self.driver.find_element(name, value)

    # 点击操作
    def click(self, name, value):
        self.locate(name, value).click()

    # 输入
    def input(self, name, value, txt):
        self.locate(name, value).send_keys(txt)

    # 退出
    def quit(self):
        self.driver.quit()

    # 显式等待
    def web_el_wait(self, name, value):
        return WebDriverWait(self.driver, 10, 0.5).until(
            lambda el: self.locate(name, value), message='元素查找失败')

    # 强制等待
    def wait(self, txt):
        sleep(txt)

    # 切换Iframe
    '''
        传入一个参数：可以是id，name，webelement
    '''

    def switch_frame(self, value, name=None):
        # try:
        #     self.driver.switch_to.frame(self.locate('id', value))
        # except NoSuchElementException:
        #     try:
        #         self.driver.switch_to.frame(self.locate('name', value))
        #     except NoSuchElementException:
        #         self.driver.switch_to.frame(self.locate(name, value))

        if name is None:
            self.driver.switch_to.frame(value)
        else:
            self.driver.switch_to.frame(self.locate(name, value))

    # def switch_frame_simple(self, name, value):
    #     self.driver.switch_to.frame(self.locate(name, value))

    # 切换default窗体
    def switch_default(self):
        self.driver.switch_to.default_content()

    # 相对定位器
    def locator_with(self, method, value, el_name, el_value, direction):
        el = self.locate(el_name, el_value)
        direction_dict = {
            'left': 'to_left_of',  # 左侧
            'right': 'to_right_of',  # 右侧
            'above': 'above',  # 上方
            'below': 'below',  # 下方
            'near': 'near'  # 靠近
        }
        if isinstance(method, str):
            method_dict = {
                "id": By.ID,
                "xpath": By.XPATH,
                "link text": By.LINK_TEXT,
                "partial link text": By.PARTIAL_LINK_TEXT,
                "name": By.NAME,
                "tag name": By.TAG_NAME,
                "class name": By.CLASS_NAME,
                "css selector": By.CSS_SELECTOR
            }
            return self.driver.find_element(getattr(
                locate_with(method_dict.get(method), value), direction_dict.get(direction))(el))
            '''
                method_dict.get(method):BY的定位方法，value:获取定位方法的值，direction_dict.get(direction):判断相对定位的方法
                getattr(类,属性)
                相当于 类.属性 的意思 self.locate(locate_with(method_dict.get(method), value).direction_dict.get(direction))(el)
                                     ↓              ↓          ↓                     ↓           ↓                         ↓
                                  self.locate(locate_with(By.TAG_NAME,             'input').  to_left_of                 (el))
            '''

    # 句柄的切换（考虑不同场景的不同切换）
    def switch_handle(self, close=False, index=1):
        handles = self.driver.window_handles
        if close:
            # 是否关闭当前页再进行句柄切换
            self.driver.close()
        self.driver.switch_to.window(handles[index])

    # 句柄切换2，不做任何关闭
    # def switch_handle_1(self, index):
    #     handles = self.driver.window_handles
    #     self.driver.switch_to.window(handles[index])

    # 断言文本信息：可以捕获异常进行处理，也可以不捕获，因为报错就相当于断言失败。
    def assert_text(self, name, value, expect):
        try:
            reality = self.locate(name, value).text
            assert expect == reality, '断言失败，实际结果为：{}'.format(reality)
            return True
        except Exception as e:
            print('断言失败信息：' + str(e))
            return False
        # reality = self.locate(name, value).text
        # assert expect == reality, '断言失败，实际结果为：{}'.format(reality)
# if __name__ == '__main__':
# Keys().switch_frame('id', 'su')
# Keys().switch_frame('su')
# Keys().switch_frame_simple('id', 'su')
