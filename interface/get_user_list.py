import requests
from commom.send_method import Send_Method,Is_Json
from commom.read_ini import Read_ini
from commom.get_keyword import Get_Keyword

class Get_UserList():
    """获取会员列表接口"""
    def __init__(self):
        self.path = "s=App.User.GetList"
        self.readini = Read_ini()
        self.url = self.readini.get_value("interface","url")+self.path
        self.app_key = self.readini.get_value("interface","app_key")
        self.req = Send_Method()

    def get_user_list(self,method):
        data = {"app_key": self.app_key}
        resp = self.req.send_method(method=method,url=self.url,json_data=data)
        return resp


if __name__ == '__main__':
    g = Get_Keyword()
    a = Get_UserList()
    j = Is_Json()
    r = a.get_user_list("post")
    uuid1 = g.get_value_by_keyword(data=r,keyword="uuid")
    # data = j.json(r)
    print(r)
    print(uuid1)
