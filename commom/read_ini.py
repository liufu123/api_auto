import configparser
import os
class Read_ini():
    def __init__(self,file_name=""):
        if file_name == "":
            pro_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
            file_name = os.path.join(pro_path, "data", "guochuangyun.ini")
        self.ct = self.loading_ini(file_name)

    def loading_ini(self,file_name):
        ct = configparser.ConfigParser()
        ct.read(file_name)
        return ct

    def get_value(self,element,key):
        data = self.ct.get(element,key)
        return data

if __name__ == '__main__':
    ct = Read_ini()
    s = ct.get_value('interface','url')
    g = ct.get_value('interface','app_key')
    print(s)
    print(g)