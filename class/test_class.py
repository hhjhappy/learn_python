# from nose.tools import *
# class test_class(object):
#     def __init__(self,pra,prab = {}):
#         self.pra = pra
#         self.prab = prab

#     def sing_test(self):
#         print(self.pra)
#         print(self.prab.a)
#         # print(self.prab)
#         # print(type(self.prab))
#         for k,v in self.prab.items():
#             print(k,v)

# class Animal(object):
#     pass

# class Dog(object):
#     def __init__(self,name):
#         self.name = name

# class Cat(object):
#     def __init__(self,name):
#         self.name = name

# class Person(object):
#     def __init__(self,name):
#         self.name = name
#         print(self.name)
#         # print(self.__name__)

#     def echo_message(self,nameb):
#         print(nameb)

# class Employee(Person):
#     def __init__(self,name):
#         # self.name = name
#         super().echo_message(name)
#         # print(self.__name__())

# Employee('fff')


# # ff = test_class('aaaa',{'ff':1})
# # ff.sing_test()

dir_list = [
'/ser/www/d1_weather.com.cn/htdocs/forecast7d_jsp/',
'/ser/www/d1_weather.com.cn/htdocs/alarm_cj/',
'/ser/www/d1_weather.com.cn/htdocs/scdz/',
'/ser/www/d1_weather.com.cn/htdocs/sg/',
'/ser/www/d1_weather.com.cn/htdocs/tempnotes/',
'/ser/www/d1_weather.com.cn/htdocs/zs_index/',
'/ser/www/d1_weather.com.cn/htdocs/baidumusic/',
'/ser/www/d1_weather.com.cn/htdocs/wap_180h/',
'/ser/www/d1_weather.com.cn/htdocs/cw_120h/',
'/ser/www/d1_weather.com.cn/htdocs/airfc_trweb/',
'/ser/www/d1_weather.com.cn/htdocs/wap_15d/',
'/ser/www/d1_weather.com.cn/htdocs/ruji/',
'/ser/www/d1_weather.com.cn/htdocs/tempnotes1h/',
'/ser/www/d1_weather.com.cn/htdocs/fc1h_48/',
'/ser/www/d1_weather.com.cn/htdocs/fc1h24/',
'/ser/www/d1_weather.com.cn/htdocs/flash_gw/',
'/ser/www/d1_weather.com.cn/htdocs/water/',
'/ser/www/d1_weather.com.cn/htdocs/fly/',
'/ser/www/d1_weather.com.cn/htdocs/rise_tianqiguanjia/',
'/ser/www/d1_weather.com.cn/htdocs/cwdata/',
]


# for i in dir_list:
#     print("%s" %i.split('/')[5],)

for i in dir_list:
    rsync_list = []
    rsync_list.append("[%s] \n" %i.split('/')[5])
    rsync_list.append('path = /ser/www/d1_weather.com.cn/htdocs/%s \n'%i.split('/')[5])
    rsync_list.append('read only=false \n')
    rsync_list.append('write = true \n')
    rsync_list.append("host allow = 220.243.129.134 \n")
    rsync_list.append("\n")


    with open('rsyncd.conf','a+') as rsync:
        for line in rsync_list:
            rsync.write(line)

    



# print(rsync_list)

