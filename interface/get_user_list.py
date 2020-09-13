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
        """只传必要参数app_key"""
        data = {"app_key": self.app_key}
        resp = self.req.send_method(method=method,url=self.url,json_data=data)
        return resp

    def get_user_list_by_page(self,method,page=1):
        """必要参数app_key和可选参数page"""
        data = {"app_key": self.app_key,"page":page}
        resp = self.req.send_method(method=method, url=self.url, json_data=data)
        return resp

    def get_user_list_by_sort_type(self,method,sort_type=1):
        """必要参数app_key和可选参数sort_type"""
        data = {"app_key": self.app_key, "sort_type": sort_type}
        resp = self.req.send_method(method=method, url=self.url, json_data=data)
        return resp

    def get_user_list_by_role(self,method,role="all"):
        """必要参数app_key和可选参数role"""
        data = {"app_key": self.app_key, "role": role}
        resp = self.req.send_method(method=method, url=self.url, json_data=data)
        return resp

if __name__ == '__main__':
    g = Get_Keyword()
    a = Get_UserList()
    j = Is_Json()
    r = a.get_user_list_by_role("post",role="user")
    data = j.json(r)
    print(data)

