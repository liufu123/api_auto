import pytest
from interface.user_login import User_Login
from commom.get_keyword import Get_Keyword
from commom.readExcel import Excel_read
import os

pro_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
file_name = os.path.join(pro_path,"data","testdata.xlsx")
data = Excel_read(file_name)
test_data = data.dict_data()

class Test_Login_user():
    """用户登录接口"""
    def setup_class(self):
        self.login = User_Login()
        self.get = Get_Keyword()

    @pytest.mark.parametrize("username,password",[(test_data[0]["username"],test_data[0]["password"]),
                                                  (test_data[1]["username"],test_data[1]["password"]),
                                                  (test_data[2]["username"],test_data[2]["password"]),
                                                  (test_data[3]["username"],test_data[3]["password"])])
    def test_user_login(self,username,password,):
        """
        1.正确的用户名密码  2.正确的用户名，错误的密码  3.不存在的帐号登录
        """
        login_resp = self.login.login(method="post",username=username,password=password)
        value = self.get.get_value_by_keyword(login_resp,"err_code")
        assert value in [0,1,2]

    def test_error_app_key(self):
        """错误的app_key参数"""
        login_resp = self.login.error_app_key_params(method="post")
        value = self.get.get_value_by_keyword(login_resp, "ret")
        assert value==400

if __name__ == '__main__':
    pytest.main("-s test_login_pytest.py")