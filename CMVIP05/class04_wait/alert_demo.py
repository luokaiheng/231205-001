'''
    浏览器本身的弹窗操作行为:alert
        1. alert弹窗：只有确定
        2. confirm弹窗：有确定和取消
        3. prompt弹窗：有文本框和确认和取消
    友情提醒：请认清楚这个东西到底是不是alert，只有浏览器本身的弹窗才是alert
    浏览器弹窗已经是被淘汰的东西了。只是为了避免遇到的同学不知道怎么处理才讲解的内容。
'''
from selenium import webdriver

driver = webdriver.Chrome()


#  切换到弹窗
alert = driver.switch_to.alert
# 确认按钮
alert.accept()
# 取消
alert.dismiss()
# 输入文本
alert.send_keys('你需要输入的文本字符串')
# 获取弹窗的文本信息
text = alert.text
