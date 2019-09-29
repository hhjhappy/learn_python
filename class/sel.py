import pymysql
import time


def Select_donamename(domainname):
    try:
        con = pymysql.connect(host='220.243.129.4', port=3306, db='domain_name', user='hhj',password='{av:3oY#~tkWKI(iLL)!', charset='utf8')
        cur = con.cursor()
        cur.execute("select * from weathername where domain_name='%s' limit 20 ;" %domainname)
        result = cur.fetchall()
        for i in result:
            print(i)
    except pymysql.Error() as error:
        print(error)
    finally:
        con.close()


Select_donamename('gs.weather.com.cn')


