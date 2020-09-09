import unittest
from commom.HTMLTestRunner_cn import HTMLTestRunner
import os
import time
from commom.mail import Mail


yag = Mail()
pro_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
case_path = os.path.join(pro_path,'python_requests\case')
report_path = os.path.join(pro_path,'python_requests\\report')
def all_case():
    '''构造待执行的测试用例'''
    discover = unittest.defaultTestLoader.discover(case_path,pattern='test*.py')
    return discover
if __name__ == '__main__':
    now_time = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = os.path.join(report_path,now_time+'result.html')
    fp = open(filename,'wb')
    # 执行测试，输出HTML格式的测试报告
    runner = HTMLTestRunner(stream=fp,title='自动化测试报告',description='用例执行情况：')
    runner.run(all_case())
    fp.close()
    yag.send_mail(filename) #发送邮件



