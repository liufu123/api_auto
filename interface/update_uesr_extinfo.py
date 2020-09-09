from commom.send_method import Send_Method,Is_Json
from commom.read_ini import Read_ini
from interface.user_login import User_Login
import random
class Update_user_info():
    """修改会员扩展信息接口"""
    def __init__(self):
        self.path = "s=App.User.UpdateExtInfo"
        self.req = Send_Method()
        self.readini = Read_ini()
        # self.user_login = User_Login()
        self.url = self.readini.get_value("interface","url")+self.path
        self.app_key = self.readini.get_value("interface","app_key")

    def update_uesr_info(self,method,token,uuid):
        data = {"app_key":self.app_key,"token":token,"uuid":uuid,"ext_info":{"sex":"男","age":random.randint(1,100)}}
        resp = self.req.send_method(method=method,url=self.url,json_data=data)
        return resp

if __name__ == '__main__':
    u = Update_user_info()
    login = User_Login()
    login_resp = login.login(method="post")
    token = login.get_token(login_resp)
    uuid = login.get_uuid(login_resp)
    updata = u.update_uesr_info(method="post",token=token,uuid=uuid)
    print(updata)