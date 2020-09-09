from commom.send_method import Send_Method
from commom.read_ini import Read_ini
from commom.hashlib_md5 import md5_value
import time

class User_Registered:
    """注册用户接口"""
    def __init__(self):
        self.path = "s=App.User.Register"
        self.readini = Read_ini()
        self.req = Send_Method()
        self.url = self.readini.get_value("interface", "url") + self.path
        self.app_key = self.readini.get_value("interface", "app_key")

    def user_registered(self,method="post",username=str(time.time())+"user"):
        data = {"app_key":self.app_key,"username":username,"password":md5_value("123456")}
        res = self.req.send_method(method=method,url=self.url,json_data=data)
        return res

if __name__=="__main__":
    a = User_Registered()
    print(a.user_registered())