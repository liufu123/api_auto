from commom.send_method import Send_Method,Is_Json
from commom.read_ini import Read_ini

class Del_user:
    def __init__(self):
        """删除会员接口"""
        self.path = "s=App.User.RemoveUserForAdmin"
        self.readini = Read_ini()
        self.url = self.readini.get_value("interface", "url") + self.path
        self.app_key = self.readini.get_value("interface", "app_key")
        self.req = Send_Method()

    def del_user(self,other_uuid,admin_uuid,admin_token):
        """正确的请求"""
        data = {"app_key":self.app_key,
                "other_uuid": other_uuid,
                "admin_uuid":admin_uuid,
                "admin_token":admin_token}
        resp = self.req.send_method(method="post",url=self.url,json_data=data)
        return resp

    def def_user_error(self,other_uuid,admin_uuid,admin_token):
        """错误的参数请求"""
        data = {"app_key": self.app_key,
                "other_uuid": other_uuid,
                "admin_uuid": admin_uuid,
                "admin_tokan": admin_token} #参数错误
        resp = self.req.send_method(method="post", url=self.url, json_data=data)
        return resp

if __name__ == '__main__':
    print(1)