from commom.send_method import Send_Method,Is_Json
from commom.read_ini import Read_ini
from commom.get_keyword import Get_Keyword
class User_Login():
    """会员登录接口"""
    def __init__(self):
        self.path = "s=App.User.LoginExt"
        self.readini = Read_ini()
        self.req = Send_Method()
        self.get = Get_Keyword()
        self.url = self.readini.get_value("interface","url")+self.path
        self.app_key = self.readini.get_value("interface","app_key")
        self.error_app_key = self.readini.get_value("interface", "error_app_key")
        self.username = self.readini.get_value("account","username")
        self.password = self.readini.get_value("account","password")


    def login(self,method,username="postman",password="123456"):
        data = {"app_key": self.app_key, "username": username, "password": password}
        res = self.req.send_method(method=method,url=self.url,json_data=data)
        return res

    def error_app_key_params(self,method):
        """错误的app_key请求参数"""
        data = {"appkey": self.error_app_key,"username":self.username,"password":self.password}
        res = self.req.send_method(method=method, url=self.url, json_data=data)
        return res

    def get_token(self,resp_data):
        """获得登录用户的token"""
        token = self.get.get_value_by_keyword(resp_data,"token")
        return token

    def get_uuid(self,resp_data):
        """获得登录用户的uuid"""
        uuid = self.get.get_value_by_keyword(resp_data, "uuid")
        return uuid

if __name__ == '__main__':
    a = User_Login()
    j = Is_Json()
    r = a.login("post")
    data1 = a.get_token(r)
    data = j.json(r)
    print(data,data1)