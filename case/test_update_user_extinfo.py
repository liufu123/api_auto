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

    @pytest.mark.parametrize("username",["postman","99999999"])#参数化
    def test_update_user_info(self,username):
        """修改用户的扩展信息"""
        self.login_resp = self.login.login(method="post",username=username)
        result = self.get.get_value_by_keyword(self.login_resp,"err_code")
        assert result==0 ,"判断登录是否成功，0表示成功。当前的result值为：%s"%result
        if  result==0:
            token = self.login.get_token(self.login_resp)
            uuid = self.login.get_uuid(self.login_resp)
            update_resp = self.update.update_uesr_info(method="post", token=token, uuid=uuid)
            value = self.get.get_value_by_keyword(update_resp, "err_code")
            assert value == 0

if __name__ == '__main__':
    pytest.main(["./test_update_user_extinfo.py"])