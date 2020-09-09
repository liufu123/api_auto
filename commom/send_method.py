import requests
import json
class Send_Method():
    def send_method(self,method,url,json_data=None,params_data=None,header=None):
        if method == "post":
            self.r =requests.post(url=url,json=json_data,headers=header)
        elif method == "get":
            self.r = requests.get(url=url,params=params_data,headers=header)
        else:
            print("请求方法不正确！请使用post或者get方法")
            return None
        return self.r.json()

class Is_Json():
    def json(self,data):
        json_data = json.dumps(data,indent=2,ensure_ascii=False)
        return json_data

if __name__ == '__main__':
    url = "http://hn216.api.yesapi.cn/?s=App.User.GetList"
    data = {"app_key": "7040A01E94149B13BA561B41892116E6"}
    method = "get"
    a = Send_Method()
    r = a.send_method(method=method,url=url,params_data=data)
    print(r)