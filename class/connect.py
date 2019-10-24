#coding:utf8
import pymysql
import configparser
import json

config = configparser.ConfigParser()
config.read('config.conf')
# class Connect():
#     def Insert_sql(self,in_sql):
#         try:
#             con = pymysql.connect(host,port,db,user,password,charset)
#             cur = con.cursor()
#             cur.execute(in_sql)
#             con.commit()
#         except pymysql.Error as err:
#             print(err)
#         finally:
#             con.close()
#     def Select_sql(self,sel_sql):
#         try:
#             con = pymysql.connect(config['MySQL']['host'],config['MySQL']['port'],config['MySQL']['db'],config['MySQL']['user'],config['MySQL']['password'],config['MySQL']['charset'])
#             cur = con.cursor()
#             cur.execute(sel_sql)
#             result = cur.fetchall()
#             print(result)
#             con.close()
#         except pymysql.Error as err:
#             print(err)


def Select_sql(select):
    host = config['MySQL']['host']
    port = config['MySQL']['port']
    db = config['MySQL']['db']
    user = config['MySQL']['user']
    password = config['MySQL']['password']
    charset = config['MySQL']['charset']
    try:
        # con = pymysql.connect(host,int(port),db,user,password,charset)
        con = pymysql.connect(host='220.243.129.4', port=3306, db='domain_name', user='hhj',password='{av:3oY#~tkWKI(iLL)!', charset='utf8',unix_socket=None)
        cur = con.cursor()
        cur.execute("select * from weathername where domain_name='%s's limit 20 ;"% select)
        print(cur.fetchall())
        con.close()
    except pymysql.Error as err:
        print(err)
Select_sql("gs.weather.com.cn")





