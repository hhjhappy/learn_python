from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import smtplib
# i = None
# number = []

# while i < 6:
#     print('Are you ok?')
#     number.append(i)
#     i += 1
#     print(number)

# while True:
#     i += 1
#     print(i)
#     if i == 10:
#         break

# try:
#     # i += 1
#     if i is None :
#         raise NameError
#         print(i)
# except TypeError:
#     print("ffff")


# def is_odd(n):
#     return n % 2 == 1

# fff = lambda n: n % 2 == 1

# print(fff(3))

# print(is_odd(3))

# def add_unit(num):
#     return 


# from_add = 'hejian@weather.com.cn'
# #发送人密码
# from_passwd = '123.coM'
# #抄送人列表
# # Cs = ['hejian@weather.com.cn','wuy@weather.com.cn','gaos@weather.com.cn','wuj@weather.com.cn']
# #发送人列表
# to_add = ['hejian@weather.com.cn']
# smtp_server = 'smtp.exmail.qq.com'

# def send_email():
#     m = MIMEMultipart()
#     content = 'hello baidu.weather.com.cn'
#     contentApart = MIMEText(content, _charset='utf-8')

#     # for i in fj:
#     #     zipApart = MIMEApplication(open(i, 'rb').read())
#     #     zipApart.add_header('Content-Disposition', 'attachment', filename=i)
#     #     m.attach(zipApart)
#     #     m.attach(contentApart)

#     m['Subject'] = 'subject'
#     m["From"] = 'hejian@weather.com.cn'
#     m['To'] = ','.join(to_add)
#     m.attach(contentApart)
#     print(m)
#     # m['Cc'] = ",".join(Cs)

#     try:
#         server = smtplib.SMTP(smtp_server)
#         server.login(from_add, from_passwd)
#         server.sendmail(from_add,to_add,m.as_string())
#         server.quit()
#     except smtplib.SMTPException as error:
#         print('Send error', error)

# send_email()

# list = 'abcdef'
# things = []
# for i in list:
#     things.append(i)
# print(things[:-1])

states = {
    'Oregon':'OR',
    'Flordia':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}

cities ={
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
print("NY state has:",cities['NY'])
print("OR state has:",cities['OR'])


print('\n')
print('-' * 10)
print('\n'*10)
for state,abbrev in states.items():
    print('%s is abbreviated %s' %(state,abbrev))














