import json
import pymysql


# with open('domain_list.txt','r') as domain:
#     for  i in domain.readlines():
#
#         print(eval(i).values())


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
            value.append(eval(i).values())
    print(value)
append_key()
# print(value)


# print(insert_sql)
# try:
#     con = pymysql.connect(host = '220.243.129.4',port = 3306, db = 'domain_name',user = 'hhj',password = '{av:3oY#~tkWKI(iLL)!',charset = 'utf8')
#     cur = con.cursor()
#     cur.execute(insert_sql)
#     cur.close()
# except pymysql.Error as error:
#     print(error)

