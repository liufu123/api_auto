from commom.get_keyword import Get_Keyword
from interface.get_user_list import Get_UserList
import pytest

class Test_pytest:
    """获取用户列表接口测试"""
    def setup_class(self):
        self.user = Get_UserList()
        self.get = Get_Keyword()

    def test_get_user(self):
        resp = self.user.get_user_list(method="post")
        value = self.get.get_value_by_keyword(resp, "err_code")
        assert value == 0

    @pytest.mark.parametrize("role",["admin","user","all"])
    def test_get_user_role(self,role):
        resp = self.user.get_user_list_by_role(method="post",role=role)
        value = self.get.get_value_by_keyword(resp, "err_code")
        assert value == 0

    @pytest.mark.parametrize("sort_type", [1,2,3,4])
    def test_get_user_sort_type(self,sort_type):
        resp = self.user.get_user_list_by_sort_type(method="post",sort_type=sort_type)
        value = self.get.get_value_by_keyword(resp, "err_code")
        assert value == 0

    def test_get_user_page(self):
        resp = self.user.get_user_list_by_page(method="post",page=1)
        value = self.get.get_value_by_keyword(resp, "err_code")
        assert value == 0

if __name__ == '__main__':
    pytest.main(['./test_get_userlist.py'])