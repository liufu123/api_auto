import requests
from commom.send_method import Send_Method,Is_Json
from commom.read_ini import Read_ini

class Get_UserList():
    """获取会员列表接口"""
    def __init__(self):
        self.path = "s=App.User.GetList"
        self.readini = Read_ini()
        self.url = self.readini.get_value("interface","url")+self.path
        self.req = Send_Method()
        self.data = {"app_key": self.readini.get_value("interface","app_key")}

    def get_user_list(self,method):
        resp = self.req.send_method(method=method,url=self.url,json_data=self.data)
        return resp


if __name__ == '__main__':
    a = Get_UserList()
    j = Is_Json()
    r = a.get_user_list("post")
    data = j.json(r)
    print(data)