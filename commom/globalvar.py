class Global_Dict:
    def __init__(self):
        global global_dict
        self.global_dict = {}

    def set_value(self,name,value):
        self.global_dict[name] = value

    def get_value(self,name,defvalue = None):
        try:
            return self.global_dict[name]
        except KeyError:
            return defvalue

if __name__=="__main__":
    a=Global_Dict()
    a.set_value('name',"liufu")
    b = a.get_value("name")
    print(b)