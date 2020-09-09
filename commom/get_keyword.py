import jsonpath
from commom.send_method import Send_Method
class Get_Keyword():
    def get_value_by_keyword(self,data,keyword,num=0):
        """获取单个数据"""
        self.resp = jsonpath.jsonpath(data,f"$..{keyword}")[num]
        return self.resp

    def get_values_by_keyword(self,data,keyword):
        """获取多个数据"""
        self.resp = jsonpath.jsonpath(data,f"$..{keyword}")
        return self.resp



if __name__ == '__main__':
    url = "http://hn216.api.yesapi.cn/?s=App.User.GetList"
    data = {"app_key": "7040A01E94149B13BA561B41892116E6"}
    method = "get"
    a = Send_Method()
    g = Get_Keyword()
    r = a.send_method(method=method, url=url, params_data=data)
    rsp = g.get_value_by_keyword(data=r,keyword="nickname")
    print(rsp)

