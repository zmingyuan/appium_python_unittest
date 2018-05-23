#coding=utf-8
'''
    Project:通过测试套件执行多个测试用例，并生成报告
'''
import unittest
import time
import os
import HTMLTestRunner_cn

cur_path = os.path.dirname(os.path.realpath(__file__))
case_path = os.path.join(cur_path, "test_case/test_case")        # 测试用例的路径
report_path = os.path.join(cur_path, "report")  # 报告存放路径

if __name__ == "__main__":

    testunit = unittest.TestSuite()
    # discover 方法定义
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test*.py', top_level_dir=None)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            for test_unit in test_case:
                print(test_unit)

    now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
    fp = open(report_path+"\\"+now+".html", "wb")

    # retry，指定重试次数，如果save_last_try 为True ，一个用例仅显示最后一次测试的结果,False，则显示所有重试的结果。
    run = HTMLTestRunner_cn.HTMLTestRunner(title="微信测试报告",
                                            description="测试用例运行结果",
                                            stream=fp,
                                            retry=0,
                                            save_last_try=True)

    run.run(discover)
    fp.close()