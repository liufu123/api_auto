import pytest
from commom.get_keyword import Get_Keyword
from interface.user_registered import User_Registered

class Test_registered():
    """用户注册接口测试"""
    def setup_class(self):
        self.user = User_Registered()
        self.key_word = Get_Keyword()

    def test_userregistered_success(self):
        """注册用户成功"""
        res = self.user.user_registered()
        value = self.key_word.get_value_by_keyword(res,"err_code")
        assert value==0

    def test_userregistered_fail(self):
        """用户已注册"""
        res = self.user.user_registered(username="postman")
        value = self.key_word.get_value_by_keyword(res, "err_code")
        assert value==1

if __name__=="__main__":
    pytest.main(["./test_user_registered.py"])