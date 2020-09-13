from commom.get_keyword import Get_Keyword
from interface.get_user_list import Get_UserList
from interface.del_user import Del_user
from interface.user_login import User_Login
import pytest

class Test_del_user:
    """删除用户接口测试"""
    def setup_class(self):
        self.get = Get_Keyword()
        self.user_list = Get_UserList()
        self.login = User_Login()
        self.del_user = Del_user()

    def login_get_userlist(self,username):
        login_resp = self.login.login(method="post",username=username)  # 管理员帐号登录，获取管理员的token和uuid
        admin_token = self.login.get_token(login_resp)
        admin_uuid = self.login.get_uuid(login_resp)
        user_liat_resp = self.user_list.get_user_list(method="post")  # 获取用户列表，获取到被删除的用户uuid
        del_uuid = self.get.get_value_by_keyword(data=user_liat_resp, keyword="uuid")
        return admin_token,admin_uuid,del_uuid

    def test_user_del(self):
        """成功删除用户"""
        result = self.login_get_userlist(username="postman")
        admin_token,admin_uuid,del_uuid = result
        del_resp = self.del_user.del_user(other_uuid=del_uuid,admin_uuid=admin_uuid,admin_token=admin_token)#传参，发起接口请求
        value = self.get.get_value_by_keyword(del_resp,"err_code")
        assert value==0

    @pytest.mark.parametrize("admin_token", ["A1C4BBFA8"])
    def test_error_req(self,admin_token):
        """错误的请求，参数错误"""
        result = self.login_get_userlist(username="postman")
        admin_token, admin_uuid, del_uuid = result
        del_resp = self.del_user.def_user_error(other_uuid=del_uuid, admin_uuid=admin_uuid,admin_token=admin_token)  # 传参，发起接口请求
        value = self.get.get_value_by_keyword(del_resp, "ret")
        assert value == 400

    def test_not_admin_del(self):
        """非管理员帐号不能删除其他用户"""
        result = self.login_get_userlist(username="liufu")
        admin_token,admin_uuid,del_uuid = result
        del_resp = self.del_user.del_user(other_uuid=del_uuid, admin_uuid=admin_uuid,admin_token=admin_token)  # 传参，发起接口请求
        value = self.get.get_value_by_keyword(del_resp, "err_code")
        assert value == 1

    def test_admin_del_oneself(self):
        """管理员不能删除自己的帐号"""
        result = self.login_get_userlist(username="postman")
        admin_token,admin_uuid,del_uuid = result
        del_resp = self.del_user.del_user(other_uuid=admin_uuid, admin_uuid=admin_uuid,admin_token=admin_token)  # 传参，发起接口请求
        value = self.get.get_value_by_keyword(del_resp, "err_code")
        assert value == 2

    @pytest.mark.parametrize("other_uuid",["A1C4BBFA8F55C6FA715528DC0A06878B"])
    def test_admin_del_admin(self,other_uuid):
        """管理员不能删除别的管理员帐号"""
        login_resp = self.login.login(method="post")  # 管理员帐号登录，获取管理员的token和uuid
        admin_token = self.login.get_token(login_resp)
        admin_uuid = self.login.get_uuid(login_resp)
        del_resp = self.del_user.del_user(other_uuid=other_uuid, admin_uuid=admin_uuid,admin_token=admin_token)  # 传参，发起接口请求
        value = self.get.get_value_by_keyword(del_resp, "err_code")
        assert value == 3

if __name__ == '__main__':
    pytest.main("-s test_del_user.py")

