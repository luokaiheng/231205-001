'''
    测试用例的真正管理手段，测试套件的应用：
        测试套件：
            相当于一个list的存在，物理形态其实就是文件夹。
            UnitTest.TestSuite中可以自定义添加测试用例，
            套件的运行是依托于运行器runner来进行的。
    HTMLTestRunner:测试报告模块的应用
        环境部署： 不需要通过PIP去安装，直接下载py文件，放入python安装路径下的Lib文件夹即可
        修改py文件的源码：
            第94行，将import StringIO修改成import io
            第539行，将self.outputBuffer = StringIO.StringIO()修改成 self.outputBuffer = io.StringIO()
            第642行，将if not rmap.has_key(cls):修改成if not cls in rmap:
            第766行，将uo = o.decode('latin-1')修改成uo = e
            第772行，将ue = e.decode('latin-1')修改成ue = e
            第631行，将print >> sys.stderr, '\nTime Elapsed: %s' %  (self.stopTime-self.startTime)修改成print(sys.stderr, '\nTime  Elapsed: %s' % (self.stopTime-self.startTime))
        照着修改即可。如果不会改。没有关系，课后有源文件自行下载
'''
import os
import unittest

# 创建套件
from class10_suite_runner.test_demo import Demo, Demo01
# from HTMLTestRunner import HTMLTestRunner
from HTMLTestReportCN import HTMLTestRunner

suite = unittest.TestSuite()
# 1. 添加单个测试用例,基于测试用例的名称
# suite.addTest(Demo('test_04'))
# suite.addTest(Demo('test_02'))
# suite.addTest(Demo('test_03'))
# 2. 添加多个测试用例：通过list实现
# cases = [Demo('test_02'), Demo('test_04')]
# suite.addTests(cases)
# 3. 通过添加一整个class进入套件
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Demo01))
# 4. 通过文件名称添加
# cases = [unittest.TestLoader().loadTestsFromName('demo.Demo'), unittest.TestLoader().loadTestsFromName('demo.Demo01')]
# suite.addTests(cases)
# cases = ['demo.Demo', 'demo.Demo01']
# suite.addTests(unittest.TestLoader().loadTestsFromNames(cases))
# 5. 批量添加：在持续集成中，和批量管理中特别好用
# 定义测试用例文件的获取路径
path = './'
discover = unittest.defaultTestLoader.discover(start_dir=path, pattern='test*.py')

# 配置测试报告信息
# 测试执行者：在HTMLTestReport报告中专属参数
report_tester = '虚竹'
# 保存路径
report_dir = './report/'
# 测试报告的title
report_title = '虚竹的测试报告'
# 描述
report_description = '这是测试报告的描述'
# 测试报告文件
report_file = report_dir + 'reportCN.html'
# 生成路径
if not os.path.exists(report_dir):
    os.mkdir(report_dir)

# 生成HTMLTestRunner测试报告，本质意义上就是写入一个文件
with open(report_file, 'wb', encoding="utf-8") as file:
    runner = HTMLTestRunner(stream=file, title=report_title,
                            description=report_description, verbosity=2, tester=report_tester)
    runner.run(discover)
# 运行套件内的测试用例：默认运行器,verbosity是日志等级，0-1-2
# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(discover)
