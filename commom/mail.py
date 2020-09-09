import yagmail
from commom.read_ini import Read_ini
import os
import time
# from common.logger import Log
# log = Log()
class Mail():
    '''发送邮件'''
    def send_mail(self,report):
        config = Read_ini()
        username = config.get_value('Mail_account', 'user')
        psw = config.get_value('Mail_account', 'psw')
        receive = config.get_value('Mail_account','receive_user')
        yag = yagmail.SMTP(user = username,password = psw,host = 'smtp.163.com')
        subject = "果创云接口自动化测试报告"
        content = "请查看附件"
        yag.send(receive, subject, contents=[content, report])
        print("邮件发送成功！")

if __name__ == "__main__":
    report_path = os.path.join(os.getcwd(), 'report')
    now_time = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = os.path.join(report_path, now_time + 'result.html')
    a = Mail()
    a.send_mail(filename)