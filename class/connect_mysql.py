import json
import pymysql
import configparser

create_sql = '''
CREATE TABLE  weathername (
domain_id int(25) NOT NULL PRIMARY KEY,
domain_name varchar(100)  NOT NULL,
service_type varchar(20)  NOT NULL,
name varchar(50)  NOT NULL,
status varchar(20)  NOT NULL,
cdn_service_status varchar(20)  NOT NULL,
enabled varchar(10)  NOT NULL
) ENGINE InnoDB DEFAULT CHARSET utf8 COLLATE utf8_bin;
'''
insert_lan = '''insert into weathername(domain_id,domain_name,service_type,name,status,cdn_service_status,enabled) values '''

def append_key():
    value = []
    with open('domain_list.txt', 'r') as domain:
        for i in domain.readlines():
            value.append(list(eval(i).values()))
    try:
        con = pymysql.connect(host='220.243.129.4', port=3306, db='domain_name', user='hhj',password='{av:3oY#~tkWKI(iLL)!', charset='utf8')
        cur = con.cursor()
        for k in value:
            new_lang = []
            new_lang.append((int(k[0]),str(k[1]),str(k[2]),str(k[3]),str(k[4]),str(k[5]),str(k[6])))
            insert_sql = insert_lan + str(new_lang).strip('[').strip(']') + ';'
            cur.execute(insert_sql)
            con.commit()
    except pymysql.Error as error:
        print(error)
    finally:
        con.close()

append_key()