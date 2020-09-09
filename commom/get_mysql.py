import pymysql
from commom.read_ini import Read_ini
class Mysql_database:
    def __init__(self):
        """读取配置信息连接数据库"""
        readini = Read_ini()
        host = readini.get_value('Database','host')
        user = readini.get_value('Database','user')
        password = readini.get_value('Database','password')
        database = readini.get_value('Database','database')
        port = int(readini.get_value('Database','port'))
        charset = readini.get_value('Database','charset')
        self.db = pymysql.connect(host=host,user=user,password=password,database=database,port=port,charset=charset)

    def get_mysql(self,sql):
        cursor = self.db.cursor()#建立一个游标
        cursor.execute(sql)#执行sql语句
        data = cursor.fetchall()#获取查询出的所有的值
        cursor.close()#关闭游标
        self.db.close()#关闭数据库连接
        return data

if __name__ == '__main__':
    a = Mysql_database()
    b = a.get_mysql("SELECT name FROM student WHERE id=1")
    print(type(b))
    print(b[0][0])