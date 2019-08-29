from sys import argv

script,filename = argv

print("We're going to erase %r." %filename)
print("If you don't want that,hit CTRL-C(^C).")
print("If you wang that, hit RETURN.")

input("?")

print("Opening the file...")

#以写权限打开文件
target = open(filename,'w+')
print("Truncating the file. Goodbye!")

#seek()方法用于移动文件读取指针到指定位置。

#fileObject.seek(offset[, whence])

#offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
#whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
# target.seek(5)

#清空指针位置以后的文件内容
target.truncate()

print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write('\n')
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')


# line = target.readline()
# print(line)

# target.seek(0,0)
# txt = target.readline()
# print(txt)

print("And finally,we close it.")
target.close()

# with open(filename,'r') as txt:
#     txt.seek(2)
#     while True:
#         line = txt.readline()
#         if line:
#             print(line.strip())
#         else:
#             break
    

# with open(filename,'w') as target:
#     print("Truncating the file. Goodbye!")
#     target.truncate()
    # target.translate()