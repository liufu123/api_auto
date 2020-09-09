import unittest
from interface.user_login import User_Login
from commom.get_keyword import Get_Keyword
from commom.readExcel import Excel_read
import os
import ddt


pro_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
file_name = os.path.join(pro_path,"data","testdata.xlsx")
data = Excel_read(file_name)
test_data = data.dict_data()

@ddt.ddt
class Login_user(unittest.TestCase):
    """用户登录接口"""
    def setUp(self):
        self.login = User_Login()
        self.get = Get_Keyword()

    @ddt.data(*test_data)
    def test_user_login(self,data):
        """
        1.正确的用户名密码  2.正确的用户名，错误的密码  3.不存在的帐号登录
        """
        login_resp = self.login.login(method="post",username=data["username"],password=data["password"])
        value = self.get.get_value_by_keyword(login_resp,"err_code")
        self.assertIn(value,[1,2,0])

    def test_error_app_key(self):
        """错误的app_key参数"""
        login_resp = self.login.error_app_key_params(method="post")
        value = self.get.get_value_by_keyword(login_resp, "ret")
        self.assertEqual(value,400)

if __name__ == '__main__':
    unittest.main()