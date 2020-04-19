import unittest
import os,time
from common.readconf import *
import HTMLTestRunner

cases_path = ReadConf().get_cases_url()
report_path = ReadConf().get_report_url()

# 用discover获取所有test_开头的case文件
discover = unittest.defaultTestLoader.discover(start_dir = cases_path,
                                               pattern = 'test_*.py')
main_suite = unittest.TestSuite()
main_suite.addTest(discover)    # 添加所有testcase
now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
report_name = report_path + '/result_%s.html'%now_time
print(report_name)
file = open(report_name, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                       title= '禅道UI测试',
                                       description= '测试描述')
runner.run(main_suite)
file.close()
