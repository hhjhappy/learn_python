import pymysql
import configparser
import json

config = configparser.ConfigParser()
config.read('config.conf')
class Connect():
    def Insert_sql(self,in_sql):
        try:
            con = pymysql.connect(host,port,db,user,password,charset)
            cur = con.cursor()
            cur.execute(in_sql)
            con.commit()
        except pymysql.Error as err:
            print(err)
        finally:
            con.close()
    def Select_sql(self,sel_sql):
        try:
            con = pymysql.connect(config['MySQL'['host']],config['MySQL'['port']],config['MySQL'['db']],config['MySQL'['user']],config['MySQL'['password']],config['MySQL'['charset']])
            cur = con.cursor()
            cur.execute(sel_sql)
            result = cur.fetchall()
            print(result)
            con.close()
        except pymysql.Error as err:
            print(err)



# Connect_domain_db = Connect(host='220.243.129.4', port=3306, db='domain_name', user='hhj',password='{av:3oY#~tkWKI(iLL)!', charset='utf8')
Connect_domain_db = Connect()

Connect_domain_db.Select_sql("select * from weathername where domain_name='gs.weather.com.cn' limit 20 ;")



