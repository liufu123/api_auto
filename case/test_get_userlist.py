from commom.get_keyword import Get_Keyword
from interface.get_user_list import Get_UserList
import pytest

class Test_pytest:
    def setup_class(self):
        self.a = Get_UserList()
        self.b = Get_Keyword()

    def test_get_user(self):
        self.resp = self.a.get_user_list(method="post")
        self.value = self.b.get_value_by_keyword(self.resp, "err_code")
        assert self.value==0

if __name__ == '__main__':
    pytest.main(['./test_get_userlist.py'])