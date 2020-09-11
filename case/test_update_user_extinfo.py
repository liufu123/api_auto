import pytest
from interface.update_uesr_extinfo import Update_user_info
from interface.user_login import User_Login
from commom.get_keyword import Get_Keyword



class TestUpdate_userinfo():
    """修改会员扩展信息"""
    def setup_class(self):
        self.login = User_Login()
        self.update = Update_user_info()
        self.get = Get_Keyword()

    @pytest.mark.parametrize("username",["postman"])#参数化
    def test_update_user_info_success(self,username):
        """修改用户的扩展信息"""
        self.login_resp = self.login.login(method="post",username=username)
        token = self.login.get_token(self.login_resp)
        uuid = self.login.get_uuid(self.login_resp)
        print(token,uuid)
        update_resp = self.update.update_uesr_info(method="post", token=token, uuid=uuid)
        value = self.get.get_value_by_keyword(update_resp, "err_code")
        assert value == 0


    @pytest.mark.parametrize("token,uuid",[("E7177FEBC2E92E555705C631C21BCBF1967A48ACDE45929A2A6260E1AF89","3EF51FAADF0A046C1C415950F4E62A7B")])
    def test_update_uesr_info_fail(self,token,uuid):
        """修改用户的扩展信息失败"""
        update_resp = self.update.update_uesr_info(method="post", token=token, uuid=uuid)
        value = self.get.get_value_by_keyword(update_resp, "ret")
        assert value == 400

if __name__ == '__main__':
    pytest.main(["./test_update_user_extinfo.py"])