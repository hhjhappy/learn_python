# import os,time
# from sys import argv
# print('Hens',25+30/6)
# print(100-25*3%4)
# print('What is 3+2?',3+2)
# print('What is 5-7?',5-7)
# print(5 >- 2)
# print(5 >= -2)
# print(7.0/4.0)
# print(7/4)

# dats = "Mon Tue wed Thu Fri sst sun"
# months = "\nJan\nFeb\nMar\nApr\nMay\nJun\n"
# print("Here are the days:",dats)
# print('Here are the months:',months)
# aaa = '''ffffffff'''
# print('gggg %s'%aaa)
# for i in months:
#     print(i)
# print('\a \b \f \n aaa \r  aaa \t fff \v fdfdfdf')
#while True:
#    for  i in ["/","-","|","\\","|"]:
#        print("%s\r"%i,)
#        time.sleep(2)


# print("How old are you?",)
# # age = raw_input()
# age = input()
# print('How tall are you?',)
# height = input()
# print('How much do you weigh?',)
# weight = input()

# print("So,you're %r old, %r tall and %r heavr."%(age,height,weight))
# print("So,you're %r old, %r tall and %r heavr."%(age,height,weight),)

# a = [script,first,second,third] = sys.argv
# for i in a:
#     print(i)
# print('aaaa',script)
# print('bbb',first)
# print('ccc',second)
# print('ddd',third)


# script,user_name = argv
# prompt = '>'
# print("Hi %s, I'm the %s script."%(user_name,script))
# print("I'd like to ask you a few questions.")
# likes = input(prompt)
# print("What kind of computer do you have?")
# computer = input(prompt)
# lives = input(prompt)
# print(''' Alright,so you said %r about liking me.
#     You live in %r Not sure where that is.
#     And you have a %r computer Nicd
#     '''%(likes,lives,computer))

# script,filename = argv
# print(script,)
# print(filename,)
# if os.path.isfile(filename):
#     with open(filename,'r') as f:
#         print(f.read())
# print("Type the filename again:")
# file_again = input('>')
# txt_again = open()

from sys import argv

# script,filename = argv

# file = open(filename,'r')
# while True:
#     txt_line = file.readline()
#     if txt_line:
#         print(type(txt_line),txt_line)
#     else:
#         break
# file.close()
# with open(filename,'r') as f:
#     while True:
#         txt_line = f.readline()
#         if txt_line:
#             print(txt_line.strip('\n'))
#             # if '那到底是一个什么地方' in txt_line:
#                 # print(txt_line.strip('\n'))
#         else:
#             break

# with open(filename,'r') as txt:
#     # print("Here's your file %r:" %filename)
#     while txt:
#         print(txt.readline())

# txt = open(filename,'r')
# line = txt.readline()
# while line:
#     print(line)
#     line = txt.readline()
# txt.close()
# print("Type the filename again:")
# file_again = input(">")

# with open(file_again,'r') as txt_again:
#     print(txt_again.read())





with open('dmbj.txt','r')as f:
    l = list(f)
    for line in l:
        print(type(line))
        print(line)







